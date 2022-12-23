# Workflow Automation
Collection of scripts to manage web development workflows

## Getting Started
To use this repo you'll need some prerequisites, feel free to skip any you don't need

### 1. Install pyenv

```zsh
brew install pyenv
```
This will install pyenv which you can use to manage python versions
```zsh
pyenv init
```
This will give you some text that you will need to add to the bottom of you `~/.zshrc` file before continuing and then restart your shell. 

### 2. Install python
We're going to need python so, lets do that
```zsh
pyenv install 3.10.9
```
We are using python 3.10 in this project so lets download that. 

Now we need to tell pyenv we want to use that verision. You can wither set this globally, or just for this directory.

*Global:*
```zsh
pyenv global 3.10.9
```
*Local:*
```zsh
pyenv local 3.10.9
```

## Sources

https://medium.com/nerd-for-tech/how-to-build-and-distribute-a-cli-tool-with-python-537ae41d9d78

https://dev.to/bowmanjd/build-command-line-tools-with-python-poetry-4mnc

https://python-poetry.org/docs/basic-usage/