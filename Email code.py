import re

chaine = "exampleeemail@gmail.com"
check = re.search(r'[\w.]+\@[\w.]+\@[\w.]+\.', chaine)
if(check):
  print("Valid Email")
else:
    print("Invalid Email")
