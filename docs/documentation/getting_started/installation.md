To ensure a clean and isolated environment, we recommend installing `instant-python` using a virtual environment. At your
own risk, you can install it at your system Python installation, but this is not recommended.
Below are the preferred installation methods.

!!! note "Supported Python Versions"
    Instant Python tries to support the latest Python versions, we officially support from Python 3.10 to 3.13.
    Older versions of Python may work, but they are not guaranteed to be compatible.

## Installation Methods

### Install script (recommended)

The recommended way to install `instant-python` is via the install script. It downloads a self-contained `ipy` binary with
Python bundled in, so **no local Python installation is required** to install or run it.

**macOS / Linux**

```bash
curl -LsSf https://raw.githubusercontent.com/dimanu-py/instant-python/main/scripts/install.sh | sh
```

By default the binary is installed to `~/.local/bin`. You can override this with the `IPY_BIN_DIR` environment variable:

```bash
IPY_BIN_DIR="$HOME/bin" curl -LsSf https://raw.githubusercontent.com/dimanu-py/instant-python/main/scripts/install.sh | sh
```

**Windows**

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://raw.githubusercontent.com/dimanu-py/instant-python/main/scripts/install.ps1 | iex"
```

This adds `%USERPROFILE%\.local\bin` to your user `PATH` automatically; restart your terminal afterwards so it picks up the
change. You can override the install directory with the `IPY_BIN_DIR` environment variable.

!!! note "Supported platforms"
    The install script currently provides prebuilt binaries for macOS (Apple Silicon), Linux (x86_64 and arm64), and Windows
    (x86_64). On other platforms (Intel Mac, Windows on ARM), use one of the alternative methods below.

### Other installation methods

If your platform isn't covered by the install script, or you prefer to manage `instant-python` as a regular Python package,
you can install it with `pipx` or `pip` instead.

#### Using `pipx`

`pipx` installs Python applications in isolated environments, ensuring that they do not interfere with other Python applications.

```bash
pipx install instant-python
```

If you do not have `pipx` installed, you can install it using `pip`.

```bash
pip install --user pipx
```

#### Using `pyenv`

If you already manage your Python versions using a tool like Pyenv, you can install `instant-python` using `pip` with
pyenv's global Python version.

```bash
pip install instant-python
```

A guide to install and configure pyenv can be found [here](https://github.com/pyenv/pyenv?tab=readme-ov-file#installation)

## Next steps

Now that you have installed `instant-python` you can advance to the [first steps](first_steps.md)
section to learn the basic features of `instant-python` and create your first project.