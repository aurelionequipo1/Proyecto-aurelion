# INICIO

import webbrowser

# Simular acceso a la carpeta "Proyecto Aurelion"
print("Accediendo a la carpeta 'Proyecto Aurelion'...\n")

# Mostrar archivos disponibles enumerados
archivos = ["clientes.xlsx", "productos.xlsx", "ventas.xlsx", "detalles_ventas.xlsx", "documentacion.md"]

print("Archivos disponibles:")
for i, archivo in enumerate(archivos, start=1):
    print(f"{i}. {archivo}")

# Solicitar número de selección al usuario
try:
    opcion = int(input("\nSeleccione el número del archivo al que desea acceder: "))

    # Verificar si la opción está en rango
    if 1 <= opcion <= len(archivos):
        nombre_archivo = archivos[opcion - 1].lower()
        print(f"\nHas seleccionado: {nombre_archivo}")

        # Solo permitir acceso al archivo documentacion.md
        if nombre_archivo == "documentacion.md":
            try:
                # 🔗 Abrir archivo directamente en GitHub
                enlace_github = "https://github.com/luis0221/Proyecto-aurelion/blob/387b5910d4853f7c744af856ef37570d9343e048/documentacion_demo1_con_diagrama1.md"
                print(f"\nAbriendo archivo en GitHub: {enlace_github}")
                webbrowser.open(enlace_github)

            except Exception as e:
                print(f"\nError al intentar abrir el enlace: {str(e)}")
        else:
            print("\nSolo se puede acceder al archivo de documentación (documentacion.md).")
    else:
        print("\nOpción no válida. Por favor seleccione un número del 1 al", len(archivos))

except ValueError:
    print("\nError: Debe ingresar un número válido.")

print("\nFin del proceso.")

# FIN
