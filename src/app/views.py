from pyramid.view import view_config
from .libs.github import GitHub


@view_config(route_name='index', renderer='index.html')
def index(request):
    if request.user is None:
        return {}

    github = GitHub(request.user.social_auth.one().extra_data['access_token'])

    for repo in github.fetch_repos():
        full_name = repo['full_name']
        pull_requests = github.fetch_repo_pull_requests(full_name)
        print('{} has {} pull requests'.format(full_name, len(pull_requests)))
        for pull_request in pull_requests:
            comments = github.fetch_repo_pull_request_comments(full_name, pull_request['number'])
            for comment in comments:
                print(comment['body'])

    return {}
