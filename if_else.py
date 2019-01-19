#!/bin/python3

N = int(input())


def if_else(number):
    if number % 2 is not 0 or 6 <= number <= 20:
        print('Weird')
    else:
        print('Not Weird')


def one_liner(number):
    print('Weird') if number % 2 is not 0 or 6 <= number <= 20 else print('Not Weird')


one_liner(N)
