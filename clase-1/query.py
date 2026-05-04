# ── Tablas disponibles en clase1.db ──────────────────────────────────────────
#
# empleados (10 filas)
#   id          INTEGER   identificador único
#   nombre      TEXT      nombre de pila
#   apellido    TEXT      apellido
#   departamento TEXT     'IT' | 'Ventas' | 'Finanzas' | 'RRHH'
#   salario     REAL      entre 38000 y 70000
#   activo      INTEGER   1 = activo, 0 = inactivo
#
#   Ejemplo:
#   id | nombre | apellido | departamento | salario | activo
#   1  | Ana    | García   | Ventas       | 45000.0 | 1
#   2  | Carlos | López    | IT           | 62000.0 | 1
#
# productos (10 filas)
#   id          INTEGER   identificador único
#   nombre      TEXT      nombre del producto
#   categoria   TEXT      'Electrónica' | 'Accesorios' | 'Almacenamiento' | 'Cables'
#   precio      REAL      entre 9.99 y 1299.99
#   stock       INTEGER   unidades disponibles
#
#   Ejemplo:
#   id | nombre           | categoria   | precio  | stock
#   1  | Laptop Pro       | Electrónica | 1299.99 | 15
#   2  | Mouse Inalámbrico| Accesorios  | 25.5    | 80
#
# clientes (10 filas)
#   id          INTEGER   identificador único
#   nombre      TEXT      nombre completo
#   ciudad      TEXT      'Madrid' | 'Barcelona' | 'Sevilla' | 'Valencia'
#   edad        INTEGER   entre 24 y 61
#   saldo       REAL      entre 150 y 9800
#
#   Ejemplo:
#   id | nombre         | ciudad    | edad | saldo
#   1  | Sofía Herrera  | Madrid    | 29   | 1500.0
#   2  | Tomás Jiménez  | Barcelona | 45   | 3200.5
#
# ─────────────────────────────────────────────────────────────────────────────

import sqlite3
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import evaluacion
import esperados

DB_PATH = os.path.join(os.path.dirname(__file__), "clase1.db")

EJERCICIO = 1

def conectar():
    return sqlite3.connect(DB_PATH)

def ejecutar(sql):
    if not sql.strip():
        raise ValueError("SQL vacío")
    con = conectar()
    cur = con.cursor()
    cur.execute(sql)
    filas = cur.fetchall()
    encabezados = [d[0] for d in cur.description]
    con.close()
    return encabezados, filas

def mostrar(encabezados, filas):
    ancho = max(len(str(v)) for fila in filas for v in fila) if filas else 10
    ancho = max(ancho, max(len(h) for h in encabezados))
    sep = "+" + "+".join("-" * (ancho + 2) for _ in encabezados) + "+"
    fmt = "| " + " | ".join(f"{{:<{ancho}}}" for _ in encabezados) + " |"
    print(sep)
    print(fmt.format(*encabezados))
    print(sep)
    for fila in filas:
        print(fmt.format(*[str(v) for v in fila]))
    print(sep)
    print(f"{len(filas)} fila(s)\n")

# ── Ejercicios SELECT básico ──────────────────────────────────────────────────

def ejercicio_1():
    # Seleccioná dos columnas específicas (nombre y apellido) de la tabla empleados.
    # Debe devolver una fila por cada empleado que existe en la tabla (10 en total).
    #
    # Resultado esperado:
    #   nombre  | apellido
    #   Ana     | García
    #   Carlos  | López
    #   María   | Martínez
    #   ...     (10 filas)
    return ejecutar("""

    """)

def ejercicio_2():
    # Seleccioná el nombre y el precio de todos los productos de la tabla productos.
    # Debe devolver los 10 productos con sus precios.
    #
    # Resultado esperado:
    #   nombre            | precio
    #   Laptop Pro        | 1299.99
    #   Mouse Inalámbrico | 25.5
    #   Monitor 27"       | 349.0
    #   ...               (10 filas)
    return ejecutar("""

    """)

# ── Ejercicios SELECT * ───────────────────────────────────────────────────────

def ejercicio_3():
    # Traé todas las columnas de todos los clientes usando el atajo *.
    # Las columnas son: id, nombre, ciudad, edad, saldo.
    #
    # Resultado esperado:
    #   id | nombre          | ciudad    | edad | saldo
    #   1  | Sofía Herrera   | Madrid    | 29   | 1500.0
    #   2  | Tomás Jiménez   | Barcelona | 45   | 3200.5
    #   3  | Valeria Moreno  | Sevilla   | 33   | 800.0
    #   ...                  (10 filas)
    return ejecutar("""

    """)

def ejercicio_4():
    # Traé todas las columnas de todos los productos usando el atajo *.
    # Las columnas son: id, nombre, categoria, precio, stock.
    #
    # Resultado esperado:
    #   id | nombre           | categoria      | precio  | stock
    #   1  | Laptop Pro       | Electrónica    | 1299.99 | 15
    #   2  | Mouse Inalámbrico| Accesorios     | 25.5    | 80
    #   3  | Monitor 27"      | Electrónica    | 349.0   | 22
    #   ...                   (10 filas)
    return ejecutar("""

    """)

# ── Ejercicios WHERE ──────────────────────────────────────────────────────────

