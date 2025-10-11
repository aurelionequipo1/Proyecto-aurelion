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
## 5. Conclusión
La base de datos **AurelionDB** permitirá al supermercado **centralizar toda la información de su operación**, mejorar el **control de inventario** y generar **reportes automáticos** que faciliten la toma de decisiones.  
Su estructura relacional ofrece escalabilidad y compatibilidad con sistemas de análisis más avanzados en el futuro.
