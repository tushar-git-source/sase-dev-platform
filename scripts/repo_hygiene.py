import os
import sys

print("\n🔎 Checking outdated dependencies...\n")
os.system("pip list --outdated")

print("\n🛡 Running vulnerability scan...\n")
exit_code = os.system("pip-audit -r requirements.txt")

if exit_code != 0:
    print("\n❌ Vulnerabilities detected. Failing.")
    sys.exit(1)

print("\n✅ Repository hygiene check passed.\n")
