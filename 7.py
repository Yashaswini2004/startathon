import re
def search_cantact(file_name):
  with open(file_name,'r') as file:
     text=file.read()
     phone_number=re.findall('\+\d{12}',text)
     email_address=re.findall('\s+@\s+',text)
     for number in phone_number:
        print(number)
     for email in email_address:
        print(email)
search_cantact('little.txt')

