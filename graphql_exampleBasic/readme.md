# README - Ejemplo básico

En este README te explicaré sobre un programa en Python que utiliza una API en GraphQL para obtener una cadena de texto a traves de un Query y hacer una mutación. Para poder ejecutar este programa, necesitarás tener las siguientes dependencias instaladas:

- Flask
- flask-graphql
- graphene

## Instalación de dependencias

Para instalar las dependencias, puedes utilizar el administrador de paquetes pip, en python viene la instado por defecto. Si no tienes pip instalado en tu sistema, puedes descargarlo desde [aquí](https://pip.pypa.io/en/stable/installation/).

Una vez que tengas pip instalado, puedes ejecutar los siguientes comandos en tu terminal:

```bash
pip install flask flask-graphql graphene
```

## Configuración del programa

Confgurada de manera local en el puerto 5000:

```bash
API_URL = 'https://127.0.0.1:5000/graphql'
```

## Ejecución del programa

Para ejecutar el programa, simplemente ejecuta el archivo index.py desde tu terminal:

`python index.py`

El programa se conectará a la API en GraphQL y levantará un servidor para realizar una serie de consultas y mutaciones.
