"""
Command Line Interface for Network Packet Analyzer
"""

import click
from .analyzer import PacketAnalyzer
from colorama import Fore, Style
import json
from pathlib import Path

@click.command()
@click.option('--interface', '-i', help='Network interface to capture from')
@click.option('--count', '-n', type=int, help='Number of packets to capture (default: infinite)')
@click.option('--filter', '-f', help='BPF filter string (e.g., "tcp port 80")')
@click.option('--output', '-o', help='Save captured packets to PCAP file')
@click.option('--stats-file', '-s', help='Save statistics to JSON file')
@click.option('--list-interfaces', '-l', is_flag=True, help='List available network interfaces')
@click.option('--analyze', '-a', help='Analyze existing PCAP file')
def main(interface, count, filter, output, stats_file, list_interfaces, analyze):
    """Network Packet Analyzer (NPA) - A professional-grade packet capture and analysis tool"""
    if list_interfaces:
        ifaces = PacketAnalyzer.list_interfaces()
        print(f"\n{Fore.CYAN}Available Network Interfaces:{Style.RESET_ALL}")
        for iface in ifaces:
            print(f"- {iface}")
        return

    if analyze:
        stats = PacketAnalyzer.analyze_pcap(analyze)
        if stats:
            print(f"\n{Fore.CYAN}Analysis Results:{Style.RESET_ALL}")
            print(f"Total Packets: {stats['total']}")
            print(f"TCP Packets:   {stats['tcp']}")
            print(f"UDP Packets:   {stats['udp']}")
            print(f"ICMP Packets:  {stats['icmp']}")
            print(f"Other Packets: {stats['other']}")
            
            if stats_file:
                try:
                    with open(stats_file, 'w') as f:
                        json.dump(stats, f, indent=4)
                    print(f"\nResults saved to: {stats_file}")
                except Exception as e:
                    print(f"{Fore.RED}Error saving results: {str(e)}{Style.RESET_ALL}")
        return

    # Default behavior: packet capture
    analyzer = PacketAnalyzer(
        interface=interface,
        output_file=output,
        filter_str=filter
    )
    
    stats = analyzer.start_capture(count=count)
    
    if stats and stats_file:
        analyzer.save_stats(stats_file)

if __name__ == '__main__':
    main() 