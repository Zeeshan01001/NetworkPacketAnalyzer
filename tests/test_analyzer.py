import unittest
from unittest.mock import patch, MagicMock
from npa.analyzer import PacketAnalyzer
from scapy.all import IP, TCP, UDP, ICMP

class TestPacketAnalyzer(unittest.TestCase):
    def setUp(self):
        self.analyzer = PacketAnalyzer()

    def test_init(self):
        """Test analyzer initialization"""
        self.assertIsNotNone(self.analyzer)
        self.assertIsNone(self.analyzer.interface)
        self.assertIsNone(self.analyzer.output_file)
        self.assertIsNone(self.analyzer.filter_str)
        self.assertEqual(self.analyzer.stats, {'tcp': 0, 'udp': 0, 'icmp': 0, 'other': 0})

    @patch('npa.analyzer.get_if_list')
    def test_list_interfaces(self, mock_if_list):
        """Test interface listing functionality"""
        mock_if_list.return_value = ['eth0', 'lo']
        interfaces = self.analyzer.list_interfaces()
        self.assertEqual(interfaces, ['eth0', 'lo'])
        mock_if_list.assert_called_once()

    @patch('npa.analyzer.sniff')
    def test_start_capture(self, mock_sniff):
        """Test packet capture functionality"""
        mock_packet = MagicMock()
        mock_sniff.return_value = [mock_packet]
        
        self.analyzer.interface = 'eth0'
        self.analyzer.filter_str = 'tcp'
        stats = self.analyzer.start_capture(count=1)
        
        self.assertIsNotNone(stats)
        mock_sniff.assert_called_once()
        kwargs = mock_sniff.call_args[1]
        self.assertEqual(kwargs['iface'], 'eth0')
        self.assertEqual(kwargs['filter'], 'tcp')
        self.assertEqual(kwargs['count'], 1)

    def test_packet_callback(self):
        """Test packet callback functionality"""
        # Create mock packets
        tcp_packet = MagicMock(spec=IP)
        tcp_packet.haslayer.side_effect = lambda x: x in [IP, TCP]
        tcp_packet.__contains__ = lambda s, x: x in [IP, TCP]
        tcp_packet[IP].src = '192.168.1.1'
        tcp_packet[IP].dst = '192.168.1.2'
        tcp_packet[TCP].sport = 12345
        tcp_packet[TCP].dport = 80
        
        udp_packet = MagicMock(spec=IP)
        udp_packet.haslayer.side_effect = lambda x: x in [IP, UDP]
        udp_packet.__contains__ = lambda s, x: x in [IP, UDP]
        udp_packet[IP].src = '192.168.1.1'
        udp_packet[IP].dst = '192.168.1.2'
        udp_packet[UDP].sport = 53
        udp_packet[UDP].dport = 53
        
        icmp_packet = MagicMock(spec=IP)
        icmp_packet.haslayer.side_effect = lambda x: x in [IP, ICMP]
        icmp_packet.__contains__ = lambda s, x: x in [IP, ICMP]
        icmp_packet[IP].src = '192.168.1.1'
        icmp_packet[IP].dst = '192.168.1.2'

        # Test packet classification
        self.analyzer.packet_callback(tcp_packet)
        self.analyzer.packet_callback(udp_packet)
        self.analyzer.packet_callback(icmp_packet)

        # Verify statistics
        self.assertEqual(self.analyzer.stats['tcp'], 1)
        self.assertEqual(self.analyzer.stats['udp'], 1)
        self.assertEqual(self.analyzer.stats['icmp'], 1)
        self.assertEqual(self.analyzer.stats['other'], 0)

if __name__ == '__main__':
    unittest.main() 