# weather-logger
It is a python project to log weather data which is maintained by a bash cron job.

To deploy, add your hosts in the current_hosts file and run **ansible-playbook automate_weatherlogging.yml -vv**

The following tasks are performed using ansible:
* Install pyenv dependencies and install pyenv while ensuring proper shell configurations
* Transfer the project source code to remote and other supporting bash scripts
* Install python version 3.7.4 on pyenv and create a virtual environment in the project directory
* Install poetry package using pip and run "poetry install"
* Schedule "weather-logger" and "delete-old-logs" scripts using cron module

As apt is used as the package manager in the playbook, only debian based distros are supported.

