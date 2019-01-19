def print_num_loop(number):
    if 1 <= number <= 20:
        for i in range(number):
            print(i * i)


if __name__ == '__main__':
    n = int(input())
    print_num_loop(n)
