import os
import sys
import json
from datetime import datetime

from thttp import request


def cleanup():
    token = os.environ.get('GITHUB_TOKEN')
    if not token:
        print('GITHUB_TOKEN missing from environment')
        sys.exit()

    headers = {
        'accept': 'application/vnd.github.v3+json',
        'Authorization': 'token {token}'
    }

    response = request('https://api.github.com/user/repos', {'visibility': 'public', 'affiliation': 'owner', 'per_page': 100}, headers=headers)

    for repo in response.json:
        days_ago = (datetime.now() - datetime.strptime(repo['pushed_at'], '%Y-%m-%dT%H:%M:%SZ')).days

        if repo['permissions']['admin'] and repo['stargazers_count'] < 3 and days_ago > 365:
            if repo['fork']:
                print(f'DELETING {repo["full_name"]} {repo["url"]}')
                response = request(repo['url'], method='DELETE', headers=headers)
            else:
                print(f'Making {repo["full_name"]} private')
                response = request(repo['url'], json={'private': 'true'}, method='PATCH', headers=headers)

            if response.status > 399:
                print(f'    Failed? {response.json}')


if __name__ == "__main__":
    cleanup()