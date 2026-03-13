import re
with open("input.txt", "r") as file:
    text = file.read()
email_pattern = r"[a-zA-Z0-9._]+@[a-zA-Z]+\.[a-zA-Z]+"
phone_pattern = r"\b[6-9]\d{9}\b"
date_pattern = r"\b\d{2}-\d{2}-\d{4}\b"
number_pattern = r"\b\d+\b"
repeat_pattern = r"\b(\w+)\s+\1\b"
url_pattern = r"https?://[^\s]+"
ip_pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
password_pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$"
emails = re.findall(email_pattern, text)
phones = re.findall(phone_pattern, text)
dates = re.findall(date_pattern, text)
numbers = re.findall(number_pattern, text)
repeated_words = list(set(re.findall(repeat_pattern, text)))
urls = re.findall(url_pattern, text)
ips = re.findall(ip_pattern, text)
passwords = re.findall(r"Password\d+:\s*(\S+)", text)

valid_passwords = []
invalid_passwords = []

for pwd in passwords:
    if re.match(password_pattern, pwd):
        valid_passwords.append(pwd)
    else:
        invalid_passwords.append(pwd)
print("Emails:", emails)
print("Phone Numbers:", phones)
print("Dates:", dates)
print("Numbers:", numbers)
print("Repeated Words:", repeated_words)
print("URLs:", urls)
print("IP Addresses:", ips)
print()
print("Valid Passwords:", valid_passwords)
print("Invalid Passwords:", invalid_passwords)