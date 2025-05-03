# Documentación del Proyecto: SGFood

## Descripción General
El proyecto **SGFood** implementa un modelo de datos para un sistema de análisis de ventas y compras, utilizando un esquema de Data Warehouse basado en tablas de hechos y dimensiones. Este modelo permite realizar análisis detallados de las operaciones comerciales, integrándose con herramientas como **SQL Server Analysis Services (SSAS)**, **SQL Server Reporting Services (SSRS)** y **Power BI**.

---

## Estructura del Modelo de Datos

### Modelo de Constelación de Tablas
El modelo de datos sigue un esquema de constelación de hechos, donde las tablas de hechos (`Hechos_Ventas` y `Hechos_Compras`) están relacionadas con múltiples tablas de dimensiones. Esto permite realizar análisis desde diferentes perspectivas.

#### **Diagrama del Modelo**
![Modelo de Constelación](Documentacion/img/constelacion.png)

#### **Descripción del Modelo**
1. **Tablas de Dimensiones**:
   - **Dim_Cliente**: Información sobre los clientes.
   - **Dim_Proveedor**: Información sobre los proveedores.
   - **Dim_Producto**: Información sobre los productos.
   - **Dim_Sucursal**: Información sobre las sucursales.
   - **Dim_Fecha**: Información temporal para análisis por fechas.
   - **Dim_Vendedor**: Información sobre los vendedores.

2. **Tablas de Hechos**:
   - **Hechos_Ventas**: Contiene datos transaccionales de ventas.
   - **Hechos_Compras**: Contiene datos transaccionales de compras.

3. **Relaciones**:
   - Cada tabla de hechos está relacionada con las dimensiones mediante claves foráneas (`id_cliente`, `id_producto`, `id_fecha`, etc.).
   - Esto permite realizar análisis multidimensionales, como ventas por región, compras por proveedor, etc.

---

## Tablas de Dimensiones

### **Dim_Cliente**
- **Descripción**: Contiene información sobre los clientes.
- **Columnas**:
  - `id_cliente` (PK): Identificador único del cliente.
  - `nombre_cliente`: Nombre del cliente.
  - `tipo_cliente`: Tipo de cliente (por ejemplo, "Regular", "VIP").
  - `direccion_cliente`: Dirección del cliente.
  - `numero_cliente`: Número de contacto del cliente.
  - `vacacionista`: Indicador de si el cliente está de vacaciones (`0` o `1`).

### **Dim_Proveedor**
- **Descripción**: Contiene información sobre los proveedores.
- **Columnas**:
  - `id_proveedor` (PK): Identificador único del proveedor.
  - `nombre_proveedor`: Nombre del proveedor.
  - `direccion_proveedor`: Dirección del proveedor.
  - `numero_proveedor`: Número de contacto del proveedor.
  - `web_proveedor`: Sitio web del proveedor.

### **Dim_Producto**
- **Descripción**: Contiene información sobre los productos.
- **Columnas**:
  - `id_producto` (PK): Identificador único del producto.
  - `nombre_producto`: Nombre del producto.
  - `marca_producto`: Marca del producto.
  - `categoria_producto`: Categoría del producto.

### **Dim_Sucursal**
- **Descripción**: Contiene información sobre las sucursales.
- **Columnas**:
  - `id_sucursal` (PK): Identificador único de la sucursal.
  - `nombre_sucursal`: Nombre de la sucursal.
  - `direccion_sucursal`: Dirección de la sucursal.
  - `region`: Región donde se encuentra la sucursal.
  - `departamento`: Departamento donde se encuentra la sucursal.

### **Dim_Fecha**
- **Descripción**: Contiene información sobre las fechas.
- **Columnas**:
  - `id_fecha` (PK): Identificador único de la fecha.
  - `fecha`: Fecha completa.
  - `dia`: Día del mes.
  - `mes`: Mes del año.
  - `trimestre`: Trimestre del año.
  - `año`: Año.

### **Dim_Vendedor**
- **Descripción**: Contiene información sobre los vendedores.
- **Columnas**:
  - `id_vendedor` (PK): Identificador único del vendedor.
  - `nombre_vendedor`: Nombre del vendedor.
  - `vacacionista`: Indicador de si el vendedor está de vacaciones (`0` o `1`).

---

## Tablas de Hechos

### **Hechos_Ventas**
- **Descripción**: Contiene información sobre las ventas realizadas.
- **Columnas**:
  - `id_factura` (PK): Identificador único de la factura.
  - `id_fecha` (FK): Fecha de la venta.
  - `id_cliente` (FK): Cliente que realizó la compra.
  - `id_producto` (FK): Producto vendido.
  - `id_sucursal` (FK): Sucursal donde se realizó la venta.
  - `unidades`: Cantidad de unidades vendidas.
  - `precio_unitario`: Precio por unidad.
  - `id_vendedor` (FK): Vendedor que realizó la venta.

### **Hechos_Compras**
- **Descripción**: Contiene información sobre las compras realizadas.
- **Columnas**:
  - `id_factura` (PK): Identificador único de la factura.
  - `id_fecha` (FK): Fecha de la compra.
  - `id_proveedor` (FK): Proveedor que realizó la venta.
  - `id_producto` (FK): Producto comprado.
  - `id_sucursal` (FK): Sucursal donde se recibió la compra.
  - `unidades`: Cantidad de unidades compradas.
  - `costo_unitario`: Costo por unidad.

---

## Índices
Se han creado índices para optimizar las consultas en las tablas de hechos:

### Índices en `Hechos_Ventas`
- `idx_fecha_ventas`: Índice en la columna `id_fecha`.
- `idx_cliente_ventas`: Índice en la columna `id_cliente`.
- `idx_producto_ventas`: Índice en la columna `id_producto`.
- `idx_sucursal_ventas`: Índice en la columna `id_sucursal`.
- `idx_vendedor_ventas`: Índice en la columna `id_vendedor`.

### Índices en `Hechos_Compras`
- `idx_fecha_compras`: Índice en la columna `id_fecha`.
- `idx_proveedor_compras`: Índice en la columna `id_proveedor`.
- `idx_producto_compras`: Índice en la columna `id_producto`.
- `idx_sucursal_compras`: Índice en la columna `id_sucursal`.

---

## Conclusión
El modelo de datos de **SGFood** permite realizar análisis detallados de las operaciones comerciales, integrándose con herramientas de BI para generar reportes y dashboards interactivos. Este diseño optimiza el rendimiento y facilita la toma de decisiones basada en datos.