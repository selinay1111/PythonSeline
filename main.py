# This is a sample Python script.
from Stack import Stack1


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_stack = Stack1()
    my_stack2 = Stack1()
    my_stack3 = Stack1()
    print(my_stack.is_empty())
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    print(my_stack)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
