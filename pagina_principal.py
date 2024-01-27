import streamlit as st
import pandas as pd

# Datos simulados de ventas de carnitas
data = pd.DataFrame({
    'Fecha': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'Producto': ['Carnitas de cerdo', 'Tacos de carnitas', 'Orden de carnitas'],
    'Cantidad': [20, 35, 15],
    'Precio_Unitario': [10.50, 2.50, 8.00],
    'Total': [210.00, 87.50, 120.00]
})

# Aplicación Streamlit
def main():
    st.title("Punto de Venta - Carnitas de Cerdo")

    # Mostrar la tabla de ventas
    st.table(data[['Fecha', 'Producto', 'Cantidad', 'Precio_Unitario', 'Total']])

    # Resumen de ventas
    total_ventas = data['Total'].sum()
    st.write(f"**Total de Ventas:** ${total_ventas:.2f}")

    # Seleccionar un producto para ver detalles
    selected_producto = st.selectbox("Selecciona un producto para ver detalles:", data['Producto'])

    # Obtener detalles del producto seleccionado
    producto_details = data[data['Producto'] == selected_producto]

    # Mostrar detalles del producto
    st.write(f"**Detalles de {selected_producto}:**")
    st.write(producto_details)

if __name__ == "__main__":
    main()
