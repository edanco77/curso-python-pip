import random



print(False and True)

print(int(4.54))

def elegir_opciones():
  opciones = ('piedra','papel','tijera')
  user_option = input('piedra, papel o tijera => ')
  

  if not user_option in opciones:
    print('Esa Opcion no es Valida')
    return None, None
  
  computer_option = random.choice(opciones)
  user_option = user_option.lower()

  
  print('opcion del PC '+computer_option)

  return user_option, computer_option


def reglas(user_option, computer_option,  puntosusuario, puntoscomputer):
  if user_option == computer_option:
    print('Empate')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera, usuario gano')
      puntosusuario+=1
    else:
      print('papel gana a piedra, computer gano')
      puntoscomputer+=1
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra, usuario gano')
      puntosusuario+=1
    else:
      print('tijera gana a papel , computer gano')
      puntoscomputer+=1
  else: 
    if computer_option == 'papel':
      print('tijera gana a papel , usuario gano')
      puntosusuario+=1
    else:
      print('piedra gana a tijera1 , computer gano')
      puntoscomputer+=1
  return puntosusuario, puntoscomputer

def run_game():
  puntosusuario =0;
  puntoscomputer = 0;
  ronda = 1

  while True:
  
    print('Ronda :' ,ronda)
  
    user_option, computer_option = elegir_opciones();
    puntosusuario, puntoscomputer = reglas(user_option, computer_option,puntosusuario, puntoscomputer)
    
    ronda+=1    
  
   
    if puntoscomputer == 3 or puntosusuario == 3:
      if puntoscomputer == 3:
        print('**** GANO COMPUTER')
        break
      else:
        print('**** GANO USUARIO')
        break
  


run_game()

