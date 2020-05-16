import random

upper_char=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','X','Y','Z']
lower_char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','x','y','z']
num=['1','2','3','4','5','6','7','8','9','0']
special_char =['~','!','#','$','%','^','&','*','_','-']
password= random.choice(upper_char)+random.choice(lower_char)+random.choice(special_char)+random.choice(num)+random.choice(upper_char)+random.choice(lower_char)+random.choice(special_char)+random.choice(num)
print(password)
