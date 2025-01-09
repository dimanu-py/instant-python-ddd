# How to Use

First thing we need to do to use this template and create our project is to install [`cookiecutter`](https://github.com/cookiecutter/cookiecutter):

```bash
pip install --user cookiecutter
```

With this done, now we can generate our new project and customize it to our needs.

```bash
cookiecutter gh:dimanu-py/python-skeleton
```

The template will ask us some questions to customize our project. After that, we will have a new project ready to be used.

Once we have your project created, we should probably want to keep track of your files, so let's create a git repository:

```bash
cd <project_name>
git init
```

Finally, depending on the project structure we've chosen, we could apply some custom git hooks that are under _scripts/hooks_. 
To do so, run:

```bash
make local-setup
```