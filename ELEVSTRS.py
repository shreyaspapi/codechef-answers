user_test = int(input())

cases = []
time = []
answers = []
time = 0
for _ in range(user_test):
    user_string = input().split()
    cases.append(user_string)

for case_ in cases:
    for j in range(len(case_)):
        case_[j] = int(case_[j])

for case in cases:
    if case[0] * 2 ** 0.5 / case[1] < case[0] / case[2] * 2:
        answers.append("Stairs")
    else:
        answers.append("Elevator")

for i in answers:
    print(i)
