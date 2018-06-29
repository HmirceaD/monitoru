"""unittest to see if ParseArguments returns the correct values"""
import unittest

from monitoru.parse_arguments import ParseArguments


class TestParseArguments(unittest.TestCase):
    """unit test class, tests the ParseArguments.parse_arguments function"""
    @classmethod
    def setUpClass(cls):
        cls.parse_arg = ParseArguments()

    def test_parse_arguments(self):
        """checks to see if function returns
        the expected values under certain circumstances"""
        self.assertEqual(self.parse_arg.check_command("help"), 0)
        self.assertEqual(self.parse_arg.check_command("stop"), 1)
        self.assertEqual(self.parse_arg.check_command("reset"), 2)
        self.assertEqual(self.parse_arg.check_command("config"), 3)
        self.assertEqual(self.parse_arg.check_command(
                            "sunt un calut fericit"), -1)
        self.assertEqual(self.parse_arg.check_command("help start"), -1)
