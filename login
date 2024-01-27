import streamlit as st
import pandas as pd
import hashlib

# Datos simulados de usuarios
usuarios = {
    'usuario1': {'contrasena': 'hashed_password1'},
    'usuario2': {'contrasena': 'hashed_password2'},
    # Agrega más usuarios según sea necesario
}

# Función para verificar las credenciales del usuario
def authenticate(username, password):
    if username in usuarios and hashlib.sha256(password.encode()).hexdigest() == usuarios[username]['contrasena']:
        return True
    return False

# Aplicación Streamlit con login y mejoras visuales
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

    # Añadir sección de login
    st.subheader("Login")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")

    if st.button("Iniciar Sesión"):
        if authenticate(username, password):
            st.success(f"Bienvenido, {username}!")
            show_data()
        else:
            st.error("Credenciales incorrectas. Por favor, inténtalo de nuevo.")

def show_data():
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
