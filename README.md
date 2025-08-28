# Network Packet Analyzer (NPA)

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/) [![Scapy](https://img.shields.io/badge/scapy-latest-green.svg)](https://scapy.net/) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) [![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A powerful and user-friendly network packet analyzer built with Python and Scapy. Monitor, capture, and analyze network traffic with ease.

## Features

- Real-time packet capture and analysis
- Support for TCP, UDP, and ICMP protocols
- Colorized output for different packet types
- PCAP file analysis
- Network interface listing
- Packet filtering capabilities
- Statistics collection and reporting

## Installation

### Prerequisites

- Python 3.7 or higher
- Root/sudo privileges (only required for packet capture operations)

```bash
# Install system dependencies (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install python3-dev python3-pip python3-venv libpcap-dev

# Install the package
pip install .
```

For development installation:
```bash
pip install -e .
```

## Usage

### Basic Commands (No sudo required)

1. List available network interfaces:
```bash
npa --list-interfaces
# or
npa -l
```

2. Analyze existing PCAP file:
```bash
npa --analyze capture.pcap
# or
npa -a capture.pcap
```

3. View help and options:
```bash
npa --help
```

### Capture Commands (sudo required)

1. Capture packets on a specific interface:
```bash
sudo npa --interface eth0
# or
sudo npa -i eth0
```

2. Capture with filter:
```bash
sudo npa --interface eth0 --filter "tcp port 80"
```

3. Capture specific number of packets:
```bash
sudo npa --interface eth0 --count 100
```

4. Save captured packets to a file:
```bash
sudo npa --interface eth0 --output capture.pcap
```

### Advanced Usage

- Combine filters (requires sudo):
```bash
sudo npa --interface eth0 --filter "tcp and port 443" --count 50
```

- Save statistics to JSON (requires sudo for live capture):
```bash
sudo npa --interface eth0 --count 100 --stats stats.json
```

- Analyze saved capture and generate stats (no sudo required):
```bash
npa --analyze capture.pcap --stats analysis.json
```

## Command Options

- `-l, --list-interfaces`: List available interfaces
- `-i, --interface`: Network interface to capture from (requires sudo)
- `-n, --count`: Number of packets to capture
- `-f, --filter`: BPF filter string
- `-o, --output`: Save captured packets to PCAP file
- `-s, --stats-file`: Save statistics to JSON file
- `-a, --analyze`: Analyze existing PCAP file
- `-h, --help`: Show help message

## Development

### Setting up Development Environment

```bash
# Clone the repository
git clone https://github.com/yourusername/NetworkPacketAnalyzer.git
cd NetworkPacketAnalyzer

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install development dependencies
pip install -e ".[dev]"
```

### Running Tests

```bash
python -m pytest tests/
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with [Scapy](https://scapy.net/)
- Inspired by Wireshark and tcpdump
- Thanks to all contributors

## 🚀 Key Features

- **Real-time Traffic Analysis**: Capture and analyze network packets in real-time
- **Protocol Support**: Comprehensive analysis of TCP, UDP, ICMP, and other protocols
- **Advanced Filtering**: Sophisticated packet filtering based on multiple criteria
- **Data Export**: Export captured data in PCAP format for further analysis
- **Interface Flexibility**: Support for multiple network interfaces
- **Statistical Analysis**: Generate traffic patterns and network usage statistics
- **Simple CLI**: Single command interface for all operations

## 📋 Prerequisites

- Python 3.x
- Scapy library
- Root/Administrator privileges (required for packet capturing)
- Linux/Unix environment (recommended)

## 🛠️ Installation

1. Verify Python installation:
   ```bash
   python3 --version
   ```

2. Install the package globally:
   ```bash
   pip install network-packet-analyzer
   ```

   Or install in development mode:
   ```bash
   git clone https://github.com/yourusername/NetworkPacketAnalyzer
   cd NetworkPacketAnalyzer
   pip install -e .
   ```

## 💻 CLI Usage

The Network Packet Analyzer uses a single command `npa` with various options:

### List Available Network Interfaces
```bash
npa --list-interfaces
# or
npa -l
```

### Capture Packets
```bash
# Basic capture
npa

# With options
npa --interface eth0 --count 100 --filter "tcp port 80" --output capture.pcap --stats-file stats.json
# or short form
npa -i eth0 -n 100 -f "tcp port 80" -o capture.pcap -s stats.json
```

### Analyze PCAP Files
```bash
npa --analyze capture.pcap --stats-file analysis.json
# or
npa -a capture.pcap -s analysis.json
```

### Options
- `-i, --interface`: Network interface to capture from
- `-n, --count`: Number of packets to capture
- `-f, --filter`: BPF filter string
- `-o, --output`: Save captured packets to PCAP file
- `-s, --stats-file`: Save statistics to JSON file
- `-l, --list-interfaces`: List available interfaces
- `-a, --analyze`: Analyze existing PCAP file

## 🔒 Security Best Practices

1. **Access Control**
   - Always run with appropriate permissions
   - Use principle of least privilege
   - Implement proper user authentication

2. **Data Protection**
   - Avoid capturing sensitive data
   - Implement data encryption when storing captures
   - Regular cleanup of captured data

3. **Compliance**
   - Follow network monitoring regulations
   - Obtain necessary permissions
   - Document all monitoring activities

## 🐛 Troubleshooting Guide

### Common Issues

1. **Permission Errors**
   - Run with appropriate privileges
   - Check file permissions

2. **Interface Problems**
   ```bash
   npa --list-interfaces
   ```

3. **Performance Optimization**
   - Use appropriate packet filters
   - Implement packet count limits
   - Regular memory cleanup

## 📈 Future Enhancements

- GUI Interface
- Real-time traffic visualization
- Machine learning-based traffic analysis
- Protocol-specific detailed analysis
- Network anomaly detection
- Custom plugin support

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Scapy development team
- Python networking community
- Open source contributors

## ⚠️ Disclaimer

This tool is designed for professional network analysis and educational purposes. Users must comply with all applicable laws and regulations regarding network monitoring and packet capturing in their jurisdiction. Root/sudo privileges are only required for live packet capture operations. 