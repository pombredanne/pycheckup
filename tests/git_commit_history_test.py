from datetime import datetime
from unittest import TestCase
from pycheckup.git import GitRepo


class GitCommitHistoryTest(TestCase):

    def setUp(self):
        self.repo = GitRepo('webpy', 'webpy')
        with open('tests/git_commit_history.txt', 'r') as f:
            self.commits = self.repo._parse_commit_log(f.read())

    def test_parses_each_commit(self):
        self.assertEqual(len(self.commits), 4)

    def test_commit_hash(self):
        self.assertEqual(len(self.commits[0]['rev']), 40)

    def test_commit_date(self):
        expected = datetime(year=2012, month=8, day=2, hour=22, minute=47, second=46)
        self.assertEqual(self.commits[0]['date'], expected)
