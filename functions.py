lista_componentes = []

def _validar_string(texto):
    if len(texto) > 0:
        return True
    return False

def _validar_int(numero):
    if numero > 0:
        return True
    return False

def _validar_stock(numero):
    if numero >= 0:
        return True
    return False

def estado_booleano(reposicion):
    if reposicion == False:
        return "Stock Adecuado"
    return "Requiere Reposición"

def menu():
    print("====== Gestión de Hardware =======")
    print("1. Registrar nuevo componente")
    print("2. Buscar componente por SKU")
    print("3. Eliminar componente sin stock")
    print("4. Actualizar alertas de reposición")
    print("5. Mostrar inventario completo")
    print("6. Salir")

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: \n"))
            if opcion > 0 and opcion <= 6:
                return opcion
            else:
                print("Opción debe ser entre 1 y 6")
        except:
            print("Valor debe ser numérico")

def registrar_componente(lista_componentes):
    while True:
        sku = input("Ingrese código único del componente: \n").strip()
        if _validar_string(sku):
            break
    while True:
        nombre = input("Ingrese nombre del componente: \n").strip()
        if _validar_string(nombre):
            break
    while True:
        precio = int(input("Ingrese precio del componente: \n $"))
        if _validar_int(precio):
            break
    while True:
        stock = int(input("Ingrese stock de unidades en bodega: \n"))
        if _validar_stock(stock):
            break
    producto = {
        "sku" : sku,
        "nombre" : nombre,
        "precio" : precio,
        "stock" : stock,
        "reposicion" : False
    }
    lista_componentes.append(producto)
    print("Componente agregado a la lista")

def buscar_componente(lista_componentes, sku):
    for c in range(len(lista_componentes)):
        if lista_componentes[c]["sku"] == sku:
            return c
    return -1

def actualizar_alertas(lista_componentes):
    if _validar_lista(lista_componentes) == False:
        print("Lista se encuentra vacia")
        return
    for c in lista_componentes:
        if c["stock"] < 5:
            c["reposicion"] = True
        else:
            c["reposicion"] = False
    print("Alertas actualizadas")

def mostrar_inventario(lista_componentes):
    if _validar_lista(lista_componentes) == False:
        print("Lista se encuentra vacia")
        return
    actualizar_alertas(lista_componentes)
    print("=== Inventario Actual ===")
    for c in lista_componentes:
            print(f"SKU: {c["sku"]}")
            print(f"Componente: {c["nombre"]}")
            print(f"Precio: ${c["precio"]}")
            print(f"Stock: {c["stock"]}")
            alerta = estado_booleano(c["reposicion"])
            print(f"Alerta: {alerta}")
            print("**************************************")

def _validar_lista(lista_componentes):
    if len(lista_componentes) > 0:
        return True
    return False