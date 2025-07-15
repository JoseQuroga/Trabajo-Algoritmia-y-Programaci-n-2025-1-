# Manual de Usuario - Sistema Hotel Maison 33

## ¿Qué hace este programa?
Este programa fue desarrollado para facilitar la gestión operativa del Hotel Maison 33, permitiendo registrar huéspedes, realizar y gestionar reservas, controlar ingresos y salidas de huéspedes, generar reportes administrativos y visualizar gráficos de uso.

## ¿Que cosas deben tener para iniciar el programa correctamente?
Tener instaladas todas las librerias que estan al inicio del codigo para que este pueda funcionar correctamente, ademas de tener el archivo adming.csv en el cual deben colocar los usuarios y contraseñas que usaran los administradores del hotel, los demas archivos como lo pueden ser huespedes.csv, ingresos.csv, reservas.csv. El codigo los creara automaticamente 

## ¿Como iniciar el programa correctamente?
En donde pongan a funcionar el programa ya sea CMD, alguna consola de python o un libro de colab, donde ya tengan pegado el codigo y lo ejecuten exitosamente.
Encontraran el menú del programa para poder usar todas las funciones que este les brinda. Algo como esto:

Bienvenidos al Hotel Maison 33
1. Registrar huésped
2. Realizar reserva
3. Registrar Ingreso (check-In)
4. Registrar salida (Check-Out)
5. Administracion (Acceso Restringido)
6. Salir

Seleccione una opcion:

## ¿Como usar el programa correctamente?
#### Registrar huésped (1)
En esta primera opcion el usuario debera ingresar el numero 1 (Uno), seguido a esto apareceran opciones como lo son Nombre y apellido, documento, correo electronico y telefono, donde cada uno de estos datos aparecera en el archivo "huespedes.csv" y cada uno de estos datos tiene sus recciones

- Nombre y Apellido (mínimo 3 letras, sin números)
- Documento (solo números, 3-15 dígitos)
- Correo electrónico (formato válido con dominio real usando el @)
- Teléfono (solo números, 7-15 dígitos)

#### Realizar Reserva (2)
En esta opcion el usuario debera ingresar el numero 2 (Dos), donde permite relizar la reserva a alguna de las habitaciones del hotel que en este caso tenemos la estandar y la suite por precios de 120.000 y 250.000 respectivamente, y los datos se guardaran en el archivo reservas.csv para lograr la reserva el usuario debera poner:

- Documento de identidad
- Tipo de habitacion
- Numero de noches

#### Registrar Ingreso (3)
En esta opcion el usuario debera ingresar el numero 3 (Tres), Donde se permite registrar el ingreso del huespedes con una reserva previa, para poder hacer el Check-in el usuario debera ingresar su documento de identidad, y se guardara en el archivo ingresos.csv

#### Registrar Salida (Check-Out)
En esta opcion el usuario debera ingresar el numero 4 (Cuatro), y sirve para darle salida a algun huespued, dandonos el valor total que debera pagar, basado en el tipo de habitacion y el numero de noches

#### Modulo Administrativo
En esta opcion es donde los administradores del hotel podran ver cosas como lo son todos los datos del hotel y los huespedes, para ingresar aqui deben tener su usuario y contraseña puestos en el archivo admin.csv, y una vez los ingreses ya se habilitara todo el modulo administrativo en donde podemos hacer cosas como

Reportes Grafficos 
Donde se muestra una grafica de barras con la ocupacion de habitaciones de cada tipo 

#### Salir
Para esta opcion se debe colocar el numero 6 (Seis) y ya el programa se dara por finalizado y no se podra ingresar ninguna otra opcion a no ser de que el programa se ejecute nuevamente 
