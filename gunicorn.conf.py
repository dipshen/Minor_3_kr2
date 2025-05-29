# Gunicorn configuration file
wsgi_app = "minor_3_kr1.wsgi:application"
workers = 4
threads = 1
timeout = 120
bind = "0.0.0.0:8000" 