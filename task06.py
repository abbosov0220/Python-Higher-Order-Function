emails = ["ali@gmail.com", "vali@yahoo.com", "sami@gmail.com", "bek@outlook.com"]
gmail_emails = list(filter(lambda x: x.endswith("@gmail.com"), emails))
print(gmail_emails)
