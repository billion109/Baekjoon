import sys
from collections import deque

input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().split())
    belt = deque(list(map(int, input().split())))
    robot = deque([False] * 2 * N)
    robot_q = deque()
    cnt = 0
    broken_num = 0

    while broken_num < K:
        cnt += 1
        belt.rotate(1)
        robot.rotate(1)
        for i in range(len(robot_q)):
            robot_q[i] = (robot_q[i] + 1) % N

        new_robot_q = deque()
        while robot_q:
            index = robot_q.popleft()
            if index == N - 1:
                robot[index] = False
                continue



            next_index = (index + 1) % (2 * N)
            if (not robot[next_index]) and belt[next_index] > 0:
                robot[index] = False
                belt[next_index] -= 1
                if belt[next_index] == 0:
                    broken_num += 1

                if next_index != N - 1:
                    robot[next_index] = True
                    new_robot_q.append(next_index)
                else:
                    robot[next_index] = False
            else:
                new_robot_q.append(index)

        robot_q = new_robot_q
        if not robot[0] and belt[0]>0:
            robot[0] = True
            robot_q.append(0)
            belt[0] -= 1
            if belt[0] == 0:
                broken_num += 1


    print(cnt)
