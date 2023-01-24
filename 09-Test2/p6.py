import json
def f(age,course,average):
    f = open("data.json", 'r')
    x = f.read()
    number_of_students = 0
    content = json.loads(x)
    for person in content:
        if person["age"] >= age:
            for c in person["studies"]["courses"]:
                if c['name'] != course: 
                    continue
                elif sum(c['grades'])/len(c['grades']) >= average:
                    number_of_students += 1        
    return number_of_students
    f.close()

f(25, "programming", 3)