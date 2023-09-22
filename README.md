# **Proyecto Individual 1** 
## **Machine Learning Operations (MLOps) en Steam**

### Introducción
El objetivo principal de este proyecto es crear un Producto Mínimo Viable (MVP) que incluye una API en la nube y un modelo de Machine Learning. 

Se utilizaron conjuntos de datos que contienen opiniones de usuarios de juegos, detalles sobre juegos en Steam y datos de usuarios.

Una de las funciones clave es un modelo de análisis de sentimientos para evaluar opiniones de usuarios. También se desarrollaron otras funciones, que se describen más adelante.

Se implementó un sistema de recomendación de juegos basado en la similitud entre géneros.

En resumen, este proyecto busca mejorar la experiencia de los usuarios de Steam mediante ciencia de datos y Machine Learning.

### Contexto
Steam es una plataforma líder en la industria de los videojuegos que ofrece una amplia variedad de juegos para PC y otras plataformas. Desarrollada por Valve Corporation, Steam se destaca por su sólida infraestructura de actualización y gestión de juegos, así como por su plataforma de desarrollo de juegos Steamworks. Steam ha sido un pionero en la distribución digital de videojuegos y ha influido en la evolución de la industria de los videojuegos en línea.

### Conjuntos de Datos
El proyecto se basa en tres conjuntos de datos de Steam:

1. steam_games: Contiene información sobre juegos disponibles en Steam, como nombre, género, fecha de lanzamiento y más.

2. user_reviews: Contiene reseñas de usuarios sobre juegos en Steam.

3. user_items: Contiene información sobre la actividad de los usuarios en Steam.

### Desarrollo del Proyecto

1. Ingesta de Datos: Se cargan los conjuntos de datos mencionados anteriormente para su procesamiento.

2. Tratamiento de Datos (ETL): Los datos se limpian y transforman para que sean adecuados para su análisis.

3. Ingeniería de Características: Se desarrolla un modelo de análisis de sentimientos para las reseñas de los usuarios, utilizando la librería TextBlob para determinar si las opiniones son positivas, negativas o neutrales.

4. Funciones y Disponibilidad de Datos: Se crean seis funciones para proporcionar información relevante, como gastos de usuario, cantidad de reseñas, género en el ranking, usuarios principales por género, productos de desarrolladores y análisis de sentimientos.

5. Análisis Exploratorio de Datos (EDA): Se realiza un análisis exploratorio de los datos para comprender patrones y relaciones antes de construir el modelo de recomendación.

6. Modelado (Desarrollo de Modelo de Machine Learning): Se desarrolla un modelo de recomendación de juegos basado en la similitud de géneros.

### Implementación (Deployment)
La API se despliega en la nube utilizando la plataforma Render. Render permite alojar y servir la API para que los usuarios puedan acceder a ella desde un navegador web.

### Conclusiones
Este proyecto ha sido una oportunidad para aplicar los conocimientos adquiridos en el curso de Data Science en la academia Henry. Se ha abordado una variedad de tareas relacionadas con la ingeniería de datos y el desarrollo de modelos de Machine Learning.

Aunque se han logrado avances significativos, se reconoce que el sistema de recomendación tiene margen para mejoras futuras. La automatización de procesos, la incorporación de más fuentes de datos y la implementación de algoritmos de Machine Learning más avanzados son pasos que podrían perfeccionar aún más el sistema. 

Este proyecto ha sido un viaje de aprendizaje y desafío, enfrentando desafíos del mundo real, desde la calidad de los datos hasta la necesidad de desarrollar un MVP de manera eficiente. Se ha aprendido la importancia de la limpieza y estructuración de datos, la selección adecuada de algoritmos de recomendación y el equilibrio entre velocidad y calidad en la implementación de un MVP.