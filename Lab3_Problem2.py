names = ['name 2', 'other name', 'name1']

for i in range(len(names)):
    shortest = i

    for j in range(i + 1, len(names)):
        if len(names[j]) < len(names[shortest]):
            shortest = j

    names[i], names[shortest] = names[shortest], names[i]

print("Sorted List:")
print(names)


