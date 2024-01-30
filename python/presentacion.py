#!/usr/bin/python3

import subprocess

def execute_playbook(playbook_name):
    command = ["ansible-playbook", playbook_name]
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    print(f"=== Playbook Output ===\n{output.decode()}")

    if process.returncode == 0:
        print(f"Playbook {playbook_name} executed successfully.")
    else:
        print(f"Error executing playbook {playbook_name}.\nError message: {error.decode()}")

if __name__ == "__main__":
    while True:
        print("\nSelect a playbook to execute:")
        print("1. playbook_connectivity.yml")
        print("2. playbook_domain.yml")
        print("3. playbook_mysql.yml")
        print("4. playbook_web.yml")
        print("0. Exit")

        choice = input("Enter your choice (0-4): ")

        if choice == "0":
            print("Exiting the script.")
            break
        elif choice == "1":
            execute_playbook("../playbook_connectivity.yml")
        elif choice == "2":
            execute_playbook("../playbook_domain.yml")
        elif choice == "3":
            execute_playbook("../playbook_mysql.yml")
        elif choice == "4":
            execute_playbook("../playbook_web.yml")
        else:
            print("Invalid choice. Please enter a number between 0 and 4.")
