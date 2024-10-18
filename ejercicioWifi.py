import os


redes =[]
red ={
    
}


while(True):
    os.system('clear' if os.name == 'posix' else 'cls')    
    print("1. Agregar Red")
    print("2. Ver redes")
    print("3. Salir")

    opcion = int(input("ingrese una opcio: "))

    if opcion == 1:
        os.system('clear' if os.name == 'posix' else 'cls')    
        print("Ingrese la red")
        nombre = input()
        red["nombre"] = nombre
        print("ingrese la contraseña")
        clave = input()
        red["clave"] = clave
        redes.append(red)
    elif opcion ==2:
        # os.system('clear' if os.name == 'posix' else 'cls')    
        for i in range(len(redes)):
            print(redes[i])
        
        input("presione enter para salir")
        
        
    else:
        print("Saliendo...")
        os.system('clear' if os.name == 'posix' else 'cls')    
        break
        

        
        
        
    
    
    