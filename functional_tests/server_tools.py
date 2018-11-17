import os
from fabric.api import run
from fabric.context_managers import settings

SITE_NAME = 'www.staging-lists.com'
PORT = os.environ.get('_PORT_SITE')
USER = os.environ.get('_USER_SITE')

def _get_manage_dot_py():
    return f'~/sites/{SITE_NAME}/env/bin/python ~/sites/{SITE_NAME}/source/manage.py'

def reset_database(host):
    manage_dot_py = _get_manage_dot_py()
    with settings(host_string=f'{USER}@{host}:{PORT}'):
        run(f'{manage_dot_py} flush --noinput')

def create_session_on_server(host, email):
    manage_dot_py = _get_manage_dot_py()
    with settings(host_string=f'{USER}@{host}:{PORT}'):
        session_key = run(f'{manage_dot_py} create_session {email}')
        return session_key.strip()
