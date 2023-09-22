## FUNCIONES A UTILIZAR EN app.py

#IMPORTAMOS LIBRERÍAS 
from fastapi import FastAPI
import pandas as pd
import numpy as np
import pyarrow as pa
import fastparquet as fp
from textblob import TextBlob
from fastapi.responses import HTMLResponse

#INSTANCIAMOS LA API 
app = FastAPI()

#DATAFRAME  
df_playtime_forever = pd.read_parquet("df_playtime_forever.parquet")



def presentacion():
    """"
    <DOCTYPE html>
    <html>
    <head>
        <title>Mi Página Web en FastAPI</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f0f0f0;
                margin: 0;
                padding: 0;
            }
            .container {
                max-width: 800 px;
                margin: 0 auto;
                padding: 20 px;
                background-color: #fff;
                box-shadow: 0 0 10 px rgba(0, 0, 0, 0.1);
                border-radius: 5 px;
    }

            h1 {
                color: #333;
                font-size: 24 px;
                margin-bottom: 10 px;
            }
            p {
                color: #666;
                font-size: 16 px;
                line-height: 1.5;
            }
            .highlight {
                color: #007bff;
                font-weight: bold;
            }
            .author {
                margin-top: 20 px;
                font-size: 14 px;
                color: #888;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Bienvenido a mi entorno FastAPI</h1>
            <p>Estás a punto de descubrir una serie de herramientas que te permitirán acceder a valiosa información sobre la plataforma de juegos Steam.</p>
            <p>Para explorar estas herramientas, simplemente agrega <span class="highlight">"/docs"</span> al final de la URL actual. Por ejemplo, visita <span class="highlight">www.suURL.com/docs</span>.</p>
            <p>De esta manera, tendrás acceso a todas las funcionalidades y podrás aprender cómo utilizarlas de manera efectiva.</p>
            <p>Esperamos que disfrutes explorando!</p>
            <div class="author">
                <p>Autor: María García R.</p>
                <p>Año: 2023</p>
            </div>
        </div>
    </body>
    </html>
    """

        
#FUNCIÓN 1    
@app.get("/countreviews/{inicio}/{fin}", name = "COUNTREVIEWS")
async def count_reviews(Start, End):
    '''
    Calcula la cantidad de usuarios que realizaron reviews entre las fechas dadas y 
    el porcentaje de recomendacion de esos usuarios.
    
    Argumentos:
    inicio (str): Fecha de inicio del periodo a evaluar.
    fin (str): Fecha de fin del periodo a evaluar
    '''
    # Start = pd.to_datetime(Start)
    # End = pd.to_datetime(End) 
    
    reviews_entre_fechas = df_countreviews[df_countreviews['posted'].between(Start, End)]
    
    cantidad_usuarios = reviews_entre_fechas['user_id'].nunique()
    
    porcentaje_recomendacion = (reviews_entre_fechas['recommend'].sum() / len(reviews_entre_fechas)) * 100
    
    return {'Cantidad de usuarios:': cantidad_usuarios,
            'Porcentaje de recomendación:': round(porcentaje_recomendacion, 2)
    }

    
#FUNCION 2
@app.get("/genre/{genero}", name = "GENRE")
async def genre(genero):
    # Busca el ranking para el género de interés
    rank = df_posicion[df_posicion['genres'] == genero]['ranking'].iloc[0]
    return {
        'rank': rank
    }
    


#FUNCIÓN 3
@app.get("/userforgenre/{genre}", name = "USERFORGENRE")
async def userforgenre(genero):
    # Filtra el DataFrame principal (df_playtime_forever) para obtener datos relacionados con el género especificado.
    data_por_genero = df_playtime_forever[df_playtime_forever['genres'] == genero]
    
    # Agrupa los datos filtrados por usuario y suma las horas de juego para cada uno.
    top_users = data_por_genero.groupby(['user_url', 'user_id'])['playtime_horas'].sum().nlargest(5).reset_index()
    
    # Crea un diccionario para almacenar la información de los mejores usuarios.
    top_users_dict = {}
    
    # Itera a través de los datos de los mejores usuarios y los agrega al diccionario.
    for index, row in top_users.iterrows():
        user_info = {
            'user_id': row['user_id'],
            'user_url': row['user_url']
        }
        top_users_dict[index + 1] = user_info
    
    # Devuelve el diccionario de los mejores usuarios.
    return top_users_dict



#FUNCIÓN 4
@app.get("/developer/{desarrollador}", name="DEVELOPER")
async def developer(desarrollador):
    '''
    Devuelve la cantidad de elementos y el porcentaje de contenido gratuito por año según la empresa desarrolladora.

    Argumento:
    desarrollador (str): El desarrollador del juego (elemento) para el cual se desean obtener los valores mencionados. 
    '''
    
    # Filtrar el DataFrame por el desarrollador especificado
    developer_df = df_ITGA[df_ITGA['developer'] == desarrollador]
    
    # Crear un DataFrame para elementos gratuitos
    elementos_gratuitos = developer_df[developer_df['price'] == 0]
    
    # Agrupar y contar elementos totales por año
    elementos_totales_por_anio = developer_df.groupby(developer_df['release_date'].dt.year)['item_id'].nunique()
    
    # Agrupar y contar elementos gratuitos por año
    elementos_gratuitos_por_anio = elementos_gratuitos.groupby(elementos_gratuitos['release_date'].dt.year)['item_id'].nunique()
    
    # Calcular el porcentaje de contenido gratuito por año
    porcentaje_gratuito_por_anio = (elementos_gratuitos_por_anio / elementos_totales_por_anio) * 100
    
    # Crear un DataFrame con los resultados
    resultados = pd.DataFrame({
        'Año': elementos_totales_por_anio.index,
        'Cantidad de Elementos': elementos_totales_por_anio.values,
        'Porcentaje Gratuito': porcentaje_gratuito_por_anio.values
    })
    
    # Devolver los resultados como una lista de registros (diccionarios)
    return resultados.to_dict(orient='records')








