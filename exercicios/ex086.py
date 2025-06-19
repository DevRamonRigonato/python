n = []
even = []
odd = []
while True:
    n.append(int(input('Enter a value: ')))
    resp = ' '
    while resp not in 'YN':
        resp = str(input('Do you want to continue? [Y/N] ')).strip().upper()[0]
    if resp == 'N':
        break
for i, v in enumerate(n):
    print(f'Index {i}: {v}')
    if v % 2 == 0:
        even.append(v)
    elif v % 2 == 1:
        odd.append(v)
for i, v in enumerate(n):
    print(f'Index {i}: {v}')
print(f'The full list is {n}')
print(f'The list of even numbers is {even}')
print(f'The list of odd numbers is {odd}')
