from features import Cmd


while True:
    cmd = Cmd()
    scan = input(f"{cmd.base}~$ ")
    commands = scan.split()

    x = commands[0]
    match x:
        case "cd":
            if len(commands) == 1:
                pass
            elif commands[1] == '..':
                cmd.cd_go_back()
            else:
                try:
                    cmd.cd(commands[1])
                except FileNotFoundError as exception:
                    print(exception)
        case "ls":
            cmd.ls()

        case "mkdir":
            if len(commands) ==1:
                print("mkdir: missing operand")
            else:
                cmd.mkdir(commands[1])

        case "rmdir":
            if len(commands) == 1:
                print("mkdir: missing operand")
            else:
                cmd.rmdir(commands[1])
        case "touch":
            if len(commands) == 1:
                print("touch: missing operand")
            else:
                cmd.create_file(commands[1])

        case "less":
            if len(commands) == 1:
                print("less: missing operand")
            else:

                cmd.open_file(commands[1])
        case "help":
            cmd.help_of()
            print()
        case  _:
            print(f"command not found")

