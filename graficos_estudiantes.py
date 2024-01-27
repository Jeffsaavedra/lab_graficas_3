import pandas as pd
import plotly.express as px

# Cargar el dataset
data = {
    'id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    'materia': ['Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje', 'Matemáticas', 'Historia', 'Ciencias', 'Lenguaje'],
    'nota': [80, 65, 90, 75, 95, 70, 85, 60, 78, 82, 93, 68, 73, 88, 77, 50, 92, 63, 85, 79],
    'aprobado': ['Aprobado', 'No Aprobado', 'Aprobado', 'Aprobado', 'Aprobado', 'Aprobado', 'Aprobado', 'No Aprobado', 'Aprobado', 'Aprobado', 'Aprobado', 'Aprobado', 'Aprobado', 'Aprobado', 'Aprobado', 'No Aprobado', 'Aprobado', 'No Aprobado', 'Aprobado', 'Aprobado']
}

df = pd.DataFrame(data)

# Definir colores por materia
colores_materias = {'Matemáticas': 'blue', 'Historia': 'red', 'Ciencias': 'green', 'Lenguaje': 'purple'}

# Graficar la distribución de notas con un boxplot
fig_boxplot = px.box(df, x='materia', y='nota', title="Distribución de Notas",
                     labels={'nota': 'Nota', 'materia': 'Materia'},
                     color='materia', color_discrete_map=colores_materias, range_y=[50, 90])

# Agregar etiquetas al eje y
fig_boxplot.update_yaxes(title_text="Nota")

# Agregar cuadritos de leyenda en la parte externa derecha del gráfico
for materia, color in colores_materias.items():
    fig_boxplot.add_shape(type='rect',
                         x0=1.1, x1=1.15,
                         y0=1 - list(colores_materias.values()).index(color) * 0.1,
                         y1=1 - list(colores_materias.values()).index(color) * 0.1 + 0.05,
                         fillcolor=color, line=dict(width=0))

# Guardar el gráfico de boxplot sin outliers en un archivo HTML
fig_boxplot.write_html("boxplot_notas_colores_cuadritos.html")

# Graficar la distribución de aprobados con un pie chart
fig_piechart = px.pie(df, names='aprobado', title="Proporción de Estudiantes Aprobados/No Aprobados")

# Agregar etiquetas al pie chart
fig_piechart.update_traces(textinfo='percent+label')

# Agregar etiquetas y título al pie chart
fig_piechart.update_layout(
    xaxis_title='Categoría',
    yaxis_title='Porcentaje',
    legend_title_text='Estado'
)

# Guardar el gráfico de pie chart en un archivo HTML
fig_piechart.write_html("piechart_aprobados.html")