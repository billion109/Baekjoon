import re
from collections import defaultdict


def solution(inp_str):
    answer = []
    # 1번조건
    if len(inp_str) < 8 or len(inp_str) > 15:
        answer.append(1)

    # 2번조건
    new = re.sub(r"[a-zA-Z0-9~!@#$%^&*]", "", inp_str)
    if new:
        answer.append(2)

    # 3번조건
    cnt = 0
    lower = re.sub(r"[^a-z]", "", inp_str)
    upper = re.sub(r"[^A-Z]", "", inp_str)
    number = re.sub(r"[^0-9]", "", inp_str)
    char = re.sub(r"[^~!@#$%^&*]", "", inp_str)
    for is_include in [lower, upper, number, char]:
        if is_include:
            cnt += 1
    if cnt < 3:
        answer.append(3)

    # 4번조건
    cnt = 1
    temp = [inp_str[0]]
    for i in inp_str[1:]:
        if temp.pop() == i:
            cnt += 1
        else:
            cnt = 1
        temp.append(i)
        if cnt >= 4:
            answer.append(4)
            break

    # 5번조건
    dic = defaultdict(int)
    for i in inp_str:
        dic[i] += 1
    if max(dic.values()) >= 5:
        answer.append(5)

    if answer:
        return answer
    else:
        return [0]



if __name__ == "__main__":
    inp_str = ["AaTa+!12-3", "aaaaZZZZ)", "CaCbCgCdC888834A", "UUUUU", "ZzZz9Z824"]
    for i in inp_str:
        print(solution(i))
