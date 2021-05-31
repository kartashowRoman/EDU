import sys
from requests import get
from collections import Counter

class Repository:
    def __init__(self, json):
        self.name = json['name']
        self.description = json['description']
        self.language = json['language']

class User:
    def __init__(self, name):
        self.name = name
        self.url = f'https://github.com/{name}'

        self.repos = []
        self._update_repos()

        self.follower_count = None
        self._update_follower_count()

    def _update_repos(self):
        cur_page = 1
        while True:
            url = f'https://api.github.com/users/{self.name}/repos'
            params = {'page': cur_page}
            r = get(url, params=params).json()
            if not r:
                break
            self.repos.extend([Repository(x) for x in r])
            cur_page += 1

    def _update_follower_count(self):
            url = f'https://api.github.com/users/{self.name}/followers'
            r = get(url).json()
            self.follower_count = len(r)


    def print_lang_count(self):
        c = Counter(x.language for x in self.repos)
        print(f'Language counts for user {self.name}:')
        for lang, cnt in c.items():
            print(f'{lang}: {cnt}')
        print()

    def _update_repos(self):
        cur_page = 1
        while True:
            url = f'https://api.github.com/users/{self.name}/repos'
            params = {'page': cur_page}
            r = get(url, params=params).json()
            if not r:
                break
            self.repos.extend([Repository(x) for x in r])
            cur_page += 1

user_names = sys.argv[1:]
cur_user = 'fabpot' # input()
users = {name: User(name) for name in user_names}


users[cur_user].print_lang_count()
max_repos_user_name = max(users, key=lambda u: len(users[u].repos))
print(f'User with max count of repos: {max_repos_user_name}')

total_lang_cnt = Counter([r.language for u in users.values() for r in u.repos if r.language is not None])
most_popular_lang = max(total_lang_cnt, key=lambda lang: total_lang_cnt[lang])
print(f'Most popular language: {most_popular_lang}')

most_followed_user = max(users, key=lambda u: users[u].follower_count)
print(f'Most follower user: {most_followed_user}')
