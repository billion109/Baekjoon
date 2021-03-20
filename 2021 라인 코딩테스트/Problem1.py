def solution(table, languages, preference):
    arr = []
    for i in table:
        arr.append(i.split()[1:])

    ans = [[0, "SI"], [0, "CONTENTS"], [0, "HARDWARE"], [0, "PORTAL"], [0, "GAME"]]
    for i in range(len(languages)):
        for j in range(5):
            if languages[i] in arr[j]:
                temp = 5 - arr[j].index(languages[i])
            else:
                temp = 0
            ans[j][0] += temp * preference[i]

    ans = sorted(ans, key=lambda x: (-x[0], x[1]))
    print(ans[0][1])
    return ans


if __name__ == "__main__":
    table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
             "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
             "GAME C++ C# JAVASCRIPT C JAVA"]
    languages = ["PYTHON", "C++", "SQL"]
    preference = [7, 5, 5]

    table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++",
             "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP",
             "GAME C++ C# JAVASCRIPT C JAVA"]
    languages = ["JAVA", "JAVASCRIPT"]
    preference = [7, 5]
    solution(table, languages, preference)
