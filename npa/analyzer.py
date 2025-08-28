"""
Core functionality for Network Packet Analyzer
"""

from scapy.all import *
from colorama import Fore, Style, init
import time
import json
from pathlib import Path

# Initialize colorama
init()

class PacketAnalyzer:
    def __init__(self, interface=None, output_file=None, filter_str=None):
        self.interface = interface
        self.output_file = output_file
        self.filter_str = filter_str
        self.stats = {
            'tcp': 0,
            'udp': 0,
            'icmp': 0,
            'other': 0
        }
    
    def packet_callback(self, packet):
        """Process each captured packet"""
        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        
        if IP in packet:
            ip_src = packet[IP].src
            ip_dst = packet[IP].dst
            
            if TCP in packet:
                self.stats['tcp'] += 1
                print(f"{Fore.GREEN}[{timestamp}] TCP{Style.RESET_ALL} "
                      f"{ip_src}:{packet[TCP].sport} → {ip_dst}:{packet[TCP].dport}")
            elif UDP in packet:
                self.stats['udp'] += 1
                print(f"{Fore.BLUE}[{timestamp}] UDP{Style.RESET_ALL} "
                      f"{ip_src}:{packet[UDP].sport} → {ip_dst}:{packet[UDP].dport}")
            elif ICMP in packet:
                self.stats['icmp'] += 1
                print(f"{Fore.YELLOW}[{timestamp}] ICMP{Style.RESET_ALL} "
                      f"{ip_src} → {ip_dst}")
            else:
                self.stats['other'] += 1
                print(f"{Fore.WHITE}[{timestamp}] OTHER{Style.RESET_ALL} "
                      f"{ip_src} → {ip_dst}")

    def start_capture(self, count=None):
        """Start packet capture"""
        try:
            kwargs = {
                'prn': self.packet_callback,
                'store': False
            }
            
            if self.interface:
                kwargs['iface'] = self.interface
            if self.filter_str:
                kwargs['filter'] = self.filter_str
            if count:
                kwargs['count'] = count
            if self.output_file:
                kwargs['store'] = True
            
            print(f"{Fore.CYAN}Starting packet capture...{Style.RESET_ALL}")
            if self.interface:
                print(f"Interface: {self.interface}")
            if self.filter_str:
                print(f"Filter: {self.filter_str}")
            
            packets = sniff(**kwargs)
            
            if self.output_file:
                wrpcap(self.output_file, packets)
                print(f"\nPackets saved to: {self.output_file}")
            
            return self.stats
            
        except PermissionError:
            print(f"{Fore.RED}Error: Root privileges required.{Style.RESET_ALL}")
            print("Try running with sudo")
            return None
        except Exception as e:
            print(f"{Fore.RED}Error: {str(e)}{Style.RESET_ALL}")
            return None

    @staticmethod
    def list_interfaces():
        """List available network interfaces"""
        return get_if_list()

    @staticmethod
    def analyze_pcap(pcap_file):
        """Analyze existing PCAP file"""
        try:
            packets = rdpcap(pcap_file)
            stats = {
                'tcp': 0,
                'udp': 0,
                'icmp': 0,
                'other': 0,
                'total': len(packets)
            }
            
            for packet in packets:
                if TCP in packet:
                    stats['tcp'] += 1
                elif UDP in packet:
                    stats['udp'] += 1
                elif ICMP in packet:
                    stats['icmp'] += 1
                else:
                    stats['other'] += 1
            
            return stats
        except Exception as e:
            print(f"{Fore.RED}Error analyzing PCAP file: {str(e)}{Style.RESET_ALL}")
            return None

    def save_stats(self, output_file):
        """Save capture statistics to JSON file"""
        try:
            with open(output_file, 'w') as f:
                json.dump(self.stats, f, indent=4)
            print(f"\nStatistics saved to: {output_file}")
        except Exception as e:
            print(f"{Fore.RED}Error saving statistics: {str(e)}{Style.RESET_ALL}") 