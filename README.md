<p align=center><img src=https://d31uz8lwfmyn8g.cloudfront.net/Assets/logo-henry-white-lg.png><p>

# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

Alumna: María Celia Pérez Schmit

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>

## Contexto

El ciclo de vida de un proyecto de Machine Learning debe contemplar desde el tratamiento y recolección de los datos (Data Engineer) hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.

Empecé a trabajar como Data Scientist en una start-up que provee servicios de agregación de plataformas de streaming. Cree un sistema de recomendación de ML para solucionar un problema del del negocio.

Como los datos están sin transformar, se realiza un rápido trabajo de Data Engineer para tener un MVP (Minimum Viable Product).

<br/>

## **ETAPAS DEL PROCESO**

## Proceso de ETL

El proyecto consiste en realizar una ingesta de datos, posteriormente realizar un ETL, y luego disponibilizar los datos limpios para su consulta a través de una API construida en un entorno virtual.

+ Se generó el campo **`id`**: Cada id se compuso de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **`as123`**)

+ Los valores nulos del campo rating se reemplazaron por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”

+ Las fechas se conviertieron a formato **`AAAA-mm-dd`**

+ Los campos de texto se pasaron a **minúsculas**

+ El campo ***duration*** se convirtió en dos campos: **`duration_int`** y **`duration_type`**. El primero se transformó en integer y el segundo a string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

<br/>

## Desarrollo de la API    

Consideraciones a tener en cuenta para el correcto funcionamiento de la API::

* Pegar el código correspondiente a cada query a continuación de esta URL.
* Modificar el valor del parámetro introduciendo valores válidos que se encuentren en el Dataset.
* Respetar siempre la ubicación que cada parámetro como se provee en el código.
* No modificar el primer bloque de texto que está entre barras /get_.../

ej: La API le devolverá la cantidad de veces que la palabra amazing está en la plataforma amazon si pega el código

/get_count_platform/amazon  


Las consultas propuestas son las siguientes:

:small_blue_diamond: Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función se llama: get_max_duration(year, platform, duration_type))

Ej: https://space-1-s2382403.deta.app/get_max_duration/2018/amazon/min

:small_blue_diamond: Cantidad de películas por PLATAFORMA con un PUNTAJE mayor a XX en determinado AÑO (la función se llama: get_score_count(platform, scored, year))

Ej: https://space-1-s2382403.deta.app/get_score_count/hulu/3/2019

:small_blue_diamond: Cantidad de películas por PLATAFORMA. (La función se llama get_count_platform(platform))

Ej: https://space-1-s2382403.deta.app/get_count_platform/disney

:small_blue_diamond: Actor que más se repite según PLATAFORMA y AÑO. (La función se llama: get_actor(platform, year))

Ej: https://space-1-s2382403.deta.app/get_actor/netflix/2014

:purple_circle: API: https://space-1-s2382403.deta.app/docs#/

<br/>

## Proceso de EDA: _(Exploratory Data Analysis)_

Con los datos ya limpios, se investigó las relaciones que hay entre las variables de los datasets, outliers y si hay algún patrón interesante que valga la pena explorar en un análisis posterior.  

<br/>

## Sistema de Recomendación  

Una vez que toda la data es consumible por la API se los disponibiliza a los departamentos de Analytics y de Machine Learning. 

Se generó un un sistema de recomendación de películas para usuarios (se utilizó el algoritmo SVD para hacer el entrenamiento), donde dado un id de usuario y una película, nos dice si la recomienda o no para dicho usuario. 

El sistema de recomendación fue deployado en Gradio (interfaz gráfica) para ser utilizada
 


