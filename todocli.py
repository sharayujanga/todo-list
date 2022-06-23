

from re import A


print ("\n MY TODO LIST")

instructions = "\n 'A' to add \n 'D' to delete \n 'V' to view list"
print(instructions)

list = []

x = 1
while(x == 1):
    ans = input("enter letter: ")

    if (ans == 'A'):
        task = input("enter task: ")
        list.append(task)

    if (ans == 'D'):
        print("which task enter the number: ")
        task = int(input())
        list.remove(list[task - 1])

    if (ans == 'V'):
        print(list)

    if (ans == 'Q'):
        x = 0
print(list)