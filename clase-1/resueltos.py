import sqlite3
import os
import sys

DB_PATH = os.path.join(os.path.dirname(__file__), "clase1.db")

EJERCICIO = 1

def conectar():
    return sqlite3.connect(DB_PATH)

def ejecutar(sql):
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
    return ejecutar("SELECT nombre, apellido FROM empleados")

def ejercicio_2():
    return ejecutar("SELECT nombre, precio FROM productos")

# ── Ejercicios SELECT * ───────────────────────────────────────────────────────

def ejercicio_3():
    return ejecutar("SELECT * FROM clientes")

def ejercicio_4():
    return ejecutar("SELECT * FROM productos")

# ── Ejercicios WHERE ──────────────────────────────────────────────────────────

def ejercicio_5():
    return ejecutar("SELECT * FROM empleados WHERE departamento = 'IT'")

def ejercicio_6():
    return ejecutar("SELECT nombre, precio FROM productos WHERE precio < 100")

# ── Ejercicios LIMIT ──────────────────────────────────────────────────────────

def ejercicio_7():
    return ejecutar("SELECT * FROM clientes LIMIT 3")

def ejercicio_8():
    return ejecutar("SELECT nombre, salario FROM empleados LIMIT 5")

# ── Ejercicios combinados ─────────────────────────────────────────────────────

def ejercicio_9():
    return ejecutar("SELECT nombre, salario FROM empleados WHERE departamento = 'Ventas' LIMIT 2")

def ejercicio_10():
    return ejecutar("SELECT * FROM productos WHERE categoria = 'Electrónica' LIMIT 3")

def ejercicio_11():
    return ejecutar("SELECT nombre, ciudad, saldo FROM clientes WHERE ciudad = 'Madrid' AND saldo > 2000")

def ejercicio_12():
    return ejecutar("SELECT * FROM empleados WHERE activo = 1 AND salario >= 55000 LIMIT 4")

# ── Resultados esperados ──────────────────────────────────────────────────────

