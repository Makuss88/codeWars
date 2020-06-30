import random

# TODO rozwiazanie moje, działa, ale wolniej :P
personsList = ['1', '2', '3', '4']
if len(personsList) != len(set(personsList)):
    print("dupa zbita")

if len(personsList) < 2:
    print('za mało ludzików...')

result = {}
duplicate = personsList.copy()

count = 0
while count <= len(duplicate) - 1:
    k = duplicate[count]  # key
    v = str(random.choice(personsList))  # value
    if k == v:
        count = 0
        result = {}
        personsList = duplicate.copy()
    else:
        count += 1
        result[k] = v
        personsList.remove(v)

print(result)

# TODO rozwiazanie numer 2, szybsze zdecydowanie :)
personList = ['a', 'b', 'c', 'd']
random.shuffle(personList)
result = [personList[0] + ' ma ' + personList[-1]]
for i in range(len(personList)):
    if i == 0:
        continue
    result.append(personList[i] + ' ma ' + personList[i - 1])

print(result)
