from fabric.api import *


PROJECT_NAME = 'familyfeed'
PROJECT_DIR = '/srv/code/' + PROJECT_NAME


def run_in_virtualenv(command):
    run('source env/bin/activate && ' + command)

#
# Different servers
#


def test():
    env.hosts = ['root@hydra.sciworth.com']


def production():
    env.hosts = ['root@vorushin.ru']

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


import settings
db_settings = settings.DATABASES['default']


def fetch_db():
    with cd(PROJECT_DIR):
        run('mysqldump %(NAME)s -u %(BACKUP_USER)s -p%(BACKUP_PASSWORD)s '
            '--skip-lock-tables > dump.sql' % db_settings)
        get('dump.sql', 'dump.sql')
    local('./manage.py flush --noinput')
    local('./manage.py dbshell < dump.sql')
