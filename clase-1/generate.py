import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "clase1.db")

def create_db():
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()

    cur.executescript("""
        DROP TABLE IF EXISTS empleados;
        DROP TABLE IF EXISTS productos;
        DROP TABLE IF EXISTS clientes;

        CREATE TABLE empleados (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            departamento TEXT NOT NULL,
            salario REAL NOT NULL,
            activo INTEGER NOT NULL
        );

        CREATE TABLE productos (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        );

        CREATE TABLE clientes (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            ciudad TEXT NOT NULL,
            edad INTEGER NOT NULL,
            saldo REAL NOT NULL
        );
    """)

    cur.executemany(
        "INSERT INTO empleados VALUES (?, ?, ?, ?, ?, ?)",
        [
            (1,  "Ana",     "García",    "Ventas",      45000, 1),
            (2,  "Carlos",  "López",     "IT",          62000, 1),
            (3,  "María",   "Martínez",  "RRHH",        38000, 1),
            (4,  "José",    "Rodríguez", "Ventas",      51000, 0),
            (5,  "Laura",   "Fernández", "IT",          70000, 1),
            (6,  "Pedro",   "Sánchez",   "Finanzas",    55000, 1),
            (7,  "Isabel",  "González",  "Ventas",      43000, 1),
            (8,  "Miguel",  "Torres",    "IT",          68000, 0),
            (9,  "Carmen",  "Díaz",      "RRHH",        41000, 1),
            (10, "David",   "Ruiz",      "Finanzas",    59000, 1),
        ],
    )

    cur.executemany(
        "INSERT INTO productos VALUES (?, ?, ?, ?, ?)",
        [
            (1,  "Laptop Pro",      "Electrónica",  1299.99, 15),
            (2,  "Mouse Inalámbrico","Accesorios",    25.50,  80),
            (3,  "Monitor 27\"",    "Electrónica",   349.00,  22),
            (4,  "Teclado Mecánico","Accesorios",    89.99,  45),
            (5,  "Auriculares BT",  "Electrónica",  129.00,  30),
            (6,  "Webcam HD",       "Accesorios",    59.99,  55),
            (7,  "Disco SSD 1TB",   "Almacenamiento",99.00,  40),
            (8,  "USB Hub 7p",      "Accesorios",    35.00,  70),
            (9,  "Tablet 10\"",     "Electrónica",  449.00,   8),
            (10, "Cable HDMI 2m",   "Cables",         9.99, 120),
        ],
    )

    cur.executemany(
        "INSERT INTO clientes VALUES (?, ?, ?, ?, ?)",
        [
            (1,  "Sofía Herrera",    "Madrid",     29, 1500.00),
            (2,  "Tomás Jiménez",    "Barcelona",  45, 3200.50),
            (3,  "Valeria Moreno",   "Sevilla",    33, 800.00),
            (4,  "Andrés Castillo",  "Madrid",     52, 5100.75),
            (5,  "Elena Romero",     "Valencia",   27, 200.00),
            (6,  "Rubén Navarro",    "Barcelona",  38, 4400.00),
            (7,  "Natalia Suárez",   "Madrid",     61, 9800.20),
            (8,  "Diego Molina",     "Sevilla",    24, 150.00),
            (9,  "Claudia Ortega",   "Valencia",   43, 2700.00),
            (10, "Marcos Gil",       "Madrid",     35, 3600.80),
        ],
    )

    con.commit()
    con.close()
    print(f"Base de datos creada en: {DB_PATH}")

if __name__ == "__main__":
    create_db()
