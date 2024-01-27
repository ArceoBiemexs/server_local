import streamlit as st
import pandas as pd

# Datos simulados de vlogs de BMX
data = pd.DataFrame({
    'Fecha': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'Titulo': ['Vlog de BMX #1', 'Vlog de BMX #2', 'Vlog de BMX #3'],
    'Descripcion': [
        'Recorriendo nuevos lugares para practicar BMX.',
        'Trucos y acrobacias en el parque de skate.',
        'Entrevista con un profesional de BMX.'
    ],
    'Video_URL': [
        'https://www.youtube.com/watch?v=video1',
        'https://www.youtube.com/watch?v=video2',
        'https://www.youtube.com/watch?v=video3'
    ]
})

# Aplicación Streamlit
def main():
    st.title("Vlog de BMX")

    # Mostrar la tabla de vlogs
    st.table(data[['Fecha', 'Titulo', 'Descripcion']])

    # Seleccionar un vlog para ver el video
    selected_vlog = st.selectbox("Selecciona un vlog para ver el video:", data['Titulo'])

    # Obtener la URL del video seleccionado
    video_url = data[data['Titulo'] == selected_vlog]['Video_URL'].iloc[0]

    # Mostrar el video embebido
    st.video(video_url)

if __name__ == "__main__":
    main()
