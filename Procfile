web: gunicorn new_portal.wsgi --log-file - 
#or works good with external database
web: python manage.py migrate && gunicorn new_portal.wsgi