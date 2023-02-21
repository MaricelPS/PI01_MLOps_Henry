from fastapi import FastAPI , File , UploadFile
from fastapi.responses import HTMLResponse, StreamingResponse
import pandas as pd

app = FastAPI(title = 'Consultas Proyecto O1 - MLOps',
description= 'API para realizar consultas sobre plataformas: Amanzon. Disney, Hulu, Netflix')

url = 'https://drive.google.com/uc?id=1Du_gvJUXktgUGZTi7dF7CHyR-R7H_U8m'
df = pd.read_csv(url)


@app.get("/")  
def index():
    consideraciones = """
Para el correcto funcionamiento de la API se debe considerar los siguiente:
* Pegar el código correspondiente a cada query a continuación de esta URL.
* Modificar el valor del parámetro introduciendo valores válidos que se encuentren en el Dataset.
* Respetar siempre la ubicación de cada parámetro como se provee en el código.
* Nunca modifique el primer bloque de texto que está entre barras /get_.../


CODIGOS PARA LAS QUERIES

Query 1 -- > Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.

/get_max_duration/year/platform/duration_type
Ej: /get_max_duration/2016/amazon/min

Query 2 --> Cantidad de películas por PLATAFORMA con un PUNTAJE mayor a XX en determinado AÑO.

/get_score_count/platform/score/year
Ej: /get_score_count/disney/3.5/2018

Query 3 --> Cantidad de películas por PLATAFORMA.

/get_count_platform/platform
Ej: /get_count_platform/hulu

Query 4 --> Actor que más se repite según PLATAFORMA y AÑO.

/get_actor/platform/year

Ej: /get_actor/disney/2019

"""
    return  print(consideraciones)

# CODIGOS DE LAS QUERIES

# Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN.

@app.get('/get_max_duration/{year}/{platform}/{duration_type}')
async def get_max_duration(year:int , platform:str, duration_type:str):
    q1 = df[(df['plataforma'] == platform) & (df['release_year'] == year) & (df['duration_type'] == duration_type)].sort_values(by = 'duration_int' , ascending = False).iloc[0,3]
    
    return  f' La pelicula con mayor duración de la plataforma {platform}, del año {year} es: {q1}.'

# Cantidad de películas por PLATAFORMA con un PUNTAJE mayor a XX en determinado AÑO.

@app.get('/get_score_count/{platform}/{score}/{year}') 
async def get_score_count(platform:str, score:int, year:int):
    q2 = df[(df['plataforma'] == platform) & (df['score'] > score) & (df['release_year'] == year)].shape[0]
    
    return  f' La cantidad de peliculas con mayor puntaje ({score}) de la plataforma {platform} en el año {year} es: {q2}.'

# Cantidad de películas por PLATAFORMA.

@app.get('/get_count_platform/{platform}')
async def get_count_platform(platform:str):
    q3 = df[(df['plataforma'] == platform) & (df['type'] == 'movie') ].shape[0]
    
    return  f' La cantidad total de peliculas por la plataforma ({platform}) es: {q3}.'

# Actor que más se repite según PLATAFORMA y AÑO.
@app.get('/get_actor/{platform}/{year}') 
async def get_max_duration(platform:str, year:int):
    q4_aux1 = df[(df['plataforma'] == platform) & (df['release_year'] == year)]
    q4_aux2 = q4_aux1.assign(actor=q4_aux1.cast.str.split(',')).explode('cast')
    q4_aux3 = q4_aux2.cast.value_counts()
    
    max_actor = q4_aux3.index[0]
    max_count = int(q4_aux3.iloc[0])
    q4 = dict({'actor/actriz': max_actor, 'vez/veces que aparece': max_count})

    return  f'Se repite mas El/la {q4}'