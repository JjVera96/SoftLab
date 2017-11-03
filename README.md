# SoftLab

Este repositorio es para el proyecto de Laboratorio de Software UTP

### PYTHON (Django) y PostgreSQL

Para poder correr el proyecto, primero debemos instalar Python 2.7 y añadirlo al PATH de Windows

https://www.python.org/

Tambien se debe instalar PostgreSQL

https://www.postgresql.org/?&

Despues debemos instalar Pip 

https://bootstrap.pypa.io/get-pip.py

Despues de haber instalado pip, instalaremos un entorno virtual y django.

pip install virtualenv 

Vamos a la carpeta en la cual vamos a crear el entorno virtual 

virtualenv nombre

Entramos a la carpeta y activamos en entorno virtual 

.\Scripts\activate

Despues luego de esto instalamos Django

pip install django

Despues instalamos el conector de PostgreSQL con Django
 
https://www.lfd.uci.edu/~gohlke/pythonlibs/

Buscamos Psycog y descargamos x32 bits

psycopg2‑2.7.3.2‑cp27‑cp27m‑win32.whl

Y para x64 bits

psycopg2‑2.7.3.2‑cp27‑cp27m‑win_amd64.whl

Lo instalamos 

pip install archivo

Luego de esto clonamos el repo en el entorno virtual y lo ejecutamos 