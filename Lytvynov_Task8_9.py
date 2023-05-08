import random
def greeting(array_users):
    if len(array_users)==0: print('We need to find some users!')
    else:
       for i in array_users:
           if i in ['admin','Admin']:
               print(str('Hello Admin,I hope you\'re well..'))
           else:print(i+', thank you for ligging in again..')
    
def number_of_sides(count):
    if count>6 or count<3: print('Error... Number of sides must be from 3 to 6')
    else:
       lst={'3':'Triangle',
            '4':'Quadrilateral',
            '5':'Pentagon',
            '6':'Hexagon'}
       print(lst[str(count)])

def func_for_1(array_for3):
    for i in array_for3:
       if i==1:print(str(i)+'st')
       elif i==2:print(str(i)+'nd')
       elif i==3:print(str(i)+'rd')
       else:print(str(i)+'th')

def days_in_month(month):
    tpl={'January':31,'Februar':'28/29','March':31,'April':30,'May':31,'June':30,'July':31,'August':31,'September':30,'October':31,'November':30,'December':31}
    print(tpl[month.title()])

def leap_ordinary(year):
    print(year%4, year%100)
    if year%4==0 and year%100!=0:
        print('Leap year')
    else:print('Ordinary year')

def calculate(lst3):
    x=float(lst3[0])
    y=float(lst3[1])
    act=lst3[2]
    if act=='+':
        print(f'{x}+{y}={x+y}')
    elif act=='-':
        print(f'{x}-{y}={x-y}')
    elif act=='/':
        try:
            print(f'{x}/{y}={x/y}')
        except ZeroDivisionError:
            print('Error: Division by zero!')
    elif act=='mod':
        print(f'{x}%{y}={x%y}')
    elif act=='pow':
        print(f'{x}^{y}={pow(x,y)}')
    elif act=='div':
        print(f'{x}//{y}={x//y}')
def money_function(number):
    lst={20:'Двадцять гривень/Іван Франко',
         50:'П\'ятдесять гривень/Михайло Грушевський',
         100:'Сто гривень/Тарас Шевченко',
         200:'Двісті гривень/Леся Українка',
         500:'П\'ятсот гривень/Григорій Сковорода',
         1000:'Тисяча Гривень/Владимир Вернадський'}
    if number in lst:
        print('Номінал:',lst[number][:(lst[number].find('/'))],'   Зображен:',lst[number][(lst[number].find('/'))+1:])        
    else:
        print('Uncorrect value!')
def chess(pos1,pos2):
    lst={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7}
    x=str()
    for i in reversed(range(8)):
        print('')
        for j in reversed(range(8)):
            if i+j==0 or (i+j)%2==0:
                if pos1==i+1 and lst[pos2]==j-1:
                    print('□',end=' ')
                    x='w'
                else:
                    print('w',end=' ')    
            else:
                if pos1==i and lst[pos2]==j:
                    print('■',end=' ')
                    x='b'
                else:
                    print('b',end=' ')
    print('\nYour postition is :','White' if x=='w' else 'Black')

def from_ten_to_two(value):
    result=''
    while value!=0:
        if value%2==0:
            result+='0'
            value=value/2
        else:
            result+='1'
            value=(value-(value%2))/2
    print(result[::-1])

def from_two_to_ten(value):
    x=len(value)
    y=1
    result=0
    for i in value:
        result+=int(i)*pow(2,x-y)
        y+=1
    print(result)

def  rock_paper_scissors(value):
    lst=['rock','paper','scissors']
    if value not in lst:
        print('Ошибка. Ваш ход не соответствует не одному из : rock,paper,scissors')
        return()
    x=value
    y=random.choice(lst)
    print(f'Ваш ход: {value}')
    print(f'Ход компьютера: {y}')
    if x=='rock' and y=='scissors':
        print('Вы победили!')
    elif x=='scissors' and y=='paper':
        print('Вы победили!')
    elif x=='paper' and y=='rock':
        print('Вы победили!')
    elif x==y:
        print('Ничья,попробуй еще!')
    else:
        print('К сожалению,Вы проиграли.')
if __name__=='__main__':
    '''#1
    greeting(['Admin','Stas','Jan','Nikita'])
    
	#2
    number_of_sides(7)
    
    #3
    func_for_1([1,2,3,4,5,6,7,8,9])

    #4
    print('Парне' if int(input())%2==0 else 'Непарне')

    #5
    days_in_month(str(input('Month: ')))

    #6
    leap_ordinary(int(input('Year must be between 1900 to 3000')))
    
    #7
    summ=0
    value=10
    while value!=0:
        value=int(input())
        summ+=value
    print(summ)
    
    #8
    lst3=[]
    for i in range(3):
        lst3.append(str(input()))  
    calculate(lst3)

    #9
    money_function(20)

    #10
    chess(5,'d')

    #11
    from_ten_to_two(375)
    from_two_to_ten('101110111')

    #12
    rock_paper_scissors(random.choice(['rock','paper','scissors']))
    '''