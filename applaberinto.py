import streamlit as st
from maze_solver import MAZE, START, END, solve_maze_bfs

st.title("Visualizador de Algoritmo de Búsqueda en Laberinto")

def render_maze(maze, path=None):
    if path is None:
        path = []
    
    display_maze = []
    for r_idx, row in enumerate(maze):
        display_row = []
        for c_idx, col in enumerate(row):
            if (r_idx, c_idx) == START:
                display_row.append("🚀")  # Inicio
            elif (r_idx, c_idx) == END:
                display_row.append("🏁")  # Fin
            elif (r_idx, c_idx) in path:
                display_row.append("🔹")  # Camino
            elif col == 1:
                display_row.append("⬛")  # Muro
            else:
                display_row.append("⬜")  # Libre
        display_maze.append("".join(display_row))
    
    st.markdown("<br>".join(display_maze), unsafe_allow_html=True)


st.sidebar.header("Opciones")
algorithm = st.sidebar.selectbox("Selecciona el algoritmo", ["BFS"])
solve_button = st.sidebar.button("Resolver Laberinto")

render_maze(MAZE)

if solve_button:
    if algorithm == "BFS":
        path, casillas = solve_maze_bfs(MAZE, START, END)

        if path:
            st.success(f"¡Camino encontrado con BFS! Casillas usadas: {casillas}")
            render_maze(MAZE, path)
        else:
            st.error("No se encontró un camino.")
