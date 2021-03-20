def solution(program, flag_rules, commands):
    answer = []

    # flag rule type, Alias 찾기쉽게 딕셔너리에 저장
    flag_type = dict()
    alias_dict = dict()
    for flag_rule in flag_rules:
        if "ALIAS" in flag_rule:
            alias_name, _, flag_name = flag_rule.split()
            alias_dict[alias_name] = flag_name

        else:
            flag_name, flag_argument_type = flag_rule.split()
            flag_type[flag_name] = flag_argument_type

    # 커맨드별 판별 루프
    for command in commands:
        command_list = command.split()

        # 조건1. program 으로 시작
        if not command_list[0] in program:
            answer.append(False)
            continue

        # 조건2,3,4. flag argument 일치 여부, flag 최대1번, flag_rules 만족
        index = 1
        flag_set = set()

        # 조건을 만족못하면 flag를 False로 처리하고 루프종료
        flag = True
        try:
            # Command_list 루프 시작
            while index < len(command_list) and flag:

                # flag 가 중복해서 나오는 경우(ALIAS포함)
                temp_length = len(flag_set)
                if command_list[index] in alias_dict.keys():
                    flag_set.add(alias_dict[command_list[index]])
                else:
                    flag_set.add(command_list[index])

                if temp_length == len(flag_set):
                    flag = False
                    continue

                # ALIAS 여부 확인
                if command_list[index] in alias_dict.keys():
                    flag_type_temp = flag_type[alias_dict[command_list[index]]]
                else:
                    flag_type_temp = flag_type[command_list[index]]

                # flag_type의 case를 구분하여 실행
                if flag_type_temp == "STRING":
                    if not command_list[index + 1].isalpha():
                        flag = False
                    index += 2
                elif flag_type_temp == "NUMBER":
                    if not command_list[index + 1].isdigit():
                        flag = False
                    index += 2
                elif flag_type_temp == "NULL":
                    if index + 1 < len(command_list):
                        if not (command_list[index + 1] in flag_type.keys()):
                            flag = False
                    index += 1

                elif flag_type_temp == "NUMBERS":
                    # flag argument 가 1개이상 오지 않는경우
                    if not command_list[index + 1].isdigit():
                        flag = False
                        continue

                    while index + 1 < len(command_list):
                        index += 1
                        if command_list[index].isdigit():
                            continue
                        else:
                            # 다음에 오는 flag가 flag_dict에 있는지 확인
                            if not (command_list[index] in flag_type.keys()):
                                flag = False
                            break

                elif flag_type_temp == "STRINGS":
                    # flag argument 가 1개이상 오지 않는경우
                    if not command_list[index + 1].isalpha():
                        flag = False
                        continue

                    while index + 1 < len(command_list):
                        index += 1
                        if command_list[index].isalpha():
                            continue
                        else:
                            # 다음에 오는 flag가 flag_dict에 있는지 확인
                            if not (command_list[index] in flag_type.keys()):
                                flag = False
                            break

            # 조건을 만족못해 중간에 멈춘경우
            if not flag:
                answer.append(False)
                continue

        # flag_name 이 flag_type 안에 없는경우
        except KeyError:
            answer.append(False)
            continue

        # flag 후에 flag_argument 가 오지 않는경우
        except IndexError:
            answer.append(False)
            continue

        # 모든 조건 만족
        answer.append(True)

    return answer

if __name__ == "__main__":
    program = ["line", "bank"]
    flag_rules = [["-s STRING", "-num NUMBER", "-e NULL", "-n ALIAS -num"],
                  ["-send STRING", "-a ALIAS -amount", "-amount NUMBERS"]]
    commands = [["line -n 100 -s hi -e", "line -n 100 -e -num 150"],
                ["bank -send abc -amount 500 200 -a 400", "bank -send abc -a hey"]]
    for i in range(len(program)):
        print(solution(program[i], flag_rules[i], commands[i]))
