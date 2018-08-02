<img width="320" src="https://images.britcdn.com/wp-content/uploads/2015/03/amazon-dash-button-2.png" align="right" />

# Amazon Dash Hacks y Utilidades

## Introducción

En este repositorio se encuentran algunos Hacks y utilidades desarrolladas para el Dash Button de Amazon versión **JK29LP**. La idea principal
de Amazon con este botón es facilitar todavía más el proceso de compra en su tienda. Solo tienes que pulsar una vez un botón,
y el producto llegará a tu casa al día siguiente (siempre y cuando seas usuario del famoso Amazon Prime).

Sin embargo, la misma idea de acelerar el proceso de compra con el botón puede aplicarse a otros procesos. La idea es *hackear* el
Dash Button para que haga lo que se requiera con solo pulsar el botón.

## Instalación de requisitos

Previamente es necesario instalar una serie de utilidades y módulos de Python. Para ello, introduciremos los siguientes
comandos en la terminal de nuestro *Linux*.

`sudo apt-get update && sudo apt-get upgrade`

`sudo apt-get install python-pip`

`sudo pip install pydhcplib`

## Configuración inicial

### Dirección MAC del Dash Button
Para la configuración inicial del dispositivo es necesario conocer la dirección MAC del Dash. Para ello seguiremos los siguientes pasos:
1. Pulsa el botón durante 6 segundos hasta que la luz del mismo se ponga **azul**, en ese momento el Dash se encontrará en modo de configuración.
2. Con un dispositivo que disponga de conexión Wi-fi, realiza un escaneo de las redes disponibles. Una nueva red con el SSID (el nombre de la red
  Wi-fi) 'Amazon ConfigureMe' ha debido aparecer.
3. Conecta tu dispositivo a esta nueva red Wi-fi, abre tu navegador y entra en [http://192.168.0.1](http://192.168.0.1). Verás la siguiente información.

<img width="600" src="https://cdn-images-1.medium.com/max/800/1*wdPTqesE6QpJVUgZZY9gEA.png" align="center" />

No olvides apuntar en algún lugar la dirección MAC de tu dispositivo.

### Configuración en la app de Amazon
Una vez conocida la dirección MAC podemos proceder a conectar el Dash button a la red Wi-fi que queramos. Para ello seguiremos estos pasos:
1. Descargar la aplicación de Amazon de la tienda oficial en nuestro dispositivo móvil.
2. Ir a Mi Cuenta > Dash Button y Dispositivos
3. Configura el Dash Button y conectalo a la misma red Wi-fi de tu dispositivo.
4. Cierra la App en el momento en que te salga la lista de productos para comprar. **NO SELECCIONES NINGÚN PRODUCTO DE LA LISTA**.De esta manera, el botón
no pedirá un artículo cuando lo pulsemos y no llenaremos la casa de trastos pedidos por accidente.

## Referencias

- [Cómo conocer la dirección MAC del Dash Button](https://medium.com/@bahman./hack-the-amazon-dash-button-jk29lp-on-macos-sierra-fe8b2312a471)
- [Listener para el Dash Button con Raspberry Pi](https://www.nathankowald.com/blog/2017/05/dash-button-with-raspberry-pi/)
