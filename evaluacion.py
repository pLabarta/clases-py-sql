import sys
import os
import importlib.util


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


def check_all(ejercicios, esperados):
    passed = 0
    for num, fn in ejercicios.items():
        try:
            enc_real, filas_real = fn()
            if not filas_real:
                print(f"\033[33mEjercicio {num:>2} — ⚠️  VACÍO (la query no devolvió ninguna fila)\033[0m")
                continue
            enc_esp, filas_esp = esperados[num]
            ok = enc_real == enc_esp and list(filas_real) == list(filas_esp)
            label = "✅ CORRECTO" if ok else "FAIL"
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
        except ValueError:
            print(f"\033[90mEjercicio {num:>2} — ❌ PENDIENTE\033[0m")
        except Exception as e:
            print(f"\033[91mEjercicio {num:>2} — ❌ ERROR: {e}\033[0m")
    print(f"\n{passed}/{len(ejercicios)} ejercicios correctos")


def _cargar_modulo(path, nombre):
    spec = importlib.util.spec_from_file_location(nombre, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[nombre] = mod
    spec.loader.exec_module(mod)
    return mod


def _cargar_clase(numero):
    root = os.path.dirname(os.path.abspath(__file__))
    clase_dir = os.path.join(root, f"clase-{numero}")

    if not os.path.isdir(clase_dir):
        print(f"No existe el directorio clase-{numero}")
        sys.exit(1)

    for path in (
        os.path.join(clase_dir, "esperados.py"),
        os.path.join(clase_dir, "query.py"),
    ):
        if not os.path.isfile(path):
            print(f"Falta el archivo: {path}")
            sys.exit(1)

    if clase_dir not in sys.path:
        sys.path.insert(0, clase_dir)

    esperados_mod = _cargar_modulo(os.path.join(clase_dir, "esperados.py"), "esperados")
    query_mod = _cargar_modulo(os.path.join(clase_dir, "query.py"), "query")

    return query_mod.EJERCICIOS, esperados_mod.ESPERADOS


if __name__ == "__main__":
    if "--clase" not in sys.argv:
        print("Uso: python evaluacion.py --clase <número>")
        print("Ejemplo: python evaluacion.py --clase 1")
        sys.exit(1)

    idx = sys.argv.index("--clase")
    if idx + 1 >= len(sys.argv):
        print("Especificá el número de clase después de --clase")
        sys.exit(1)

    numero = sys.argv[idx + 1]
    ejercicios, esperados = _cargar_clase(numero)

    if "--resultados" in sys.argv:
        ridx = sys.argv.index("--resultados")
        if ridx + 1 >= len(sys.argv):
            print("Especificá el número de ejercicio después de --resultados")
            sys.exit(1)
        num_ej = int(sys.argv[ridx + 1])
        fn = ejercicios.get(num_ej)
        if fn is None:
            print(f"Ejercicio {num_ej} no existe en clase-{numero}")
            sys.exit(1)
        print(f"── Clase-{numero} · Ejercicio {num_ej} ──────────────────────────────────")
        try:
            enc, filas = fn()
            if not filas:
                print("\033[33m⚠️  La query se ejecutó pero no devolvió ninguna fila.\033[0m")
            else:
                mostrar(enc, filas)
                enc_esp, filas_esp = esperados[num_ej]
                ok = enc == enc_esp and list(filas) == list(filas_esp)
                if ok:
                    print("✅ CORRECTO")
                else:
                    print("FAIL")
                    if enc != enc_esp:
                        print(f"  encabezados esperados : {enc_esp}")
                        print(f"  encabezados obtenidos : {enc}")
                    if list(filas) != list(filas_esp):
                        print(f"  filas esperadas  ({len(filas_esp)}): {list(filas_esp)}")
                        print(f"  filas obtenidas  ({len(filas)}): {list(filas)}")
        except ValueError:
            print("\033[90m❌ PENDIENTE — completá el SQL de este ejercicio\033[0m")
        except Exception as e:
            print(f"\033[91m❌ ERROR — {e}\033[0m")
    else:
        print(f"── Evaluación clase-{numero} ─────────────────────────────────")
        check_all(ejercicios, esperados)
