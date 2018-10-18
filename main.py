###https://github.com/denyszamiatin/task_manager/blob/master/main.py

import collections

tasks = collections.defaultdict(list)


#########  1
def date_input():
    date = input("Date?")
    task = input("Task?")
    if date not in tasks:
        tasks[date] = [task]
    else:
        tasks[date].append(task)

######### 2

def validate_date_exist(tasks):
    date = input("Task exist on the date?")
    if date in tasks:
        for index, task in enumerate(tasks[date], 0):
            print(index, tasks)
        else:
            tasks[date].append(task)
    print("No tasks on this date")


#############  3

def pop_date_record(date, index):
    try:
        tasks[date].pop(index)
    except (KeyError, IndexError):
        print("incorrect input")

        ###########  4
def show_actions():
    return input("""input: 
                        a - add atask
                        v- validate date exist
                        l -List of tasks
                        d - delete task
                        q - quit
                        """).lower()

###############
#
# def composition(f, g):
#     return lambda x: f(g(x))

def check_function(action):
    if action == 'q':
        exit()
    elif action == 'a':
        date_input()
    elif action == 'v':
        validate_date_exist(tasks)

    elif action == 'd':
        date = input("Date")
        index = input("Number&")
        pop_date_record(date, index)

    else:
        print("Incorrect action")

####################  main

while True:
    action = show_actions()
    check_function(action)
print(tasks)