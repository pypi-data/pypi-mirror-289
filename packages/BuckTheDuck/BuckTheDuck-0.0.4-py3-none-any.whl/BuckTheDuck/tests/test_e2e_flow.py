import os
from unittest.mock import patch

import pytest

from BuckTheDuck.manager.cli_manager import CliManager
from BuckTheDuck.common.exceptions import UnsupportedOperation


class TestE2EFlow:

    def test_project_will_not_start_without_config(self):
        try:
            CliManager().run('commit', [])
            assert False, 'Expected to fail to commit as no config file were set'
        except UnsupportedOperation:
            assert True

    def test_init_flow(self):
        CliManager().run('init', [])

    def test_commit_flow(self):
        CliManager().run('commit', [])

    def test_commit_and_push_flow(self):
        CliManager().run('cop', ['-c', '-v'])

    def test_code_review(self):
        CliManager().run('cr', [])

    def test_file_manager(self):
        CliManager().run('file_control', [])

    def test_project_summarizer(self):
        CliManager().run('summarize_repo', [])
