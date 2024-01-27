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

# Aplicación Streamlit con mejoras visuales
def main():
    st.title("Punto de Venta - Carnitas de Cerdo")
    st.image("tu_logo.png", width=200)  # Añade tu logo

    # Colores personalizados
    st.markdown(
        """
        <style>
            .big-font {
                font-size: 24px !important;
            }
            .highlight {
                background-color: #f5f5f5;
                padding: 10px;
                border-radius: 5px;
            }
            .button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 20px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 5px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Mostrar la tabla de ventas con colores
    st.table(data.style.applymap(lambda x: 'background-color: #aaffaa', subset=['Total']))

    # Resumen de ventas
    total_ventas = data['Total'].sum()
    st.markdown(f"<p class='big-font highlight'>Total de Ventas: ${total_ventas:.2f}</p>", unsafe_allow_html=True)

    # Seleccionar un producto para ver detalles
    selected_producto = st.selectbox("Selecciona un producto para ver detalles:", data['Producto'])

    # Obtener detalles del producto seleccionado
    producto_details = data[data['Producto'] == selected_producto]

    # Mostrar detalles del producto
    st.write(f"**Detalles de {selected_producto}:**")
    st.write(producto_details)

    # Botón de recarga manual (puedes hacerlo más interactivo)
    if st.button("Recargar página"):
        st.experimental_rerun()

if __name__ == "__main__":
    main()
