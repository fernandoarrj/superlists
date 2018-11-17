from fabric.api import run
from fabric.context_managers import settings

SITE_NAME = 'www.staging-lists.com'

def _get_manage_dot_py():
    return f'~/sites/{SITENAME}/env/bin/python ~/sites/{SITENAME}/source/manage.py'

def reset_database(host):
    manage_dot_py = _get_manage_dot_py()
    with settings(host_string=f'eslpeth@{host}'):
        run(f'{manage_dot_py} flush --noinput')

def create_session_on_server(host, email):
    manage_dot_py = _get_manage_dot_py()
    with settings(host_string=f'eslpeth@{host}'):
        session_key = run(f'{manage_dot_py} create_session {email}')
        return session_key.strip()
