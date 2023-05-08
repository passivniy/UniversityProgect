# IKM-221D Task_6 Lytvynov Danyil
print('IKM-221D Task_6')
print('Lytvynov Danyil')

'''#6.1	
inp=open("input/numbers.txt",'r')
summ=int()
for line in inp:
   summ+=int(line)
out=open('output/sum_numbers.txt','w')
out.write(str(summ))   
print('#6.1: ',summ)



#6.2
print("----6.2----")
x=int(input())
print("----end----")
with open('output/typeOfNumber.txt','w') as fileForNumber:
   fileForNumber.write('Even' if x%2==0 else 'Odd')


#6.3
sentenceList=[]
print("----6.3----")
with open('input/learning_python.txt','r') as inpSentence:
      sentenceList=inpSentence.read()
print(sentenceList)
print('----end----')


#6.4
print('----6.4----')
print(sentenceList.replace('Python','C'))
print('----end----')


#6.5
print('----6.5----')
name='Name'
while name!='':
    name=str(input())
    if name=='':break
    with open('output/guest_book.txt','a') as hello:
        hello.write('Hi,'+name+'\n')
    print('Hi,',name)
print('----end----')


#6.6
print('----6.6----')
lst=['The','the']
with open('input/book.txt','r') as book:
    string_book=book.read()
count=0
for i in lst:
    count+=string_book.count(i)
print(count)
print('----end----')
'''
list=''
#6.7
with open('input/book_for_6_7.txt','r',encoding='utf8') as book:
    for text in book:
        list+=text

print(list)
#while "  " in list_task_7:
#    list_task_7= list_task_7.replace("  "," ")