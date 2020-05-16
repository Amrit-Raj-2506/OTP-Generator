import random

wordlist=[]
special_char =['~','!','#','$','%','^','&','*','_','-']
number=['1','2','3','4','5','6','7','8','9','0']

with open("readable.txt",'r',encoding="utf-8")as file:
    data= file.readlines()
    for line in data:
        words=line.split()
        for item in words:
            if len (item)>4:
                wordlist.append(item.capitalize())
word=random.choice(wordlist)
spec=random.choice(special_char)
num=random.choice(number)

password=word+spec+num
print(password)
