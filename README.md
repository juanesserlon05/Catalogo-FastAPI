Catálogo de Productos API
Esta es una API desarrollada en Python utilizando FastAPI y Virtual Environments para gestionar un catálogo de productos. La API permite realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) en productos, los cuales están identificados por un ID único y tienen atributos como Nombre (Name), Descripción (Description) y Unidades (Units).


Instalación
Clona este repositorio en tu máquina local:
git clone https://github.com/tu-usuario/tu-repositorio.git


Accede al directorio del proyecto:
cd tu-repositorio


Crea un entorno virtual:
python -m venv venv


Activa el entorno virtual:
En Windows:
venv\Scripts\activate

En Linux/Mac:
source venv/bin/activate


Instala las dependencias utilizando el siguiente comando:
pip install -r requirements.txt


Uso
Ejecutar la API
Para ejecutar la API, utiliza el siguiente comando:

uvicorn main:app --port 2331 --reload --host 0.0.0.0

La API estará disponible en http://(ip de tu maquina:2331.

Endpoints
La API cuenta con los siguientes endpoints para gestionar el catálogo de productos:

Obtener todos los productos:
GET /products

Obtener un producto por ID:
GET /products/{product_id}

Crear un nuevo producto:
POST /products

Enviar un JSON en el cuerpo de la solicitud con los datos del producto:
json
{
    "Name": "Nombre del Producto",
    "Description": "Descripción del Producto",
    "Units": 10
}

Actualizar un producto existente:
PUT /products/{product_id}

Enviar un JSON en el cuerpo de la solicitud con los datos actualizados del producto:
{
    "Name": "Nuevo Nombre",
    "Description": "Nueva Descripción",
    "Units": 20
}
Eliminar un producto por ID:
DELETE /products/{product_id}

Contribuciones
Si encuentras algún problema o tienes sugerencias de mejora, ¡no dudes en abrir un issue o enviar un pull request
