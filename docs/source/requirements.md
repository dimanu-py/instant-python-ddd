# Requirements

This project is compatible with multiple Python versions, which are managed using [pyenv](https://github.com/pyenv/pyenv).

First things first, let's install `pyenv` in our computers:

```bash
curl https://pyenv.run | bash
```

Then, we need to set up the shell environment . To do so, add the following to your shell profile.

<details><summary>Fish</summary>

```bash
set -Ux PYENV_ROOT $HOME/.pyenv
fish_add_path $PYENV_ROOT/bin
```

Add the following line to `~/.config/fish/config.fish`:

```bash
echo pyenv init - | source >> ~/.config/fish/config.fish
```

</details>

<details><summary>Zsh</summary>

Add the following commands to your `.zshrc` file:

```bash
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
  echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
  echo 'eval "$(pyenv init - zsh)"' >> ~/.zshrc
```

</details>

<details><summary>Bash</summary>

Add the following commands to your `.bashrc` file:

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init - bash)"' >> ~/.bashrc
```

Then, if you have a `.bash_profile` file, add the following line. If you have not create one.

```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo '[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init - bash)"' >> ~/.bash_profile
```

</details>
   
```{note}
If you have any problem or question, we recommend to visit [pyenv documentation](https://github.com/pyenv/pyenv#readme).
```