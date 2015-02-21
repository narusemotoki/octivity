from pyramid.config import Configurator
from pyramid.session import UnencryptedCookieSessionFactoryConfig
from social.apps.pyramid_app.models import init_social
from sqlalchemy import engine_from_config

from .models import Base
from .models import DBSession
import sys
sys.path.append('../..')


def route(config: Configurator):
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index', '/')
    config.add_route('login_callback_github', '/login/callback/github')


def template_enginge(config: Configurator):
    config.include('pyramid_jinja2')
    config.add_renderer('.html', 'pyramid_jinja2.renderer_factory')


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    engine = engine_from_config(settings, 'sqlalchemy.')
    DBSession.configure(bind=engine)
    Base.metadata.bind = engine

    session_factory = UnencryptedCookieSessionFactoryConfig('thisisasecret')

    config = Configurator(settings=settings,
                          session_factory=session_factory,
                          autocommit=True)

    config.add_request_method('.auth.get_user', 'user', reify=True)

    route(config)

    config.include('.config')
    config.include('social.apps.pyramid_app')
    init_social(config, Base, DBSession)

    config.scan()
    config.scan('social.apps.pyramid_app')

    template_enginge(config)

    return config.make_wsgi_app()
