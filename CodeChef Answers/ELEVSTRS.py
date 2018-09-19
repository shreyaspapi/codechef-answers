user_test = int(input())

cases = []
time = []
answers = []
time = 0
for i in range(user_test):
    user_string = input().split()
    cases.append(user_string)

for i in range(len(cases)):
    for j in range(len(cases[i])):
        cases[i][j] = int(cases[i][j])

for i in range(len(cases)):
    if (cases[i][0] * (2 ** 0.5) / cases[i][1]) < (cases[i][0] / cases[i][2] * 2):
        answers.append("Stairs")
    else:
        answers.append("Elevator")

for i in answers:
    print(i)
