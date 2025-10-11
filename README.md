# 🛒 Proyecto Aurelion
### Tema: Gestión de productos y análisis de ventas de un supermercado

El supermercado **Aurelion** registra la información de clientes, productos y ventas en diferentes archivos de Excel.  
Con el objetivo de organizar el stock y optimizar las ventas para las fechas navideñas, se busca centralizar y analizar los datos de forma más eficiente.
---
## 1. Problema identificado
El supermercado **Aurelion** actualmente registra la información de clientes, productos y ventas en diferentes archivos de Excel independientes.  
Esta forma de manejo genera varios inconvenientes:

- Duplicidad de datos y dificultad para actualizarlos.  
- Falta de control sobre el stock disponible.  
- Dificultad para identificar los productos más vendidos o con baja rotación.  
- Limitaciones para realizar análisis de ventas por fechas o temporadas (como la época navideña).

Como consecuencia, la administración enfrenta retrasos en la toma de decisiones, desabastecimiento o exceso de inventario y poca capacidad para planificar campañas de venta efectivas.
---
## 2. Solución propuesta
Para optimizar la gestión de inventario y análisis de ventas, se propone integrar los datos en una sola **base de datos relacional** y desarrollar un **sistema en Python**, que:

- Lea los datos desde los archivos: `clientes.xlsx`, `productos.xlsx`, `ventas.xlsx` y `detalle_ventas.xlsx`.  
- Permita realizar consultas automáticas sobre ventas, clientes y productos.  
- Genere reportes simples como:  
  - Total de ventas por período.  
  - Productos más vendidos.  
  - Productos con bajo stock para reposición.  
- Centralice la información en un entorno de trabajo unificado (**VS Code**) usando librerías como **pandas** y **openpyxl**.

El objetivo final es que el supermercado automatice la consulta y el control del stock, reduzca errores de registro y disponga de información confiable en tiempo real para la toma de decisiones.
---
## 3. Base de datos representativa
### 3.1 Nombre de la base de datos:
**AurelionDB**

### Tablas principales y relaciones

| Tabla | Descripción | Campos principales |
|--------|--------------|--------------------|
| **clientes** | Contiene los datos de los clientes del supermercado. | id_cliente, nombre, apellido, correo, telefono, direccion |
| **productos** | Registra los artículos disponibles para la venta. | id_producto, nombre_producto, categoria, precio_unitario, stock_actual, stock_optimo |
| **ventas** | Guarda la información general de cada venta. | id_venta, id_cliente, fecha_venta, total_venta |
| **detalle_ventas** | Registra los productos vendidos en cada transacción. | id_detalle, id_venta, id_producto, cantidad, subtotal |

### Relaciones entre tablas
- Un **cliente** puede realizar varias **ventas** → Relación **1 a muchos** (`clientes` → `ventas`)  
- Una **venta** puede incluir varios **productos** → Relación **1 a muchos** (`ventas` → `detalle_ventas`)  
- Un **producto** puede aparecer en varias **ventas** → Relación **1 a muchos** (`productos` → `detalle_ventas`)

**Diagrama relacional (descripción textual):**
```
clientes (1)───< ventas (1)───< detalle_ventas >───(1) productos
```
---
## 4. Estructura, tipos y escala de los datos

### Estructura
- **Modelo:** Relacional (con claves primarias y foráneas).  
- **Tablas:** 4 principales (`clientes`, `productos`, `ventas`, `detalle_ventas`).  
- **Formato actual:** Archivos Excel `.xlsx` integrados en Python con `pandas`.  
- **Formato ideal:** Base de datos SQL (SQLite o MySQL) para futuras ampliaciones.  

### Tipos de datos

| Tipo de dato | Uso en la BD | Ejemplo |
|---------------|--------------|----------|
| **Entero (INT)** | Identificadores y cantidades | id_cliente, id_producto, cantidad |
| **Texto (VARCHAR)** | Nombres, direcciones, categorías | nombre_producto, categoria, direccion |
| **Decimal / Float** | Precios y totales | precio_unitario, subtotal, total_venta |
| **Fecha (DATE)** | Registro temporal de ventas | fecha_venta |
| **Lógico (BOOLEAN)** | Estados activos o inactivos | producto_activo |

### Escala de la base de datos
- **Escala:** Pequeña a mediana.  
- **Volumen esperado:**
  - Entre 50 y 200 productos activos.  
  - Aproximadamente 300 clientes.  
  - Miles de registros de ventas anuales (especialmente en temporadas altas).  
- **Uso previsto:** Consultas analíticas, reportes de ventas, control de stock y análisis de tendencias.

---
## 5. Pseudocódigo del Sistema Aurelion (Versión PSeInt)

El siguiente pseudocódigo corresponde a la versión funcional del sistema de gestión de productos y análisis de ventas desarrollada en **PSeInt**. Esta implementación simula la operación del sistema sin necesidad de conectarse a una base de datos externa. Se mantienen los comentarios principales para comprender la estructura del flujo.

