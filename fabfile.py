from fabric.api import *


def run_in_virtualenv(command):
    run('source env/bin/activate && ' + command)

#
# Different servers
#


def test():
    env.hosts = ['root@hydra.sciworth.com']


def production():
    env.hosts = ['root@173.255.236.60']

#
# Actual commands
#


def deploy():
    with cd('/home/django/FamilyFeed'):
        run('sudo -u django git pull')
        run_in_virtualenv('pip install -r requirements.txt')
        run_in_virtualenv('./manage.py syncdb')
        run_in_virtualenv('./manage.py migrate --noinput')
        run('initctl reload-configuration')
        run('restart familyfeed')
