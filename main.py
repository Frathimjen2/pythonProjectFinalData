
menu_options = {
    1: 'Pilas',
    2: 'Colas',
    3: 'Arboles',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key])

def option1():
    print('Por Opcion 1 \'Pilas\'')

    def isEmpty(pla):
        if pla == []:
            return True
        else:
            return False

    def Push(pla, elemento):
        pla.append(elemento)
        arriba = len(pla) - 1

    def Pop(pla):
        if isEmpty(pla):
            return "Subflujo"
        else:
            elemento = pla.pop()
            if len(pla) == 0:
                arriba = None
            else:
                arriba = len(pla) - 1
            return elemento

    def Display(pla):
        if isEmpty(pla):
            print("La pila esta vacia")
        else:
            arriba = len(pla) - 1
            print('\n' + str(pla[arriba]) + " <-- Elemento arriba")
            for a in range(arriba - 1, -1, -1):
                print(pla[a])

    Pila = []  # initially stack is empty
    arriba = None
    while True:
        print("\nPor Opcion 1 (Pilas)")
        print("1. Insertar")
        print("2. Extraer")
        print("3. Visualizar")
        print("4. Salida")
        ch = int(input("Please enter a choice(1-5): "))
        if ch == 1:
            elemento = int(input("\nIngresar elemento: "))
            Push(Pila, elemento)
        elif ch == 2:
            elemento = Pop(Pila)
            if elemento == "Subflujo":
                print("Subflujo! Pila esta vaica!")
            else:
                print("Elemento extreido es", elemento)
        elif ch == 3:
            Display(Pila)
        elif ch == 4:
            break
def option2():
    print('Por Opcion 2 \'Colas\'')

    def cls():
        print("\n" * 2)

    def isEmpty(Cl):
        if Cl == []:
            return True
        else:
            return False

    def Enqueue(Cl, elemento):
        Cl.append(elemento)
        if len(Cl) == 1:
            adelante = detras = 0
        else:
            detras = len(Cl) - 1

    def Dequeue(Cl):
        if isEmpty(Cl):
            return "Subflujo"
        else:
            elemento = Cl.pop(0)
        if len(Cl) == 0:
            adelante = detras = None
        return elemento

    def Display(Cl):
        if isEmpty(Cl):
            print("Queue Empty!")
        elif len(Cl) == 1:
            print(Cl[0], "<==adelante, rear")
        else:
            adelante = 0
            detras = len(Cl) - 1
            print(Cl[adelante], "<--adelante")
            for a in range(1, detras):
                print(Cl[a])
            print(Cl[detras], "<--detras")

    cola = []
    adelante = None
    while True:
        cls()
        print("Por Opción 2 (Colas)")
        print("1. Insertar")
        print("2. Extraer")
        print("3. Visualizar")
        print("4. Salida")
        ch = int(input("Ingrese opcion de (1-4): "))
        if ch == 1:
            elemento = int(input("Insertar elemento: "))
            Enqueue(cola, elemento)
            input("Elemento ingresado en Cola")
        elif ch == 2:
            elemento = Dequeue(cola)
            if elemento == "Subflujo":
                print("Subflujo! Cola vacia!")
            else:
                print("Elemento sacado de Cola es", elemento)
            input("Elemento sacdado")
        elif ch == 3:
            Display(cola)
            input("Cola observada")
        elif ch == 4:
            break
def option3():
     print('Por Opcion 3 \'Arboles Binarios\'')


if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
           option1()
        elif option == 2:
            option2()
        elif option == 3:
            option3()
        elif option == 4:
            print('Gracias por usar este programa')
            exit()
        else:
            print('Opcion invalida, elegir numero entre 1 hasta 4.')