s=str(input('Introduceti sirul: '))
print('a)numărul de apariţii ale caracterului ’A’ în şirul S:', s.count('A'))
print('b)şirul obţinut prin substituirea caracterului ’A’ prin caracterul ’*’:', s.replace('A','*'))
s1=list(s)
s1.remove('B')
s1=''.join(s1)
print('c)şirul obţinut prin radierea din şirul S a tuturor apariţiilor caracterului ’B’:', s1)
print('d)numărul de apariţii ale silabei MA în şirul S:', s.count('MA'))
print('e)şirul obţinut prin substituirea tuturor apariţiilor în şirul S a silabei MA prin silaba TA:', s.replace('MA','TA'))
print('g)scrierea inversă a şirului S:', s[::-1])
