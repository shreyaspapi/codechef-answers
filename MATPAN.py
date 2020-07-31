import string

t = int(input())

answers = []

while t:

    letter_value = list(map(int, input().split()))
    letter_pangram = list(map(str, input().split()))
    all_string = []
    full_price = 0
    not_string = []

    for i in string.ascii_lowercase[:26]:
        all_string.append(i)
        not_string.append(i)

    for i in letter_pangram[0]:
        if i in not_string:
            not_string.remove(i)

    if not not_string:
        full_price = 0
    else:
        for i in not_string:
            a = all_string.index(i)
            full_price += letter_value[a]

    answers.append(full_price)

    t -= 1

for i in answers:
    print(i)
