GITHUB_CLIENT_ID = '{{ GITHUB_CLIENT_ID }}'
GITHUB_CLIENT_SECRET = '{{ GITHUB_CLIENT_SECRET }}'

SOCIAL_AUTH_GITHUB = {
    'SOCIAL_AUTH_GITHUB_KEY': GITHUB_CLIENT_ID,
    'SOCIAL_AUTH_GITHUB_SECRET': GITHUB_CLIENT_SECRET,
    'SOCIAL_AUTH_GITHUB_SCOPE': ['repo:status', 'read:org'],
}

SOCIAL_AUTH_SETTINGS = {
    'SOCIAL_AUTH_LOGIN_URL': '/',
    'SOCIAL_AUTH_LOGIN_REDIRECT_URL': '/',
    'SOCIAL_AUTH_USER_MODEL': 'src.app.models.User',
    'SOCIAL_AUTH_LOGIN_FUNCTION': 'src.app.auth.login_user',
    'SOCIAL_AUTH_LOGGEDIN_FUNCTION': 'src.app.auth.login_required',
    'SOCIAL_AUTH_AUTHENTICATION_BACKENDS': (
        'social.backends.github.GithubOAuth2',
    )
}


def includeme(config):
    config.registry.settings.update(SOCIAL_AUTH_GITHUB)
    config.registry.settings.update(SOCIAL_AUTH_SETTINGS)
