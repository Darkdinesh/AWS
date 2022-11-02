print("\t'leave application")

a=('''To
The Principle 
college
address
date:<|date|>
subject:- Application for leave
respected sir/madam,
Respectfully, I am here to inform you that, 
I am suffering from typhoid since last night, 
The doctor had suggestion me to take rest for 
3 days.
\t Hence, kindely grant me leave for 3 days.
I shall be thankful to you
your's obediently
name:|name|
class:|class|
roll no:|roll no|
'''
)

b=input("name:")
c=input("class:")
d=input("roll no:")
e=input("date:")
f=input("time period:")
g=input("school:")
h=input("address:")

print('___________________________________________')
a=a.replace('school',g)
a=a.replace('address',h)
a=a.replace('<|date|>',e)
a=a.replace('|name|',b)
a=a.replace('|class|',c)
a=a.replace('|roll no|',d)
a=a.replace('___',f)
print(a)