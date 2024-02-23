import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

def plot_love_for_neto():
    # Definir los momentos del día y el nivel de amor correspondiente
    moments_of_day = ['Mañana', 'Tarde', 'Noche']
    love_levels = np.random.randint(0, 100, size=len(moments_of_day))

    # Crear el gráfico de barras
    fig, ax = plt.subplots()
    ax.bar(moments_of_day, love_levels, color='skyblue')
    ax.set_ylabel('Nivel de amor')
    ax.set_title('¿Cuánto quiero a Neto?')

    # Mostrar el gráfico en la aplicación de Streamlit
    st.pyplot(fig)

def main():
    st.title('¡Neto, te quiero mucho!')
    st.write("Esta aplicación muestra cuánto te quiero en diferentes momentos del día.")
    
    plot_love_for_neto()

if __name__ == "__main__":
    main()
