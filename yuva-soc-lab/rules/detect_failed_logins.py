import csv
from collections import Counter

log_file = "/home/kali/yuva-soc-lab/logs/auth.log"
threshold = 3

failed_attempts = Counter()

with open(log_file, "r") as file:
    reader = csv.reader(file)

    for row in reader:
        if len(row) != 4:
            continue

        timestamp, ip, username, status = row

        if status == "FAILED":
            failed_attempts[ip] += 1

print("=== SOC Login Detection Report ===")

alerts_found = False

for ip, count in failed_attempts.items():
    if count >= threshold:
        print(
            f"ALERT: {count} failed login attempts "
            f"from IP {ip}"
        )
        alerts_found = True

if not alerts_found:
    print("No suspicious login patterns detected.")
