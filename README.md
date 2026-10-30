Yuva Internship Task 2 – SOC Lab
Overview

This project demonstrates basic Security Operations Center (SOC) monitoring and failed-login detection using Kali Linux, Python, Docker, and OWASP Juice Shop.

Objectives
Set up a local security testing environment.
Collect Docker container logs.
Analyze authentication logs using Python.
Detect repeated failed-login attempts.
Document findings and save evidence.
Tools Used
Kali Linux
Python 3
Docker
OWASP Juice Shop
Detection Result

The Python script detected four failed login attempts from the fictional training IP address 192.0.2.10.

The alert threshold is three failed attempts per IP address.

Project Structure
evidence/ – Screenshots demonstrating the lab results.
logs/ – Application and fictional authentication logs.
reports/ – SOC analysis report.
rules/ – Python failed-login detection script.
Disclaimer

This project is intended for educational purposes. Authentication records are fictional training data.

Author

Vrushank Sabale
