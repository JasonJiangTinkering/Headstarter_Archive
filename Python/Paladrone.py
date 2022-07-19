def solution(s):
    s =s.lower()
    string = ""
    for i in s:
        if 61 <= ord(i) <=122:
            string += i

    if (len(string) <= 1):
        return True
    lower = 0
    higher = len(string) - 1 

    while lower < higher:
        lower_value = string[lower]
        higher_value = string[higher]
        if (higher_value != lower_value):
            return False
        lower += 1
        higher -= 1

    return True
print(solution(s = 'race a car'))
print(solution(s = 'A man, a plan, a canal: Panama'))
print(solution(s = ' '))
