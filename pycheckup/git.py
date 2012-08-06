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
        self._check_env()
        cmd = ['git', 'clone', self.github_url, self.working_dir]
        subprocess.check_call(cmd)

    def cleanup(self):
        if os.path.isdir(self.working_dir):
            shutil.rmtree(self.working_dir)

    def load_commits(self):
        cmd = ['git', 'log', '--since=2011-12-01', '--no-notes', '--date=iso']

        raw = subprocess.check_output(cmd, cwd=self.working_dir)
        self.commits = self._parse_commit_log(raw)

    def checkout(self, rev):
        cmd = ['git', 'checkout', '-q', rev]
        subprocess.check_call(cmd, cwd=self.working_dir)

    def commit_num_lines_changed(self, rev):
        cmd = ['git', 'show', rev]
        raw = subprocess.check_output(cmd, cwd=self.working_dir)

        changed = 0
        for line in raw.split("\n"):
            if line.startswith('+ ') or line.startswith('- '):
                changed += 1

        return changed

    def _check_env(self):
        if os.path.isdir('./tmp') is False:
            os.mkdir('./tmp')

        self.cleanup()

    def _parse_commit_log(self, log):
        commit_strings = [c for c in log.split("\ncommit ")]

        commits = []
        for raw in commit_strings:
            try:
                rev = raw.split("\n")[0]
                if rev.startswith('commit '):
                    rev = rev.replace('commit ', '')

                date_line = None

                for line in raw.split("\n"):
                    if line.startswith('Date: '):
                        date_line = line

                commits.append({
                    'rev': rev,
                    'date': datetime.strptime(date_line[8:-6], '%Y-%m-%d %H:%M:%S')
                })
            except (TypeError, ValueError):
                pass

        return commits

    def _working_dir(self):
        return './tmp/%s' % self._working_dir_hash()

    def _working_dir_hash(self):
        return hashlib.sha1('%s/%s' % (self.user, self.repo_name)).hexdigest()

    def _github_url(self):
        return 'https://github.com/%s/%s.git' % (self.user, self.repo_name)
