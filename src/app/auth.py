from pyramid.events import BeforeRender
from pyramid.events import subscriber
from social.apps.pyramid_app.utils import backends

from .models import DBSession
from .models import User


def login_user(strategy, user, user_social_auth):
    print(dir(strategy.strategy))
    strategy.strategy.session_set('user_id', user.id)


def login_required(request):
    return getattr(request, 'user', None) is not None


def get_user(request):
    user_id = request.session.get('user_id')
    if user_id:
        return DBSession.query(User).filter(User.id == user_id).first()
    return None


@subscriber(BeforeRender)
def add_social(event):
    request = event['request']
    event['social'] = backends(request, request.user)
