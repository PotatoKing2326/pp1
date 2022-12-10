file = open('shopping.txt','a')
x = input("Add product")
file.write(x)
file.close()

file = open('shopping.txt','r')
content = file.read()
print(content)
file.close()