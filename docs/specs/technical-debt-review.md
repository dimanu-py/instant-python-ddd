# Technical Debt Review — instant-python v0.21.0

## Resumen Ejecutivo

| Métrica | Resultado |
|---------|-----------|
| Tests totales | 103 ✅ |
| Cobertura global | **84%** |
| Lint (ruff) | 0 errores ✅ |
| Type checking (mypy) | 1 error (template Jinja2) |
| Arquitectura | Hexagonal (Ports & Adapters) |
| Líneas de código fuente | ~1,264 |

---

## 1. Evaluación Arquitectónica

### Puntos fuertes

- Hexagonal Architecture bien aplicada: separación clara en `domain/` (ABCs), `application/` (orquestación), `infra/` (implementaciones), `delivery/` (CLI).
- Inyección de dependencias consistente (constructor injection).
- Uso de `Mother` objects en tests.
- ABCs para todas las fronteras del sistema.

### Problemas de arquitectura

#### 1.1 MetricsMiddleware acopla creación de dependencias en el constructor

**Archivo:** `instant_python/metrics/delivery/metrics_middleware.py:20-26`

```python
def __init__(self, *args, **kwargs) -> None:
    super().__init__(*args, **kwargs)
    self._config_snapshot_creator = ConfigSnapshotCreator(repository=YamlConfigRepository())
    self._metrics_sender = UsageMetricsSender(
        reporter=PostHogMetricsReporter(
            config=PostHogConfig(),
            user_identity_manager=UserIdentityManager(),
        ),
    )
```

**Impacto:** Viola Dependency Inversion — hardcodea implementaciones concretas en lugar de recibirlas por inyección. Esto imposibilita testear MetricsMiddleware de forma aislada. La cobertura real de esta clase es **48%**, la más baja del proyecto.

**Solución:** Recibir `ConfigSnapshotCreator` y `UsageMetricsSender` por constructor.

#### 1.2 `_extract_config_path` contiene un bug lógico

**Archivo:** `instant_python/metrics/delivery/metrics_middleware.py:54-62`

```python
if ctx.args and ["--config", "-c"] in ctx.args:
```

La condición `["--config", "-c"] in ctx.args` **nunca** puede ser `True` porque busca una lista dentro de una lista de strings (`ctx.args` es `list[str]`). El parsing manual de `ctx.args` es frágil comparado con usar el API de Typer/Click (`ctx.params`).

#### 1.3 `JinjaProjectRenderer` usa `print()` para errores

**Archivo:** `instant_python/initialize/infra/renderer/jinja_project_renderer.py:52`

```python
except (TemplateNotFound, KeyError):
    print(f"Warning: Template not found for file {node.get('name')}, leaving content empty.")
```

**Impacto:** Un renderer no debería hacer I/O de consola. Viola separación de concerns.

**Solución:** Usar logging estructurado o lanzar una excepción manejada en capas superiores.

#### 1.4 `SystemConsole` usa `shell=True`

**Archivo:** `instant_python/initialize/infra/env_manager/system_console.py:38`

```python
result = subprocess.run(command, shell=True, check=False, ...)
```

**Impacto:** Riesgo de seguridad por shell injection. Los comandos construidos con strings concatenados (como en `UvEnvManager._build_dependency_install_command`) son vectores de ataque potenciales.

**Solución:** Pasar comandos como listas de argumentos (`subprocess.run([...])`) en lugar de strings.

#### 1.5 `UsageMetricsSender` mezcla lógica de dominio con infraestructura

**Archivo:** `instant_python/metrics/application/usage_metrics_sender.py`

La clase construye objetos de dominio (`UsageMetricsEvent`, `ErrorMetricsEvent`) y llama al reportero directamente. Debería delegar la construcción de eventos a una capa separada.

---

## 2. Test Desiderata — Análisis por Propiedad

### 2.1 Isolated — ✅ BUENO

Los tests usan `Mock()` de doublex y `setup_method()` para estado fresco por test. Sin estado mutable compartido.

**Ejemplo correcto:** `test_config_generator.py`, `test_project_initializer.py`.

### 2.2 Composable — ✅ BUENO

Uso extensivo de Mothers que permiten composición y reutilización:

- `ConfigSchemaMother`, `DependencyConfigMother`, `GeneralConfigMother`, `GitConfigMother`, `TemplateConfigMother`
- `NodeMother`, `ProjectStructureMother`, `CommandExecutionResultMother`
- `ConfigSnapshotMother`, `UsageMetricsEventMother`, `ErrorMetricsEventMother`

### 2.3 Deterministic — ⚠️ OBSERVACIÓN

