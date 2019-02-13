# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
phone_book = dict()

for _ in range(num):
    name, number = input().split()
    phone_book[name] = number

for _ in range(num):
    name = input()
    print(f'{name}={phone_book[name]}') if name in phone_book else print('Not found')
