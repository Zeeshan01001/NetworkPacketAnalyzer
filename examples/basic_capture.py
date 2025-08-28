#!/usr/bin/env python3
"""
Basic example of using the Network Packet Analyzer
"""

from npa.analyzer import PacketAnalyzer
import time

def main():
    # Initialize the analyzer
    analyzer = PacketAnalyzer(
        interface="eth0",  # Change this to your interface
        filter_str="tcp",  # Only capture TCP packets
        output_file=f"capture_{int(time.time())}.pcap"
    )
    
    print("Starting packet capture... Press Ctrl+C to stop")
    try:
        # Capture 100 packets
        stats = analyzer.start_capture(count=100)
        
        if stats:
            print("\nCapture Statistics:")
            print(f"TCP Packets:   {stats['tcp']}")
            print(f"UDP Packets:   {stats['udp']}")
            print(f"ICMP Packets:  {stats['icmp']}")
            print(f"Other Packets: {stats['other']}")
    
    except KeyboardInterrupt:
        print("\nCapture stopped by user")

if __name__ == "__main__":
    main() 