str = """
QUEUE_NAME      PRIO STATUS          MAX JL/U JL/P JL/H NJOBS  PEND   RUN  SUSP
staf             70  Open:Active     500    -    -    -     0     0     0     0
dev              60  Open:Active     500    -    -    -     0     0     0     0
pos              55  Open:Active      50    -    -    -     0     0     0     0
"""

str = str.split('\n')
str.pop(0)
str.pop()
name = input('Enter user name: ')
parameter = input('Enter the parameter to be checked: ')
k = str[0].split()
para_index = k.index(parameter)

for i in range(1,len(str)):
    j = str[i].split()
    for z in j:
        if z == name:
            print('\nUser Name: {} \n{}:{}'.format(name,parameter,j[para_index]))



































