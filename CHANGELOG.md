# CHANGELOG

<!-- version list -->

## v0.24.2 (2026-08-07)

### 🪲 Bug Fixes

- **config**: Ask for dependency name again if user enters an empty string instead of reseting the
  dependency question process
  ([`8984c3e`](https://github.com/dimanu-py/instant-python/commit/8984c3eb639287393ef32d781d22de14ba52aa54))

### ♻️ Refactoring

- **config**: Extract semantic variable to remove magic string to represent empty group
  ([`3e1a0e4`](https://github.com/dimanu-py/instant-python/commit/3e1a0e49f1c7da00921951df25eac973b3c4eca4))

- **config**: Modify the message to ask whether to add a dependency or not depending on initial
  answer
  ([`4717cad`](https://github.com/dimanu-py/instant-python/commit/4717cad914d00b406759973db694c4296d7beed7))

- **config**: Ask the user if they want to add initial dependencies when it's the first time
  ([`5149deb`](https://github.com/dimanu-py/instant-python/commit/5149deb359e2c7ae856078cd7a55d1f9216049e1))


## v0.24.1 (2026-08-06)

### 🪲 Bug Fixes

- **config**: Correctly detect when user wants to specify the first bounded context when DDD
  template is selected
  ([`510010d`](https://github.com/dimanu-py/instant-python/commit/510010da4ea912eb9675d8771827d3b80bc6ff2c))

- **templates**: Correct wrong reference to precommit hook built in feature in github ci workflow
  ([`5ced652`](https://github.com/dimanu-py/instant-python/commit/5ced652e51021c0999cf1f810d6deec949ac4b87))

- **templates**: Correct wrong reference to custom documenation built in feature
  ([`63f019e`](https://github.com/dimanu-py/instant-python/commit/63f019e23a24d0737d01d3b1fb5f5fe406590624))

- **shared**: Add timezone to default year variable in general config
  ([`0ef8a1f`](https://github.com/dimanu-py/instant-python/commit/0ef8a1f2b2018247727275e30b06b52a931938e4))

### ⚙️ Build System

- Update uv.lock file
  ([`07aa03b`](https://github.com/dimanu-py/instant-python/commit/07aa03b7d0653bc79c3068843f426cc01b027eeb))

- Specify test path for mutation
  ([`89a3cfc`](https://github.com/dimanu-py/instant-python/commit/89a3cfce2f9d7e8cdcc7e63a3f4e10b0c81fbffa))

- Update dependencies in uv.lock file
  ([`eb5858c`](https://github.com/dimanu-py/instant-python/commit/eb5858cb1c54b3bbcf796924c0e02cb385db3e32))

- Add mutmut to test dependencies to run mutation tests on the project
  ([`8a835cc`](https://github.com/dimanu-py/instant-python/commit/8a835cc73b6a4b78b3f3ff36b0abf8068555df9a))

- Bump pymdown-extensions from 10.21.3 to 11.0
  ([`584fb81`](https://github.com/dimanu-py/instant-python/commit/584fb8113143ad2a7eab08af04fc92500f2f3ea7))

- Bump the production-minor-patch group across 1 directory with 4 updates
  ([`ece841a`](https://github.com/dimanu-py/instant-python/commit/ece841a31a704e1faea35cabf1caa600b70c1308))

- Bump the development-minor-patch group with 4 updates
  ([`21567a6`](https://github.com/dimanu-py/instant-python/commit/21567a6fe4dc9769ea5baffc64d704d52893a080))

- Bump the production-minor-patch group with 2 updates
  ([`dbff7e6`](https://github.com/dimanu-py/instant-python/commit/dbff7e676f7b10fbcab9c3309390e2001261bd00))

- Manually upgrage pydanctic-settings library due to vulnerability reported by audit job in ci
  ([`b28318d`](https://github.com/dimanu-py/instant-python/commit/b28318d91e745afc6f99af67a4b525a49ef376d5))

- Bump vcrpy from 8.1.1 to 8.2.1
  ([`fc81715`](https://github.com/dimanu-py/instant-python/commit/fc81715efeed4bf7c7fa269ef5c84a4d0b799636))

- Bump msgpack from 1.1.2 to 1.2.1
  ([`d4a0c09`](https://github.com/dimanu-py/instant-python/commit/d4a0c09d36b30956b08bbc17c6655e42aaa687a7))

- Bump the development-minor-patch group with 4 updates
  ([`9661de9`](https://github.com/dimanu-py/instant-python/commit/9661de9eeae160f10293a83c4e9849c7425d1d90))

- Bump the production-minor-patch group with 2 updates
  ([`05a0fc9`](https://github.com/dimanu-py/instant-python/commit/05a0fc9fe4402e104ac26a8a5e394330d4a0bf93))

- Bump the development-minor-patch group with 2 updates
  ([`fc52a31`](https://github.com/dimanu-py/instant-python/commit/fc52a3128ee4df0b7b814af5c84670ca7910c7e5))

- Bump the production-minor-patch group with 2 updates
  ([`1fa0495`](https://github.com/dimanu-py/instant-python/commit/1fa049545803dc8a6b882e875d816a8300e92fd9))

### ♻️ Refactoring

- **config**: Apply early return when user selects custom template
  ([`5127195`](https://github.com/dimanu-py/instant-python/commit/51271957ceebc577b8683ac10dec6939fac2ea4c))

- **config**: Rename inner method in git step question wizard to detect if user wants to create the
  project in a git repository
  ([`684080c`](https://github.com/dimanu-py/instant-python/commit/684080c8663f47639a652abbc233fde6715b83e7))

- **config**: Remove all invalid characters from slug in general config and normalize invalid
  characters to hyphens
  ([`8892c58`](https://github.com/dimanu-py/instant-python/commit/8892c585a6c99e6ac66bdbca3d98a0b4fbfa4618))

- **config**: Improve question prompting for the different steps in the wizard
  ([`7120665`](https://github.com/dimanu-py/instant-python/commit/712066576ac065f0f25df1f3747dda8fed389635))

- **templates**: Update convention_keeper template to improve how it detects and writes conventions
  to avoid them to be feature specific
  ([`c375429`](https://github.com/dimanu-py/instant-python/commit/c375429aee599650518884a59728f70c55192c23))

- **config**: Show the user some progress when answering the questions and let them know the
  sections they are answering to
  ([`9f8b44c`](https://github.com/dimanu-py/instant-python/commit/9f8b44cab3efe7b9457db34fff89ae23d9423131))

- **templates**: Update agents main file to keep track of conventions in the file to avoid putting
  in the different subagents which conventions it should read
  ([`76f500f`](https://github.com/dimanu-py/instant-python/commit/76f500f35648121551d43cd5c3d6d90f024dfbb4))

- **templates**: Update help comment in mutate make target template
  ([`9e156a0`](https://github.com/dimanu-py/instant-python/commit/9e156a05958d243b7c3eb4350d95c511608f279c))

- **templates**: Update instruction for running mutation testing in judge subagent template
  ([`ff6ec09`](https://github.com/dimanu-py/instant-python/commit/ff6ec09fc7a22feae33c74e1bb3d7f95394150e4))

- **templates**: Remove setting the leader subagent to be the default when starting a conversation
  so subagents workflow has to be triggered manually
  ([`4925e62`](https://github.com/dimanu-py/instant-python/commit/4925e62454942d36477f9d15e6c12bbd6f96cd51))

- **templates**: Ignore CLAUDE.md file when ai agents built in feature is selected
  ([`3d0698d`](https://github.com/dimanu-py/instant-python/commit/3d0698d0295983ef07cb93e5f56f5a96e65a0b36))

- **templates**: Remove conditional in precommit hook template file to always include local hooks
  that use makefile
  ([`576d9ce`](https://github.com/dimanu-py/instant-python/commit/576d9ce56eaf0abda0428cfd0bedd6b75a007a2c))

- **templates**: Modify subagents specifications, turn some commands into skills and add mutation
  target in makefile template
  ([`1da35f9`](https://github.com/dimanu-py/instant-python/commit/1da35f9552ebe58accb60973d12f32f79db6cd64))

- **templates**: Rename craftsman leader subagent to just leader
  ([`c3067d1`](https://github.com/dimanu-py/instant-python/commit/c3067d1bd046cbd2f94abf8ad38d970e25a5847c))

- Fix all linting errors due to class vars not being typed, exceptions handle too broadly or imports
  not being organized
  ([`c22a212`](https://github.com/dimanu-py/instant-python/commit/c22a212349c58c239991aac087b145262a24c9b0))


## v0.24.0 (2026-06-10)

### ✨ Features

- **templates**: Add local tasks management templates for agent harness
  ([`5452009`](https://github.com/dimanu-py/instant-python/commit/5452009e27909967ea9a20893a06a665dc2c3cc2))

- **templates**: Ignore docs/progress, opencode and claude folders from git when ai agents feature
  is selected
  ([`a572448`](https://github.com/dimanu-py/instant-python/commit/a5724488607509dc12513a195a562cf813cb888c))

- **templates**: Add new agent harness setup focused on automated subagents and update previous
  skills and commands name
  ([`c303364`](https://github.com/dimanu-py/instant-python/commit/c30336455985f8c382a463399cf57c1d44e1ba2f))

- **templates**: Avoid ignoring spec files located inside docs/features files
  ([`f759bc9`](https://github.com/dimanu-py/instant-python/commit/f759bc94b6ab2cf1e49bacb86f33b41ca6e1fa3e))

### 🪲 Bug Fixes

- **templates**: Avoid REFERENCE.md content to be interpreted as jinja syntax by wrapping it in {%
  raw %}
  ([`a9e4968`](https://github.com/dimanu-py/instant-python/commit/a9e4968484df6e6e886b4744e4f2e87db2e97e6e))

- **templates**: Modify how boilerplate for .gitignore checks if ai agents built in feature is
  selected to include some extra folders to be ignored
  ([`4fa3ffe`](https://github.com/dimanu-py/instant-python/commit/4fa3ffefb8f2a2aeaa19dd9e0a1b943597442805))

- **templates**: Include mutmut dev dependency in pyproject.toml template file when ai agents is
  selected
  ([`9398f57`](https://github.com/dimanu-py/instant-python/commit/9398f57b42651b9e5260fd84718c5c3448e738fd))

### ♻️ Refactoring

- **templates**: Modify how spec partner and specs in general are generated by separating a spec
  file in markdown format and a feature file with Gherking scenarios, both in their respective
  folders
  ([`20f7b02`](https://github.com/dimanu-py/instant-python/commit/20f7b02f030f9e1071a952bf6431df40b9ad46b5))

- **templates**: Include all ai agents related configuration for .gitignore template together
  ([`315c063`](https://github.com/dimanu-py/instant-python/commit/315c063afdd8932bb3419a9104880aa298ff3dc8))

- **templates**: Update agent harness setup to not be fixed to a Linear project and propose a local
  task management system to start
  ([`dd47044`](https://github.com/dimanu-py/instant-python/commit/dd47044fd745f931ebd3b94f610d78b7ccf0ad1a))

- **templates**: Update agents project structure template to include new subagents and new naming
  ([`8cdbf71`](https://github.com/dimanu-py/instant-python/commit/8cdbf715da0bdd0eba8dc547af00285b68b3f717))

- **templates**: Modify test targets in makefile template to allow passing an optional path to run
  specific module
  ([`05a2089`](https://github.com/dimanu-py/instant-python/commit/05a2089c00374ae919f7be0082695a62d834d960))


## v0.23.2 (2026-06-05)

### 🪲 Bug Fixes

- **templates**: Remove extra '.md' from AGENTS.md project structure template
  ([`dda40ba`](https://github.com/dimanu-py/instant-python/commit/dda40bab7c5e1249e4306b608e91a90bb3f25f7d))


## v0.23.1 (2026-06-05)

### ⚙️ Build System

- Remove pinned dependencies that generated problems in the past
  ([`709490c`](https://github.com/dimanu-py/instant-python/commit/709490c3391f61a0f74fdd23803a27e84a5b77a2))

- Update dependencies due to detected vulnerabilities
  ([`77084a1`](https://github.com/dimanu-py/instant-python/commit/77084a14475798566e96895e29b69a6077cd54e0))

### ♻️ Refactoring

- **templates**: Update 'make upgrade' command when using uv to perfom uv lock --upgrade and uv sync
  --all-groups instead of uv sync --upgrade
  ([`3416e31`](https://github.com/dimanu-py/instant-python/commit/3416e315c471499d0afc14316679cffc5beecadf))

- **templates**: Update github actions versions in boilerplate templates
  ([`f913c6a`](https://github.com/dimanu-py/instant-python/commit/f913c6ad94940ea4470ba59d8939b92a4bded7bc))


## v0.23.0 (2026-06-05)

### ✨ Features

- **config**: Add new custom documentation to built in features selection
  ([`73f9976`](https://github.com/dimanu-py/instant-python/commit/73f99763c39082d1d9b9b1bf3d63eaf55976bdf1))

- **templates**: Introduce custom documentation structure in main default applications when is
  selected
  ([`a6a101d`](https://github.com/dimanu-py/instant-python/commit/a6a101d5b8171af2113bad93951486ba2bac56b1))

- **templates**: Specify documentation folder structure to be created when custom documentation
  feature is selected
  ([`482aa99`](https://github.com/dimanu-py/instant-python/commit/482aa99e84bf5edb2ea9e7b4059727ec51708d71))

- **templates**: Add github action to publish documentation to github pages when built in feature
  for custom docs is selected
  ([`bae3778`](https://github.com/dimanu-py/instant-python/commit/bae37789a0845a281ee6a6f1c791ded35ef8648e))

- **templates**: Add mkdocs dependencies to pyproject.toml template when custom documentation built
  in feature is selected
  ([`4c52158`](https://github.com/dimanu-py/instant-python/commit/4c52158fdb6e429dfb0be5815e312360c7b3ea67))

- **templates**: Add new command to makefile template to allow serving documentation locally when
  built in feature is selected
  ([`390b4f7`](https://github.com/dimanu-py/instant-python/commit/390b4f798dd8d1d3342dfaba3e89ca84286c9aa9))

- **templates**: Add mkdocs basic template with single Home section and common features
  ([`11901d8`](https://github.com/dimanu-py/instant-python/commit/11901d84b4c7b38fc419d61efd18f91ba36c33e1))

- **templates**: Add dependabot automatically when github actions built in feature is selected
  ([`08db5de`](https://github.com/dimanu-py/instant-python/commit/08db5de21af8bfa7decfed1572a5df94da785344))

- **templates**: Avoid installing dependencies newer than 3 days when uv is selected
  ([`feae9d7`](https://github.com/dimanu-py/instant-python/commit/feae9d790802b02bb723d2eecf6dd8d611ae9cc8))

### 🪲 Bug Fixes

- **templates**: Correct invalid time format when dependabot.yml is updated
  ([`aa4c67a`](https://github.com/dimanu-py/instant-python/commit/aa4c67a40bc858b6e0949dcfd3bf3980493e511c))

### ♻️ Refactoring

- **templates**: Update github actions versions in templates to newer versions and using commit sha
  ([`a6a96de`](https://github.com/dimanu-py/instant-python/commit/a6a96de5c49a8f94959f6222dd4a65beda47e210))


## v0.22.0 (2026-06-03)

### ✨ Features

- **config**: Add ai agents built in feature option to be selected when generating config file
  ([`9c87804`](https://github.com/dimanu-py/instant-python/commit/9c878045be4010923ef7599bb9b9b30c074e5f76))

- **templates**: Include agents built in feature in project main structure for the different default
  templates
  ([`022f676`](https://github.com/dimanu-py/instant-python/commit/022f676633d788eeef8db0e1fdf85840d2f9040a))

- **templates**: Add folder and file structure for agents built in feature
  ([`25d1ae5`](https://github.com/dimanu-py/instant-python/commit/25d1ae5ccfa667f541493930e571baa73a7ec380))

- **templates**: Add compatibility commands with CLAUDE and opencode agents when agents built in
  feature is selected
  ([`0dca00d`](https://github.com/dimanu-py/instant-python/commit/0dca00d288fc95d20ca31e3db30bc146b8d68bd2))

- **templates**: Add boilerplate with AI agents configuration, commands and skills
  ([`be65472`](https://github.com/dimanu-py/instant-python/commit/be65472f0ccb76576c05b12975b0a32f7a8e8dea))

- **templates**: Embed pytest config in pyproject.toml instead of generating separate pytest.ini
  ([`b589bd6`](https://github.com/dimanu-py/instant-python/commit/b589bd6f8335bbb1b82e82c78cae19807de18cf2))

- **templates**: Add dev dependency group with conditional includes for release, lint, and test
  ([`ae52934`](https://github.com/dimanu-py/instant-python/commit/ae52934819f198723e445c9335a7eef50d055870))

- **templates**: Migrate sindripy dependency when value_objects built in feature is selected to
  value-object-sindri
  ([`e941a39`](https://github.com/dimanu-py/instant-python/commit/e941a39f49bb5c70d40e601d52859c5a485c75e7))

### 🪲 Bug Fixes

- **metrics**: Evaluate correctly when init command has been executed with custom path to config
  file when sending metrics
  ([`7fe9c46`](https://github.com/dimanu-py/instant-python/commit/7fe9c468c6b5371525dc336a6fe2e714ee6de8d0))

- **metrics**: Avoid sending error as successfull metrics
  ([`3cb2fcf`](https://github.com/dimanu-py/instant-python/commit/3cb2fcfa86ac6e9e61489b965dae2a6e257fc91d))

- **tests**: Replace Typer CliRunner isolated_filesystem with standalone helper to fix
  AttributeError
  ([`d403571`](https://github.com/dimanu-py/instant-python/commit/d4035715f1bdc45a6a4f16249ec271bc330638b5))

- **templates**: Modify precommit template to create the file with 'yaml' format instead of 'yml'
  and avoid error
  ([`cb5cb5b`](https://github.com/dimanu-py/instant-python/commit/cb5cb5b8f94b877c9cf59593bbb3e99a4a7327d6))

- **templates**: Write python version in pre commit config file as a string instead of as a float to
  avoid error when executing precommit
  ([`0cc2506`](https://github.com/dimanu-py/instant-python/commit/0cc2506ded939a05786a7764e870f22144e7cde1))

### ⚙️ Build System

- Update uv.lock dependencies
  ([`340d09c`](https://github.com/dimanu-py/instant-python/commit/340d09cb1cf8db20f379f3a6375132b7f84368b5))

- **cli**: Add missing explicit dependencies
  ([`c4e46e0`](https://github.com/dimanu-py/instant-python/commit/c4e46e095bacddbe7cfb197f02a04ae941c15c08))

- Update dependencies versions
  ([`5dad140`](https://github.com/dimanu-py/instant-python/commit/5dad14074de3815404879a976b5a75d2956748af))


## v0.21.0 (2025-12-12)

### ✨ Features

- **metrics**: Set default values for api_key and host in PostHogConfig
  ([`8cfd3c2`](https://github.com/dimanu-py/instant-python/commit/8cfd3c23ebe08ec54bb06d8ed7f646a7d8105a13))

- **metrics**: Add metrics disabled check in PostHogMetricsReporter to prevent sending metrics when
  disabled
  ([`11e3cd3`](https://github.com/dimanu-py/instant-python/commit/11e3cd3f8a5e97065e54bf2d101647fb59d913a8))

- **config**: Add metrics_enabled field to configuration for controlling metrics collection
  ([`841cd9f`](https://github.com/dimanu-py/instant-python/commit/841cd9f73a8d6aa779a05f48cc160fe5f33d0123))

- **metrics**: Add error metrics handling in metrics middleware for improved exception tracking
  ([`7192e88`](https://github.com/dimanu-py/instant-python/commit/7192e88fc6c294065bd2c4d74223f0de552c0d6b))

- **metrics**: Implement error handling in send_error method for capturing exceptions
  ([`49d227f`](https://github.com/dimanu-py/instant-python/commit/49d227f700de0a550e7849a169f146df7fc33cde))

- **metrics**: Add error handling for command failures in usage metrics sender
  ([`364a731`](https://github.com/dimanu-py/instant-python/commit/364a7317b0ed8c08a29d7525f98366eae7715835))

- **metrics**: Create class to store all data related to error event
  ([`8174b3f`](https://github.com/dimanu-py/instant-python/commit/8174b3fc9f975cd338aeefcc0b28fb0cad86c180))

- **metrics**: Add send_error method to metrics reporter for error handling
  ([`c3e2cdb`](https://github.com/dimanu-py/instant-python/commit/c3e2cdb6676c23c8476cb222f7d37c0de1b05a84))

- **metrics**: Add ConfigSnapshotPrimitives type and to_primitives method
  ([`eb28115`](https://github.com/dimanu-py/instant-python/commit/eb28115bd5a3a62c3996d03fdc5f4fc3daadd168))

- **metrics**: Add snapshot creator instance inside metrics middleware
  ([`a7f4984`](https://github.com/dimanu-py/instant-python/commit/a7f498437b503bf956ed9f40b95f1c6ebf9deaf2))

- **metrics**: Add method to create unknown ConfigSnapshot and handle missing config file
  ([`4e17a87`](https://github.com/dimanu-py/instant-python/commit/4e17a8750b2c3d292da8d3280a4f25a4f521abda))

- **metrics**: Implement method to be able to compare two snapshots
  ([`ec00d47`](https://github.com/dimanu-py/instant-python/commit/ec00d47167a5a47bb34394ce02a2fc663f542fb9))

- **metrics**: Implement 'is_unknown' method in config snapshot class to determine if it has been
  properly read or not
  ([`910c8d1`](https://github.com/dimanu-py/instant-python/commit/910c8d1502fa076167092ecad57dfd93314a9ccf))

- **metrics**: Implement use case to create a snapshot of the configuration file
  ([`4ab1892`](https://github.com/dimanu-py/instant-python/commit/4ab18922bb15f5e73353ee646baa8be339445494))

- **shared**: Add 'for_metrics' method in config schema to be able to get only the data I need for
  metrics and not need to access all the internals of the class
  ([`feb27b7`](https://github.com/dimanu-py/instant-python/commit/feb27b77e9feab6c4a2b37bc5c790fb83544a2a2))

- **metrics**: Inject config repository to snapshot creator to be able to read an existing
  configuration file
  ([`e10e26c`](https://github.com/dimanu-py/instant-python/commit/e10e26cc0d46c46895cd4551897994a88f64008e))

- **metrics**: Create config snapshot class to store all the data related to the config file that
  will be sent to metrics
  ([`32db003`](https://github.com/dimanu-py/instant-python/commit/32db00308a09cecf12aa202574ad9e1a3f945d3b))

- **metrics**: Integrate MetricsMiddleware into InstantPythonTyper for enhanced command execution
  metrics
  ([`2b9db62`](https://github.com/dimanu-py/instant-python/commit/2b9db621867a196018afd6348c78e2b2adf0559a))

- **metrics**: Add MetricsMiddleware to handle command execution and send usage metrics data after
  command execution has finished
  ([`bdbbe00`](https://github.com/dimanu-py/instant-python/commit/bdbbe000e191ab72ca5c0eda97ba8a364346b5b4))

- **metrics**: Implement execute method in metrics sender use case to send usage metrics data
  ([`2fbecb8`](https://github.com/dimanu-py/instant-python/commit/2fbecb804c15b95228df6612abaadc5a74e50ef1))

- **metrics**: Validate distinct ID format when loading from metrics file
  ([`007c9d2`](https://github.com/dimanu-py/instant-python/commit/007c9d2958082d4b15d96eb0f5c0a4666153e24a))

- **metrics**: Handle JSON decoding errors and missing distinct ID in metrics file
  ([`c2e6be6`](https://github.com/dimanu-py/instant-python/commit/c2e6be60a8191b710402356daddac43c6cb8f30b))

- **metrics**: Retrieve distinct ID from metrics.json if it exists so an existing user does not
  generate a new id
  ([`9b52f46`](https://github.com/dimanu-py/instant-python/commit/9b52f469598ee8b197448693e4a94e91f8396ab1))

- **metrics**: Store distinct ID in metrics.json on first execution
  ([`da050c9`](https://github.com/dimanu-py/instant-python/commit/da050c94e57653fe56ad09e5aee3704d6e3638fb))

- **metrics**: Add UserIdentityManager to generate distinct user IDs
  ([`36ef740`](https://github.com/dimanu-py/instant-python/commit/36ef7401467d4b20502e0c6d19cc80ffe8e0c588))

- **metrics**: Implement fire-and-forget strategy for metric sending
  ([`6cc0761`](https://github.com/dimanu-py/instant-python/commit/6cc0761a8ca86d15472448f03724105cdb4e47e2))

- **metrics**: Enable sync mode for PostHog client initialization
  ([`51c52bc`](https://github.com/dimanu-py/instant-python/commit/51c52bc235f16a70c5f646d3445fecc889063d78))

- **metrics**: Capture event to be sent to posthog using a temporary distinct_id
  ([`db27119`](https://github.com/dimanu-py/instant-python/commit/db27119b567f438caf5444b0cc91e0a7872d85f1))

- **metrics**: Create posthog client inside reporter to be able to send metrics
  ([`59aa393`](https://github.com/dimanu-py/instant-python/commit/59aa3938c5c9c29af31b5f52f21245c5d0a058c5))

- **metrics**: Create post hog config class to handle env variables related with post hog
  ([`95a4516`](https://github.com/dimanu-py/instant-python/commit/95a4516df3defeb2f0b528b1a08d4f0426586869))

- **metrics**: Create dataclass to store all data related to usage metrics that will be send to
  posthog
  ([`0368a98`](https://github.com/dimanu-py/instant-python/commit/0368a98c71f82ab96db4e4bcb23e6142f6c3703a))

### ⚙️ Build System

- **pyproject**: Add platformdirs as production dependency as it's not built-in with all supported
  python versions
  ([`ef5dcf3`](https://github.com/dimanu-py/instant-python/commit/ef5dcf34c9b1b9c6f16e6a0e83f29d67898a6694))

- **pyproject**: Update dependencies to remove vulnerability
  ([`c858003`](https://github.com/dimanu-py/instant-python/commit/c858003272d4516a6b13e11f478a2cb9f2de895b))

- **pyproject**: Add vcr dependency to run posthog integration test without affecting current
  project
  ([`ccc11f0`](https://github.com/dimanu-py/instant-python/commit/ccc11f011ffe615c3b581c89de68db774c353033))

- **pyproject**: Add pydantic settings dependency to handle env variables gracefully
  ([`0b8b19f`](https://github.com/dimanu-py/instant-python/commit/0b8b19fd7c315403f134c08272ca5ad9f0d0813f))

### ♻️ Refactoring

- **metrics**: Streamline success metrics handling in metrics middleware
  ([`65962b6`](https://github.com/dimanu-py/instant-python/commit/65962b630f2b049b0aec1336991dc79cf4757587))

- **metrics**: Update send_error method to include error parameter
  ([`61210ac`](https://github.com/dimanu-py/instant-python/commit/61210acf4724a307a3b838821a59e00c06b97e87))

- **metrics**: Rename send method to send_success in metrics reporter
  ([`462db4c`](https://github.com/dimanu-py/instant-python/commit/462db4c55778647dc82fe7095cb20a5712083951))

- **metrics**: Rename execute method to execute_on_success
  ([`ac34809`](https://github.com/dimanu-py/instant-python/commit/ac34809dc85437768c9db23e429ddf44e2b622b5))

- **metrics**: Modify metrics middleware to take config snapshots to avoid errors when init command
  finished its execution and config file is moved
  ([`0716f62`](https://github.com/dimanu-py/instant-python/commit/0716f62fc01aaf4c598e3580714110fcb9807fbd))

- **metrics**: Enhance UsageMetricsEvent with dependency_manager and adjust built_in_features
  initialization
  ([`0281909`](https://github.com/dimanu-py/instant-python/commit/0281909b089a0bbfab5dc46dc8d0088e7ab0e59d))

- **metrics**: Update execute method to accept config_snapshot parameter and not need to read
  configuration file
  ([`ee03fc9`](https://github.com/dimanu-py/instant-python/commit/ee03fc9cb1e1c391caf0d650dbbe9514eaef9131))

- **metrics**: Rename UsageMetricsData to UsageMetricsEvent for clarity
  ([`24a47ab`](https://github.com/dimanu-py/instant-python/commit/24a47ab97fc30bd7f9ad43a4acbb6a3573b1dacc))

- **metrics**: Simplify UsageMetricsSender initialization by removing repository parameter
  ([`e5d5917`](https://github.com/dimanu-py/instant-python/commit/e5d5917df1044368f709183b0d5fa0a2c0bf41aa))

- **metrics**: Rename method to improve clarity in config reading
  ([`9468e1a`](https://github.com/dimanu-py/instant-python/commit/9468e1a4ed7d96ef69c4eae1b4a52f712fdb37b9))

- **metrics**: Update ConfigSnapshotCreator to utilize for_metrics method for improved config
  handling
  ([`2ce0140`](https://github.com/dimanu-py/instant-python/commit/2ce0140eda8234fdcf722b7d0ef3c48ee612ce59))

- **config**: Improve error handling in configuration file loading
  ([`1114c17`](https://github.com/dimanu-py/instant-python/commit/1114c17d570b989d85245dd0a032aeaf2a9af9f5))

- **metrics**: Extract configuration data handling into a separate method and streamline metrics
  data creation
  ([`e316523`](https://github.com/dimanu-py/instant-python/commit/e31652391e93f7da8c254a4e8283792eeb62f63e))

- **metrics**: Simplify execute method by removing success and error message parameters now that it
  will be handled automatically by posthog reporter
  ([`77469a9`](https://github.com/dimanu-py/instant-python/commit/77469a93fb411ef5ce6c8d000b25da1d2c9bc700))

- **metrics**: Rename get_distinct_id method to get_or_create_distinct_id for clarity
  ([`0a068c7`](https://github.com/dimanu-py/instant-python/commit/0a068c7e6903e00a590d76b058510627108be592))

- **metrics**: Rename metric reporter classes for consistency
  ([`15f122f`](https://github.com/dimanu-py/instant-python/commit/15f122f472c3e270e2ec3461be626c9b874eb12d))

- **metrics**: Remove success an error message data from metrics object as posthog is configured to
  report errors automatically
  ([`0f4eb0b`](https://github.com/dimanu-py/instant-python/commit/0f4eb0b94f5fbe63477a8da6586ad39d74219125))

- **metrics**: Update post hog metric reporter to use user identity manager and create consistent
  distinct ids
  ([`b5ad406`](https://github.com/dimanu-py/instant-python/commit/b5ad406236641adaad3590a767245caad610427f))

- **metrics**: Set config dir to be the .config folder of user system if is not passed and extract
  named variables to improve readability
  ([`2e54e8e`](https://github.com/dimanu-py/instant-python/commit/2e54e8edc72ca118f47222302d4fa6c2c2e94556))

- **metrics**: Modify distinct ID handling to improve readability and maintainability
  ([`aa8d52b`](https://github.com/dimanu-py/instant-python/commit/aa8d52b462f486c47a72a3c33cc2d392ae726249))

- **metrics**: Use usage metrics data class for send method in metric reporter
  ([`96393c2`](https://github.com/dimanu-py/instant-python/commit/96393c27088fbfb691b9c0fbb205bdd31f609ad2))


## v0.20.0 (2025-12-05)

### ✨ Features

- **schema**: Add JSON schema for custom project template structure to enable syntax and key/value
  detection
  ([`bf918b5`](https://github.com/dimanu-py/instant-python/commit/bf918b5b1efdcb9ddc38786814a5038144ca958b))

- **schema**: Add JSON schema for instant-python project configuration to enable syntax and
  key/value detection when modifying ipy config file manually
  ([`2e3d4f7`](https://github.com/dimanu-py/instant-python/commit/2e3d4f786020ead95324784497015e698477a891))

- **templates**: Add autostyle command to makefile to automatically format, lint and commit modified
  files
  ([`96c4610`](https://github.com/dimanu-py/instant-python/commit/96c46109c811198b70598df2c9f3e0674f6be1e7))

- **initialize**: Implement 'write' method in yaml config repository to be able to write ipy config
  file in working directory
  ([`ca04b4c`](https://github.com/dimanu-py/instant-python/commit/ca04b4c97392970399ed7b8a6e3a86984ed6779b))

- **initialize**: Add 'write' method to config repository to be able to use it with config command
  and move it to shared
  ([`e081a34`](https://github.com/dimanu-py/instant-python/commit/e081a342ccac66e45cef0cad728681c5aa9f301d))

### ⚙️ Build System

- **makefile**: Add command to makefile to automatically format, lint and commit modified files
  ([`2837703`](https://github.com/dimanu-py/instant-python/commit/28377039628f755b503192aef85723f3e3b4704c))

- **pyproject**: Add posthog dependency
  ([`b3df1c0`](https://github.com/dimanu-py/instant-python/commit/b3df1c0587709a39e9e702142bdad4e8e293b07a))

- **makefile**: Modify add-dep and remove-dep commands in makefile to not need scripts files
  ([`b9d5286`](https://github.com/dimanu-py/instant-python/commit/b9d528636f5a051c865f4ea45196443ff322b55e))

### ♻️ Refactoring

- **templates**: Rename all templates for project structure to remove the '.j2' extension as it is
  not need it
  ([`cde9f87`](https://github.com/dimanu-py/instant-python/commit/cde9f87670273e6711fd08919c525208e7075fd9))

- **initialize**: Modify file name for project structure template to not include j2 extension
  ([`e8cd1f1`](https://github.com/dimanu-py/instant-python/commit/e8cd1f1aadb637f0a359783f11f95b164ca4cbd8))

- **cli**: Modify main callback to print ipy help if no subcommand is called
  ([`1784a3d`](https://github.com/dimanu-py/instant-python/commit/1784a3d129253cd197640680fbd85351ff074ec8))

- **initialize**: Move config repository port and its adapter to shared folder so it can be properly
  shared among commands
  ([`438f89c`](https://github.com/dimanu-py/instant-python/commit/438f89cdf75ff58ce0477e88a54cad55ad4e93ae))

- **config**: Remove legacy config writer now that its behavior has been unified in the config
  repository
  ([`3bcd3c9`](https://github.com/dimanu-py/instant-python/commit/3bcd3c9d858e342d9deca9bdc7bcd5db766de94b))

- **config**: Extract semantic method to keep use case with the same abstraction level and make it
  more readable
  ([`7077e6a`](https://github.com/dimanu-py/instant-python/commit/7077e6a50a23df5e3d080b89265a935d83d8d68c))

- **config**: Modify config generator dependency to receive a config repository instead of a config
  writer
  ([`89ed351`](https://github.com/dimanu-py/instant-python/commit/89ed35135d679a4fb4375eece5329162c454fb91))

- **initialize**: Modify 'write' method so it uses absolute config file path instead of creating it
  ([`5acc795`](https://github.com/dimanu-py/instant-python/commit/5acc795ba127292d5144d18da3ba718faf880b9e))

- **shared**: Make default config file path absolute from users root folder to avoid incorrect
  destination and relative path errors
  ([`074e4a7`](https://github.com/dimanu-py/instant-python/commit/074e4a76f5319f2d167243935ca449a3ff80ca10))


## v0.19.1 (2025-11-27)

### 🪲 Bug Fixes

- **templates**: Correct indentation level for source and test templates in standard project
  ([`54b36ca`](https://github.com/dimanu-py/instant-python/commit/54b36cac14dc9a12157223207b47236b063262ef))

- **templates**: Remove aggregate and value object file from event bus folder structure now that
  these implementation have delegated to sindripy
  ([`13a7780`](https://github.com/dimanu-py/instant-python/commit/13a7780f0263edf83ac5751c26bf6d5f04073b2a))

- **templates**: Modify EventAggregate template to use Aggregate from sindripy instead of legacy
  aggregate that doesn't exist anymore
  ([`dcbf2d3`](https://github.com/dimanu-py/instant-python/commit/dcbf2d3f913327a2f909ab48526f32c958e26db2))

- **templates**: Include sindripy dependency when event bus feature is selected to be able to use
  the Aggregate implementation
  ([`b5c3000`](https://github.com/dimanu-py/instant-python/commit/b5c30002596fc639316f93d403b4bedc18cb1e7c))

### ♻️ Refactoring

- **templates**: Rename value objects template to errors now that it only contains errors and value
  objects are handled with sindripy
  ([`df8458b`](https://github.com/dimanu-py/instant-python/commit/df8458b18497574f48a075550e3d75e0a11e58e1))

- **templates**: Move new advanced macros to root of templates folder and use it along project
  structure templates
  ([`736314c`](https://github.com/dimanu-py/instant-python/commit/736314c5612b7d7518e780d8026951372a189755))

- **templates**: Remove legacy templates now that they are better organized
  ([`c1b6c44`](https://github.com/dimanu-py/instant-python/commit/c1b6c44a04837f06db6a4db91d1e6d389b352be5))

- **templates**: Update main templates for standard project structure using new macros and organized
  templates folder
  ([`4fe22f3`](https://github.com/dimanu-py/instant-python/commit/4fe22f3b4bb4efca55531b52b8612aa29d2a3047))

- **templates**: Add advanced macros to be able to reuse render logic for templates and avoid
  conditionals
  ([`76cc909`](https://github.com/dimanu-py/instant-python/commit/76cc9090ef73f7e17ef7736ec64a50a86d6dea65))

- **templates**: Separate and modularize structure of standard project template in layers
  ([`7123c85`](https://github.com/dimanu-py/instant-python/commit/7123c85bfbbabecd0ad1245b58ac668546343721))

- **templates**: Update main templates for ddd project structure using new macros and organized
  templates folder
  ([`613f361`](https://github.com/dimanu-py/instant-python/commit/613f36175902befddf45d8a0b56ef9069ae30df1))

- **templates**: Add advanced macros to be able to reuse render logic for templates and avoid
  conditionals
  ([`f96a178`](https://github.com/dimanu-py/instant-python/commit/f96a1787d978e6e56fae478a26ddf6d858f14da9))

- **templates**: Separate and modularize structure of ddd template in layers
  ([`66044d5`](https://github.com/dimanu-py/instant-python/commit/66044d56011e28b695b5a0b7af591415732ad426))

- **templates**: Move config files for projects templates to specific folder for better organization
  ([`5bc4e15`](https://github.com/dimanu-py/instant-python/commit/5bc4e15fcbdd6f20eaf69ffe24ae92866175c138))

- **templates**: Move github related templates to specific folder for better organization
  ([`ee42c25`](https://github.com/dimanu-py/instant-python/commit/ee42c2556037af6ba69bb0a973cf67c0659b9e0e))

- **templates**: Move fastapi templates to specific folders for better organization
  ([`7437c95`](https://github.com/dimanu-py/instant-python/commit/7437c9513f7e963e41f51a28a6ba90a432cef12c))

- **templates**: Move documentation templates such as readme, citation and security to specific
  folders for better organization
  ([`3608d27`](https://github.com/dimanu-py/instant-python/commit/3608d2777cd324a51f3d841cd5c92a651d6ee7e5))

- **templates**: Modify test structure to include application folder too
  ([`b0bc458`](https://github.com/dimanu-py/instant-python/commit/b0bc45873d3ee57b86282fccba8ddc89b54a1d80))

- **templates**: Remove conditional logic to include features in infra tests for clean architecture
  and use render_children_for macro to make it clearer and easier to extend
  ([`87fe7fc`](https://github.com/dimanu-py/instant-python/commit/87fe7fc32b65f8933699402d508a4770f5a0c748))

- **templates**: Update test infra template to include mock event bus from template
  ([`20fd887`](https://github.com/dimanu-py/instant-python/commit/20fd88768cd12acaea632bb6af16de37d9a1ae96))

- **templates**: Do not include mock event bus in test domain folder for clean architecture template
  ([`20e1d73`](https://github.com/dimanu-py/instant-python/commit/20e1d73cf632f022d8541b3ed625217cb17b15b1))

- **templates**: Modify template paths for event features pointing to better organized folders
  ([`35e56ac`](https://github.com/dimanu-py/instant-python/commit/35e56ac685d7d88fe7d0a3b2dcd54c9c409bde8a))

- **templates**: Organize events templates inside a specific folder to keep them better organized
  ([`2552a60`](https://github.com/dimanu-py/instant-python/commit/2552a60e49df586ec890a628e51db10002820907))

- **templates**: Update template paths in clean architecture project structure to use new organized
  persistence templates
  ([`ad4fced`](https://github.com/dimanu-py/instant-python/commit/ad4fced04cc5c127acbd2b2c96d79e514454d9ac))

- **templates**: Organize persistence templates inside a specific folder to keep them better
  organized
  ([`b3ff817`](https://github.com/dimanu-py/instant-python/commit/b3ff8170ad24c280796a3f21dac341bd4e7be95f))

- **templates**: Remove legacy templates for clean architecture structure now that new version is
  stable
  ([`d5293fc`](https://github.com/dimanu-py/instant-python/commit/d5293fc4ca28164859521978532554d34f22fa0b))

- **templates**: Modify jinja macro to be able to handle cases where one template file has to be
  included in more than once scenario so it's not get created two times
  ([`99e6572`](https://github.com/dimanu-py/instant-python/commit/99e6572e16e9388dc5e3491a1b8bc3dbfc11a25e))

- **templates**: Rename old main structure, source and test templates files to mark them as legacy
  but having them as backup
  ([`2ea3614`](https://github.com/dimanu-py/instant-python/commit/2ea361497d722b2eb15ad57d5bdaf2e44a2c1e6f))

- **templates**: Separate clean architecture source and test structure in separate folders to handle
  easily each folder and its features
  ([`f92b499`](https://github.com/dimanu-py/instant-python/commit/f92b4992b57ecdf62689b58a044264e298591452))

- **templates**: Write advanced macros to render children blocks and built in features for clean
  architecture
  ([`720bf69`](https://github.com/dimanu-py/instant-python/commit/720bf694ebfa12105d58f46549977dc072c786aa))


## v0.19.0 (2025-11-24)

### ✨ Features

- **cli**: Add logic to return installed version of instant python with --version flag
  ([`f083e18`](https://github.com/dimanu-py/instant-python/commit/f083e189a621c627bbac8611d2eaa03f4d08df20))


## v0.18.1 (2025-11-19)

### ♻️ Refactoring

- **initialize**: Improve error message when configuration file is not found
  ([`851f725`](https://github.com/dimanu-py/instant-python/commit/851f725e91482bc3a5d40aa96a7cd522955909ca))


## v0.18.0 (2025-11-17)

### ✨ Features

- **templates**: Add sindri value objects error handler for fastapi application if value objects
  feature is selected
  ([`8ac4773`](https://github.com/dimanu-py/instant-python/commit/8ac47733f7e33932a23be3bb5665275209d2ab50))

- **templates**: Remove value object folders from project structure templates
  ([`6029ca6`](https://github.com/dimanu-py/instant-python/commit/6029ca6fcb5fc565040bbdcf9bdb151787b15361))

- **templates**: Remove value object implementation templates now that this feature is provided by
  sindripy
  ([`1164d85`](https://github.com/dimanu-py/instant-python/commit/1164d85d5a0e5410f492b6e6f327946cde20345b))

- **templates**: Add sindripy to value_objects dependencies
  ([`b563be5`](https://github.com/dimanu-py/instant-python/commit/b563be513465603f45966b33e57bdb5b535c30b6))

### ♻️ Refactoring

- **templates**: Remove faker and random generator as it's not need it
  ([`0ba348b`](https://github.com/dimanu-py/instant-python/commit/0ba348bc5cd36ebb64c653f4ff32e1b8b17f76a5))

- **templates**: Stop including pytest if value objects feature is selected as it doesn't include
  tests anymore
  ([`c747731`](https://github.com/dimanu-py/instant-python/commit/c74773198cc939996e5e166e755a90e22865393a))

- **templates**: Include random generator template only if value objects feature is not selected
  ([`2ad49c3`](https://github.com/dimanu-py/instant-python/commit/2ad49c323f9596b854e85b46094d343f202f9de3))

- **templates**: Remove test value object templates from project structures now that it has been
  substituted by sindripy library
  ([`9e27b5b`](https://github.com/dimanu-py/instant-python/commit/9e27b5b792a9f2b28d1f582451d044f7c0195152))


## v0.17.0 (2025-11-12)

### ✨ Features

- **templates**: Include conftest with async session fixture when async sqlalchemy built in feature
  is included
  ([`b105b6a`](https://github.com/dimanu-py/instant-python/commit/b105b6a2ce1fcc2c8f0d4005d11e314fcf554422))

### 🪲 Bug Fixes

- **initialize**: Modify virtual environment creation with uv to install main and dev dependencies
  ([`73696f6`](https://github.com/dimanu-py/instant-python/commit/73696f6f63364c0497349e058ce6d063a21da8a0))

- **templates**: Include correctly logger templates when is selected in domain driven design
  ([`5348fe3`](https://github.com/dimanu-py/instant-python/commit/5348fe3624729997836a45c3196ec3d5554ab814))


## v0.16.0 (2025-11-12)

### ✨ Features

- **initialize**: Add resolve_import_path filter to jinja environment
  ([`22d7fa7`](https://github.com/dimanu-py/instant-python/commit/22d7fa7d9d671f21a9807e8f08ea5882f99eefcb))

- **initialize**: Add _resolve_import_path function to be able to get the full import path
  ([`1b284ab`](https://github.com/dimanu-py/instant-python/commit/1b284ab4821d3ff91c73bac00717dd96b366b566))

### 🪲 Bug Fixes

- **templates**: Include pydantic and pydantic settings deps by default when async sqlalchemy is
  selected
  ([`a8b1f5d`](https://github.com/dimanu-py/instant-python/commit/a8b1f5df7ffb96040ea0abaa78c4f884b6eaa097))

- **templates**: Correct import in domain_event_json_deserializer.py template
  ([`33a8864`](https://github.com/dimanu-py/instant-python/commit/33a88646e57251b7c818839388373a1c0ee9ca6d))

- **templates**: Correct templates names in event_bus_infra.yml.j2
  ([`41a49f8`](https://github.com/dimanu-py/instant-python/commit/41a49f8ddb5a7c456025e7996a511fe8f4fdb1fb))

- **templates**: Write correct names in GitHub action and value object templates
  ([`7b96b4c`](https://github.com/dimanu-py/instant-python/commit/7b96b4c0378a0b92cf65c5ad5d43ada73e87e4fa))

- **templates**: Import UUID inside uuid.py template
  ([`c5d0045`](https://github.com/dimanu-py/instant-python/commit/c5d0045defadf3d36f323a0e878dce32abc89b70))

- **templates**: Correct wrong indentation in dependencies in pyproject.toml file and write them in
  separate lines
  ([`60c6ca0`](https://github.com/dimanu-py/instant-python/commit/60c6ca059d99451a73287d147e107581c95e3f96))

### ♻️ Refactoring

- **templates**: Move persistence folder with postgres settings structure to its separate template
  and import it as expected in sqlalchemy and migrator
  ([`022ead8`](https://github.com/dimanu-py/instant-python/commit/022ead8119bcb53147e796311a6396643d1fb102))

- **templates**: Modify imports in boilerplate to import postgres settings from persistence
  ([`f5cefc3`](https://github.com/dimanu-py/instant-python/commit/f5cefc333c268a26cf8e95c7684df7dfda1c158c))

- **templates**: Write postgres settings file inside persistence folder instead of
  persistence/sqlalchemy
  ([`841f24e`](https://github.com/dimanu-py/instant-python/commit/841f24ea8c39967f759ae1b1e0210f4e50697ce4))

- **templates**: Include models metadata file only if async sqlalchemy has been included
  ([`ca892e6`](https://github.com/dimanu-py/instant-python/commit/ca892e61973761b6dba52ccdb813ea99a0e69a0b))

- **templates**: Remove extra empty lines in makefile template
  ([`1cb2153`](https://github.com/dimanu-py/instant-python/commit/1cb2153f6c7a59bebb751c5d07452a21faae75c8))

- **templates**: Update how development dependencies are set in the pyproject.toml template file
  ([`9613543`](https://github.com/dimanu-py/instant-python/commit/961354338756f6d8d2f95eaca173fdc540ecd67f))

- **templates**: Update how production dependencies are set in the pyproject.toml template file
  ([`7dd9be7`](https://github.com/dimanu-py/instant-python/commit/7dd9be7051cae7dacb7c780c072383410111602b))

- **templates**: Update pyproject.toml to support dynamic dependency manager and conditional ruff
  configuration
  ([`5209286`](https://github.com/dimanu-py/instant-python/commit/52092862625d8d75d920afabf266562f92c32fb5))

- **templates**: Modify github release workflow to use user's dependency manager to build library
  instead of hardcoding uv
  ([`6555ba1`](https://github.com/dimanu-py/instant-python/commit/6555ba12921c4e052bce1d64ed093cb339b8d6bb))

- **templates**: Modify default github ci workflow to use user's dependency manager to run tests
  instead of hardcoding uv
  ([`d2a8fd0`](https://github.com/dimanu-py/instant-python/commit/d2a8fd014e3988a0aa5874202a77d07e8b4bb3cd))

- **templates**: Modify makefile template to be easier to change with local variables
  ([`9ba8ead`](https://github.com/dimanu-py/instant-python/commit/9ba8eadc8578c2a93f0b6a21906d09adbb2abcc3))

- **templates**: Include pre push stages in pre commit hook file only if makefile built in feature
  is selected
  ([`e138a0e`](https://github.com/dimanu-py/instant-python/commit/e138a0ec765cabcb1cd7d028fa805a42916df8ef))

- **templates**: Simplify import statements using resolve_import_path filter
  ([`644da31`](https://github.com/dimanu-py/instant-python/commit/644da319a4a8694aa235ee855e0282f10e5a17a9))


## v0.15.2 (2025-11-10)

### 🪲 Bug Fixes

- **initialize**: Add warning for missing templates in file content
  ([`6574822`](https://github.com/dimanu-py/instant-python/commit/65748223287161c86d7e663e28a8f2a7bd786624))


## v0.15.1 (2025-11-10)

### 🪲 Bug Fixes

- **initialize**: Handle KeyError in template rendering
  ([`cedeb7b`](https://github.com/dimanu-py/instant-python/commit/cedeb7b065c6032a21490c9e256a882376fdfe3d))


## v0.15.0 (2025-11-10)

### ✨ Features

- **initialize**: Modify how custom project structure is discover but not making compulsory create a
  folder named 'custom'
  ([`e35d882`](https://github.com/dimanu-py/instant-python/commit/e35d8825083c5fe1a542b6fb3d39b0a5c9dea828))

- **initialize**: Ensure presence of pyproject.toml file in project structure
  ([`d677228`](https://github.com/dimanu-py/instant-python/commit/d677228541cf87838b899908c013ac4ff73f1d43))

- **shared**: Temporary remove source_path attribute in template section if custom template is
  selected
  ([`c6f9e0c`](https://github.com/dimanu-py/instant-python/commit/c6f9e0c9c4c6daa148e41ffdb6e353b1bb55e980))

- **initialize**: Modify 'move' method from yaml config repository to store config file always with
  the name ipy.yml even if it's a file created by the user
  ([`2e3d53f`](https://github.com/dimanu-py/instant-python/commit/2e3d53febea46247c0939aa61fb6c372eaec509e))

- **initialize**: Handle missing templates by setting content to None
  ([`deb6195`](https://github.com/dimanu-py/instant-python/commit/deb61959f62184f7e7881eabf0d17d4cc4749344))

- **shared**: Prompt user for custom template file path when selecting custom template
  ([`1b30673`](https://github.com/dimanu-py/instant-python/commit/1b3067327b20cc2937c932ab4f009730161bbba4))

- **shared**: Ensure source path is set for custom templates
  ([`5f51c83`](https://github.com/dimanu-py/instant-python/commit/5f51c8300ad70439007b5a2e7c79eaf8532166b9))

- **shared**: Add source path attribute to template config object
  ([`a3f5e40`](https://github.com/dimanu-py/instant-python/commit/a3f5e4066ffa8d14a220619f7c368ec75f7fbdc0))

- Delete old implementation for init command
  ([`c99e43d`](https://github.com/dimanu-py/instant-python/commit/c99e43dbd1a3195b02e386f6876a8b7b70b85fdb))

- **initialize**: Update path parameters to use Path type for improved type safety
  ([`8dc2bc2`](https://github.com/dimanu-py/instant-python/commit/8dc2bc21058bfbd803407639f7bec0cb06f9689b))

- **initialize**: Implement write method in YamlConfigRepository to move config file
  ([`39f6c88`](https://github.com/dimanu-py/instant-python/commit/39f6c88b856709c9e9a0b7c6c80e6f2f67321310))

- **initialize**: Remove config parameter from ProjectInitializer execute method
  ([`459c8c2`](https://github.com/dimanu-py/instant-python/commit/459c8c266135dc041d5a2af13ca13661dafb7b5e))

- **initialize**: Invoke repository write method in ProjectInitializer
  ([`20d1c1d`](https://github.com/dimanu-py/instant-python/commit/20d1c1dc027fb641a346739c95c563e4e679bbf3))

- **initialize**: Add config_path parameter to ProjectInitializer execute method
  ([`fa92d33`](https://github.com/dimanu-py/instant-python/commit/fa92d33f6789b546c0287571fe79c17fc89cb164))

- **repository**: Add write method to ConfigRepository interface
  ([`04ab916`](https://github.com/dimanu-py/instant-python/commit/04ab916492accc666a763adba74e213223524332))

- **config**: Update ConfigSchema class to allow instantiation from primitives and validate content
  structure to avoid inconsistent data
  ([`a6dc931`](https://github.com/dimanu-py/instant-python/commit/a6dc9311f1d363294ee1a35e5a08844b0fd818d6))

- **initialize**: Add 'execute_or_raise' method to SystemConsole to encapsulate command execution
  and error handling when needed
  ([`87f2b6f`](https://github.com/dimanu-py/instant-python/commit/87f2b6ff55bf0d26176b5d842cf9efba549d8844))

- **initialize**: Add property to check if version control needs initialization
  ([`ac41ab0`](https://github.com/dimanu-py/instant-python/commit/ac41ab07d407193f579cb5f6e3d9067d298822ba))

- **initialize**: Conditionally initialize git repository based on config setting
  ([`187f334`](https://github.com/dimanu-py/instant-python/commit/187f33432b4300ff97dfa290a94ba0e152035888))

- **initialize**: Integrate version control setup in ProjectInitializer
  ([`0a706c2`](https://github.com/dimanu-py/instant-python/commit/0a706c2b020821718638d62b15fa8ac7bda0f17c))

- **initialize**: Inject VersionControlConfigurer into ProjectInitializer
  ([`5cf1669`](https://github.com/dimanu-py/instant-python/commit/5cf16697aa9864019aa8f7958fc53ffb0d13b620))

- **initialize**: Add abstract VersionControlConfigurer class for git configuration setup
  ([`43a24a5`](https://github.com/dimanu-py/instant-python/commit/43a24a58d7751d1a03b410592fcfc8541a1ba3f7))

- **initialize**: Add abstract ProjectFormatter class for project formatting
  ([`ab8c177`](https://github.com/dimanu-py/instant-python/commit/ab8c1777ae31bc9673be26adefd6354f5db71036))

- **initialize**: Add error handling for command execution in RuffProjectFormatter
  ([`2bc7b2d`](https://github.com/dimanu-py/instant-python/commit/2bc7b2d58fa776ff0a0e69872f25babccadd39b6))

- **initialize**: Call formatter after project configuration for improved output formatting
  ([`7c467cd`](https://github.com/dimanu-py/instant-python/commit/7c467cd72bc578ee2b6c2c21fa8d7925dd7d1efa))

- **initialize**: Use console when is injected to install uv
  ([`8feeb28`](https://github.com/dimanu-py/instant-python/commit/8feeb28e8a015c2aac625b59afb4d15ce0b11670))

- **initialize**: Use console when is injected to install dependencies
  ([`e74c046`](https://github.com/dimanu-py/instant-python/commit/e74c0464bfaeeeac7213de10bff99cbe91200e78))

- **initialize**: Use console when is injected to create virtual environment
  ([`38f85ab`](https://github.com/dimanu-py/instant-python/commit/38f85ab218c16d7537e80c1ad8bf4cf2fb92d784))

- **initialize**: Use console when is injected to install python version
  ([`8eb81e4`](https://github.com/dimanu-py/instant-python/commit/8eb81e407c372c603be3c68ae79687afd6eaaace))

- **initialize**: Use console when is injected to check if uv has been installed
  ([`f202a3d`](https://github.com/dimanu-py/instant-python/commit/f202a3d97056eb81b48ef356b84a98106de40013))

- **initialize**: Inject system console to uv manager
  ([`a5b6dae`](https://github.com/dimanu-py/instant-python/commit/a5b6daedc080276f8c39aa82d67a7b0df2982dbd))

- **initialize**: Handle unexpected errors during command execution
  ([`951398c`](https://github.com/dimanu-py/instant-python/commit/951398c2a6ea07848c5e7bc98d734df4b704ee33))

- **initialize**: Add method to CommandExecutionResult to know if it has succeeded or not
  ([`6dd97dc`](https://github.com/dimanu-py/instant-python/commit/6dd97dc085f4d1c254ffdf4b029b6af1efb59ca8))

- **initialize**: Implement command execution using subprocess
  ([`1bad062`](https://github.com/dimanu-py/instant-python/commit/1bad062dcac0f61aa2167d82bd34e96cee5d306a))

- **initialize**: Modify EnvManager interface to adhere to previous DependencyManager manager to
  keep the same behavior until refactor
  ([`09d68fc`](https://github.com/dimanu-py/instant-python/commit/09d68fcdfbd630054b8b42d3bcc96dbfd7a2e79b))

- **initialize**: Integrate EnvManager into ProjectInitializer for environment setup
  ([`e307135`](https://github.com/dimanu-py/instant-python/commit/e3071354d0bef7316cd5b9d1052f9870b0d13783))

- **initialize**: Introduce abstract Node class with create method for extensibility
  ([`8fbde36`](https://github.com/dimanu-py/instant-python/commit/8fbde36ab47a7ece26d79377af13229926d603e6))

- **initialize**: Implement directory and file creation methods in FileSystemNodeWriter
  ([`126f87c`](https://github.com/dimanu-py/instant-python/commit/126f87c8f202d4d1cfaa3c56742290322321a9f8))

- **initialize**: Add FileSystemNodeWriter for directory and file creation
  ([`6d555da`](https://github.com/dimanu-py/instant-python/commit/6d555da88f086f05457b7ddd4a3a4f5fd6c415d2))

- **initialize**: Implement recursive creation of child nodes in directory
  ([`94a0a46`](https://github.com/dimanu-py/instant-python/commit/94a0a46e3b1e9c8639facd159b59108f8fcc7de6))

- **initialize**: Add support for creating __init__.py in Python modules
  ([`45d77c2`](https://github.com/dimanu-py/instant-python/commit/45d77c2a91fb7e1c120f5bfc8a0debc274cbe0af))

- **initialize**: Add create method to handle directory creation with NodeWriter
  ([`f97ebb1`](https://github.com/dimanu-py/instant-python/commit/f97ebb185dd43309e4441fcfcf3920de455f2efc))

- **initialize**: Add create method to handle file creation using NodeWriter
  ([`dd741c4`](https://github.com/dimanu-py/instant-python/commit/dd741c4a44a4092caa3a78c05802d99ff78de2eb))

- **initialize**: Create abstract base class for file and directory creation
  ([`339ca96`](https://github.com/dimanu-py/instant-python/commit/339ca961bb4aab8f1a492ac98c02a85116bb4f6a))

- **initialize**: Add support for creating files in the file system
  ([`7845c4d`](https://github.com/dimanu-py/instant-python/commit/7845c4d47188c0e13fbc5796042921afb252373e))

- **writer**: Implement write method to create directories and __init__.py for Python modules
  ([`d720f7d`](https://github.com/dimanu-py/instant-python/commit/d720f7db78d24e273daa0808cf9b5d0af65e0889))

- **initialize**: Modify project initializer use case to receive the folder where the project will
  be created
  ([`b507bc4`](https://github.com/dimanu-py/instant-python/commit/b507bc4d263ccdb1db97bbc5e9b3bc6a2fa17b9f))

- **initialize**: Write project structure using writer
  ([`c9952ba`](https://github.com/dimanu-py/instant-python/commit/c9952baa7d070eb84c1365153ffcddde91d65299))

- **initialize**: Add ProjectWriter dependency to ProjectInitializer
  ([`16a645c`](https://github.com/dimanu-py/instant-python/commit/16a645c6560e4315de1f52413ce51eba12cd746c))

- **initialize**: Make Directory iterable through iteration of its children
  ([`0c4bf05`](https://github.com/dimanu-py/instant-python/commit/0c4bf05f5c122bafca870a42f856ef166873d390))

- **initialize**: Add flatten method to ProjectStructure for iterating through nodes
  ([`724b96c`](https://github.com/dimanu-py/instant-python/commit/724b96cfa6dff7bdd00599787306c57be0fa660d))

- **initialize**: Modify ProjectRenderer port and adapter signatures to return a ProjectStructure
  ([`b0c251f`](https://github.com/dimanu-py/instant-python/commit/b0c251f7df1820240b81ef74375c808d9ee34cef))

- **initialize**: Add __iter__ and __len__ methods to ProjectStructure class to be able to iterate
  through them
  ([`d733664`](https://github.com/dimanu-py/instant-python/commit/d733664053ee8f13e0da2756659415d8cf6e7091))

- **initialize**: Implement ProjectStructure class for building project nodes
  ([`a8a36c2`](https://github.com/dimanu-py/instant-python/commit/a8a36c29a92d847e59b81c043bb355cfaf9dbc11))

- **initialize**: Add Directory class with path building and representation methods
  ([`bdfcd14`](https://github.com/dimanu-py/instant-python/commit/bdfcd143205a16da9f2ae5d0a8a961b78f052180))

- **initialize**: Add __repr__ method to File class
  ([`2e88d75`](https://github.com/dimanu-py/instant-python/commit/2e88d75f678d5d422efed04f836723c751431363))

### 🪲 Bug Fixes

- **initialize**: Add pyproject file to standard template in acceptance tests
  ([`1a9e6e3`](https://github.com/dimanu-py/instant-python/commit/1a9e6e3531b07d2d865a8899b27ebcf26ccc021e))

- **initialize**: Use file name and extension as default template name if not provided in file node
  ([`e07a2cb`](https://github.com/dimanu-py/instant-python/commit/e07a2cb6129aea90f4720b7268f1b647ec544e24))

- **templates**: Correct template path for value_object in YAML configuration
  ([`cd4d6a4`](https://github.com/dimanu-py/instant-python/commit/cd4d6a4b956adb7f82131512b5e39f6d15a46d83))

- **templates**: Write correct template name for python version file
  ([`b6adb23`](https://github.com/dimanu-py/instant-python/commit/b6adb236ce1cea9b021f2b4296321c04d5c87ecd))

- **templates**: Remove 'project_structure/' prefix from all templates
  ([`60cecf0`](https://github.com/dimanu-py/instant-python/commit/60cecf08ea9592a3733aa8511343acb055562024))

- **initialize**: Introduce UnknownTemplateError
  ([`d507ed7`](https://github.com/dimanu-py/instant-python/commit/d507ed726ccc4cddc5be75a7dd68a28d644c06e1))

- **initialize**: Introduce UnknownNodeTypeError
  ([`b155055`](https://github.com/dimanu-py/instant-python/commit/b1550557508b6af6b8377530c1e000bc0bf7beb0))

- **templates**: Format templates correctly so ruff formatter does not fail
  ([`30bb6b1`](https://github.com/dimanu-py/instant-python/commit/30bb6b1cbeaf5969eace22f40997af95db1bfd4a))

- **initialize**: Improve error message formatting for command execution failures
  ([`d8bfc8d`](https://github.com/dimanu-py/instant-python/commit/d8bfc8dcafb8d6a35133eb4c138e1c80fbd60ae9))

- **initialize**: Correct failing uv test due to interface change
  ([`a65910f`](https://github.com/dimanu-py/instant-python/commit/a65910f7a207c96d23f75077c479d600756ca357))

- **initialize**: Update import of NodeWriter to be conditional for type checking
  ([`1afe2ad`](https://github.com/dimanu-py/instant-python/commit/1afe2adc7d2d50afcd3838d5e3e4a37f504a30cb))

### ⚙️ Build System

- Fix misspelling in pyproject.toml pytest config section
  ([`84cf27c`](https://github.com/dimanu-py/instant-python/commit/84cf27ce01d6aca47f79f90e572f6220c3e62b1e))

### ♻️ Refactoring

- **shared**: Remove unused methods from ConfigSchema class
  ([`5ef231f`](https://github.com/dimanu-py/instant-python/commit/5ef231fd3d36ce1801cdf4d0c9d84d0e9af4b0a9))

- Inline all messages in call to super method in application errors
  ([`3980af5`](https://github.com/dimanu-py/instant-python/commit/3980af5bc6252bf036838c431d2ac456d548105a))

- **shared**: Delete error types enum
  ([`9ef7981`](https://github.com/dimanu-py/instant-python/commit/9ef798172abce517ddec1bcfa9e2558657ea0642))

- **shared**: Remove 'type' attribute in application errors as it's not used
  ([`00674fa`](https://github.com/dimanu-py/instant-python/commit/00674fa87a429330c1ee1de3d36d19f016dd3a70))

- **initialize**: Streamline project setup process by modularizing methods
  ([`f9f0632`](https://github.com/dimanu-py/instant-python/commit/f9f063286bfaf95b29e6fe1f1b7f13a2f81f3d21))

- **config**: Move ConfigSchema domain object to shared folder
  ([`fbd8bd0`](https://github.com/dimanu-py/instant-python/commit/fbd8bd0febca0f1890e991f364429e4036f64e87))

- **initialize**: Delete config reader use case
  ([`2bfe0cc`](https://github.com/dimanu-py/instant-python/commit/2bfe0cc824ca166ea8130ed9baac24861dd2ff96))

- **initialize**: Rename destination_path to base_directory for clarity
  ([`bc96230`](https://github.com/dimanu-py/instant-python/commit/bc96230ecffab2407fd68c12a2e57f5107283032))

- **cli**: Update working directory handling for project initialization
  ([`b9025e8`](https://github.com/dimanu-py/instant-python/commit/b9025e8a359841388d220caac691bca32f23be93))

- **initialize**: Add custom error for missing configuration files
  ([`1daec9d`](https://github.com/dimanu-py/instant-python/commit/1daec9dcc27a456022fea9e09cc7d3cb299bf760))

- **initialize**: Rename write method to move for clarity
  ([`f29dbaa`](https://github.com/dimanu-py/instant-python/commit/f29dbaabda7caccbd42ea8a0a21413685ad54410))

- **initialize**: Allow optional user template path in initializer
  ([`6b722e2`](https://github.com/dimanu-py/instant-python/commit/6b722e2cc852d1d40b9de4e57a5aa9e72566751c))

- **initialize**: Streamline project initialization by integrating ProjectInitializer and
  simplifying config handling
  ([`791a841`](https://github.com/dimanu-py/instant-python/commit/791a8410fe8ca06e808d6408f72f40c65989cc73))

- **templates**: Add 'template' field to all templates structures
  ([`745bcd7`](https://github.com/dimanu-py/instant-python/commit/745bcd76ee6efdf5a400d20b59e08d431184fcd8))

- **initialize**: Remove repository dependency and update execute method signature
  ([`148d3bb`](https://github.com/dimanu-py/instant-python/commit/148d3bb4afed116be36cc71066562f16fe7f1d5d))

- **initialize**: Simplify project creation by removing custom template option
  ([`ca697d0`](https://github.com/dimanu-py/instant-python/commit/ca697d0a9d1b58779edc114b14530fca80e2bf04))

- **initialize**: Change config_file_path type to str and convert to Path in execute method
  ([`961b162`](https://github.com/dimanu-py/instant-python/commit/961b162df244136d0771edb18897474038782458))

- **repository**: Rename config_repository to yaml_config_repository and update imports
  ([`688937a`](https://github.com/dimanu-py/instant-python/commit/688937a66f1caa239298509f1efbd9f7a86caa23))

- **config**: Update ConfigRepository to return ConfigSchema instead of dict
  ([`4d5e4ed`](https://github.com/dimanu-py/instant-python/commit/4d5e4ed1e6fa7584f5c4e6dbe27e5bb33223ba25))

- **initialize**: Add ConfigRepository dependency to ProjectInitializer
  ([`440a420`](https://github.com/dimanu-py/instant-python/commit/440a420143b5f5a21777f8ad036a8e88c89c1221))

- **config**: Remove parser port and adapter now that config schema validates structure
  ([`d228200`](https://github.com/dimanu-py/instant-python/commit/d22820066f8437f87e9eab4c9e79e66a9ae2a54a))

- **initialize**: Simplify ConfigReader by removing parser dependency and using ConfigSchema for
  configuration parsing
  ([`ed8b871`](https://github.com/dimanu-py/instant-python/commit/ed8b871dd15b2bd7944315d996c4ebecd2ad2f55))

- **config**: Modify config generator to instantiate a ConfigSchema instead of using parser
  ([`4ac7e15`](https://github.com/dimanu-py/instant-python/commit/4ac7e158bb812c413927e5844f10d2ce19385fcd))

- **config**: Move ConfigKeyNotPresent and EmptyConfigurationNotAllowed to config_schema.py
  ([`0ecb482`](https://github.com/dimanu-py/instant-python/commit/0ecb48244e31c3b8b7c7f27bb7f90e6d43bbb271))

- **initialize**: Replace command execution with execute_or_raise for improved error handling in pdm
  env manager
  ([`4903ece`](https://github.com/dimanu-py/instant-python/commit/4903ece3c63a9485d01ea8086400b3799b4d7db2))

- **initialize**: Replace command execution with execute_or_raise for improved error handling in uv
  env manager
  ([`2972f57`](https://github.com/dimanu-py/instant-python/commit/2972f57083c8fa8e9e3ce01f341f69a2698d5d00))

- **initialize**: Replace command execution with execute_or_raise for improved error handling
  ([`506cd56`](https://github.com/dimanu-py/instant-python/commit/506cd561d2be59e537a46d46019b55fe1b4ca0a4))

- **initialize**: Modify GitConfigurer internal methods to use 'execute_or_raise' from console for
  those commands that can fail
  ([`3c18406`](https://github.com/dimanu-py/instant-python/commit/3c18406d27da61b4633f5a239a5540468aaf6514))

- **initialize**: Inject console into GitConfigurer and update setup method
  ([`551419c`](https://github.com/dimanu-py/instant-python/commit/551419c35e4070c2477ac1767110989611ab132a))

- **initialize**: Remove project_directory parameter from GitConfigurer
  ([`d376364`](https://github.com/dimanu-py/instant-python/commit/d37636439f2ed519a40ff5037b4914f02bc245dd))

- **initialize**: Remove unused _run_command method from GitConfigurer
  ([`ac76479`](https://github.com/dimanu-py/instant-python/commit/ac76479eb0e3a116bcf2806447c17b294ac675c2))

- **initialize**: Streamline command execution by removing console checks in GitConfigurer methods
  ([`cd88a92`](https://github.com/dimanu-py/instant-python/commit/cd88a9233da914e6399ca200c446e146884e4eff))

- **initialize**: Use console when is injected to execute git commands
  ([`1299f0a`](https://github.com/dimanu-py/instant-python/commit/1299f0a6483342cfd8cf329ed754a8b5bc14f2ad))

- **initialize**: Add console parameter to GitConfigurer constructor
  ([`4f9e9e9`](https://github.com/dimanu-py/instant-python/commit/4f9e9e9baa4aef3b796c7037f8b1191357f11063))

- **initialize**: Rename setup_repository to setup and update parameter naming
  ([`4bff249`](https://github.com/dimanu-py/instant-python/commit/4bff249562649645babb821ae66061346ef07847))

- **initialize**: Reorganize git configurer imports and file structure
  ([`e894a87`](https://github.com/dimanu-py/instant-python/commit/e894a87b899481a5e484c905dfafa61f1720ccaa))

- **initialize**: Make RuffProjectFormatter inherit from ProjectFormatter
  ([`278b16e`](https://github.com/dimanu-py/instant-python/commit/278b16e89344f8159f2663868c4dd4383776d2dc))

- **initialize**: Reorganize CommandExecutionError import and remove redundant definitions
  ([`b8f1074`](https://github.com/dimanu-py/instant-python/commit/b8f1074e20cf2900b5fe6a69ad32a857f5b50e8d))

- **initialize**: Inject console into RuffProjectFormatter
  ([`4e147b7`](https://github.com/dimanu-py/instant-python/commit/4e147b788411ef67c6bd036d05129f2746807237))

- **initialize**: Remove project_directory parameter from RuffProjectFormatter
  ([`0a6d292`](https://github.com/dimanu-py/instant-python/commit/0a6d292de9bb733b3d67260c264a4c004410763b))

- **initialize**: Use console when is injected to run format command
  ([`f87905c`](https://github.com/dimanu-py/instant-python/commit/f87905cfd83472e4bc299479272a3740fabfb9ce))

- **formatter**: Add console parameter to RuffProjectFormatter for enhanced flexibility
  ([`b741778`](https://github.com/dimanu-py/instant-python/commit/b7417781d08f39e0543aafb398eab92aa26417f5))

- **initialize**: Rename ProjectFormatter to UvxProjectFormatter and update references
  ([`bf3078c`](https://github.com/dimanu-py/instant-python/commit/bf3078c04f85cc58dedea911ab0ff0283aeeac4d))

- **initialize**: Move ProjectFormatter to initialize.infra for better organization
  ([`8be7870`](https://github.com/dimanu-py/instant-python/commit/8be787092f02ada1584c251332c6ab5452e5f909))

- **initialize**: Add ProjectFormatter to ProjectInitializer for enhanced project formatting
  ([`2603d66`](https://github.com/dimanu-py/instant-python/commit/2603d665c75a5618416941086c014ee2034126ad))

- **initialize**: Inject console instance into env manager factory instead of passing project folder
  path
  ([`bc695ef`](https://github.com/dimanu-py/instant-python/commit/bc695eff244709a8fdd6843e7b0afcb1e1e5a969))

- **initialize**: Remove 'project_directory' attribute from env managers as is console who executes
  the commands
  ([`327922f`](https://github.com/dimanu-py/instant-python/commit/327922f9d6bab25f2cce1e475350f560d13dbfe2))

- **initialize**: Replace subprocess calls with SystemConsole for command execution in pdm env
  manager
  ([`fba2167`](https://github.com/dimanu-py/instant-python/commit/fba2167a5210ff7ed32f24097344509e74cd4a10))

- **initialize**: Extract method to encapsulate all the logic executed to install one dependency
  ([`750f7e7`](https://github.com/dimanu-py/instant-python/commit/750f7e785776e812e115b1cf8ccd75d5976aef1c))

- **initialize**: Extract method for raising command execution error
  ([`02edb57`](https://github.com/dimanu-py/instant-python/commit/02edb57777f0d3037db96e7b17e5c526d281856f))

- **initialize**: Remove unused subprocess command execution method
  ([`380bb4f`](https://github.com/dimanu-py/instant-python/commit/380bb4fc78ff042bcd82d50e5032ec8743ceb70c))

- **initialize**: Simplify setup method by removing unnecessary try-except block
  ([`88bb72a`](https://github.com/dimanu-py/instant-python/commit/88bb72aa61ed4e3a006ad33a222713fac19ebcd3))

- **initialize**: Clean up UvEnvManager removing old implementation that run directly commands in
  the console
  ([`699db31`](https://github.com/dimanu-py/instant-python/commit/699db31414748d6e428bbae7f1dc8377ec8c0936))

- **initialize**: Pull down _run_command and attributes from EnvManager to leave it as a pure
  interface and begin refactor to inject SystemConsole
  ([`b197e68`](https://github.com/dimanu-py/instant-python/commit/b197e68b622a719ac13c5ed63c67dbd71ee4fcd3))

- **initialize**: Extract command execution method to run commands
  ([`1753fd4`](https://github.com/dimanu-py/instant-python/commit/1753fd40e05f984be3e5943bd1649c2e1312ce13))

- **initialize**: Enhance error message for unknown dependency managers
  ([`e1dcb29`](https://github.com/dimanu-py/instant-python/commit/e1dcb290a70b7999b4b57dc34017671b4eedfcd2))

- **dependency-manager**: Remove old files for dependency manager concept
  ([`41b2558`](https://github.com/dimanu-py/instant-python/commit/41b255870f8138e3abcd7f71e68821348f364a33))

- **initialize**: Move previous implementation for dependencies managers to env manager concept in
  new initialize command architecture
  ([`aacc3d3`](https://github.com/dimanu-py/instant-python/commit/aacc3d3d4e864be902d732d6080d78da7b453bae))

- **initialize**: Remove config parameter from write method in ProjectWriter and
  FileSystemProjectWriter
  ([`d30d142`](https://github.com/dimanu-py/instant-python/commit/d30d142b68e80f2459a80a64d358485b972ec65f))

- **initialize**: Convert File and Directory classes to inherit from Node
  ([`6abad70`](https://github.com/dimanu-py/instant-python/commit/6abad7077d45d212d070683ecb5c15ae0ffc3073))

- **initialize**: Rename nodes module to node and update imports
  ([`f91b46c`](https://github.com/dimanu-py/instant-python/commit/f91b46c0cfe59949e51ee274eb693766126694e1))

- **initialize**: Simplify node writing logic by delegating to node's create method
  ([`ad2b780`](https://github.com/dimanu-py/instant-python/commit/ad2b78082da62cbb6b2fbed01194f86cea23604a))

- **initialize**: Rename build_path_for to _build_path_for and update create method
  ([`5fc167d`](https://github.com/dimanu-py/instant-python/commit/5fc167de71228d2e2003336bed8c8cc2a33d5654))

- **initialize**: Convert 'build_path_for' method in File to protected as now it wont be accessed
  from outside
  ([`f211a85`](https://github.com/dimanu-py/instant-python/commit/f211a857047072f33575406da612463142637bf4))

- **initialize**: Build path for file and directory using Path instead of string
  ([`a0ca50c`](https://github.com/dimanu-py/instant-python/commit/a0ca50c0fe6e36374bd0b481b756f7c00ffcf126))

- **initialize**: Update import statement for NodeType in jinja_project_renderer.py
  ([`6c1531c`](https://github.com/dimanu-py/instant-python/commit/6c1531c43899c9f82d027c2b12d9bcbaeaf938a9))

- **initialize**: Update jinja project renderer to return ProjectStructure using named constructor
  ([`6e20b78`](https://github.com/dimanu-py/instant-python/commit/6e20b78fe29767f70ea95a0a3516239b611d80e5))

- **initialize**: Modify project structure constructor to receive the list of Nodes and implement a
  named constructor to build the nodes from raw structure
  ([`2eeba6f`](https://github.com/dimanu-py/instant-python/commit/2eeba6fbb87186c039a3852ae5d1fd81a9f5698c))


## v0.14.0 (2025-11-03)

### ✨ Features

- **templates**: Add new template that implements a general way of getting async sessions
  ([`0f6d37e`](https://github.com/dimanu-py/instant-python/commit/0f6d37e1ae9cf676c41719bd7c39e7056b15d15c))

- **initialize**: Implement build_path_for method to construct file paths
  ([`f1f253f`](https://github.com/dimanu-py/instant-python/commit/f1f253f1cd255b416bb7f337e7dcd85db8c4cf09))

- **initialize**: Enhance project structure rendering by adding template content to files
  ([`8b6c98c`](https://github.com/dimanu-py/instant-python/commit/8b6c98c35a4572f905bfae9a52e744cf02af7817))

- **initialize**: Implement rendering of project structure using YAML template
  ([`6d93e9a`](https://github.com/dimanu-py/instant-python/commit/6d93e9a61d2822068163cfe983be8c9ea189b3a4))

- **initialize**: Enhance JinjaEnvironment to support multiple template loaders
  ([`5b69e4f`](https://github.com/dimanu-py/instant-python/commit/5b69e4f7c35b526b8de41b663108918c2d2ffba3))

- **initialize**: Implement render_template method in JinjaEnvironment
  ([`860bc0b`](https://github.com/dimanu-py/instant-python/commit/860bc0b6285c0bf4ec36d9c20d3c6febf71d0a37))

- **initialize**: Add render_template method to JinjaEnvironment with placeholder implementation
  ([`4c67ad3`](https://github.com/dimanu-py/instant-python/commit/4c67ad300473719fbac6f8dab3470407dc1c5559))

- **initialize**: Set FileSystemLoader with user_template_path in JinjaEnvironment
  ([`d6ef776`](https://github.com/dimanu-py/instant-python/commit/d6ef7766adcc89ef03f8ad2905931fc8541b949e))

- **initialize**: Add user_template_path parameter to JinjaEnvironment constructor
  ([`42d34ac`](https://github.com/dimanu-py/instant-python/commit/42d34ac4a46c097a7dca0f75175e7ad64b3ca98c))

- **initialize**: Add custom filters for jinja and load them by default in jinja env
  ([`4194509`](https://github.com/dimanu-py/instant-python/commit/419450927edd6b3e81199b7301ebdad25fbfb8b2))

- **initialize**: Add method to register custom filters in jinja environment
  ([`ec1d01a`](https://github.com/dimanu-py/instant-python/commit/ec1d01a84faa2c65618938ccbd47d46f3026dddc))

- **initialize**: Add test to verify jinja environment loads custom filters
  ([`31ff4a5`](https://github.com/dimanu-py/instant-python/commit/31ff4a50d1a6b8dff97813ccc4fe99db4376301b))

- **initialize**: Instantiate jinja 2 environment inside wrapper class
  ([`c0f7ec0`](https://github.com/dimanu-py/instant-python/commit/c0f7ec0d39f721d999cd4a9330c3fab7c32192c9))

- **initializer**: Implement project structure rendering in execute method
  ([`a91b8ae`](https://github.com/dimanu-py/instant-python/commit/a91b8ae66e81291b56963b8e9ea39eb47618daba))

### 🪲 Bug Fixes

- **templates**: Correct spelling error in sqlalchemy repository template
  ([`97f6003`](https://github.com/dimanu-py/instant-python/commit/97f6003a4b89d9553e969bce9794ce3f0e59ac17))

- **initialize**: Search for default template that is at first level of boilerplate folder
  ([`841badc`](https://github.com/dimanu-py/instant-python/commit/841badc6af64490729fd448f3797393d9ed47cd4))

### ⚙️ Build System

- Update testpaths to point to the correct directory
  ([`61bc700`](https://github.com/dimanu-py/instant-python/commit/61bc700f99533bf119c03590fabd44738f88f7a7))

### ♻️ Refactoring

- **templates**: Modify all errors template to not include 'error_type' attribute and leave just
  typical message field
  ([`1fc2a39`](https://github.com/dimanu-py/instant-python/commit/1fc2a39e0662a50c5a701c1f2cacb625482175c1))

- **templates**: Modify source structure of all project templates so exclude sync sqlalchemy and
  include async sqlalchemy when present
  ([`244b597`](https://github.com/dimanu-py/instant-python/commit/244b5975c6fb2d64d503a9a64b1961ee0837e082))

- **templates**: Modify async sqlalchemy structure template to exclude sqlalchemy repository
  template and include async session template
  ([`447caa4`](https://github.com/dimanu-py/instant-python/commit/447caa4472a7e080f15bc45a5da37c3694b686ae))

- **initialize**: Extract semantic method to populate file keys with content from template
  ([`5ceb8ec`](https://github.com/dimanu-py/instant-python/commit/5ceb8ec574d366902d671b816cc893df8d4d919f))

- **initialize**: Extract semantic method to express operation of rendering the project structure
  using jinja
  ([`f610639`](https://github.com/dimanu-py/instant-python/commit/f61063922d0e64c3fbb19832d6e663c5b15adbad))

- **initialize**: Extract semantic method to generate main structure template path
  ([`ff69c87`](https://github.com/dimanu-py/instant-python/commit/ff69c87829d71e52d4f66fa36dbc879fd276dc56))

- **config**: Extract semantic methods in ConfigGenerator use case to keep high level expressions in
  main 'execute' method
  ([`766a2bc`](https://github.com/dimanu-py/instant-python/commit/766a2bcd1ed614a093dfe6bd99a1f45ba997df8b))

- **initialize**: Update render_template method to accept Any type for context
  ([`e6501bc`](https://github.com/dimanu-py/instant-python/commit/e6501bcb777f5ba2be8903f04629affd6ba66521))

- **initialize**: Rename render_project_structure method to render
  ([`49fd942`](https://github.com/dimanu-py/instant-python/commit/49fd942a0bdcfdbababee08d0f0c304e5f9d78a5))

- **initialize**: Rename configuration repository classes for consistency
  ([`4b4fa94`](https://github.com/dimanu-py/instant-python/commit/4b4fa94e95f77e9f08d64dc96462551b218324f8))

- **initialize**: Move config repository to a persistence module to keep modules organized
  ([`3d9a7e0`](https://github.com/dimanu-py/instant-python/commit/3d9a7e02481c5fe5401f28c035ca21bc20374ba0))

- **initialize**: Modify signature of renderer interface to only accept context config parameter
  ([`835060f`](https://github.com/dimanu-py/instant-python/commit/835060feb47d2446a06977b2deb3116beed67adf))

- **initialize**: Clean up jinja environment tests extracting common object instantiation
  ([`c73e2e3`](https://github.com/dimanu-py/instant-python/commit/c73e2e38e75d839a1c1ae8a63798db9630d05fd9))

- **config**: Rename all references from 'configuration' to 'config' for naming consistency
  ([`7691173`](https://github.com/dimanu-py/instant-python/commit/769117371e59d5642b5cc8fbffe9a55099e5386d))

- **config**: Remove unused method 'save_on_current_directory' method
  ([`e760771`](https://github.com/dimanu-py/instant-python/commit/e760771438653b669cbdac0a9c8049dc298d7c0c))


## v0.13.0 (2025-10-26)

### ✨ Features

- **config**: Raise error when git repo is set to be initialized but username or email is either not
  passed or an empty string
  ([`2e9f852`](https://github.com/dimanu-py/instant-python/commit/2e9f85287b3beab29bfd2745a830d6972939938f))

- **dependency-manager**: Inform the user that the selected dependency manager is already installed
  ([`71ac1f7`](https://github.com/dimanu-py/instant-python/commit/71ac1f7c7da63ce55d27aacb9c1db03c34963de4))

- **config**: Allow custom configuration path for loading configurations
  ([`b7bfc97`](https://github.com/dimanu-py/instant-python/commit/b7bfc97fa8d7ada19d39c2c04a491e625ab83366))

- **config**: Add 'custom_config_path' parameter to Parser port to be able to generate
  configurations with custom paths to the config file
  ([`350dbeb`](https://github.com/dimanu-py/instant-python/commit/350dbebab016dda71f42bef4d389e48e0ca2b197))

- **initialize**: Handle FileNotFoundError in read_from_file method
  ([`00fb79f`](https://github.com/dimanu-py/instant-python/commit/00fb79f5ec282525433b5d0e6abb4880cac23b33))

- **initialize**: Implement read_from_file method to load YAML configuration
  ([`5630929`](https://github.com/dimanu-py/instant-python/commit/5630929f3a5615e0f93d6d688e01d07cc31bafbd))

- **initialize**: Convert ConfigurationRepository into an interface and define the signature of
  'read_from_file' method
  ([`b8c768f`](https://github.com/dimanu-py/instant-python/commit/b8c768fb958b96f9fa2749cf9668c02951d0426c))

- **initialize**: Implement execute method to return parsed configuration schema from config file
  ([`a009371`](https://github.com/dimanu-py/instant-python/commit/a00937100e8cef46036dce1dc16db18f20602a03))

### 🪲 Bug Fixes

- **dependency-manager**: Use dynamic command for version check in dependency managers
  ([`46c9726`](https://github.com/dimanu-py/instant-python/commit/46c972601cf1ad217d6a0aca845fe0410d8cc176))

- **config**: Configure parser mock in config reader unit test to be called with the config file
  path
  ([`71655ea`](https://github.com/dimanu-py/instant-python/commit/71655ea654392978c339314482a5e94a51fbf888))

- **templates**: Correct error exception boilerplate file to base_error
  ([`8dda0d7`](https://github.com/dimanu-py/instant-python/commit/8dda0d7ae296c42d9eed496920785e6f5b608779))

- **dependency-manager**: Install uv manager only if is not installed
  ([`e2a9ad5`](https://github.com/dimanu-py/instant-python/commit/e2a9ad5fdede2da1bb94e2bf7c75c74f04be9a23))

- **dependency-manager**: Install pdm manager only if is not installed
  ([`f4eb3ff`](https://github.com/dimanu-py/instant-python/commit/f4eb3fffbfe5c067f1997ddb7eb70dcddde43de4))

- **initialize**: Pass config file path to parser for accurate parsing
  ([`de58185`](https://github.com/dimanu-py/instant-python/commit/de58185ab722863a92627adf6b065c796e1860d5))

### ⚙️ Build System

- Add pytest marks to be able to discriminate which tests are run
  ([`33e8e3d`](https://github.com/dimanu-py/instant-python/commit/33e8e3df683483a3745583cc03cd9a877c33f937))

### ♻️ Refactoring

- **render**: Encapsulate filter addition in _add_filter method
  ([`caf805b`](https://github.com/dimanu-py/instant-python/commit/caf805b1f9c38782e011d237cc131798c6c9b565))

- **initialize**: Use config reader in init cli application
  ([`20f8178`](https://github.com/dimanu-py/instant-python/commit/20f8178f398b5db6b8cb7f48f12fc1a4143fe1b8))

- **initialize**: Rename read_from_file method to read to not expose implementation details on the
  interface
  ([`2aa94f4`](https://github.com/dimanu-py/instant-python/commit/2aa94f44835122421eaa8af3303c76addf30b1b0))

- **shared**: Modify ApplicationError to not be abstract class so it can be instantiated as a
  general app error
  ([`da086de`](https://github.com/dimanu-py/instant-python/commit/da086def1d643fed11b3ee7005435b6d45bea40c))


## v0.12.1 (2025-10-23)

### 🪲 Bug Fixes

- **templates**: Create github issues templates folder with correct name
  ([`751e58f`](https://github.com/dimanu-py/instant-python/commit/751e58fa2ffd637e7984e4c2040616deb300f2f8))


## v0.12.0 (2025-10-23)

### ✨ Features

- **initialize**: Move init command cli to its own folder for hexagonal architecture
  ([`3101896`](https://github.com/dimanu-py/instant-python/commit/310189634553c297095d8f3bd40fcd32cc87228f))

- **config**: Implement YAML config writer to save configuration to file
  ([`99b2e5e`](https://github.com/dimanu-py/instant-python/commit/99b2e5ed5ac0aea6859dc852a5bf5ed15e34f659))

- **config**: Return parsed configuration
  ([`330dc00`](https://github.com/dimanu-py/instant-python/commit/330dc0056fdef9ae9fc983ab9cbe080c8fc27fca))

- **config**: Add parsing logic for template section in configuration
  ([`9f9e83a`](https://github.com/dimanu-py/instant-python/commit/9f9e83a5c684c634cb00826fe57db98dcdaee45b))

- **config**: Add parsing logic for git section in configuration
  ([`818febc`](https://github.com/dimanu-py/instant-python/commit/818febc61febbc509caf1a9ec2946f3d71ff6eb3))

- **config**: Add parsing logic for dependencies section in configuration
  ([`b6fec2a`](https://github.com/dimanu-py/instant-python/commit/b6fec2a4c2d7b9773b7bca1707acf6193e0dd986))

- **config**: Implement logic to parse general section of config
  ([`e6ef56c`](https://github.com/dimanu-py/instant-python/commit/e6ef56c2988e8af8d0a9ffadcc882c643a2e580e))

- **config**: Validate required configuration keys and raise appropriate exceptions
  ([`697b115`](https://github.com/dimanu-py/instant-python/commit/697b1153472189ae7dd8b58825830644282ef9bc))

- **config**: Raise EmptyConfigurationNotAllowed for empty content in parse method
  ([`b3f51e4`](https://github.com/dimanu-py/instant-python/commit/b3f51e4a5dd483d4a2f3fa58c2e4b3b035dec1ca))

- **config**: Inject ConfigParser port into ConfigGenerator use case
  ([`4f0a8f6`](https://github.com/dimanu-py/instant-python/commit/4f0a8f6be698c54b1ae75755a4807c6c8184c9d4))

- **config**: Define ConfigParser interface as driver port
  ([`59ec2b9`](https://github.com/dimanu-py/instant-python/commit/59ec2b9c5c3ffb145547b98c06721c8121cab907))

- **config**: Extend QuestionaryQuestionWizard to inherit from QuestionWizard
  ([`ed3674c`](https://github.com/dimanu-py/instant-python/commit/ed3674c41547504a95817498c759324a7607700d))

- **config**: Add abstract QuestionWizard class for question handling
  ([`abb9a22`](https://github.com/dimanu-py/instant-python/commit/abb9a226be6f257ed5924fe935ccbfae338e9c10))

- **config**: Implement execute method for configuration generation
  ([`936b2c6`](https://github.com/dimanu-py/instant-python/commit/936b2c61fc69c013e618093bfa62e8599876f2d7))

- **config**: Create ConfigGenerator class for configuration generation
  ([`377564e`](https://github.com/dimanu-py/instant-python/commit/377564e5e9057c79f2f07b0889bae55f749e8981))

- **config**: Create yaml writer interface
  ([`4e6f3b5`](https://github.com/dimanu-py/instant-python/commit/4e6f3b5a29a7970f67836bb18c07349cc0a93897))

### 🪲 Bug Fixes

- **templates**: Point to correct base error template file when including fastapi built in feature
  ([`c2ce3f3`](https://github.com/dimanu-py/instant-python/commit/c2ce3f35a1eb9cb268906e78990abd7c25604955))

- **cli**: Correct import for new place of config command
  ([`f23b0fc`](https://github.com/dimanu-py/instant-python/commit/f23b0fc3204483bbac44c87fd70611e742c50c61))

### ⚙️ Build System

- Update audit make command to ignore pip vulnerability
  ([`963d5f6`](https://github.com/dimanu-py/instant-python/commit/963d5f6c0fdbc9528cd90489429db692a36fb8c5))

- Exclude resources folders from mypy analysis
  ([`7f2b3b8`](https://github.com/dimanu-py/instant-python/commit/7f2b3b818d4b608aa466e50d9dfdedd42e6af4f7))

### ♻️ Refactoring

- **config**: Instantiate question wizard steps inside directly coupling them
  ([`8785304`](https://github.com/dimanu-py/instant-python/commit/8785304b744f9dba777e2518014e4a40146753c0))

- **config**: Remove complex class hierarchy for different types of questions and streamline
  questions using questionary wrapper
  ([`35e266b`](https://github.com/dimanu-py/instant-python/commit/35e266bfb3afc97b88f6432e08463a80553ff32b))

- **config**: Streamline dependency installation questions in CLI
  ([`33f0bd6`](https://github.com/dimanu-py/instant-python/commit/33f0bd6d95d7aa0d9c87a74c2a5e0a638b1541a1))

- **config**: Modify cli application to use new config generator use case
  ([`530fe7e`](https://github.com/dimanu-py/instant-python/commit/530fe7e47ed7f9fb81077c4efdbe31c0967e339c))

- **config**: Move question wizard concrete implementation to new infra folder in config command
  ([`0f8b481`](https://github.com/dimanu-py/instant-python/commit/0f8b48128eb97fb1c8ed54852307cb995c183739))

- **config**: Turn config file path attribute to public
  ([`8fa7f3e`](https://github.com/dimanu-py/instant-python/commit/8fa7f3e6aa31e287b050601732db1ecd7260e325))

- **config**: Clean up parser tests adding setup_method
  ([`eb3c095`](https://github.com/dimanu-py/instant-python/commit/eb3c0958b36bb161ff7874458761b1c1871e1db4))

- **config**: Move config parsing errors to new architecture and to errors file
  ([`c18a969`](https://github.com/dimanu-py/instant-python/commit/c18a96965d35faa1a8e735974e3e1e9c8ae64810))

- **config**: Extract string values to constants
  ([`49ac047`](https://github.com/dimanu-py/instant-python/commit/49ac04775ca140464eb8f79a246bed63fe6cd9b4))

- **config**: Extract semantic methods for better readability in parser
  ([`42cc355`](https://github.com/dimanu-py/instant-python/commit/42cc35588acb3ef256d22bbf9062b9d367e28f0a))

- **config**: Decouple configuration generation from specific schema classes validating answers with
  parser
  ([`2a3bea5`](https://github.com/dimanu-py/instant-python/commit/2a3bea55ae87317580012ab6eb940675c6089c4a))

- **config**: Rename QuestionaryQuestionWizard to QuestionaryConsoleWizard
  ([`66a6671`](https://github.com/dimanu-py/instant-python/commit/66a6671f9765ca91836229d3c32c4c21ba6ecc4d))

- **config**: Apply dependency inversion to ConfigGenerator constructor
  ([`8ae285f`](https://github.com/dimanu-py/instant-python/commit/8ae285f2d0c26e03513ac874435dbc100360cea0))

- **config**: Rename YamlWriter interface to ConfigWriter
  ([`4921828`](https://github.com/dimanu-py/instant-python/commit/4921828e171c8e999c643da1df583b1c4bfa3d43))

- **config**: Update test to use QuestionWizard instead of QuestionaryQuestionWizard for mock
  ([`00fb764`](https://github.com/dimanu-py/instant-python/commit/00fb764239ed6fffa94ec211bc32b544d407cf4a))

- **config**: Rename QuestionWizard to QuestionaryQuestionWizard to express its implementation uses
  questionary
  ([`74d124d`](https://github.com/dimanu-py/instant-python/commit/74d124d68318fa333cb48f98aa43c6f59667a6c1))

- **config**: Structure tests for config domain following same structure as source
  ([`eafda5e`](https://github.com/dimanu-py/instant-python/commit/eafda5e240b84483962daeed5d5c85b3354b2a15))

- **config**: Move domain classes for config command to domain module
  ([`c6aa3ad`](https://github.com/dimanu-py/instant-python/commit/c6aa3ad5f5649fc4f3dd61d9d02fc9d0de70a7ca))

- **commands**: Move cli application for 'config' command to specific module config that will follow
  hexagonal architecture to reduce coupling
  ([`a1fa9ab`](https://github.com/dimanu-py/instant-python/commit/a1fa9ab605a0fe622e529f086352d5eefc3b8ece))


## v0.11.0 (2025-09-30)

### ✨ Features

- **templates**: Add ruff linter and formatter rules in pyproject.toml template file
  ([`b600f62`](https://github.com/dimanu-py/instant-python/commit/b600f62ab807d0ed5309ee199fd6b772dad55317))

### 🪲 Bug Fixes

- **templates**: Correct imports when selected template was standard project
  ([`4d8bda4`](https://github.com/dimanu-py/instant-python/commit/4d8bda4fb246a59e5556c78b5317845614e3f8b5))

### ♻️ Refactoring

- **templates**: Modify makefile template file simplifying add-dep and remove-dep commands
  ([`eb883f3`](https://github.com/dimanu-py/instant-python/commit/eb883f31aba41faf8b38908317ea02b53e700874))

- **templates**: Rename template file for base error
  ([`3a30d3d`](https://github.com/dimanu-py/instant-python/commit/3a30d3d3533bc88fe70f0822f204d34e3ad4280a))

- **commands**: Move ipy configuration file to project folder before creating first commit
  ([`8997e98`](https://github.com/dimanu-py/instant-python/commit/8997e984b2384e70ca2418e4cf7eb21aa3d7bdad))


## v0.10.0 (2025-09-30)

### ✨ Features

- **templates**: Add 'changelog_file' entry to semantic release section in pyproject template to
  avoid warning
  ([`0a80d5a`](https://github.com/dimanu-py/instant-python/commit/0a80d5a4dc1cec80259d4d6e9ba0ac0a9581fc6a))

### 🪲 Bug Fixes

- **templates**: Correct errors import in fastapi application template
  ([`e42cfbb`](https://github.com/dimanu-py/instant-python/commit/e42cfbb0116fa52596be60121a27bb6ee39e10cf))

- **templates**: Correct errors in release.yml template
  ([`65b96f0`](https://github.com/dimanu-py/instant-python/commit/65b96f0a0c890e18e597fb4edc4c8402b733d84d))

### ⚙️ Build System

- Add 'dev' dependency group for improved development workflow
  ([`37d4c25`](https://github.com/dimanu-py/instant-python/commit/37d4c250696c07cb22b8a594b5d68309a1659c83))

- Update dependencies
  ([`31572ab`](https://github.com/dimanu-py/instant-python/commit/31572ab38b253abfee97f3e8926499e0a8f57a00))


## v0.9.1 (2025-07-18)

### 🪲 Bug Fixes

- **cli**: Update command in tox.ini file to be able to make reference to new location for application entry point ([`a8baef2`](https://github.com/dimanu-py/instant-python/commit/a8baef2eb88018cb6a0210122348e753dc10cacb))

- **templates**: Update pyproject.toml template to include optional build dependencies when github actions built-in feature is selected ([`b765ec8`](https://github.com/dimanu-py/instant-python/commit/b765ec81f3e61ce170873eaed371910e41e2e871))

- **templates**: Update release action template to work running build command to update uv.lock ([`9824451`](https://github.com/dimanu-py/instant-python/commit/982445188567c61d31ffc11d04ccdab163fb1ee4))

### ⚙️ Build System

- Update changelog section in semantic release config ([`7a413cf`](https://github.com/dimanu-py/instant-python/commit/7a413cf7a95b4da30ef23efafdf94cb2e2118168))

- Update application entry point ([`8b5330a`](https://github.com/dimanu-py/instant-python/commit/8b5330a99ae432dc0e04c19f67ccc55e5ee9fe5a))

### ♻️ Refactoring

- **cli**: Move cli files to its own folder ([`81b8c3c`](https://github.com/dimanu-py/instant-python/commit/81b8c3c3839bf548a5ffac3432615d392ad2a05e))

- **templates**: Update name of test workflow ([`80225f5`](https://github.com/dimanu-py/instant-python/commit/80225f51014aef1d06660803aa0fec65633f41bd))

## v0.9.0 (2025-07-18)

### ✨ Features

- **templates**: Add github action release to project structure for github actions ([`9e3309f`](https://github.com/dimanu-py/instant-python/commit/9e3309f8154a72954427f947ae61753d37253060))

- **templates**: Include python semantic release library in default dependencies if github actions is selected ([`5374ba4`](https://github.com/dimanu-py/instant-python/commit/5374ba4e77f8790dc6d5b691d3f511889df87f24))

- **shared**: Add github issues template as possible built in feature ([`9d97ce5`](https://github.com/dimanu-py/instant-python/commit/9d97ce53baded8ed6e782ea437daa9110c74c316))

- **templates**: Add template for release with python semantic release ([`23569a0`](https://github.com/dimanu-py/instant-python/commit/23569a0bafb33b1726beab47bf11e6f7fde95065))

- **templates**: Include github issues template into project structure templates ([`36a2975`](https://github.com/dimanu-py/instant-python/commit/36a2975e726db3172965e2f8866b2af48488c193))

- **templates**: Add templates for github issues templates ([`fec68e4`](https://github.com/dimanu-py/instant-python/commit/fec68e48418875c57e98a16dbc041e3eeeffdea9))

- **templates**: Include pip audit and precommit as default dependencies if they are selected as built in features ([`86a8af5`](https://github.com/dimanu-py/instant-python/commit/86a8af5592c03046d0228131beb4b9718bd00f57))

- **templates**: Include audit command in makefile template if github actions is selected ([`8035fab`](https://github.com/dimanu-py/instant-python/commit/8035fab7a66b1735da07d6a750bc754b1f6c4d48))

- **templates**: Modify project structure for github action including joined ci workflow ([`4ae4bd7`](https://github.com/dimanu-py/instant-python/commit/4ae4bd77d292697761dd4b631a6f87b32dc0796e))

- **templates**: Join lint and test github workflows into one single file and include more security and code quality jobs ([`a21eafe`](https://github.com/dimanu-py/instant-python/commit/a21eafebc11da2fe2d440acdfc96e3d6910e8bdc))

- **shared**: Include security as supported built in feature ([`5cfa228`](https://github.com/dimanu-py/instant-python/commit/5cfa228abca91b5e0d09ca7f68baa0a910f5da26))

- **templates**: Include security template into project structures ([`65c9b84`](https://github.com/dimanu-py/instant-python/commit/65c9b849f2b37faf5c0fcae8993e9981b71da829))

- **templates**: Create security file template ([`21b1bb0`](https://github.com/dimanu-py/instant-python/commit/21b1bb0257e1caa23db66e645e9e047010c10920))

- **shared**: Add citation as supported built in feature ([`893abab`](https://github.com/dimanu-py/instant-python/commit/893abab4e16a66b0da7e8b9e26d2f2ed452453d5))

- **templates**: Add citation project structure template to default templates ([`0a798d5`](https://github.com/dimanu-py/instant-python/commit/0a798d57642eb990f42b2e614d840f543829c767))

- **templates**: Add citation file template ([`888e8c6`](https://github.com/dimanu-py/instant-python/commit/888e8c696ad1ab2ce9916fa4a85c6ceae529cf14))

- **shared**: Add precommit option in SupportedBuiltInFeatures enum ([`f69cadb`](https://github.com/dimanu-py/instant-python/commit/f69cadb733634a6ecb4e9ab092e2a2bb375f98c9))

- **templates**: Include precommit template project structure in all default templates ([`8601841`](https://github.com/dimanu-py/instant-python/commit/8601841cb74c7a3a68b1d06daa89c25b3b23c0f3))

- **templates**: Include specific make commands in template based on installed dependencies and selected built in features ([`62688c0`](https://github.com/dimanu-py/instant-python/commit/62688c072cb6bfa1d00e7f6a08f82a1ed975aa8e))

- **templates**: Include pre commit hook in makefile if it's selected as built in features ([`2c391fb`](https://github.com/dimanu-py/instant-python/commit/2c391fb6c1c69990ae551c6bf8621bb1b40811d1))

- **templates**: Update pre commit config file to be included as built in feature ([`972aaa4`](https://github.com/dimanu-py/instant-python/commit/972aaa4131e54d3e875b14e3d117ea30a23bc0e9))

- **templates**: Include new base aggregate in value objects and when in EDA project structure ([`4f038ef`](https://github.com/dimanu-py/instant-python/commit/4f038ef59fd4f0c54ba2880c4a505984560a4254))

- **templates**: Create base aggregate class and make aggregate for event driven architecture inherit from it ([`44f843d`](https://github.com/dimanu-py/instant-python/commit/44f843de0c6fcf739309f37350e9ba8b4c7bc650))

- **templates**: Include error handlers in fastapi application template for project structure ([`add3634`](https://github.com/dimanu-py/instant-python/commit/add36343fb11e4be42c96dca42ef00153d178187))

- **templates**: Separate template files for fastapi error handlers ([`cfd7d14`](https://github.com/dimanu-py/instant-python/commit/cfd7d14cd1f515b513774df5f25f2180baee2cb3))

- **templates**: Include new model for value objects in project structure ([`39d2ba1`](https://github.com/dimanu-py/instant-python/commit/39d2ba101aab089addd80ce38ee1753c0dff7883))

- **templates**: Update value object templates to use new version that autovalidates using @validate decorator ([`186ecd5`](https://github.com/dimanu-py/instant-python/commit/186ecd518b8c9ca685a4db04598eb55e27fc3316))

- **templates**: Update project structure templates that were using old version of domain error an include error base class as well as rename the folder to errors instead of exceptions ([`5c363b6`](https://github.com/dimanu-py/instant-python/commit/5c363b6e126942531f6bb1ca5990ede9dc92bf18))

- **templates**: Implement new error template as base class for errors and let domain error inherit from it ([`1e15d5d`](https://github.com/dimanu-py/instant-python/commit/1e15d5d58dbb583fb681df648ddda573ef2c1679))

- **templates**: Update logger project structure template to include new handler and new logger implementation ([`b33bd1e`](https://github.com/dimanu-py/instant-python/commit/b33bd1e4021006b236607d28dd7472431bfc3ddf))

- **templates**: Include log middleware in fastapi application project structure if logger is selected ([`4ca7641`](https://github.com/dimanu-py/instant-python/commit/4ca76411a0f906ec51aac38653ec29cec9cdf9b1))

- **templates**: Update fastapi main application template to include log middleware if logger is selected too ([`c92810c`](https://github.com/dimanu-py/instant-python/commit/c92810ce79b199892a03ce7e29dd03daacf00130))

- **templates**: Create fastapi log middleware template ([`b196afc`](https://github.com/dimanu-py/instant-python/commit/b196afce1838180439c2a4a900816fdda5063ef5))

- **templates**: Modify fastapi main application template with new logger ([`021039d`](https://github.com/dimanu-py/instant-python/commit/021039de56a92bf018dbbbd68d57bc60bbd2126d))

- **templates**: Add new templates for logger implementation ([`d937478`](https://github.com/dimanu-py/instant-python/commit/d9374786fd1cb95c89933331b678ef6fa0e2d7cf))

- **templates**: Remove http_response and status_code templates ([`5f75969`](https://github.com/dimanu-py/instant-python/commit/5f759699f15818cf0b73e9c88e13cc4ff567dc57))

- **templates**: Use new response model in fastapi error handlers ([`ef4e543`](https://github.com/dimanu-py/instant-python/commit/ef4e54308ae783360fb0eaa75fab8642c896a0d7))

- **templates**: Substitute http_response and status_code templates from fastapi infra for success and error responses model ([`2c086be`](https://github.com/dimanu-py/instant-python/commit/2c086bebdb646d34447f82f2cdf93aef894b0e66))

- **templates**: Add ErrorResponse and SuccessResponse templates for fastapi application ([`9ec98f1`](https://github.com/dimanu-py/instant-python/commit/9ec98f1e8db59386f76c636825f889f117ff9871))

### 🪲 Bug Fixes

- **templates**: Add semantic release config to pyproject template if github actions is selected ([`a6533ce`](https://github.com/dimanu-py/instant-python/commit/a6533ceeb62b2877b5698f4ca39eb1e4cdb2a374))

- **templates**: Fix indentations in github actions templates ([`cd0d882`](https://github.com/dimanu-py/instant-python/commit/cd0d88293612e4e83206615b903ff40af69b5dac))

- **templates**: Add {% raw %} and {% endraw %} tags in github actions templates when they access repository variables ([`46ec5c1`](https://github.com/dimanu-py/instant-python/commit/46ec5c1489b937065b6ebd8a1723ae581adc9445))

- **templates**: Correct forma of helper scripts when makefile built in feature is selected and include custom hooks only if precommit feature is not selected ([`fe15d7e`](https://github.com/dimanu-py/instant-python/commit/fe15d7e7521bd70879490e1a96973477524518f3))

- **templates**: Correct error in conditional in makefile template ([`b126eed`](https://github.com/dimanu-py/instant-python/commit/b126eed146787cf254070e4169afbde1433b5ce2))

- **templates**: Use selected dependency manager for new make commands ([`80bf833`](https://github.com/dimanu-py/instant-python/commit/80bf8333d06facae66b3f15992f0d59bc5bab785))

- **templates**: Include makefile if precommit built in feature is selected ([`9dcec97`](https://github.com/dimanu-py/instant-python/commit/9dcec97973b1a91a78d2bdf11a3bd20e097e8c68))

- **templates**: Write correct name for aggregate template file in value objects project structure ([`d651243`](https://github.com/dimanu-py/instant-python/commit/d651243d7baf602f262ed63d31bc4b0d0c2c2952))

- **render**: Create jinja environment with autoscape argument enabled to avoid potential XSS attacks ([`976d459`](https://github.com/dimanu-py/instant-python/commit/976d459538ae8eea403c65300304e6405fec46b6))

- **templates**: Format correctly if statement in application.py template ([`409d606`](https://github.com/dimanu-py/instant-python/commit/409d6064d97ef016c34dab57d3c9456a47e6542f))

- **templates**: Include logger and migrator in fastapi application only if they are selected too for DDD and standard project templates ([`f5a8087`](https://github.com/dimanu-py/instant-python/commit/f5a80870d0ecdd2f47419ad5e51d20131649b422))

- **templates**: Include logger and migrator in fastapi application only if they are selected as built in feature too in clean architecture template ([`191d81f`](https://github.com/dimanu-py/instant-python/commit/191d81fd8ace560f3a6359bc9cf767c73c310d50))

### ⚙️ Build System

- Modify release job and semantic release configuration to be able to update uv.lock with the new version ([`2d52828`](https://github.com/dimanu-py/instant-python/commit/2d5282804956e4e5ab31c20b320663f9184f0a84))

- Update version in uv.lock ([`9d1bd2c`](https://github.com/dimanu-py/instant-python/commit/9d1bd2c380293c7e1635a03da0654e7084b9e1eb))

- Update semantic release to not update major version if is zero and to allow 0 major version ([`34d251e`](https://github.com/dimanu-py/instant-python/commit/34d251e8a57eafa595a0c54e314238f389218dd6))

- Remove test hook in precommit config ([`b8d451d`](https://github.com/dimanu-py/instant-python/commit/b8d451db1a024ae41a6958dbf9513801f3b69627))

- Remove final echo from makefile commands to let output of the command itself inform the user ([`cd895ad`](https://github.com/dimanu-py/instant-python/commit/cd895adacfe1e470a746165380369c9c365996e8))

- Remove -e command from echo in makefile ([`6a624a3`](https://github.com/dimanu-py/instant-python/commit/6a624a3cacf8b96adaeba20bb635b7e43d853002))

- Exclude resources folder from being formatted or linted ([`cf00038`](https://github.com/dimanu-py/instant-python/commit/cf000382ba13a0bc4dbda8eb346e9cdeb4fe4541))

- Remove AST check from pre commit hook ([`b46437e`](https://github.com/dimanu-py/instant-python/commit/b46437e804a1d54f13444e92827bd15d9fb2fd57))

- Add docs-serve command to makefile ([`9430934`](https://github.com/dimanu-py/instant-python/commit/943093498f168f49cc8b2593ea17911321f2e012))

- Improve messages of make command and add build and clean commands ([`6a0e428`](https://github.com/dimanu-py/instant-python/commit/6a0e4285d3bb43f9e88dad32fd2f93732ab271c8))

- Remove commitizen config as is not longer needed ([`0ed6a8b`](https://github.com/dimanu-py/instant-python/commit/0ed6a8bd50c6ebf30b71e4734fd3e4a81123b280))

### ♻️ Refactoring

- **templates**: Improve format of github action template ([`a01b4b0`](https://github.com/dimanu-py/instant-python/commit/a01b4b0c5f57ecbc5c66995abda26157b923ecd8))

- **templates**: Improve formatting of makefile and reorganize commands ([`efa8de5`](https://github.com/dimanu-py/instant-python/commit/efa8de5c5bae2bd79c8e4a0a01ef4aa016b0e54c))

- **templates**: Convert local setup and custom hooks into python scripts ([`12af46c`](https://github.com/dimanu-py/instant-python/commit/12af46c7cf2bd437f2f81b412ceb615a7cd563e5))

- **templates**: Convert add and remove dependency scripts into python scripts instead of bash scripts ([`0d29c14`](https://github.com/dimanu-py/instant-python/commit/0d29c14a7aa7a113fe365d1e30055ead52908b29))


## v0.8.2 (2025-07-16)

### 🪲 Bug Fixes

- **render**: Create jinja environment with autoscape argument enabled to avoid potential XSS
  attacks
  ([`976d459`](https://github.com/dimanu-py/instant-python/commit/976d459538ae8eea403c65300304e6405fec46b6))

- **templates**: Format correctly if statement in application.py template
  ([`409d606`](https://github.com/dimanu-py/instant-python/commit/409d6064d97ef016c34dab57d3c9456a47e6542f))

- **templates**: Include logger and migrator in fastapi application only if they are selected too
  for DDD and standard project templates
  ([`f5a8087`](https://github.com/dimanu-py/instant-python/commit/f5a80870d0ecdd2f47419ad5e51d20131649b422))

- **templates**: Include logger and migrator in fastapi application only if they are selected as
  built in feature too in clean architecture template
  ([`191d81f`](https://github.com/dimanu-py/instant-python/commit/191d81fd8ace560f3a6359bc9cf767c73c310d50))

### ⚙️ Build System

- Update semantic release to not update major version if is zero and to allow 0 major version
  ([`34d251e`](https://github.com/dimanu-py/instant-python/commit/34d251e8a57eafa595a0c54e314238f389218dd6))

- Remove test hook in precommit config
  ([`b8d451d`](https://github.com/dimanu-py/instant-python/commit/b8d451db1a024ae41a6958dbf9513801f3b69627))

- Remove final echo from makefile commands to let output of the command itself inform the user
  ([`cd895ad`](https://github.com/dimanu-py/instant-python/commit/cd895adacfe1e470a746165380369c9c365996e8))

- Remove -e command from echo in makefile
  ([`6a624a3`](https://github.com/dimanu-py/instant-python/commit/6a624a3cacf8b96adaeba20bb635b7e43d853002))

- Exclude resources folder from being formatted or linted
  ([`cf00038`](https://github.com/dimanu-py/instant-python/commit/cf000382ba13a0bc4dbda8eb346e9cdeb4fe4541))

- Remove AST check from pre commit hook
  ([`b46437e`](https://github.com/dimanu-py/instant-python/commit/b46437e804a1d54f13444e92827bd15d9fb2fd57))

- Add docs-serve command to makefile
  ([`9430934`](https://github.com/dimanu-py/instant-python/commit/943093498f168f49cc8b2593ea17911321f2e012))

- Improve messages of make command and add build and clean commands
  ([`6a0e428`](https://github.com/dimanu-py/instant-python/commit/6a0e4285d3bb43f9e88dad32fd2f93732ab271c8))

- Remove commitizen config as is not longer needed
  ([`0ed6a8b`](https://github.com/dimanu-py/instant-python/commit/0ed6a8bd50c6ebf30b71e4734fd3e4a81123b280))

## 0.8.1 (2025-07-01)

### 🐛 Bug Fixes

- **git**: modify command to make initial commit so Windows system does not interpret it as three different commands

## 0.8.0 (2025-07-01)

### ✨ Features

- **dependency-manager**: get dependency manager installation command based on system os
- **dependency-manager**: set different commands for dependency executable based on system os
- **dependency-manager**: add os information in dependency manager to be able to modify installation depending on user os

### ♻️ Code Refactoring

- **dependency-manager**: add message for the user to notify uv should be added to the path when installing it on windows
- **dependency-manager**: notify the user when all dependencies have been installed
- **dependency-manager**: extract method to set executable path setting based on system os

## 0.7.0 (2025-06-30)

### ✨ Features

- **commands**: call project formatter in 'init' command once the file system has been generated
- **formatter**: add project formatter to be able to format included code in the project

### 🐛 Bug Fixes

- **templates**: include DomainError template when using fastapi application built in feature

## 0.6.2 (2025-06-30)

### 🐛 Bug Fixes

- **configuration**: ask built in template question only if selected template is not custom
- **templates**: use valid checkout action in test_lint.yml github action template
- **templates**: correct test path folder in makefile commands
- **templates**: rename _log_ folder that gets created when logger built in feature is selected to _logger_ to avoid git ignore its content
- **templates**: include faker library by default when template is not custom
- **templates**: include basic dependencies for makefile when is selected in built in features

### ♻️ Code Refactoring

- **templates**: separate template github action in two different workflows, one for test and one for linting and checks
- **templates**: include makefile by default if github actions built in feature has been selected to be able to reuse its commands
- **templates**: remove test execution in parallel by default in makefile template
- **templates**: remove unit and integration commands from makefile
- **templates**: remove insert_templates command from makefile template
- **configuration**: do not use Self typing to ensure compatibility with older python versions

## 0.6.1 (2025-06-27)

### 🐛 Bug Fixes

- correct links to README.md

## 0.6.0 (2025-06-27)

### ✨ Features

- **configuration**: remove white spaces from slug
- **configuration**: raise error for bounded context if specify_bounded_context is true and no DDD template is set or if either bounded context or aggregate name are set
- **commands**: set ipy.yml as the default configuration file
- **shared**: add SupportedBuiltInFeatures enum for built-in feature management
- **configuration**: add method to retrieve supported templates
- **configuration**: add CUSTOM template type to SupportedTemplates
- **shared**: add SupportedLicenses enum with method to retrieve supported licenses
- **shared**: add SupportedPythonVersions enum with method to retrieve supported versions
- **shared**: add method to retrieve list of supported managers
- **cli**: add config command to CLI for configuration management
- **commands**: add command to generate configuration file for new projects
- **configuration**: add save_on_current_directory method to save configuration in the current directory
- **configuration**: implement QuestionWizard class to manage question steps and parse answers
- **configuration**: add parse_from_answers method to differentiate when parsing comes from user answers
- **configuration**: add Step interface for all concrete implementations and Steps container to manage configuration steps
- **configuration**: implement DependenciesStep to manage user input for dependency installation
- **configuration**: add TemplateStep to manage template selection and built-in features
- **configuration**: implement GitStep to handle git initialization questions
- **configuration**: implement GeneralQuestionStep to store all questions that will allow the user to build the general section of the config file
- **configuration**: implement ConditionalQuestion
- **configuration**: implement MultipleChoiceQuestion
- **configuration**: implement FreeTextQuestion
- **configuration**: implement ChoiceQuestion for questions where user has to select one option between some
- **configuration**: implement boolean question
- **configuration**: create base Question class defining common logic for all concrete type of questions
- **configuration**: add wrapper of questionary library to be able to test easily question classes
- **cli**: include new "init" command in general application
- **commands**: allow the option of passing a custom template to generate a project with a custom structure
- **project-creator**: allow FileSystem to handle normal files apart from boilerplate files
- **renderer**: implement CustomProjectRenderer
- **commands**: move configuration file to project
- **configuration**: add method to move configuration file to generated project
- **configuration**: add config file path attribute and named constructor to create ConfigurationSchema from file
- **configuration**: automatically compute "year" value in general configuration
- **commands**: rename new project command to "init" so the use is ipy init
- **commands**: integrate GitConfigurer to set up repository during project command
- **git**: automate initial commit during repository setup
- **git**: set user information during repository initialization
- **git**: add repository initialization method to GitConfigurer
- **git**: do nothing if git is not set to be configured
- **git**: add "setup_repository" method to GitConfigurer
- **git**: create GitConfigurer class with basic init arguments
- **configuration**: add methods to compute flag and name of dependencies inside DependencyConfiguration to not violate encapsulation
- **templates**: add new templates using new configuration nomenclature
- **commands**: add logic to instantiate and setup virtual environment using user dependency manager selection
- **configuration**: add property to expose python version easily
- **dependency-manager**: implement factory method to encapsulate instantiation of dependency manager based on user selection
- **configuration**: add dependency_manager property to configuration schema
- **dependency-manager**: implement concrete version of dependency manager  using pdm
- **dependency-manager**: create DependencyManager interface
- **dependency-manager**: implement "setup_environment" method to orchestrate all steps to install manager and dependencies
- **dependency-manager**: add command to create virtual environment in case no additional dependencies are specified
- **dependency-manager**: add logic to install dependencies with uv
- **dependency-manager**: implement "_install_python" method to install user python version using uv
- **dependency-manager**: implement "_install" method delegating command execution to a helper "_run_command" method
- **dependency-manager**: add _install method to UvDependencyManager
- **dependency-manager**: create UvDependencyManager class
- **project-creator**: implement "write_on_disk" method for FileSystem
- **project-creator**: let FileSystem constructor receive project structure as an argument
- **project-creator**: remove unnecessary arguments for FileSystem now that project structure gets injected
- **project-creator**: treat "create_folders_and_files" method as a named constructor that is in charge of creating the file system tree
- **project-creator**: add children to Directory __repr__ method
- **project-creator**: modify file system logic to receive rendered project structure injected instead of be coupled to how it gets generated
- **project-creator**: implement logic to fill file system files
- **project-creator**: raise error when file has not been created and its tried to be filled
- **project-creator**: implement FileHasNotBeenCreated application error
- **project-creator**: implement File fill method to be able to write template content inside
- **project-creator**: add template path attribute to File class to be able to locate the template with its content
- **project-creator**: implement FileSystem class to generate the directories and files of the project
- **configuration**: add property to expose project folder name based on configuration
- **project-creator**: create inner directories in Directory
- **project-creator**: inject children argument to Directory
- **project-creator**: when directory is defined as python module, create '__init__' file inside
- **project-creator**: implement logic to create directories
- **project-creator**: create Directory class with basic attributes
- **project-creator**: create boilerplate file at desired path
- **project-creator**: add '__repr__' method to BoilerplateFile class
- **project-creator**: implement BoilerplateFile extracting file name
- **project-creator**: define basic interface for different nodes
- **commands**: render project structure based on parsed configuration file
- **builder**: include 'has_dependency' custom filter in jinja environment
- **project-generator**: implement 'has_dependency' custom filter for jinja environment
- **configuration**: add ConfigurationSchemaPrimitives typed dict to type better to_primitives return
- **configuration**: add "template_type" property to know which template the user has selected
- **builder**: implement "get_project" method in JinjaProjectRender class
- **builder**: define interface of JinjaProjectRender
- **builder**: implement basic ProjectRender class with constructor to avoid linter fail
- **builder**: implement "render_template" method to be able to process a jinja template and render its content
- **builder**: include custom filter in jinja environment
- **builder**: initialize jinja environment
- **commands**: add new command that receives config file
- **configuration**: parse template configuration
- **configuration**: handler missing mandatory fields for git configuration
- **configuration**: parse git configuration
- **configuration**: parse dependencies configuration
- **configuration**: ensure all mandatory fields are present in general configuration
- **configuration**: parse general configuration
- **configuration**: verify all required keys are present in config file
- **configuration**: handle EmptyConfigurationNotAllowed error for empty config files
- **configuration**: create Parser class with parser method that raises single error
- **configuration**: add ConfigurationSchema to encapsulate general, dependency, template, and git configurations
- **configuration**: add template configuration management with validation for templates and built-in features
- **configuration**: implement GitConfiguration class to manage user settings
- **configuration**: add validation to ensure non-dev dependencies are not included in groups
- **configuration**: add DependencyConfiguration class to store dependencies parameters
- **configuration**: validate supported dependency managers in GeneralConfiguration
- **configuration**: add InvalidDependencyManagerValue error for unsupported dependency managers
- **configuration**: validate supported Python versions in GeneralConfiguration
- **configuration**: add InvalidPythonVersionValue error for unsupported Python versions
- **configuration**: validate passed license is supported by the application
- **configuration**: create application error when invalid license is passed
- **errors**: add configuration error to possible error types
- **configuration**: add GeneralConfiguration dataclass for project settings
- **configuration**: add configuration template for project setup

### 🐛 Bug Fixes

- **template**: correct reference to built_in_features in YAML clean architecture template
- **configuration**: rename TemplateStep key from 'template' to 'name'
- **renderer**: manually include pyproject.toml boilerplate file when making a project with custom template to be able to create virtual environment
- **templates**: correct accessing general information in LICENSE template
- **commands**: pass configuration dependencies directly when setting up environment
- **project-creator**: include TemplateTypes in context when rendering files
- **templates**: correct indentantions in new templates
- **dependency-manager**: correct test that verifies dependency installation command is called with group flag
- **dependency-manager**: do not use --dev and --group flag
- **project-creator**: correct boilerplate template example for test to have correct format
- **project-creator**: modify test method that extracts project file system structure to iterate the folders in order and avoid test failing only for different order
- **builder**: modify how test examples files are accessed to use a full path all the times
- **configuration**: return empty list of dependencies when configuration file has no dependencies specified
- **commands**: correct requirements access to slug variable
- **error**: correct message formatting in NotDevDependencyIncludedInGroup exception
- **configuration**: make dependencies field a list of DependencyConfiguration

### ♻️ Code Refactoring

- **dependency-manager**: do not print installed dependency in pdm manager
- **templates**: include default dependencies when github actions is selected and write a message in the README to inform the project has been created using ipy
- **errors**: remove errors folder
- **errors**: move ApplicationError and ErrorTypes to shared module
- **render**: move UnknownTemplateError to render module
- **project-creator**: move UnknownNodeTypeError to project_creator module
- **dependency-manager**: move UnknownDependencyManagerError to the dependency manager module
- **renderer**: move TemplateFileNotFoundError import to the render module
- **dependency-manager**: move CommandExecutionError import to dependency manager module
- **project-creator**: update type hints to ensure backward compatibility with older python versions
- **configuration**: replace hardcoded options with dynamic retrieval from SupportedLicenses, SupportedManagers, SupportedPythonVersions, and SupportedBuiltInFeatures
- **configuration**: update type hints to ensure backward compatibility with older python versions
- **configuration**: replace hardcoded template name with SupportedTemplates enum
- **configuration**: replace hardcoded built-in features with dynamic retrieval from SupportedBuiltInFeatures
- **configuration**: move SupportedTemplates to shared module
- **configuration**: replace hardcoded supported templates with dynamic retrieval from SupportedTemplates
- **configuration**: rename TemplateTypes to SupportedTemplates
- **configuration**: update supported licenses to use SupportedLicenses enum
- **configuration**: update supported python versions to use respective enums
- **configuration**: update supported dependency managers to use get_supported_managers method
- **shared**: rename Managers enum to SupportedManagers
- **configuration**: update supported dependency managers to use Managers enum
- **dependency-manager**: move Managers enum to shared folder
- **templates**: rename new_templates folder to templates now that old templates folder have been removed
- **templates**: remove old templates files
- **installer**: remove old installer folder
- **dependency-manager**: move managers enum to dependency_manager folder
- **installer**: remove old installer files
- **prompter**: remove old question prompter folder
- **project-creator**: use TemplateTypes enum from configuration
- **project-generator**: remove old project generator folder
- **renderer**: move jinja_custom_filters.py to renderer folder
- **project-generator**: remove old files for generating the project
- **prompter**: remove old questions and steps
- **commands**: rename project file with init command to init
- **commands**: remove folder_cli and project_cli commands
- **cli**: remove folder_cli and project_cli from CLI application
- **configuration**: rename question step files for consistency and clarity
- **configuration**: set default value for _config_file_path in ConfigurationSchema
- **parser**: extract configuration parsing logic into separate method for improved readability
- **parser**: rename parse method to parse_from_file for clarity
- **configuration**: refactor question steps to inherit from Step interface
- **configuration**: move steps to its own folder inside configuration
- **parser**: use ConfigurationSchema named constructor to generate parsed config from user file
- **git**: enhance repository setup with informative messages
- **dependency-manager**: avoid accessing dependency configuration internal data and delegate behavior to it
- **dependency-manager**: modify uv dependency manager type hint to receive a list of DependencyConfiguration
- **dependency-manager**: move "_run_command" method to DependencyManager class to be reused by other implementations
- **dependency-manager**: let UvDependencyManager implement DependencyManager interface
- **dependency-manager**: add attribute _uv to store the name of uv command
- **dependency-manager**: add print statements to inform the user about what is happening
- **dependency-manager**: reorganize the logic to build the command for installing dependencies
- **dependency-manager**: extract "_build_dependency_install_command" method to encapsulate the logic of creating the command needed to install a dependency
- **dependency-manager**: extract "_create_virtual_environment" method to express what uv sync command is doing
- **commands**: update project command to use new "write_on_disk" file system method to create the project on disk
- **project-creator**: remove unused create_folders_and_files method
- **project-creator**: rename "build_tree" method to "build_node"
- **project-creator**: store in a list all the files that are created in the project file system
- **project-creator**: when creating a File save its path to be able to recover it when filling it
- **project-creator**: extract setup_method for file tests to clean up file creation
- **commands**: allow to execute new project command
- **commands**: change how new project command is handled using directly FyleSystem class
- **render**: rename JinjaProjectRender to JinjaProjectRenderer
- **render**: modify JinjaProjectRender return type hint
- **configuration**: modify configuration parser test for happy paths using approvaltests to verify expected configuration gets parsed correctly instead of making lots of separate tests for each section of the configuration
- **render**: remove expected project json files for tests
- **render**: modify tests to use approvaltest and don't need expected project json files
- **project-creator**: update teardown_method to delete correctly directories generated on tests
- **project-creator**: modify directory tests to use object mother
- **render**: modify resources test projects to not contain "root" key
- **project-creator**: make Directory inherit from Node interface
- **project-creator**: remove children argument from directory
- **project-creator**: modify teardown_method to delete files inside directory after test
- **project-creator**: rename boilerplate file to file
- **commands**: add type hint to project command
- **render**: rename builder module to render
- **builder**: remove old project_render.py and test
- **builder**: parametrize jinja project render tests
- **builder**: modify main_structure.yml.j2 for test case with dependency
- **builder**: load expected project structure from JSON file instead of hardcoding
- **builder**: rename config file to 'clean_architecture_config.yml' and update test to reflect the change
- **builder**: set template base dir as argument of 'render_project_structure' method instead of argument to constructor
- **builder**: rename constant for main structure template
- **builder**: remove 'main_structure_template' argument from render constructor as the main file must always be named main_structure.yml.j2
- **builder**: modify JinjaProjectRender arguments for test to point to test example project yml
- **builder**: rename "get_project" method to express better the intention of the method
- **builder**: move example template yml of project for test
- **builder**: parametrize base dir for template and main file to not be coupled to production structure when testing
- **configuration**: use typed dict to type "to_primitives" return method
- **configuration**: avoid possibility of accessing GeneralConfiguration class variables
- **builder**: add setup method to jinja environment test class to clean up jinja env instantiation
- **builder**: pass package name and template directory to jinja environment to be able to differentiate between production templates and test templates
- **cli**: rename instant_python_typer correctly and add missing type hints
- **template**: modify domain error templates to avoid repeating implementation of type and message properties
- modify all application errors to pass message and type error to base error and not implement neither type or message properties
- **error**: modify ApplicationError to pass the message and type and avoid repeating the same pattern to return the message and type of error
- **configuration**: handle when template config mandatory field is missing
- **configuration**: modify config.yml file to only include template name
- **configuration**: modify config examples for test to have git fields with same name as class argument
- **configuration**: pass parsed arguments to configuration classes using ** operator with dicts and handle TypeError to detect missing mandatory fields
- **configuration**: automatically cast attributes value to string in case yaml reading gets interpreted as a float
- **configuration**: modify config examples for test to have is_dev field with same name as class argument
- **configuration**: modify test assertion to compare expected dependencies with parsed dependencies configuration
- **tests**: update config file path handling to remove file extension
- **configuration**: extract helper function to build config file path for tests
- **configuration**: remove unnecessary empty check in tests
- **configuration**: temporarily set dependencies, template and git configs to not needed when initializing ConfigurationSchema to be able to test it step by step
- **configuration**: convert constants to class variables
- **configuration**: modify configuration errors to pass wrong value and supported values instead of accessing them
- **configuration**: create auxiliar methods for better readability when extracting config file content
- **configuration**: extract semantic method to encapsulate reading configuration file
- **configuration**: modify parse method to open config file
- **configuration**: reorganize configuration files in subfolders to expose clearer the concepts of the configuration
- **configuration**: join unsupported values test in a parametrized test
- **configuration**: move supported constants to a separate file to avoid circular import errors
- **prompter**: rename project_slug to slug for consistency across templates
- **cli**: move folder and project cli commands to specific command module

## 0.5.2 (2025-04-16)

### 🐛 Bug Fixes

- **template**: fix project slug placeholder in README template

## 0.5.1 (2025-04-15)

### 🐛 Bug Fixes

- **cli**: manage and detect correctly raised exceptions and exit the application with exit code 1

## 0.5.0 (2025-04-15)

### ✨ Features

- **cli**: create main application based on custom implementation and add error handlers
- **cli**: implement a custom version of Typer application to be able to handle exceptions in FastAPI way using decorators
- **errors**: add UnknownTemplateError for handling unknown template types
- **errors**: add TemplateFileNotFoundError for missing template files and extend ErrorTypes with GENERATOR
- **errors**: add ErrorTypes enum for categorizing error types
- **errors**: add CommandExecutionError for handling command execution failures
- **errors**: add UnknownDependencyManagerError for handling unknown dependency managers
- **installer**: remove unused PYENV manager from Enum
- **errors**: create application error to be able to capture all expected errors

### 🐛 Bug Fixes

- **errors**: correct typo in UnknownTemplateError message

### ♻️ Code Refactoring

- **project-generator**: manage when a command fails by raising custom CommandExecutionError
- **installer**: manage when a command fails by raising custom CommandExecutionError
- **cli**: enhance error handling with rich console output
- **project-generator**: raise UnknownTemplateError for unknown template types
- **project-generator**: move UnknownErrorTypeError to errors module and inherit from ApplicationError
- **project-generator**: raise TemplateFileNotFoundError for missing template files
- **errors**: use ErrorTypes enum for error type in CommandExecutionError and UnknownDependencyManagerError
- **installer**: add stderr handling for subprocess calls
- **installer**: raise UnknownDependencyManagerError for unknown user managers

## 0.4.0 (2025-04-11)

### ✨ Features

- **template**: add README template and include in main structure

## 0.3.0 (2025-04-11)

### ✨ Features

- **project-generator**: add support for creating user File instances in folder tree
- **project-generator**: create new File class to model user files
- **project-generator**: create JinjaEnvironment class to manage independently jinja env

### 🐛 Bug Fixes

- **template**: correct IntValueObject template to call super init
- **template**: remove unnecessary newline in template import
- **template**: correct typo in jinja template

### ♻️ Code Refactoring

- **template**: modify all template file types
- **project-generator**: rename File class to BoilerplateFile to be able to differentiate a normal file introduced by the user and a file of the library that contains boilerplate
- **cli**: update template command parameter from template_name to template_path
- **cli**: rename configuration variable name from user_requirements to requirements
- **prompter**: modify configuration file name from user_requirements.yml to ipy.yml
- **prompter**: rename UserRequirements to RequirementsConfiguration
- **project-generator**: rename DefaultTemplateManager to JinjaTemplateManager
- **project-generator**: delegate jinja env management to JinjaEnvironment in DefaultTemplateManager

## 0.2.0 (2025-04-08)

### ✨ Features

- **template**: add new rabbit mq error when user selects event bus built in feature
- **template**: create rabbit_mq_connection_not_established_error.py boilerplate

### 🐛 Bug Fixes

- **template**: correct domain event type not found error import and class name
- **template**: set event bus publish method async
- **template**: correct imports in value objects boilerplate

### ♻️ Code Refactoring

- **installer**: add virtual environment creation before installing dependencies
- **template**: conditionally include bounded context based on specify_bounded_context field
- **template**: add specify_bounded_context field to user requirements
- **prompter**: be able to execute nested conditional questions
- **template**: update subquestions structure to use ConditionalQuestion for bounded context specification
- **prompter**: extend ConditionalQuestion subquestions type hint
- **prompter**: remove note when prompting built in features for the user to select and remove temporarily synch sql alchemy option
- **template**: modify project structure templates to include logger and alembic migrator automatically if fastapi application is selected
- **template**: modify DomainEventSubscriber boilerplate to follow generic type syntax depending on python version

## 0.1.1 (2025-04-08)

### 🐛 Bug Fixes

- **template**: correct typo in ExchangeType enum declaration
- **template**: correct typo on TypeVar declaration

### ♻️ Code Refactoring

- **question**: use old generic type syntax to keep compatibility with old python versions
- **template**: update boilerplates so they can adhere to correct python versions syntax
- **project-generator**: standardize path separator in file name construction
- **installer**: remove unused enum OperatingSystems
- **prompter**: change TemplateTypes class to inherit from str and Enum for improved compatibility
- **project-generator**: change NodeType class to inherit from str and Enum for improved compatibility
- **installer**: change Managers class to inherit from str and Enum for better compatibility
- **project-generator**: remove override typing decorator to allow lower python versions compatibility

## 0.1.0 (2025-04-06)

### 🐛 Bug Fixes

- **project-generator**: add template types values to be able to use enum in jinja templates
- **template**: write correct option when fastapi built in feature is selected
- **template**: generate correctly the import statement in templates depending on the user selection
- **installer**: correct answers when installing dependencies
- **prompter**: modify DependenciesQuestion to not enter an infinite loop of asking the user
- **cli**: temporarily disable template commands
- **prompter**: extract the value of the base answer to check it with condition
- **prompter**: remove init argument from year field
- **cli**: access project_name value when using custom template command
- **prompter**: set default value for git field in UserRequirements to avoid failing when executing folder command
- **prompter**: include last question in TemplateStep if selected template is domain_driven_design
- **project-generator**: instantiate DefaultTemplateManager inside File class
- **build**: change build system and ensure templates directory gets included
- **project-generator**: substitute FileSystemLoader for PackageLoader to safer load when using it as a package
- **prompter**: correct default source folder name
- **template**: correct license field from pyproject.toml template
- **template**: use project_slug for project name inside pyproject.toml
- **project-generator**: correct path to templates
- **project-generator**: correct extra blocks that where being created when including templates

### ♻️ Code Refactoring

- **template**: include mypy, git and pytest configuration files only when the user has selected these options
- **template**: include dependencies depending on user built in features selection
- **prompter**: update answers dictionary instead of add manually question key and answer
- **prompter**: return a dictionary with the key of the question and the answer instead of just the answer
- **cli**: modify cli help commands and descriptions
- **prompter**: modify default values for UserRequirements
- **cli**: use new GeneralCustomTemplateProjectStep in template command
- **cli**: add name to command and rename command function
- **prompter**: substitute template and ddd specific questions in TemplateStep for ConditionalQuestion
- **prompter**: substitute set of question in GitStep for ConditionalQuestion
- **prompter**: remove should_not_ask method from Step interface
- **prompter**: remove DomainDrivenDesignStep
- **cli**: remove DDD step and add TemplateStep
- **prompter**: remove boilerplate question from DependenciesStep
- **prompter**: remove template related questions from GeneralProjectStep
- **prompter**: move git question to GitStep and remove auxiliar continue_git question
- **cli**: rename function names for better clarity
- **cli**: move new command to its own typer app
- **cli**: move folder command to its own typer app and separate the app in two commands
- **project-generator**: let DefaultTemplateManager implement TemplateManager interface
- **project-generator**: rename TemplateManager to DefaultTemplateManager
- **cli**: add template argument to both command to begin allow the user to pass a custom path for the project structure
- **cli**: add help description to both commands
- **prompter**: move python and dependency manager from dependencies step to general project step as it's information that is needed in general to fill all files information
- **cli**: rename generate_project command to new
- **prompter**: add file_path field to user requirements class
- **cli**: pass project slug name as the project directory that will be created
- **project-generator**: pass the directory where the project will be created to FolderTree
- **cli**: remove checking if a user_requirements file exists
- **template**: remove writing author and email info only if manager is pdm
- **installer**: avoid printing executed commands output by stdout
- **template**: use git_email field in pyproject.toml
- **prompter**: remove email field from UserRequirements and add git_email and git_user_name
- **prompter**: remove email question from general project step
- **project-generator**: remove condition of loading the template only when is domain driven design
- **template**: use include_and_indent custom macro inside domain_driven_design/test template
- **template**: include always mypy and pytest ini configuration
- **prompter**: rename empty project template to standard project
- **cli**: use DependencyManagerFactory instead of always instantiating UvManager
- **installer**: remove ShellConfigurator and ZshConfigurator
- **cli**: remove shell configurator injection
- **installer**: remove the use of ShellConfigurator inside installer
- **prompter**: warn the user that project name cannot contain spaces
- **prompter**: remove project name question and just leave project slug
- **installer**: remove executable attribute from UvManager
- **installer**: specify working directory to UvManager so it installs everything at the generated project
- **cli**: pass generated project path to UvManager
- **installer**: inline uv install command attribute as is not something reusable
- **cli**: inject folder tree and template manager to project generator
- **project-generator**: set the directory where user project will be generated as FolderTree attribute and expose it through a property
- **project-generator**: pass folder_tree and template_manager injected into ProjectGenerator
- **cli**: pass user dependencies to installer
- **prompter**: substitute fixed default dependencies by dynamic ones that will be asked to the user
- **prompter**: remove question definition lists and basic prompter
- **cli**: substitute BasicPrompter for QuestionWizard
- **prompter**: remove python manager and operating system questions
- **prompter**: extract helper method to know if template is ddd
- **prompter**: delegate ask logic to each question instead of letting prompter what to do depending on flags
- **prompter**: redefine questions using concrete implementations
- **prompter**: make Question abstract and add ask abstract method
- **project-generator**: rename Directory's init attribute to python_module and remove default value for children
- **project-generator**: move children extraction only when node is a directory
- **src**: remove old src folder with cookiecutter project and convert current instant_python module into src
- **cli**: generate user requirements only if no other file has been already generated.
- **template**: move makefile template to scripts folder as this folder only makes sense if it's use with the makefile
- **template**: move base from sync sqlalchemy to persistence folder as it would be the same for both sync and async
- **template**: move sqlalchemy sync templates to specific folder
- **template**: move exceptions templates to specific folder
- **template**: move value object templates to specific folder
- **template**: move github actions templates to specific folder
- **template**: move logger templates to specific folder
- **project-generator**: modify File class to be able to manage the difference between the path to the template and the path where the file should be written
- **template**: change all yml templates to point to inner event_bus folder boilerplate
- **template**: move all boilerplate related to event bus inside specific folder
- **prompter**: change github information for basic name and email
- **prompter**: move default dependencies question to general questions and include the default dependencies that will be included
- **prompter**: remove converting to snake case all answers and set directly those answers in snake case if needed
- **templates**: use raw command inside github action instead of make
- **templates**: modify error templates to use DomainError
- **templates**: change all python-module types to directory and add python flag when need it
- **project-generator**: make Directory general for any type of folder and remove python module class
- **project-generator**: remove python_module node type
- **templates**: set all files of type file and add them the extension variable
- **project-generator**: add extension field to node and remove deprecated options
- **project-generator**: create a single node type File that will work with any kind of file
- **project-generator**: substitute python file and yml file node type for single file
- **templates**: use new operator to write a single children command in source
- **project-generator**: include new custom operator in jinja environment
- **templates**: remove populated shared template
- **templates**: include value objects template when is specified by the user
- **templates**: import and call macro inside project structures templates
- **prompter**: format all answers to snake case
- use TemplateTypes instead of literal string
- **project-generator**: change template path name when generating project
- **templates**: move ddd templates inside project_structure folder
- **prompter**: migrate BasicPrompter to use questionary instead of typer to make the questions as it manages multiple selections better
- **cli**: instantiate BasicPrompter instead of using class method
- **prompter**: simplify ask method by using Question object an iterating over the list of defined questions
- **templates**: modularize main_structure file
- **project-generator**: create project structure inside a temporary directory
- **project-generator**: delegate template management to TemplateManager
- **cli**: call BasicPrompter and ProjectGenerator inside cli app

### ✨ Features

- **project-generator**: create new custom function to generate import path in templates
- **prompter**: implement general project step that will only be used when custom template is passed
- **cli**: add template command for project_cli.py to let users create a project using a custom template
- **prompter**: implement ConditionalQuestion
- **prompter**: implement TemplateStep to group all questions related to default template management
- **project-generator**: implement CustomTemplateManager to manage when user passes a custom template file
- **project-generator**: create TemplateManager interface
- **cli**: add folder command to allow users to just generate the folder structure of the project
- **project-generator**: format all project files with ruff once everything is generated
- **cli**: remove user_requirements file once project has been generated
- **prompter**: add remove method to UserRequirements class
- **cli**: call to git configurer when user wants to initialize a git repository
- **installer**: implement GitConfigurer
- **cli**: include git step into cli steps
- **prompter**: implement step to ask the user information to initialize a git repository
- **template**: add clean architecture template project structure
- **template**: add standard project project structure templates
- **installer**: create factory method to choose which dependency manager gets instantiated
- **installer**: implement PdmInstaller
- **project-generator**: expose generated project path through ProjectGenerator
- **installer**: add project_directory field to UvManager to know where to create the virtual environment
- **installer**: add install_dependencies step to Installer
- **installer**: implement logic to install dependencies selected by the user in UvManager
- **installer**: add install_dependencies method to DependencyManger interface
- **prompter**: implement DependencyQuestion to manage recursive question about what dependencies to install
- **prompter**: implement DependenciesStep with all questions related to python versions, dependencies etc.
- **prompter**: implement DomainDrivenDesignStep with bounded context questions.
- **prompter**: implement GeneralProjectStep that will have common questions such as project name, slug, license etc.
- **prompter**: implement Steps collection and Step interface
- **prompter**: implement QuestionWizard to separate questions into steps and be more flexible and dynamic
- **cli**: install uv by default and python version specified by the user
- **installer**: implement Installer that will act as the manager class that coordinates all operation required to fully install the project
- **installer**: implement zsh shell configurator
- **installer**: create ShellConfigurator interface
- **installer**: implement UvManager that is in charge of installing uv and the python version required by the user
- **installer**: add dependency manager interface
- **installer**: include enums for managers options and operating systems
- **prompter**: add question to know user's operating system
- **prompter**: create MultipleChoiceQuestion for questions where the user can select zero, one or more options
- **prompter**: create BooleanQuestion for yes or no questions
- **prompter**: create FreeTextQuestion for those questions where the user has to write something
- **prompter**: create ChoiceQuestion to encapsulate questions that have different options the user needs to choose from
- **project-generator**: create custom exception when node type does not exist
- **cli**: make sure user_requirements are loaded
- **prompter**: add load_from_file method to UserRequirements
- **template**: include mock event bus template for testing
- **template**: add scripts templates
- **prompter**: add fastapi option to built in features
- **template**: include templates for fasta api application with error handlers, http response modelled with logger
- **prompter**: add async alembic to built in features options
- **template**: include templates for async alembic
- **prompter**: add async sqlalchemy to built in features options
- **template**: add templates for async sqlalchemy
- **prompter**: include logger as built in feature
- **template**: add template for logger
- **prompter**: include event bus as built in feature
- **templates**: add project structure template for event bus
- **templates**: add LICENSE template
- **prompter**: add year to user requirements fields with automatic computation
- **templates**: include mypy and pytest init files when default dependencies are selected
- **templates**: add .python-version template
- **templates**: add .gitignore template
- **templates**: add pyproject template
- **templates**: add makefile template
- **templates**: add invalid id format error template
- **templates**: add domain error template
- **prompter**: add synchronous sqlalchemy option to built in features question
- **templates**: add synchronous sqlalchemy template
- **project-generator**: create custom operator to be applied to jinja templates
- **prompter**: add pre commit option to built in features question
- **templates**: add pre commit template
- **prompter**: add makefile option to built in features question
- **templates**: add makefile template
- **templates**: separate value objects folder template in a single yml file
- **templates**: add macro to include files easier and more readable
- **project-generator**: add TemplateTypes enum to avoid magic strings
- **prompter**: add question to know which features the user wants to include
- **prompter**: implement new function to have multiselect questions
- **prompter**: define all questions in a separate file
- **prompter**: create Question class to encapsulate questions information
- **project-generator**: create YamlFile class to create yaml files
- **project-generator**: create Directory class to create simple folders
- **templates**: add templates to create github actions and workflows
- **project-generator**: create NodeType enum to avoid magic strings
- **templates**: add python files boilerplate
- **project-generator**: implement logic to create python files with boilerplate content
- **project-generator**: create specific class to manage jinja templates
- **prompter**: add save_in_memory method to UserRequirements
- **project-generator**: implement logic to create python modules
- **templates**: create DSL to set the folder structure
- **project-generator**: create classes to model how python files and modules would be created
- **project-generator**: delegate folder generation to folder tree class
- **project-generator**: create manager class in charge of creating all project files and folders
- **prompter**: create class to encapsulate user answers
- **prompter**: create basic class that asks project requirements to user
- **cli**: create basic typer application with no implementation
