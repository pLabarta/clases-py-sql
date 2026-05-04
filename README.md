# Python + SQL — Clases prácticas

Ejercicios de SQL resueltos desde Python usando SQLite.

## Estructura

```
python-sql/
├── evaluacion.py       # Corrector de ejercicios
├── clase-1/
│   ├── CLASE.md        # Teoría y enunciados
│   ├── generate.py     # Crea la base de datos de prueba
│   ├── query.py        # Acá se resuelven los ejercicios
│   ├── resueltos.py    # Soluciones de referencia
│   └── esperados.py    # Resultados esperados para el corrector
```

## Cómo usar

```bash
# 1. Generar la base de datos
python clase-1/generate.py

# 2. Resolver un ejercicio (cambiar EJERCICIO = N en query.py)
python clase-1/query.py

# 3. Ver el resultado de un ejercicio específico
python evaluacion.py --clase 1 --resultados 2

# 4. Corregir todos los ejercicios
python evaluacion.py --clase 1
```

## Documentación

**Python**
- [Documentación oficial](https://docs.python.org/es/3/)
- [sqlite3 — módulo de la biblioteca estándar](https://docs.python.org/es/3/library/sqlite3.html)

**SQL**
- [SQLite — referencia de sintaxis](https://www.sqlite.org/lang.html)
- [SQL Tutorial — W3Schools (español)](https://www.w3schools.com/sql/)
- [SQLZoo — ejercicios interactivos](https://sqlzoo.net/wiki/SQL_Tutorial)
