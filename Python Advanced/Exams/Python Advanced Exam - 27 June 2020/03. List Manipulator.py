def list_manipulator(my_list, *args):

    if args[0] == "add":
        if args[1] =="end":
            my_list += list(args[2: ])
        elif args[1] =="beginning":
            my_list = list(args[2: ]) + my_list
        
    elif args[0] =="remove":
        if len(args) == 2:
            if args[1] =="end":
                my_list.pop()
            elif args[1] =="beginning":
                del my_list[0]
        else:
            if args[1] =="end":
                if len(my_list) > args[2]:
                    my_list = my_list[:len(my_list) - args[2]]
                else:
                    my_list = []
            elif args[1] =="beginning":
                if len(my_list) > args[2]:
                    my_list = my_list[args[2]: ]
                else:
                    my_list = []            
    
    return my_list
