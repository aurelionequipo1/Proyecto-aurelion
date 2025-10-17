# 🛒 Proyecto Aurelion

## 📌 Tema, problema y solución

**Tema:** Gestión de productos y análisis de ventas de un supermercado.  

El supermercado **“Aurelion”** registra la información de clientes, productos y ventas en diferentes archivos de Excel.  
Con el objetivo de organizar el stock y optimizar las ventas para las fechas navideñas, se busca centralizar y analizar los datos de forma más eficiente.

### 🧩 Problemas identificados
- Duplicidad de datos y dificultad para actualizarlos.
- Falta de control sobre el stock disponible.
- Limitaciones para realizar el análisis de ventas por fechas o temporadas (como por ejemplo, la época navideña).

Como consecuencia la administración enfrenta retrasos en la toma de decisiones, desabastecimiento o excesos de inventario y poca capacidad para planificar campañas de venta efectivas.

### 💡 Solución propuesta
Integrar los archivos de Excel existentes en un mismo entorno de trabajo (**VS Code**) y desarrollar un programa en **Python** que:
- Lea los datos desde los archivos: `clientes.xlsx`, `productos.xlsx`, `ventas.xlsx` y `detalle_ventas.xlsx`.  
- Permita realizar consultas automáticas sobre las ventas y productos.  
- Genere reportes simples, como el total de ventas y los productos más vendidos.  

---

## 📊 Dataset de referencia

### Fuente y definición
Los datos provienen de los registros internos del supermercado Aurelion. Se utilizan archivos Excel (.xlsx) como fuente de información principal para simular una base de datos relacional dentro del entorno Python.  

### Estructura, tipos y escala

| Tabla | Descripción | Campos principales | Relación |
|--------|--------------|--------------------|-----------|
| **clientes** | Contiene los datos de los clientes del supermercado. | `id_cliente`, `nombre`, `apellido`, `correo`, `telefono`, `direccion` | 1 a muchos con `ventas`. |
| **productos** | Registra los artículos disponibles en el supermercado. | `id_producto`, `nombre_producto`, `categoria`, `precio_unitario`, `stock_actual` | 1 a muchos con `detalle_ventas`. |
| **ventas** | Guarda la información general de cada venta realizada. | `id_venta`, `id_cliente`, `fecha_venta`, `total_venta` | 1 a muchos con `detalle_ventas`. |
| **detalle_ventas** | Desglosa los productos incluidos en cada venta. | `id_detalle`, `id_venta`, `id_producto`, `cantidad`, `subtotal` | Muchos a uno con `ventas` y `productos`. |

**Tipo de base de datos:** Relacional  
**Formato actual:** Archivos Excel (.xlsx)  
**Gestión:** Lectura mediante librerías `pandas` y `openpyxl`.  
**Escala:** Pequeña a mediana (decenas de clientes, cientos de productos y miles de ventas).  

---

## ⚙️ Información, pasos, pseudocódigo y diagrama

### 🔁 Flujo general del programa
1. Acceder a la carpeta del proyecto “Proyecto Aurelion”.  
2. Mostrar los archivos disponibles.  
3. Solicitar al usuario el nombre del archivo que desea abrir.  
4. Validar que el archivo exista en la lista.  
5. Si el archivo es `documentacion.md`, mostrar su contenido.  
6. Manejar errores de lectura, permisos o inexistencia del archivo.  
7. Finalizar el proceso con mensaje informativo.

### 💻 Pseudocódigo

```plaintext
INICIO
    ABRIR_CARPETA("Proyecto Aurelion")
    MOSTRAR_ARCHIVOS: ["clientes.xlsx", "productos.xlsx", "ventas.xlsx", "detalle_ventas.xlsx", "documentacion.md"]
    ESCRIBIR "Ingrese el nombre del archivo al que desea acceder:"
    LEER nombre_archivo

    SI nombre_archivo = "documentacion.md" ENTONCES
        LEER_ARCHIVO("documentacion.md")
        ESCRIBIR "Contenido de doc.md leído exitosamente"
    SINO
        ESCRIBIR "Fin del proceso"
    FINSI
FIN
```

### 🧭 Diagrama de flujo del programa

![Diagrama de flujo del Proyecto Aurelion](proyecto%20aurelion.drawio.png)

---

## 🤖 Sugerencias y mejoras aplicadas con Copilot

1. **Manejo de casos:** se incorporó la comparación *case-insensitive* al validar los nombres de archivos.  
2. **Validación de entrada:** se añadió verificación para comprobar si el archivo ingresado existe en la lista.  
3. **Manejo de excepciones:** ahora se manejan los errores `FileNotFoundError`, `PermissionError` y `Exception` general.  
4. **Mensajes descriptivos:** se mejoró la retroalimentación al usuario con mensajes informativos y claros.  
5. **Sugerencia de Copilot:** autocompletado de bloques de código, docstrings y validaciones condicionales.  
6. **Estructura final:** código más legible, organizado y modular, listo para futuras expansiones.

---

## 📈 Resultados esperados
El sistema permite acceder y validar archivos del proyecto, leer el contenido de `documentacion.md` y mejorar el manejo de errores en la ejecución.  
Su estructura modular permite integrarlo fácilmente con análisis posteriores mediante `pandas` para la generación de reportes o dashboards.

---

## 👨‍💻 Autor
**EQUIPO 1**  
Proyecto académico desarrollado en colaboración con **IBM SkillsBuild** y **Guayerd**.
