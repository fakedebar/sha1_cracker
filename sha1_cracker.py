import hashlib

def convert_text_to_sha1(text):
    digest = hashlib.sha1(
        text.encode()
    ).hexdigest()
    return digest

def main():
    user_sha1 = input("Enter the SHA1 to Crack: ")
    cleaned_user_sha1 = user_sha1.strip().lower()

    try:
        # Open the file with the utf-8 encoding
        with open('./password.txt', encoding='utf-8') as f:
            for line in f:
                password = line.strip()
                converted_sha1 = convert_text_to_sha1(password)

                if cleaned_user_sha1 == converted_sha1:
                    print(f"Password Found: {password}")
                    return

    except UnicodeDecodeError as e:
        print(f"Error decoding the file: {e}")

    print("Password not found.")

if __name__ == '__main__':
    main()
