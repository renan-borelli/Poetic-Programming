frase= str(input("Qual a frase que deseja codificar? \n"))
frase= frase.lower()
lista= list(frase)
for i in range(len(lista)):
  if lista[i]=='a': lista[i]='4 '
  if lista[i]=='b': lista[i]='13 '
  if lista[i]=='c': lista[i]='( '
  if lista[i]=='d': lista[i]='[) '
  if lista[i]=='e': lista[i]='3 '
  if lista[i]=='f': lista[i]='|= '
  if lista[i]=='g': lista[i]='6 '
  if lista[i]=='h': lista[i]='|-| '
  if lista[i]=='i': lista[i]='| '
  if lista[i]=='j': lista[i]='.] '
  if lista[i]=='k': lista[i]='|< '
  if lista[i]=='l': lista[i]='1 '
  if lista[i]=='m': lista[i]='|Y| '
  if lista[i]=='n': lista[i]='/\/ '
  if lista[i]=='o': lista[i]='0 '
  if lista[i]=='p': lista[i]='|> '
  if lista[i]=='q': lista[i]='0, '
  if lista[i]=='r': lista[i]='|2 '
  if lista[i]=='s': lista[i]='5 '
  if lista[i]=='t': lista[i]='7 '
  if lista[i]=='u': lista[i]='[_] '
  if lista[i]=='v': lista[i]='\/ '
  if lista[i]=='w': lista[i]='\v/ '
  if lista[i]=='x': lista[i]='}{ '
  if lista[i]=='y': lista[i]='`/ '
  if lista[i]=='z': lista[i]='2 '
  if lista[i]==' ': lista[i]='  '
codifier=''
codifier=codifier.join(lista)
print(codifier)
