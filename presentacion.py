#!/usr/bin/python3

import subprocess
import json

# Run Ansible playbook and capture output
ansible_command = ["ansible-playbook", "-i", "hosts,", "playbook_web.yml"]
ansible_process = subprocess.Popen(ansible_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
ansible_process.wait()

# Read the JSON output from the temporary file
try:
    with open("/tmp/ansible_output.json", "r") as file:
        ansible_output_json = json.load(file)

    # Do further processing or formatting with the JSON output
    formatted_output = f"Formatted output: {json.dumps(ansible_output_json, indent=2)}"
    print(formatted_output)
except json.JSONDecodeError as e:
    print(f"Error decoding Ansible output as JSON: {e}")
