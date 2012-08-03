import hashlib
import shutil
import subprocess


class GitRepo(object):

    def __init__(self, user, repo_name):
        self.user = user
        self.repo_name = repo_name
        self.working_dir = self._working_dir()
        self.github_url = self._github_url()

    def clone(self):
        cmd = ['git', 'clone', self.github_url, self.working_dir]
        subprocess.check_call(cmd)

    def cleanup(self):
        shutil.rmtree(self.working_dir)
    
    def _working_dir(self):
        return './tmp/%s' % self._working_dir_hash()

    def _working_dir_hash(self):
        return hashlib.sha1('%s/%s' % (self.user, self.repo_name)).hexdigest()

    def _github_url(self):
        return 'https://github.com/%s/%s.git' % (self.user, self.repo_name)
