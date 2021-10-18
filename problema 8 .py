lst="A B C D E F G H I J K L M N O P Q R S T U V W X Y"
l1=""
l2=""
l3=""
for i in lst:
    x=chr(ord(i)+1)
    l1+=x
    a=l1.replace('!',' ')
    s=a.replace('[','A') 
print("Sirul1:", s)
l2=s
for i in lst:
    y=l2.replace(("Z"), ("A"))
    b=y.replace('!',' ')
    k=b.replace('[','A')
print("Sirul2:", k) 
l3=k
for i in lst:
    z=l3.replace(' ','-')
    b=z.replace('[','A')
print("Sirul3:", b)