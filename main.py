print ('{: ^20}'.format('Juego Trivia'))
print("="*20)
nombre=input("ingrese su nombre : ")
print("hola ",nombre,"bienvenido al juego de Trivia\n")
rpl=' '
while rpl!='N':
  print("¿En que año se descubrio America?:\n")
  print("A)1587")
  print("B)1753")
  print("C)1652")
  print("D)1492")
  nr=0
  rsp1=(input("ingresa tu respuesta:\n"))
  if rsp1=="d":
    nr+=1
  else:
    nr+=0

  print("¿Creador De Python?:\n")
  print("A)Steven Paul Jobs")
  print("B)Bill Gates")
  print("C)Mark Elliot Zuckerberg")
  print("D)Guido Van Rossum")

  rsp2=(input("ingresa tu respuesta:\n"))
  if rsp2=="d":
    nr+=1
  else:
    nr+=0
  prt=(input("Desea saber su puntaje responder S o N : ").upper())
  if prt=="S":
    print("Respuestas correctas : ",nr)
    if nr>=0:
      rpl=input("Desea jugar otra vez Y/N : \n").upper()
      if rpl=="N":
          break
  else:
    rpl=input("Desea jugar otra vez Y/N : \n").upper()
    if rpl=="N":
      break
print("Muchas gracias por jugar")