

with open('stuinfo.txt', 'r') as inFile, open ('report.txt', 'w') as outFile:

    print(f'{"Last":<15}{"First":<15}{"StuID":<15}{"Email"}'+'\n',file = outFile)

    for line in inFile:
        line_list = line.split()
        email = line_list[0]+'@gmail.com'
        print(f'{line_list[0]:<15}{line_list[1]:<15}{line_list[2]:<15}{email}'+'\n',file = outFile)
