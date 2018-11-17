Provisionamneto de um novo site

===============================

## Pacotes necessários:

* nginx
* Python 3.6
* virtualenv + pip
* Git

Por exemplo, no Ubuntu:
    
    sudo add-apt-repository ppa:fkrull/deadsnakes
    sudo apt-get install nginx git python3.6 python3.6-venv

## Config do Nginx Virtual Host

* veja nginx.template.conf
* substitua SITENAME, por exemplo, por staging.my-domain.com

## Serviço Systemd

* veja gunicorn-systemd.template.service
* substitua SITENAME, por exmeplo, por staging.my-domain.com
* subistitua SEKRIT pela senha de email

## Estrutura de pastas:
Suponha que temos uma conta de usuário em /home/USERNAME

/home/USERNAME
--sites
    --SITENAME
        --database
        --source
        --static
        --env

