import unittest
from unittest.mock import patch
from click.testing import CliRunner
from npa.cli import main

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()

    def test_help(self):
        """Test help output"""
        result = self.runner.invoke(main, ['--help'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('Usage:', result.output)

    @patch('npa.analyzer.PacketAnalyzer.list_interfaces')
    def test_list_interfaces(self, mock_list_interfaces):
        """Test interface listing command"""
        mock_list_interfaces.return_value = ['eth0', 'lo']
        result = self.runner.invoke(main, ['--list-interfaces'])
        self.assertEqual(result.exit_code, 0)
        self.assertIn('eth0', result.output)
        self.assertIn('lo', result.output)

    @patch('npa.analyzer.PacketAnalyzer.start_capture')
    def test_capture(self, mock_capture):
        """Test packet capture command"""
        mock_capture.return_value = {'tcp': 0, 'udp': 0, 'icmp': 0, 'other': 0}
        result = self.runner.invoke(main, [
            '--interface', 'eth0',
            '--count', '1',
            '--filter', 'tcp'
        ])
        self.assertEqual(result.exit_code, 0)
        mock_capture.assert_called_once()

if __name__ == '__main__':
    unittest.main() 