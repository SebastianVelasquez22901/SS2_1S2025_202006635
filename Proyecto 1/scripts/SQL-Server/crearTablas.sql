CREATE DATABASE Pivote;
GO
USE Pivote;
GO
CREATE TABLE Compras_Temp (
    Fecha VARCHAR(50),
    CodProveedor VARCHAR(50),
    NombreProveedor VARCHAR(255),
    DireccionProveedor VARCHAR(500),
    NumeroProveedor VARCHAR(20),
    WebProveedor VARCHAR(255),
    CodProducto VARCHAR(50),
    NombreProducto VARCHAR(255),
    MarcaProducto VARCHAR(50),
    Categoria VARCHAR(50),
    SodSucursal VARCHAR(50),
    NombreSucursal VARCHAR(255),
    DireccionSucursal VARCHAR(500),
    Region VARCHAR(50),
    Departamento VARCHAR(50),
    Unidades VARCHAR(50),
    CostoU VARCHAR(50)
);
GO
CREATE TABLE Ventas_Temp (
    Fecha VARCHAR(50),
    CodigoCliente VARCHAR(50),
    NombreCliente VARCHAR(255),
    TipoCliente VARCHAR(50),
    DireccionCliente VARCHAR(500),
    NumeroCliente VARCHAR(20),
    CodVendedor VARCHAR(50),
    NombreVendedor VARCHAR(255),
    Vacacionista VARCHAR(5),
    CodProducto VARCHAR(50),
    NombreProducto VARCHAR(255),
    MarcaProducto VARCHAR(50),
    Categoria VARCHAR(50),
    SodSucursal VARCHAR(50),
    NombreSucursal VARCHAR(500),
    DireccionSucursal VARCHAR(500),
    Region VARCHAR(50),
    Departamento VARCHAR(50),
    Unidades VARCHAR(50),
    PrecioUnitario VARCHAR(50)
);
GO