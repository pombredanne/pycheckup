import hashlib
import os
import shutil
import subprocess
from datetime import datetime


class GitRepo(object):

    def __init__(self, user, repo_name):
        self.user = user
        self.repo_name = repo_name
        self.working_dir = self._working_dir()
        self.github_url = self._github_url()
        self.commits = []

    def clone(self):
        self.check_env()
        cmd = ['git', 'clone', self.github_url, self.working_dir]
        subprocess.check_call(cmd)

    def check_env(self):
        if os.path.isdir('./tmp') is False:
            os.mkdir('./tmp')

        self.cleanup()

    def cleanup(self):
        if os.path.isdir(self.working_dir):
            shutil.rmtree(self.working_dir)

    def load_commits(self):
        cmd = ['git', 'log', '--since=2011-07-01', '--no-notes', '--date=iso']

        raw = subprocess.check_output(cmd, cwd=self.working_dir)
        self.commits = self._parse_commit_log(raw)

    def _parse_commit_log(self, log):
        commit_strings = [c for c in log.split("\ncommit ")]

        def parse_commit(raw):
            date_line = None

            for line in raw.split("\n"):
                if line.startswith('Date: '):
                    date_line = line

            return {
                'rev': raw.split("\n")[0][:40],
                'date': datetime.strptime(date_line[8:-6], '%Y-%m-%d %H:%M:%S')
            }

        return [parse_commit(c) for c in commit_strings]
    
    def _working_dir(self):
        return './tmp/%s' % self._working_dir_hash()

    def _working_dir_hash(self):
        return hashlib.sha1('%s/%s' % (self.user, self.repo_name)).hexdigest()

    def _github_url(self):
        return 'https://github.com/%s/%s.git' % (self.user, self.repo_name)
