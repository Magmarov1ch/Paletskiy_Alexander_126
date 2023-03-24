from random import randint

numbers1 = [randint(0,9999) for i in range(randint(50, 101))]
numbers2 = [randint(0,9999) for i in range(randint(50, 101))]
final = []
for i in numbers2:
    if numbers1 not in numbers2:
        final.append(i)

print(final)