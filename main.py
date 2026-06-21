# ### | FICHA 6: Enunciado prueba parcial (Forma C)

# **Asignatura:** Fundamentos de Programación (FPY1101)
# **Experiencia de Aprendizaje:** EA3: Colecciones y funciones en Python

# #### Resolver:

# Desarrolla un programa en Python que implemente un **Sistema de Inventario de Componentes de Computación**, donde todo el comportamiento se organice mediante funciones bien definidas y separadas en módulos (`main.py` y `functions.py`).

# #### 1. Datos que debe manejar el sistema

# El sistema trabaja con una colección de piezas de hardware. Esta colección es una lista que comienza vacía. Cada pieza es un diccionario con los siguientes campos y restricciones:

# | Campo | Qué representa | Restricciones de validación |
# | --- | --- | --- |
# | `"sku"` | Código único del producto (ej: GPU-001) | No vacío ni solo espacios en blanco. |
# | `"nombre"` | Nombre del componente | No vacío ni solo espacios en blanco. |
# | `"precio"` | Precio de venta en pesos | Número entero mayor que 0. |
# | `"stock"` | Cantidad de unidades en bodega | Número entero mayor o igual a 0. |
# | `"reposicion"` | ¿Requiere pedir más unidades? | `False` al registrar. Su valor cambia a `True` al ejecutar la Opción 4, dependiendo del stock. |

# #### 2. Lo que debe hacer el sistema

# El programa se controla desde un menú interactivo. Recuerda la regla de oro: el ciclo para atrapar errores de tipeo (letras en vez de números) debe envolver al bloque `try-except`.

# **========== GESTIÓN DE HARDWARE ==========**

# 1. Registrar nuevo componente
# 2. Buscar componente por SKU
# 3. Eliminar componente sin stock
# 4. Actualizar alertas de reposición
# 5. Mostrar inventario completo
# 6. Salir del sistema
# **=========================================**

# **Opción 1 - Registrar nuevo componente:**
# El sistema solicita al usuario el SKU, nombre, precio y stock. Cada dato debe ser validado por funciones independientes que retornen `True` o `False`. Si los datos son correctos, se crea el diccionario (con `"reposicion"` en `False`) y se añade a la lista.

# **Opción 2 - Buscar componente por SKU:**
# El sistema pide el SKU a buscar. **Regla estricta:** La función de búsqueda debe recibir exactamente `(lista_componentes, sku)` como parámetros, en ese orden. Retorna la posición en la lista o `-1`. El `main.py` decide qué imprimir basándose en este retorno.

# **Opción 3 - Eliminar componente sin stock:**
# El sistema pide el SKU del componente a dar de baja. Reutiliza la función de búsqueda de la Opción 2. Si se encuentra, lo elimina de la lista. Si no, muestra el mensaje: *"El componente con SKU 'X' no existe en el sistema"*.

# **Opción 4 - Actualizar alertas de reposición:**
# El sistema recorre la lista completa. La regla de negocio es: todos los componentes que tengan un **stock menor a 5 unidades** deben cambiar su estado `"reposicion"` a `True`. Si tienen 5 o más, quedan en `False`. Esto debe hacerse en una función propia. *(Opcional: puedes aplicar la lógica de "herramienta universal" que vimos ayer para evaluar el stock).*

# **Opción 5 - Mostrar inventario completo:**
# El sistema primero llama a la función de la Opción 4 para actualizar los estados. Luego, recorre la lista y muestra los productos. *(Recuerda usar tu función para traducir el `True/False` a texto legible, y tu validador de listas para evitar el colapso si está vacía).*

# ```text
# === INVENTARIO ACTUAL ===
# SKU: GPU-090
# Componente: Radeon RX 9060 XT 16GB
# Precio: $450000
# Stock: 2 unidades
# Alerta: REQUIERE REPOSICIÓN
# ********************************
# SKU: CPU-056
# Componente: Ryzen 5 5600
# Precio: $135000
# Stock: 12 unidades
# Alerta: STOCK ADECUADO
# ********************************

# ```

# **Opción 6 - Salir:**
# El programa rompe el ciclo y se despide de forma limpia.

from functions import *

while True:
    menu()
    opcion = leer_opcion()
    if opcion == 1:
        registrar_componente(lista_componentes)
    elif opcion == 2:
        sku = input("Ingrese sku del componente a buscar: \n").strip()
        posicion = buscar_componente(lista_componentes, sku)
        if posicion != -1:
            print(f"La posición del componente es {posicion}")
            print(f"SKU: {lista_componentes[posicion]["sku"]}")
            print(f"Componente: {lista_componentes[posicion]["nombre"]}")
            print(f"Precio: ${lista_componentes[posicion]["precio"]}")
            print(f"Stock: {lista_componentes[posicion]["stock"]}")
            alerta = estado_booleano(lista_componentes[posicion]["reposicion"])
            print(f"Alerta: {alerta}")
    elif opcion == 3:
        sku = input("Ingrese sku del componente a eliminar: \n").strip()
        posicion = buscar_componente(lista_componentes, sku)
        if posicion != -1:
            lista_componentes.pop(posicion)
            print("Producto Eliminado")
        else:
            print(f"El componente del código {sku} no existe en el sistema")
    elif opcion == 4:
        actualizar_alertas(lista_componentes)
    elif opcion == 5:
        mostrar_inventario(lista_componentes)
    else:
        print("Gracias por usar nuestra app :D")
        break