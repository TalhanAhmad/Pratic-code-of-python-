import json
import random
import string
import base64
import os

FILE_NAME = "passwords.json"

# ------------------ Encryption ------------------ #
def encrypt(text):
    encoded = base64.b64encode(text.encode()).decode()
    return encoded

def decrypt(text):
    decoded = base64.b64decode(text.encode()).decode()
    return decoded

# ------------------ File Handling ------------------ #
def load_data():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# ------------------ Password Generator ------------------ #
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

# ------------------ Core Features ------------------ #
def add_password():
    site = input("Enter website/app name: ")
    username = input("Enter username/email: ")
    password = input("Enter password (leave blank to auto-generate): ")

    if not password:
        password = generate_password()
        print(f"Generated Password: {password}")

    data = load_data()
    data[site] = {
        "username": username,
        "password": encrypt(password)
    }

    save_data(data)
    print("✅ Password saved successfully!")

def view_password():
    site = input("Enter website/app name to retrieve: ")
    data = load_data()

    if site in data:
        decrypted_pass = decrypt(data[site]["password"])
        print("\n🔐 Details:")
        print(f"Username: {data[site]['username']}")
        print(f"Password: {decrypted_pass}")
    else:
        print("❌ No data found for this site.")

def list_all():
    data = load_data()
    if not data:
        print("No saved passwords.")
        return
    
    print("\n📂 Saved Accounts:")
    for site in data:
        print(f"- {site}")

# ------------------ Main Menu ------------------ #
def main():
    while True:
        print("\n====== Password Manager ======")
        print("1. Add Password")
        print("2. View Password")
        print("3. List All Accounts")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_password()
        elif choice == "2":
            view_password()
        elif choice == "3":
            list_all()
        elif choice == "4":
            print("👋 Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()