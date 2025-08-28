# SQL Injection: A Comprehensive Guide

[![Security](https://img.shields.io/badge/Security-Critical-red.svg)](https://owasp.org/www-project-top-ten/2017/A1_2017-Injection)
[![OWASP](https://img.shields.io/badge/OWASP-Top%2010-blue.svg)](https://owasp.org/www-project-top-ten/)

## Table of Contents
- [Introduction](#introduction)
- [Types of SQL Injection](#types-of-sql-injection)
- [Common Attack Vectors](#common-attack-vectors)
- [Prevention Techniques](#prevention-techniques)
- [Real-World Examples](#real-world-examples)
- [Best Practices](#best-practices)
- [Testing for SQL Injection](#testing-for-sql-injection)
- [Resources](#resources)

## Introduction

SQL Injection (SQLi) is a critical web security vulnerability that allows attackers to manipulate database queries by injecting malicious SQL code. This can lead to:
- Unauthorized data access
- Data manipulation or destruction
- Administrative operations on the database
- Remote command execution

## Types of SQL Injection

### 1. In-band SQLi
- **Error-based**: Relies on error messages from database
- **Union-based**: Uses UNION operator to combine results

### 2. Blind SQLi
- **Boolean-based**: Uses true/false questions
- **Time-based**: Uses time delays to infer results

### 3. Out-of-band SQLi
- Uses external channels to extract data
- Examples: DNS or HTTP requests

## Common Attack Vectors

### 1. Basic SQL Injection
```sql
-- Original query
SELECT * FROM users WHERE username = 'input' AND password = 'input'

-- Malicious input
username: admin' --
password: anything

-- Resulting query
SELECT * FROM users WHERE username = 'admin' --' AND password = 'anything'
```

### 2. Union-Based Injection
```sql
-- Malicious input
' UNION SELECT username, password FROM users--

-- Resulting query
SELECT column FROM table WHERE id = '' UNION SELECT username, password FROM users--'
```

## Prevention Techniques

### 1. Prepared Statements
```python
# Bad practice
cursor.execute("SELECT * FROM users WHERE id = '" + user_input + "'")

# Good practice
cursor.execute("SELECT * FROM users WHERE id = ?", (user_input,))
```

### 2. Input Validation
```python
import re

def validate_input(user_input):
    # Remove special characters
    return re.sub(r'[^a-zA-Z0-9]', '', user_input)
```

### 3. Parameterized Queries
```java
// Bad practice
String query = "SELECT * FROM users WHERE username = '" + username + "'";

// Good practice
PreparedStatement stmt = connection.prepareStatement("SELECT * FROM users WHERE username = ?");
stmt.setString(1, username);
```

### 4. ORM Usage
```python
# Using SQLAlchemy (Python)
user = db.session.query(User).filter(User.username == username).first()
```

## Real-World Examples

1. **The Equifax Breach (2017)**
   - 147 million records exposed
   - Caused by SQL injection vulnerability
   - Cost: $1.4 billion

2. **Yahoo Data Breach (2012)**
   - 500 million accounts compromised
   - SQL injection was one of the attack vectors

## Best Practices

### 1. Defense in Depth
- Use WAF (Web Application Firewall)
- Implement input validation
- Use prepared statements
- Apply principle of least privilege

### 2. Database Hardening
```sql
-- Restrict database user privileges
GRANT SELECT, INSERT ON application_table TO 'app_user'@'localhost';

-- Regular security audits
SHOW GRANTS FOR 'app_user'@'localhost';
```

### 3. Error Handling
```python
try:
    # Database operations
    result = execute_query(params)
except DatabaseError as e:
    # Log error securely
    log.error("Database error occurred", extra={'error': str(e)})
    # Return generic error to user
    return "An error occurred processing your request"
```

## Testing for SQL Injection

### 1. Manual Testing
Common test strings:
```
'
' OR '1'='1
' UNION SELECT NULL--
' WAITFOR DELAY '0:0:10'--
```

### 2. Automated Tools
- SQLmap
- Burp Suite
- OWASP ZAP

### 3. CI/CD Integration
```yaml
# Example GitHub Actions workflow
name: Security Scan
on: [push]
jobs:
  security:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Run SQLMap
      run: |
        pip install sqlmap
        sqlmap --url "http://target-url" --batch
```

## Resources

### Official Documentation
- [OWASP SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
- [NIST Guidelines](https://nvd.nist.gov/)

### Tools
- [SQLMap](http://sqlmap.org/)
- [OWASP ZAP](https://www.zaproxy.org/)

### Learning Resources
- [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [HackerOne CTF](https://www.hackerone.com/hacktivity)

## Contributing

Feel free to contribute to this guide by:
1. Forking the repository
2. Creating your feature branch
3. Committing your changes
4. Opening a pull request

## License

This guide is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

**Disclaimer**: This guide is for educational purposes only. Do not use these techniques against systems you don't own or have explicit permission to test. 