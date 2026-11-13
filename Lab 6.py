#1
a=['яблоко','груша','банан']
b=['груша','апельсин']
a_set=set(a)
b_set=set(b)
print(a_set-b_set)

#2
numbers=input("Введите числа через пробел: ").split()
seen=set()
for number in numbers:
    if number in seen:
        print("YES")
    else:
        print("NO")
        seen.add(number)
        
#3       
text='мама папа мама брат'
words=set(text.split())
print(len(words))

#4
a='привет'
b='пока'

a_set=set(a)
b_set=set(b)

print(a_set-b_set)
print(a_set&b_set)

#5
a=set('мама')
b=set('папа')
c=set('брат')

print(a|b|c)

#6
text=set('abcdefghijklmnopqrstuvwxyz')

alphabet=set('abcdefghijklmnopqrstuvwxyz')

print(text>=alphabet)
