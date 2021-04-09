from collections import defaultdict, deque


def solution(enter, leave):
    meet = defaultdict(list)
    enter = deque(enter)
    leave = deque(leave)
    length = len(enter)
    room = []

    flag = True
    while leave:
        if flag:
            exit_person = leave.popleft()
            flag = False
        # print(meet, enter, leave, room, exit_person)

        try:
            room.remove(exit_person)
            for person in room:
                meet[exit_person].append(person)
                meet[person].append(exit_person)
            flag = True
        except ValueError:
            if enter:
                room.append(enter.popleft())
            continue

    ans = [len(meet[i+1]) for i in range(length)]
    return ans


if __name__ == "__main__":
    enter = [[1, 3, 2], [1, 4, 2, 3], [3, 2, 1], [3, 2, 1], [1, 4, 2, 3]]
    leave = [[1, 2, 3], [2, 1, 3, 4], [2, 1, 3], [1, 3, 2], [2, 1, 4, 3]]
    for i in range(len(enter)):
        print(solution(enter[i], leave[i]))