`test/random_generator.py` usa `Faker` para datos aleatorios. Aunque no se usa directamente en asserts, podría introducir no-determinismo en configuraciones de test.

### 2.4 Fast — ⚠️ OBSERVACIÓN

- Los tests de PostHog usan VCR cassettes (aceptable).
- Los acceptance tests en `test_init_cli.py` usan `verify_all_combinations` generando muchas combinaciones (103 tests en ~2 min).

### 2.5 Writable — ✅ BUENO

Las Mothers reducen drásticamente el boilerplate. Tests como `test_config_generator.py` son muy concisos (24 líneas totales).

### 2.6 Readable — ✅ MUY BUENO

Nombres descriptivos y estructura Arrange-Act-Assert clara:

```python
def test_should_initialize_project_with_git_repository(self) -> None:
    config = ConfigSchemaMother.any()
    project_structure = ProjectStructureMother.any()
    ...
    self._project_initializer.execute(config=config, destination_project_folder=destination_folder)
    expect(self._renderer).to(have_been_satisfied)
```

### 2.7 Behavioral — ⚠️ OBSERVACIONES

**Acceso a atributo privado en test:**

`test/initialize/infra/renderer/test_jinja_project_renderer.py:52`:

```python
expect(unmatched_file).to_not(be_none)
expect(unmatched_file.is_empty()).to(be_true)
```

```
unmatched_file = next(
    (node for node in project_structure.flatten() if isinstance(node, File) and node._name == "unmatched_file"),
    None,
)
```

Accede a `node._name` (atributo privado). Si `_name` cambia de nombre, el test se rompe sin que el comportamiento haya cambiado.

**Uso de `ANY_ARG` debilita asserts:**

`test/metrics/application/test_usage_metrics_sender.py:15`:

```python
expect_call(reporter).send_success(ANY_ARG)
```

`ANY_ARG` permite que el test pase incluso si los argumentos reales son incorrectos.

### 2.8 Structure-insensitive — 🔴 PROBLEMAS

- **Acceso a `_name`** en `test_jinja_project_renderer.py` (mencionado arriba).
- **Tests acoplados a comandos exactos** en `test_uv_env_manager.py`:

```python
expect_call(self._console).execute_or_raise(
    f"{self._UV_EXECUTABLE} python install {self._A_PYTHON_VERSION}"
)
```

Refactorizar `UvEnvManager._build_dependency_install_command` rompería estos tests.

### 2.9 Automated — ✅ BUENO

Sin pasos manuales. Tests de PostHog usan VCR cassettes para grabar/reproducir respuestas HTTP.

### 2.10 Specific — ✅ BUENO

Tests enfocados (1-2 asserts por test en unit tests). Acceptance tests usan approval testing.

### 2.11 Predictive — ⚠️ BRECHAS DE COBERTURA

| Módulo | Cobertura | Riesgo |
|--------|-----------|--------|
| `MetricsMiddleware` | **48%** | Flujo completo de metrics no testeado |
| `EnvManagerFactory` | **78%** | Creación de PdmEnvManager no testeada |
| `ProjectWriter` (ABCs) | **79%** | NodeWriter ABC no testeado directamente |
| `MetricsReporter` (ABC) | **80%** | Solo implementación PostHog testeada |
| `ProjectFormatter` (ABC) | **80%** | Solo Ruff implementación testeada |
| `ConfigRepository` (ABC) | **77%** | Solo YAML implementación testeada |
| `ProjectRenderer` (ABC) | **86%** | |
| `PostHogMetricsReporter` | **74%** | Manejo de excepciones no testeado |
| `EnvManager` (ABC) | **83%** | |

### 2.12 Inspiring — ⚠️ OBSERVACIÓN

Los acceptance tests en `test_init_cli.py` usan `verify_all_combinations` que generan approval files. Esto es potente, pero confiar solo en approval testing sin asserts explícitos puede dar falsa confianza: si un approval file se actualiza sin revisión, el test pasa aunque haya cambios inesperados.

---

## 3. Deuda Técnica

### 3.1 Alta Prioridad

| ID | Archivo | Línea(s) | Problema |
|----|---------|----------|----------|
| DT-1 | `metrics_middleware.py` | 20-26 | Dependencias hardcodeadas en constructor — impide testear en aislamiento |
| DT-2 | `metrics_middleware.py` | 56 | Bug: `["--config", "-c"] in ctx.args` nunca es True |
| DT-3 | `system_console.py` | 38 | `shell=True` — riesgo de shell injection |
| DT-4 | `jinja_project_renderer.py` | 52 | `print()` para errores en lugar de logging/excepciones |
| DT-5 | `test_jinja_project_renderer.py` | 52 | Acceso a `._name` (atributo privado del objeto bajo test) |

