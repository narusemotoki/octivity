from rauth import OAuth2Service
from .. import config

class GitHub:
    """GitHub関連の処理はここ
    """
    def __init__(self, access_token: str):
        self.client = OAuth2Service(
            client_id=config.GITHUB_CLIENT_ID,
            client_secret=config.GITHUB_CLIENT_SECRET,
            name='github',
            base_url='https://api.github.com/'
        ).get_session(access_token)

    def fetch_repos(self) -> list:
        return self.client.get('/user/repos', params={
            'sort': 'updated',
        }).json()

    def fetch_repo_pull_requests(self, full_name: str) -> list:
        return self.client.get('/repos/{}/pulls'.format(full_name), params={
            'sort': 'updated',
            'state': 'open',
        }).json()

    def fetch_repo_pull_request_comments(self, full_name: str, pull_request_id: int) -> list:
        return self.client.get('/repos/{}/pulls/{}/comments'.format(
            full_name, pull_request_id)).json()
