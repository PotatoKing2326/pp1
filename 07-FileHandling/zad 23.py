import re

message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "
temperatures = re.findall("\d{2}",message)
days = 0
avarage_temp = 0
for x in temperatures:
    days += 1
    avarage_temp += int(x)
avarage_temp = avarage_temp / days
print(f"Average temperature: {avarage_temp}")