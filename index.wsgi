import sae
from cineaste import wsgi

application = sae.create_wsgi_app(wsgi.application)
