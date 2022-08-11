# Num = [] # 1, 10,
# Range = int(input('Enter the range'))
#
# for j in range(Range):
#     z = 0
#     z = int(input("enter your values"))
#     Num.append(z) # 1, 10, 56, 78….
#
# sum = 0
# for i in Num:
#     sum = sum+i
# print(sum)

Str = """
QUEUE_NAME      PRIO STATUS          MAX JL/U JL/P JL/H NJOBS  PEND   RUN  SUSP
staf             70  Open:Active     500    -    -    -     0     0     0     0
dev              60  Open:Active     500    -    -    -     0     0     0     0
pos              55  Open:Active      50    -    -    -     0     0     0     0
"""

str = str.split('\n') # List with each line
name = input("enter the name") # staf , dev , pos
Value__ = input("enter the value") # prio , Status , MAX , JL ,........

dic = {}
for ln in str:
    sp_l = ln.split() # List and split each line [QUEUE_NAME,PRIO,STATUS,MAX,JL/U,JL/P,JL/H,NJOBS,PEND,RUN,SUSP]
    ind_val = sp_l.index(Value__) # 3
    for ln__ in sp_l:  # ln__ = [QUEUE_NAME,PRIO,STATUS,MAX,JL/U,JL/P,JL/H,NJOBS,PEND,RUN,SUSP]
        # dic[sp_l[0]] = sp_l[3]  # dic = {QUEUE_NAME:MAX}
        if ln__ == name:
            ind_name = sp_l.index(name) # 0
            print("Name: {}  Value: {} ".format(sp_l[ind_name],sp_l[ind_val]))  # {Name: QUEUE_NAME  Value: 500}
        else:
            continue


jugs = 3 and 5
bucket =  water
need 4 liter

5 liter - 3 liter = 2 liter

3 liter = pour 2 liter
fill 5 liter = pour i lter 3

5 liter jug 4 litrer



3 bulbs in black room

switches outside room

look only once in a room

which swich for which bulb

a=on b= c=






























