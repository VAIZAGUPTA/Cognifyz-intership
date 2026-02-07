def is_valid_email(email):
    if "@" not in email:
        return False

    parts = email.split("@")
    if len(parts) != 2:
        return False

    username, domain = parts

    if username == "" or domain == "":
        return False

    if "." not in domain:
        return False

    return True


email = input("Enter an email address: ")

if is_valid_email(email):
    print("Valid email address")
else:
    print("Invalid email address")
