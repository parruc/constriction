#!/bin/bash
cd /project/constriction
/project/bin/python manage.py collectstatic --noinput
chown www-data:www-data /var/www/static/ -R
chown www-data:www-data /var/www/media/ -R
/project/bin/python manage.py makemigrations
/project/bin/python manage.py migrate
/project/bin/python manage.py compilemessages
chown www-data:www-data /var/log/django -R