def ejercicio_5():
    # Filtrá los empleados cuyo departamento sea exactamente 'IT'.
    # Solo 3 empleados cumplen esa condición.
    #
    # Resultado esperado (completo):
    #   id | nombre | apellido  | departamento | salario | activo
    #   2  | Carlos | López     | IT           | 62000.0 | 1
    #   5  | Laura  | Fernández | IT           | 70000.0 | 1
    #   8  | Miguel | Torres    | IT           | 68000.0 | 0
    return ejecutar("""

    """)

def ejercicio_6():
    # Filtrá los productos cuyo precio sea menor a 100. Ojo: 99.0 sí cumple la condición.
    # Deben aparecer 6 productos, solo con las columnas nombre y precio.
    #
    # Resultado esperado (completo):
    #   nombre            | precio
    #   Mouse Inalámbrico | 25.5
    #   Teclado Mecánico  | 89.99
    #   Webcam HD         | 59.99
    #   Disco SSD 1TB     | 99.0
    #   USB Hub 7p        | 35.0
    #   Cable HDMI 2m     | 9.99
    return ejecutar("""

    """)

# ── Ejercicios LIMIT ──────────────────────────────────────────────────────────

def ejercicio_7():
    # Traé todas las columnas de la tabla clientes pero cortá el resultado a las primeras 3 filas.
    #
    # Resultado esperado (completo):
    #   id | nombre          | ciudad    | edad | saldo
    #   1  | Sofía Herrera   | Madrid    | 29   | 1500.0
    #   2  | Tomás Jiménez   | Barcelona | 45   | 3200.5
    #   3  | Valeria Moreno  | Sevilla   | 33   | 800.0
    return ejecutar("""

    """)

def ejercicio_8():
    # Seleccioná nombre y salario de empleados, limitado a las primeras 5 filas.
    #
    # Resultado esperado (completo):
    #   nombre | salario
    #   Ana    | 45000.0
    #   Carlos | 62000.0
    #   María  | 38000.0
    #   José   | 51000.0
    #   Laura  | 70000.0
    return ejecutar("""

    """)

# ── Ejercicios combinados ─────────────────────────────────────────────────────

def ejercicio_9():
    # Combiná WHERE y LIMIT: filtrá por departamento 'Ventas' y quedáte con los primeros 2.
    # Hay 3 empleados en Ventas, pero el resultado debe tener solo 2.
    #
    # Resultado esperado (completo):
    #   nombre | salario
    #   Ana    | 45000.0
    #   José   | 51000.0
    return ejecutar("""

    """)

def ejercicio_10():
    # Combiná WHERE y LIMIT: filtrá productos de categoría 'Electrónica' y limitá a 3.
    # Hay 4 productos en esa categoría, pero el resultado debe mostrar solo los primeros 3.
    #
    # Resultado esperado (completo):
    #   id | nombre         | categoria   | precio  | stock
    #   1  | Laptop Pro     | Electrónica | 1299.99 | 15
    #   3  | Monitor 27"    | Electrónica | 349.0   | 22
    #   5  | Auriculares BT | Electrónica | 129.0   | 30
    return ejecutar("""

    """)

def ejercicio_11():
    # Filtrá clientes usando dos condiciones a la vez: ciudad = 'Madrid' Y saldo > 2000.
    # Madrid tiene 4 clientes pero solo 3 superan ese saldo (Sofía tiene 1500, queda fuera).
    #
    # Resultado esperado (completo):
    #   nombre          | ciudad | saldo
    #   Andrés Castillo | Madrid | 5100.75
    #   Natalia Suárez  | Madrid | 9800.2
    #   Marcos Gil      | Madrid | 3600.8
    return ejecutar("""

    """)

def ejercicio_12():
    # Combiná dos filtros y un límite: empleados con activo = 1 Y salario >= 55000, máximo 4 filas.
    # Miguel Torres tiene salario alto pero activo = 0, así que queda fuera.
    # El resultado tiene exactamente 4 filas (no sobran ni faltan).
    #
    # Resultado esperado (completo):
    #   id | nombre | apellido  | departamento | salario | activo
    #   2  | Carlos | López     | IT           | 62000.0 | 1
    #   5  | Laura  | Fernández | IT           | 70000.0 | 1
    #   6  | Pedro  | Sánchez   | Finanzas     | 55000.0 | 1
    #   10 | David  | Ruiz      | Finanzas     | 59000.0 | 1
    return ejecutar("""

    """)

# ── Runner / Checker ──────────────────────────────────────────────────────────

EJERCICIOS = {
    1:  ejercicio_1,
    2:  ejercicio_2,
    3:  ejercicio_3,
    4:  ejercicio_4,
    5:  ejercicio_5,
    6:  ejercicio_6,
    7:  ejercicio_7,
    8:  ejercicio_8,
    9:  ejercicio_9,
    10: ejercicio_10,
    11: ejercicio_11,
    12: ejercicio_12,
}

if __name__ == "__main__":
    if "--check" in sys.argv:
        evaluacion.check_all(EJERCICIOS, esperados.ESPERADOS)
    else:
        fn = EJERCICIOS.get(EJERCICIO)
        if fn is None:
            print(f"Ejercicio {EJERCICIO} no existe. Opciones: {list(EJERCICIOS)}")
        else:
            print(f"── Ejercicio {EJERCICIO} ──────────────────────────────────")
            try:
                enc, filas = fn()
                mostrar(enc, filas)
            except Exception:
                print("Completá el SQL de este ejercicio.")