ESPERADOS = {
    1: (
        ["nombre", "apellido"],
        [
            ("Ana",    "García"),
            ("Carlos", "López"),
            ("María",  "Martínez"),
            ("José",   "Rodríguez"),
            ("Laura",  "Fernández"),
            ("Pedro",  "Sánchez"),
            ("Isabel", "González"),
            ("Miguel", "Torres"),
            ("Carmen", "Díaz"),
            ("David",  "Ruiz"),
        ],
    ),
    2: (
        ["nombre", "precio"],
        [
            ("Laptop Pro",       1299.99),
            ("Mouse Inalámbrico", 25.5),
            ('Monitor 27"',      349.0),
            ("Teclado Mecánico",  89.99),
            ("Auriculares BT",   129.0),
            ("Webcam HD",         59.99),
            ("Disco SSD 1TB",     99.0),
            ("USB Hub 7p",        35.0),
            ('Tablet 10"',       449.0),
            ("Cable HDMI 2m",      9.99),
        ],
    ),
    3: (
        ["id", "nombre", "ciudad", "edad", "saldo"],
        [
            (1,  "Sofía Herrera",   "Madrid",    29, 1500.0),
            (2,  "Tomás Jiménez",   "Barcelona", 45, 3200.5),
            (3,  "Valeria Moreno",  "Sevilla",   33,  800.0),
            (4,  "Andrés Castillo", "Madrid",    52, 5100.75),
            (5,  "Elena Romero",    "Valencia",  27,  200.0),
            (6,  "Rubén Navarro",   "Barcelona", 38, 4400.0),
            (7,  "Natalia Suárez",  "Madrid",    61, 9800.2),
            (8,  "Diego Molina",    "Sevilla",   24,  150.0),
            (9,  "Claudia Ortega",  "Valencia",  43, 2700.0),
            (10, "Marcos Gil",      "Madrid",    35, 3600.8),
        ],
    ),
    4: (
        ["id", "nombre", "categoria", "precio", "stock"],
        [
            (1,  "Laptop Pro",        "Electrónica",    1299.99, 15),
            (2,  "Mouse Inalámbrico", "Accesorios",       25.5,  80),
            (3,  'Monitor 27"',       "Electrónica",     349.0,  22),
            (4,  "Teclado Mecánico",  "Accesorios",       89.99, 45),
            (5,  "Auriculares BT",    "Electrónica",     129.0,  30),
            (6,  "Webcam HD",         "Accesorios",       59.99, 55),
            (7,  "Disco SSD 1TB",     "Almacenamiento",   99.0,  40),
            (8,  "USB Hub 7p",        "Accesorios",       35.0,  70),
            (9,  'Tablet 10"',        "Electrónica",     449.0,   8),
            (10, "Cable HDMI 2m",     "Cables",            9.99, 120),
        ],
    ),
    5: (
        ["id", "nombre", "apellido", "departamento", "salario", "activo"],
        [
            (2, "Carlos", "López",     "IT", 62000.0, 1),
            (5, "Laura",  "Fernández", "IT", 70000.0, 1),
            (8, "Miguel", "Torres",    "IT", 68000.0, 0),
        ],
    ),
    6: (
        ["nombre", "precio"],
        [
            ("Mouse Inalámbrico", 25.5),
            ("Teclado Mecánico",  89.99),
            ("Webcam HD",         59.99),
            ("Disco SSD 1TB",     99.0),
            ("USB Hub 7p",        35.0),
            ("Cable HDMI 2m",      9.99),
        ],
    ),
    7: (
        ["id", "nombre", "ciudad", "edad", "saldo"],
        [
            (1, "Sofía Herrera",  "Madrid",    29, 1500.0),
            (2, "Tomás Jiménez",  "Barcelona", 45, 3200.5),
            (3, "Valeria Moreno", "Sevilla",   33,  800.0),
        ],
    ),
    8: (
        ["nombre", "salario"],
        [
            ("Ana",    45000.0),
            ("Carlos", 62000.0),
            ("María",  38000.0),
            ("José",   51000.0),
            ("Laura",  70000.0),
        ],
    ),
    9: (
        ["nombre", "salario"],
        [
            ("Ana",  45000.0),
            ("José", 51000.0),
        ],
    ),
    10: (
        ["id", "nombre", "categoria", "precio", "stock"],
        [
            (1, "Laptop Pro",     "Electrónica", 1299.99, 15),
            (3, 'Monitor 27"',    "Electrónica",  349.0,  22),
            (5, "Auriculares BT", "Electrónica",  129.0,  30),
        ],
    ),
    11: (
        ["nombre", "ciudad", "saldo"],
        [
            ("Andrés Castillo", "Madrid", 5100.75),
            ("Natalia Suárez",  "Madrid", 9800.2),
            ("Marcos Gil",      "Madrid", 3600.8),
        ],
    ),
    12: (
        ["id", "nombre", "apellido", "departamento", "salario", "activo"],
        [
            (2,  "Carlos", "López",   "IT",       62000.0, 1),
            (5,  "Laura",  "Fernández","IT",       70000.0, 1),
            (6,  "Pedro",  "Sánchez", "Finanzas", 55000.0, 1),
            (10, "David",  "Ruiz",    "Finanzas", 59000.0, 1),
        ],
    ),
}

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

def check_all():
    passed = 0
    for num, fn in EJERCICIOS.items():
        enc_esp, filas_esp = ESPERADOS[num]
        enc_real, filas_real = fn()
        ok = enc_real == enc_esp and list(filas_real) == list(filas_esp)
        label = "PASS" if ok else "FAIL"
        print(f"Ejercicio {num:>2} — {label}")
        if not ok:
            if enc_real != enc_esp:
                print(f"  encabezados esperados : {enc_esp}")
                print(f"  encabezados obtenidos : {enc_real}")
            if list(filas_real) != list(filas_esp):
                print(f"  filas esperadas  ({len(filas_esp)}): {list(filas_esp)}")
                print(f"  filas obtenidas  ({len(filas_real)}): {list(filas_real)}")
        else:
            passed += 1
    print(f"\n{passed}/{len(EJERCICIOS)} ejercicios correctos")

if __name__ == "__main__":
    if "--check" in sys.argv:
        check_all()
    else:
        fn = EJERCICIOS.get(EJERCICIO)
        if fn is None:
            print(f"Ejercicio {EJERCICIO} no existe. Opciones: {list(EJERCICIOS)}")
        else:
            print(f"── Ejercicio {EJERCICIO} ──────────────────────────────────")
            enc, filas = fn()
            mostrar(enc, filas)
