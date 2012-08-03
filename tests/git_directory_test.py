from unittest import TestCase
from pycheckup.git import GitRepo


class GitDirectoryTest(TestCase):

    def setUp(self):
        self.repo = GitRepo('mjp', 'pycheckup')

    def test_hash_user_and_repo_name(self):
        self.assertEqual(len(self.repo._working_dir_hash()), 40)

    def test_working_dir_is_in_tmp(self):
        self.assertTrue(self.repo.working_dir.startswith('./tmp'))

    def test_github_url(self):
        self.assertEqual(self.repo.github_url, 'https://github.com/mjp/pycheckup.git')
