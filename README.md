# Recomendaciones-usuarios-spotify
El objetivo de este trabajo práctico es el de modelar un sistema de recomendación sobre un sistema de streaming de música: las canciones, playlists y usuarios.  Nos interesa modelar y entender cómo están compuestas las playlists, si un usuario y otro son similares, poder recomendar canciones o playlists enteras.

Trabajaremos con una ínfima porción de datos obtenidos de una competencia pública realizada por la plataforma Spotify en 2018. Cuenta con cerca de 2 millones de entradas. Pueden encontrar el archivo ya procesado aquí.

Para la modelación, se recomienda el siguiente esquema:

Tener un grafo no dirigido que relacione si a un usuario le gusta una canción (supongamos que a un usuario le gusta una canción si armó una playlist con ella). Esto formará un grafo bipartito en el cual en un grupo estarán los usuarios, y en el otro las canciones.
Tener un grafo no dirigido relacionando canciones si aparecen en una misma playlist (al menos una playlist lista a ambas canciones).
