#For finding Factorial.

#1. for multiplication
num=int(input('enter the number'))
fact=1
for i in range(num,0,-1):
    fact=fact*i
print('factorial:-',fact)  

#2. for addition
num=int(input('enter the number'))
fact=0
for i in range(num,0,-1):
    fact=fact+i
print('factorial:-',fact)  


# Finding Reverse of any number
num=int(input('enter the number'))
rev_num=0

while(num>0):
    rem=num%10
    rev_num=rev_num*10+rem
    num=num//10

print('reverse number:-',rev_num)


#Finding pallindrome  
num=int(input('enter the number'))
rev_num=0
ac_num=num

while(num>0):
    rem=num%10
    rev_num=rev_num*10+rem
    num=num//10
print('reverse number',rev_num)
if ac_num==rev_num:
    print(ac_num,'is pallindrome')
else:
    print(ac_num,'is not an pallindrome')


#Finding Armstrong number
num=int(input('enter a number'))
ac_num=num
p=len(str(num))
am_no=0

while(num>0):
    digit=num%10
    am_no=am_no+digit**p
    num=num//10

if(ac_num==am_no):
    print(ac_num,'is a armstrong number')
else:
    print(ac_num,'is not a armstrong number')


#Finding Febonacci number
t=int(input('enter a number'))
a,b=0,1
for i in range(t):
    print(a,end=' ')
    a,b=b,a+b


#Prime number program
number = int(input("Enter a number: "))

if number > 1:

    for i in range(2, number):
        if number % i == 0:
            print(number, "is Not a Prime Number.")
            break
    else:
        print(number, "is a Prime Number.")

else:
    print(number, "is Not a Prime Number.")



# End of Program



