#!/bin/bash
#source /home/pyapp/.bashrc
PATH="/home/pyapp/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
cd ~/Documents/testing
pyenv versions | grep 3.7.4 > /dev/null
if (($?)); then
    pyenv install 3.7.4
fi
pyenv virtualenvs | grep weather-app > /dev/null
if (($?)); then
    pyenv virtualenv 3.7.4 weather-app
fi
pyenv activate weather-app
pip list | grep poetry > /dev/null
if (($?)); then
    pip install poetry
fi
cd poetry_package
poetry build
pip install dist/*.whl
