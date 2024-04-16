#PROYECTO DE JOSÉ PABLO GUILLÉN Y SEBASTIAN ESCOBAR
cliente = input("Ingrese su nombre: ")
nit = input("Ingrese su NIT (si no desea, escriba cf): ")
batido = "fresa con lactosa descremada sin endulzante"
tamaño = "normal"
costo = 20.0
endulzante = 0
def mostrar_opciones():
    print("\nMenú de alternativas:")
    print("1. Ver detalles del pedido")
    print("2. Agregar endulzante")
    print("3. Cambiar lácteo")
    print("4. Agrandar")
    print("5. Confirmar")
    print("6. Salir")
def mostrar_info_pedido():
    print("\nDatos del pedido:")
    print("Nombre del cliente:", cliente)
    print("NIT:", nit)
    print("Batido:", batido)
    print("Tamaño:", tamaño)
    print("Endulzante:", endulzante)
    print("Costo:", costo)
def agregar_endulzante(endulzante, costo):
    if endulzante < 2:
        endulzante += 1
        costo += 0.5
        print("Endulzante actual:", endulzante)
        print("nuevo costo:", costo)
    else:
        print("\nNo se puede agregar más endulzante.")
    return endulzante, costo
def cambiar_lacteo(batido, costo):
    print("\nOpciones de leche:")
    print("1. Sin lácteo (agua)")
    print("2. Leche descremada")
    print("3. Leche entera")
    print("4. Leche de soya")
    opcion_lacteo = int(input("Ingrese leche deseada: "))
    if opcion_lacteo == 1:
        batido = "Batido de fresa sin lácteo (agua)"
        costo = 18.0
    elif opcion_lacteo == 2:
        batido = "Batido de fresa leche descremada"
        costo = 20.0
    elif opcion_lacteo == 3:
        batido = "Batido de fresa leche entera"
        costo = 20.0
    elif opcion_lacteo == 4:
        batido = "Batido de fresa leche de soya"
        costo = 23.0
    else:
        print("Alternativa no válida.")
    return batido, costo
def agrandar(tamaño, costo):
    if tamaño == "normal":
        tamaño = "grande"
        costo *= 1.05
        print("\nAgrando su batido.")
        print("Costo actualizado:", costo)
    else:
        print("\nNo puede agrandar mas el batido.")
    return tamaño, costo
def confirmar_pedido():
    mostrar_info_pedido()
    print("\nGracias por su compra.")
while True:
    mostrar_opciones()
    opcion = int(input("Elija una opción: "))
    if opcion == 1:
        mostrar_info_pedido()
    elif opcion == 2:
        endulzante, costo = agregar_endulzante(endulzante, costo)
    elif opcion == 3:
        batido, costo = cambiar_lacteo(batido, costo)
    elif opcion == 4:
        tamaño, costo = agrandar(tamaño, costo)
    elif opcion == 5:
        confirmar_pedido()
        break
    elif opcion == 6:
        break
    else:
        print("Porfavor seleccione una de las opciones mostradas.")