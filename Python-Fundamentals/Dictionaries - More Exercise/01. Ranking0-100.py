passwords = {}
contest_data = {}

command = input()
while command != "end of contests":
    command = command.split(":")
    contest = command[0]
    password = command[1]
    if contest not in passwords:
        passwords[contest] = password
    command = input()
    

contest_input = input()
while contest_input != "end of submissions":
    contest_input = contest_input.split("=>")
    if len(contest_input) == 4:
        contest = contest_input[0]
        password = contest_input[1]
        username = contest_input[2]
        points = int(contest_input[3])
        if contest in passwords:
            if password == passwords[contest]:
                

        
        contest_input = input()
    else:
        contest_input = input()
