0. pre
======

install mysql >= 5.5

# setup utf8mb4
sudo vim mysql/my.cnf

    [client]
    default-character-set = utf8mb4

    [mysql]
    default-character-set = utf8mb4

    [mysqld]
    character-set-client-handshake = FALSE
    character-set-server = utf8mb4
    collation-server = utf8mb4_unicode_ci
    init_connect='SET NAMES utf8mb4'


1. Setup your ENV environment
=============================

    cd ~/workspace
    virtualenv chhu_ENV
    source chhu_ENV/bin/activate


2. Download chhu project
========================

    git clone https://github.com/zonesan/ch-hu.com.git
    cd ch-hu.com/chhu_web


3. install python packages
==========================

    sudo ~/workspace/chhu_ENV/bin/pip install -r requirements.txt


4. Setup chhu_web database
==========================

    # create local DB: schema 'chhu_web'
    mysql> CREATE SCHEMA `chhu_web` DEFAULT CHARACTER SET utf8mb4 ;
    # create DBA : username 'work', password 'work'
    # grant all 'chhu_web' privileges to work user.


4.1 update allauth code
=======================

    # for utf8mb4
    sudo vim ~/workspace/chhu_ENV/lib/python2.7/site-packages/allauth/socialaccount/models.py
    # # line88, change max_length to 190
    sudo rm ~/workspace/chhu_ENV/lib/python2.7/site-packages/allauth/socialaccount/models.pyc


5. Setup tables
===============

    ./manage.py migrate
    ./manage.py syncdb
    ./manage.py collectstatic
    ./manage.py runserver

6. Visit
    http://127.0.0.1:8000/forum/
