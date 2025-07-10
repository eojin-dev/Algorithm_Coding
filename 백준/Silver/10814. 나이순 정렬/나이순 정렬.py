n = int(input())
people = []

for _ in range(n):
    age_str, name = input().split()
    age = int(age_str)
    people.append((age, name))

people.sort(key=lambda x: x[0])

for age, name in people:
    print(age, name)