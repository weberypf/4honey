import sae

from honey import wsgi


application = sae.create_wsgi_app(wsgi.application)