### 3.2 Media Prioridad

| ID | Archivo | Línea(s) | Problema |
|----|---------|----------|----------|
| DT-6 | `post_hog_metrics_reporter.py` | 31-32 | `except: pass` — traga excepciones silenciosamente sin logging |
| DT-7 | `metrics_middleware.py` | 73-78 | Thread con `join(timeout=5)` — timeout arbitrario |
| DT-8 | `usage_metrics_sender.py` | 16-24 | Construcción manual de eventos dentro del sender — mezcla capas |
| DT-9 | `test_usage_metrics_sender.py` | 15 | `ANY_ARG` en asserts que debilita la detección de cambios |
| DT-10 | `makefile` | 112-118 | `rm` con `find` anidado — frágil, mejor usar `git clean` |
| DT-11 | `system_console.py` | 60 | `stderr_output: str = None` — type hint incorrecto (debiera ser `str | None`) |

### 3.3 Baja Prioridad

| ID | Archivo | Línea(s) | Problema |
|----|---------|----------|----------|
| DT-12 | `project_initializer.py` | 26-31 | Métodos privados de 1 línea que solo delegan — over-engineering leve |
| DT-13 | `dependency_config.py` | 20-22 | Validación cross-campo (`is_dev` + `group`) dentro del dataclass |
| DT-14 | `random_generator.py` | — | Archivo de test utility con Faker que no se usa en ningún test |

---

## 4. Diagrama de Cobertura por Módulo

```
shared/domain/        ████████████████████ 97%  (config_schema, git_config)
shared/infra/         ████████████████████ 100% (yaml_config_repository)
initialize/domain/    ████████████████░░░ 86%  (project_renderer, project_structure)
initialize/infra/     ██████████████████░░ 94%  (jinja_renderer, file_writer, git, ruff)
initialize/application ████████████████████ 100% (project_initializer)
metrics/domain/       ████████████████░░░ 88%  (config_snapshot, events)
metrics/infra/        ███████████████░░░░ 74%  (posthog_reporter)
metrics/application   ████████████████████ 96%  (snapshot_creator, metrics_sender)
metrics/delivery      ████████████░░░░░░░ 48%  (metrics_middleware) ← CRÍTICO
```

---

## 5. Recomendaciones Priorizadas

### Inmediatas (Semana 1)

1. **Refactorizar `MetricsMiddleware`** — Inyectar `ConfigSnapshotCreator` y `UsageMetricsSender` por constructor. Esto subiría la cobertura de 48% a ~90% y permitiría testear el flujo completo de metrics.
2. **Corregir bug en `_extract_config_path`** — Usar `ctx.params` o el API de Click/Typer para obtener el valor de `--config`/`-c`.
3. **Eliminar acceso a `._name`** en `test_jinja_project_renderer.py` — Agregar una propiedad pública o buscar el archivo por otro criterio.

### Corto plazo (Semana 2-3)

4. **Reemplazar `shell=True`** por lista de argumentos: `subprocess.run(["uv", "add", ...])`.
5. **Reemplazar `print()` en `JinjaProjectRenderer`** por logging o excepción estructurada.
6. **Eliminar `ANY_ARG` en asserts de `test_usage_metrics_sender.py`** — Verificar args específicos del evento.
7. **Agregar tests para `EnvManagerFactory`** — Especialmente la rama que crea `PdmEnvManager`.

### Mediano plazo

8. **Evaluar `except: pass` en `PostHogMetricsReporter`** — Al menos agregar logging para no perder visibilidad de errores.
9. **Separar `UsageMetricsSender`** en dos clases: construcción de eventos y envío.
10. **Revisar approval tests** — Agregar asserts complementarios para validar comportamiento clave además del snapshot.

---

## 6. Resumen de Salud del Proyecto

| Dimensión | Puntuación | Notas |
|-----------|-----------|-------|
| Arquitectura | 8/10 | Hexagonal sólida, pero `MetricsMiddleware` rompe DI |
| Tests | 8/10 | Buenos Mothers, cobertura 84%, pero agujeros en módulos clave |
| Seguridad | 7/10 | `shell=True` es riesgo conocido |
| Legibilidad | 9/10 | Código limpio, nomenclatura clara |
| Mantenibilidad | 8/10 | Buena separación, deuda técnica incipiente en metrics |
| Rapidez de tests | 7/10 | ~2 min para 103 tests |

El proyecto está en muy buen estado general. Los problemas principales se concentran en `MetricsMiddleware` (el punto más débil: **48% cobertura**, dependencias hardcodeadas, bug lógico). El resto son detalles de seguridad/testing que no afectan el funcionamiento actual pero es recomendable abordar progresivamente.
