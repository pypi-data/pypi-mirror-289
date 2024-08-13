import unittest
import os
from pathlib import Path
from typer.testing import CliRunner
from setup_flask_app import app

runner = CliRunner()


DIRECTORIES = ['app']
FILES = ['config.py', 'run.py']
TEST_DIR = 'test_project'

class SimpleTest(unittest.TestCase):
    def test_1_check_structure(self):
        result = runner.invoke(app, [TEST_DIR])
        self.assertTrue(result.exit_code == 0, "Cli command Failed")
        for dir in DIRECTORIES:
            self.assertTrue((Path.cwd()/TEST_DIR/dir).is_dir(), f"Directory {dir} is missing")

        for file in FILES:
            self.assertTrue((Path.cwd()/TEST_DIR/file).is_file(), f"File {file} is missing")
            
        print(f"test 1 passed directory structure is OK")

    if __name__ == '__main__':
        unittest.main()