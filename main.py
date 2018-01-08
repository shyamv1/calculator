from add import add


fun_dict = {
    '+': add
}

print('Hi I am a calculator')
choice = 'Hi'

while choice != 'q':
    print('Type + for addition')
    print('Type - for subtractioin')
    choice = input().strip()
    if choice in fun_dict:
        print(fun_dict[choice]())