```pseudocode
//---------------------------------------------------------
// PROYECTO: AURELION – Gestión de productos y análisis de ventas
// OBJETIVO: Simular la gestión de productos y automatizar reportes
//---------------------------------------------------------

Proceso Gestion_Aurelion
    // -----------------------------------------------------
    // DECLARACIÓN DE VARIABLES Y ESTRUCTURAS
    // -----------------------------------------------------
    Definir i, opcion, id_cliente, id_producto, cantidad Como Entero
    Definir total_general, total_venta, subtotal Como Real
    Definir producto_mas_vendido Como Cadena

    // Arreglos simulados
    Dimension nombre_producto[5]
    Dimension precio_unitario[5]
    Dimension stock_actual[5]
    Dimension stock_optimo[5]
    Dimension vendidos[5]

    // Clientes simulados
    Dimension clientes[3]
    clientes[1] <- "Juan Pérez"
    clientes[2] <- "Ana Gómez"
    clientes[3] <- "Luis Torres"

    // -----------------------------------------------------
    // CARGA DE DATOS SIMULADOS
    // -----------------------------------------------------
    nombre_producto[1] <- "Arroz Diana 500g"
    nombre_producto[2] <- "Aceite Premier 1L"
    nombre_producto[3] <- "Azúcar Manuelita 1Kg"
    nombre_producto[4] <- "Leche Alquería 900ml"
    nombre_producto[5] <- "Café Sello Rojo 250g"

    precio_unitario[1] <- 3500
    precio_unitario[2] <- 9800
    precio_unitario[3] <- 4200
    precio_unitario[4] <- 4500
    precio_unitario[5] <- 7900

    stock_actual[1] <- 10
    stock_actual[2] <- 8
    stock_actual[3] <- 3
    stock_actual[4] <- 15
    stock_actual[5] <- 2

    stock_optimo[1] <- 10
    stock_optimo[2] <- 10
    stock_optimo[3] <- 8
    stock_optimo[4] <- 12
    stock_optimo[5] <- 5

    Para i <- 1 Hasta 5 Con Paso 1
        vendidos[i] <- 0
    FinPara

    total_general <- 0

    // -----------------------------------------------------
    // INICIO DEL SISTEMA
    // -----------------------------------------------------
    Escribir "=============================================="
    Escribir " SISTEMA DE GESTIÓN DE PRODUCTOS - AURELION"
    Escribir "=============================================="

    Repetir
        Escribir ""
        Escribir "Seleccione una opción:"
        Escribir "1. Verificar estado de stock"
        Escribir "2. Registrar una venta"
        Escribir "3. Generar reporte de productos más vendidos"
        Escribir "4. Mostrar productos con bajo stock"
        Escribir "5. Ver total de ventas acumulado"
        Escribir "6. Salir"
        Leer opcion

        Segun opcion Hacer
            1:
                Escribir "----- ESTADO DE STOCK -----"
                Para i <- 1 Hasta 5 Con Paso 1
                    Si stock_actual[i] < stock_optimo[i] Entonces
                        Escribir "⚠ Producto con stock bajo: ", nombre_producto[i]
                    Sino
                        Escribir "✔ Producto con stock óptimo: ", nombre_producto[i]
                    FinSi
                FinPara

            2:
                Escribir "Ingrese ID del cliente (1 a 3):"
                Leer id_cliente
                Escribir "Ingrese ID del producto (1 a 5):"
                Leer id_producto
                Escribir "Ingrese cantidad vendida:"
                Leer cantidad

                Si cantidad <= stock_actual[id_producto] Entonces
                    subtotal <- precio_unitario[id_producto] * cantidad
                    total_venta <- subtotal
                    total_general <- total_general + total_venta
                    stock_actual[id_producto] <- stock_actual[id_producto] - cantidad
                    vendidos[id_producto] <- vendidos[id_producto] + cantidad
                    Escribir "✅ Venta registrada con éxito."
                    Escribir "Cliente: ", clientes[id_cliente]
                    Escribir "Producto: ", nombre_producto[id_producto]
                    Escribir "Cantidad: ", cantidad
                    Escribir "Total venta: $", total_venta
                Sino
                    Escribir "⚠ No hay suficiente stock disponible para esa venta."
                FinSi

            3:
                Definir max_vendido, pos_max Como Entero
                max_vendido <- 0
                pos_max <- 0
                Para i <- 1 Hasta 5 Con Paso 1
                    Si vendidos[i] > max_vendido Entonces
                        max_vendido <- vendidos[i]
                        pos_max <- i
                    FinSi
                FinPara
                Si pos_max > 0 Entonces
                    producto_mas_vendido <- nombre_producto[pos_max]
                    Escribir "📈 El producto más vendido es: ", producto_mas_vendido, " (", max_vendido, " unidades)"
                Sino
                    Escribir "⚠ No se han registrado ventas aún."
                FinSi

            4:
                Escribir "----- PRODUCTOS CON BAJO STOCK -----"
                Para i <- 1 Hasta 5 Con Paso 1
                    Si stock_actual[i] < stock_optimo[i] Entonces
                        Escribir "- ", nombre_producto[i], " (Stock actual: ", stock_actual[i], ")"
                    FinSi
                FinPara

            5:
                Escribir "💰 Total de ventas acumulado: $", total_general

            6:
                Escribir "Saliendo del sistema... ¡Gracias por usar Aurelion!"

            De Otro Modo:
                Escribir "Opción inválida. Intente nuevamente."
        FinSegun
    Hasta Que opcion = 6
FinProceso
```
---
## 6. Conclusión
La base de datos **AurelionDB** permitirá al supermercado **centralizar toda la información de su operación**, mejorar el **control de inventario** y generar **reportes automáticos** que faciliten la toma de decisiones.  
Su estructura relacional ofrece escalabilidad y compatibilidad con sistemas de análisis más avanzados en el futuro.
