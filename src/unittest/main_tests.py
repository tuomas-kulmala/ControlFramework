import unittest
import main
from unittest.mock import MagicMock

class TestMainClass(unittest.TestCase):

    def test_queue_is_parse_at_init(self):
        runner = main.Runner()
        self.assertTrue(runner.queue != None)

    def test_verify_file_load(self):
        runner =  main.Runner()
        # what to verify ?!?


if __name__ == '__main__':
    unittest.main()