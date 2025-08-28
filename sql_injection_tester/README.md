# 🛡️ Advanced SQL Injection Testing Framework (ASITF)

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A comprehensive Python-based framework for advanced SQL injection vulnerability testing. This framework is designed for security professionals and ethical hackers to conduct thorough security assessments on authorized systems.

## 🌟 Advanced Features

### 🔍 Detection Capabilities
- Advanced payload generation using machine learning
- Multiple injection point detection (GET, POST, Headers, Cookies)
- Time-based blind SQL injection detection
- Boolean-based blind SQL injection detection
- Error-based SQL injection detection
- UNION-based SQL injection detection
- Out-of-band SQL injection testing
- Database fingerprinting
- WAF (Web Application Firewall) detection and evasion techniques

### 🛠️ Testing Features
- Multi-threaded scanning
- Proxy support (HTTP, SOCKS)
- Custom HTTP header manipulation
- Cookie handling and session management
- Authentication support
- Rate limiting and request throttling
- Response analysis using ML/pattern matching
- Automatic payload encoding/decoding
- Custom payload templating

### 📊 Reporting & Analysis
- Detailed HTML reports with vulnerability evidence
- Export results in multiple formats (JSON, CSV, XML)
- Screenshot capture of vulnerable pages
- Request/Response logging
- Integration with popular bug tracking systems
- Risk scoring and severity assessment
- Remediation suggestions

## 🏗️ Project Structure

```
sql-injection-tester/
├── src/
│   ├── core/
│   │   ├── __init__.py
│   │   ├── scanner.py          # Main scanning engine
│   │   ├── payload_gen.py      # Payload generation logic
│   │   ├── detector.py         # Injection detection algorithms
│   │   └── reporter.py         # Report generation
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── http_client.py      # Custom HTTP client
│   │   ├── encoders.py         # Payload encoding utilities
│   │   ├── logger.py           # Logging utilities
│   │   └── helpers.py          # Helper functions
│   └── ml/
│       ├── __init__.py
│       ├── trainer.py          # ML model training
│       └── predictor.py        # ML-based detection
├── data/
│   ├── payloads/
│   │   ├── error_based.txt
│   │   ├── blind.txt
│   │   ├── time_based.txt
│   │   └── union_based.txt
│   ├── patterns/
│   │   ├── error_patterns.json
│   │   └── dbms_patterns.json
│   └── ml_models/
│       └── detection_model.pkl
├── tests/
│   ├── unit/
│   │   └── test_*.py
│   └── integration/
│       └── test_*.py
├── docs/
│   ├── api/
│   ├── examples/
│   └── tutorials/
├── reports/
│   ├── templates/
│   └── outputs/
├── config/
│   ├── settings.yaml
│   └── logging.yaml
├── requirements/
│   ├── base.txt
│   ├── dev.txt
│   └── test.txt
├── scripts/
│   ├── setup.sh
│   └── install_deps.sh
├── Dockerfile
├── docker-compose.yml
├── setup.py
├── requirements.txt
├── README.md
└── LICENSE
```

## 🔧 Installation

### Using pip
```bash
pip install -r requirements/base.txt
```

### Using Docker
```bash
docker build -t asitf .
docker run -it asitf
```

### Development Setup
```bash
pip install -r requirements/dev.txt
pre-commit install
```

## 🎯 Usage Examples

### Basic Scan
```python
from asitf.core import Scanner

scanner = Scanner(
    target="http://example.com",
    threads=10,
    proxy="http://127.0.0.1:8080"
)
results = scanner.run()
```

### Advanced Configuration
```python
from asitf.core import Scanner, ScanConfig
from asitf.utils import PayloadGenerator

config = ScanConfig(
    threads=20,
    timeout=30,
    retry_count=3,
    user_agent="Custom UA",
    cookies={"session": "xyz"},
    headers={"X-Forward-For": "127.0.0.1"},
    proxy="socks5://127.0.0.1:9050"
)

# Custom payload generation
payloads = PayloadGenerator(
    template="${injection}",
    encoding="base64",
    evasion_level=2
).generate()

scanner = Scanner(
    target="http://example.com",
    config=config,
    payloads=payloads
)

# Async scanning
async def scan():
    async for result in scanner.scan_async():
        print(f"Found vulnerability: {result}")
```

### ML-based Detection
```python
from asitf.ml import SQLiPredictor

predictor = SQLiPredictor(model_path="data/ml_models/detection_model.pkl")
is_vulnerable = predictor.predict(response_data)
```

## 🔬 Advanced Features Documentation

### Custom Payload Templates
```python
# Template-based payload generation
template = """
SELECT * FROM users WHERE id=${id} AND ${injection}
"""

generator = PayloadGenerator(template=template)
payloads = generator.generate(
    injection_points=["id"],
    encoding="hex",
    evasion=True
)
```

### WAF Detection & Evasion
```python
from asitf.core import WAFDetector, WAFEvasion

# Detect WAF
waf = WAFDetector().detect(response)
if waf:
    print(f"Detected WAF: {waf.name}")
    
    # Apply evasion techniques
    payload = WAFEvasion(waf=waf.name).evade(original_payload)
```

### Custom Response Analysis
```python
from asitf.core import ResponseAnalyzer

analyzer = ResponseAnalyzer(
    ml_enabled=True,
    pattern_matching=True,
    similarity_threshold=0.85
)

result = analyzer.analyze(
    original_response=resp1,
    injected_response=resp2
)
```

## 🎓 Advanced Usage Scenarios

### Time-based Blind Detection
```python
from asitf.core import BlindSQLiDetector

detector = BlindSQLiDetector(
    delay_threshold=5,
    retry_count=3
)

is_vulnerable = await detector.detect_time_based(
    url="http://example.com",
    param="id"
)
```

### Database Fingerprinting
```python
from asitf.core import DBMSFingerprinter

fingerprinter = DBMSFingerprinter()
dbms = fingerprinter.identify(response_data)
print(f"Detected DBMS: {dbms.name} {dbms.version}")
```

## 🔐 Security Features

- Automatic request rate limiting
- IP rotation support
- Tor network integration
- Custom HTTP header signatures
- Response data sanitization
- Secure logging practices

## 📊 Reporting Features

- Detailed vulnerability analysis
- Proof of concept generation
- CVSS score calculation
- Export to various formats
- Integration with security tools
- Custom report templating

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Implement your feature
4. Add tests
5. Submit a pull request

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Legal Disclaimer

This tool is meant for ethical security testing only. Users must obtain explicit permission before testing any systems. The authors are not responsible for misuse or damages. 