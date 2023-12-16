from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.databaseProducts import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.routersProducts import productRouter
from routers.auth import auth_router

# Creamos una instancia de la clase FastAPI

app = FastAPI()
app.title = "Catalogo" 
app.version = "1.0.0"

app.add_middleware(ErrorHandler)
app.include_router(productRouter)
app.include_router(auth_router)
Base.metadata.create_all(bind=engine)

# Creación de Endpoints
@app.get("/", tags=['home']) # Aqui se agrega la ruta de inicio
def message():
    return HTMLResponse(content="<h1> Bienvenido a mi API </h1>")