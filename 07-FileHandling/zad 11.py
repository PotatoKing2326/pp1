film_titles = ["The Lord of the Rings: The Fellowship od Ring", "Star Wars ep. IV: The New Hope", "The Green Mile", "Elvis", "The Batman"]
file = open('films.txt', 'w')
for x in film_titles:
    file.write(f"{x}\n")
file.close()

file = open('films.txt','r')
content = file.read()
print(content)
file.close()