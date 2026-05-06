"""
Secure Fargate App - Pluralsight Lab.

A lightweight application that reads the DB_PASSWORD environment variable
(injected from AWS Secrets Manager) and prints it to stdout so the learner
can verify secrets injection via CloudWatch Logs.
"""

import os
import time
import json

def main():
    print("=" * 60)
    print("  Secure Fargate App - Starting Up")
    print("=" * 60)

    # Read the secret injected by ECS from Secrets Manager
    db_credentials = os.environ.get("DB_CREDENTIALS")

    if db_credentials:
        print("[OK] DB_CREDENTIALS environment variable is set.")
        try:
            creds = json.loads(db_credentials)
            print(f"[OK] Database host: {creds.get('host', 'N/A')}")
            print(f"[OK] Database name: {creds.get('dbname', 'N/A')}")
            print(f"[OK] Database user: {creds.get('username', 'N/A')}")
            print(f"[OK] Database port: {creds.get('port', 'N/A')}")
            print("[OK] Secret successfully injected via Secrets Manager!")
        except json.JSONDecodeError:
            print(f"[OK] Raw secret value received: {db_credentials[:20]}...")
            print("[OK] Secret successfully injected via Secrets Manager!")
    else:
        print("[WARNING] DB_CREDENTIALS environment variable is NOT set.")
        print("[WARNING] Secrets injection may not be configured correctly.")

    print("=" * 60)
    print("  Application is running. Logging heartbeat every 30s...")
    print("=" * 60)

    # Keep the container running with periodic heartbeat logs
    counter = 0
    while True:
        counter += 1
        print(f"[HEARTBEAT] App is healthy - tick #{counter}")
        time.sleep(30)

if __name__ == "__main__":
    main()
