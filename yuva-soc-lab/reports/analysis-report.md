# Yuva Internship - SOC Lab Analysis Report

## 1. Objective
Detect suspicious login activity using Python log analysis.

## 2. Tools Used
- Kali Linux
- Python 3
- Docker
- OWASP Juice Shop

## 3. Detection Method
A Python script analyzed authentication logs and counted failed login attempts by IP address.

## 4. Finding
The script detected 4 failed login attempts from IP 192.0.2.10.

## 5. Alert Threshold
An alert is generated when an IP address has 3 or more failed login attempts.

## 6. Conclusion
The script successfully identified a repeated failed-login pattern.
This demonstrates a basic SOC detection technique.

Note: The authentication records used in this exercise are fictional training data.
