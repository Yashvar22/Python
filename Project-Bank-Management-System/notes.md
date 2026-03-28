
Account number flow:-
alpha = ['A', 'b', 'Z'] (3 letters)

num = ['1', '5', '9'] (3 digits)

spchar = ['@'] (1 special char)

id = alpha + num + spchar = ['A', 'b', 'Z', '1', '5', '9', '@']

random.shuffle(id) → Shuffle होकर: ['Z', '1', '@', 'b', '5', 'A', '9']

return "".join(id) → "Z1@b5A9"

userdata=[i for i in Bank.data if i['accountNo']==accno and i['pin']==pin]
same as->
userdata = []
for i in Bank.data:
   if i['accountNo'] == accno and i['pin'] == pin:
      userdata.append(i)