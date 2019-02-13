if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total = 0
    if query_name in student_marks:
        marks = student_marks[query_name]
        num_of_marks = len(marks)
        for num in marks:
            total += num
    avg = total / num_of_marks
    print(format(avg, '.2f'))


