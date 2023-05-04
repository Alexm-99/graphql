# README - Cliente con el cliente de graphql

En este README te explicaré sobre un programa en Python que utiliza un cliente en GraphQL para conectarse a una api de graphql. Para poder ejecutar este programa, necesitarás tener las siguientes dependencias instaladas:

- graphqlclient

## Instalación de dependencias

Para instalar las dependencias, puedes utilizar el administrador de paquetes pip, en python viene la instado por defecto. Si no tienes pip instalado en tu sistema, puedes descargarlo desde [aquí](https://pip.pypa.io/en/stable/installation/).

Una vez que tengas pip instalado, puedes ejecutar los siguientes comandos en tu terminal:

```bash
pip install graphqlclient
```

## Configuración del programa

Confgurada de manera local en el puerto 5000:

```bash
API_URL = 'https://127.0.0.1:5000/graphql'
```

Ahora puedes continuar con el proceso de ejecución.

## Ejecución del programa

Para ejecutar el programa, simplemente ejecuta el archivo index.py desde tu terminal:

`python client.py`

El programa se conectará a la API en GraphQL y ejecutará una consulta realizada en el mismo. Si necesitas consultar otro dato es necesario hacer la respectivo cambio en el Query.
