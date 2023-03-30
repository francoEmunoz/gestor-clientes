from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
import database as db
from pydantic import BaseModel, constr, validator
import helpers


class ModeloCliente(BaseModel):
    dni: constr(min_length=8, max_length=8)
    nombre: constr(min_length=2, max_length=30)
    apellido: constr(min_length=2, max_length=30)

class ModeloCrearCliente(ModeloCliente):
    @validator("dni")
    def validar_dni(cls, dni):
        if not helpers.dni_valido(dni, db.Clientes.lista):
            raise ValueError("Cliente ya existente o DNI incorrecto")
        return dni
    

app = FastAPI(
    title="API del Gestor de clientes",
    description="Ofrece diferentes funciones para gestionar los clientes.")


@app.get('/clientes/', tags=["Clientes"])
async def clientes():
    content = [cliente.to_dict() for cliente in db.Clientes.lista]
    return JSONResponse(content = content)

@app.get('/clientes/{dni}/', tags=["Clientes"])
async def buscar_cliente(dni: str):
    cliente = db.Clientes.buscar(dni= dni)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return JSONResponse(content= cliente.to_dict())

@app.post('/clientes/', tags=["Clientes"])
async def crear_cliente(datos: ModeloCrearCliente):
    cliente = db.Clientes.crear(datos.dni, datos.nombre, datos.apellido)
    if cliente:
        return JSONResponse(content= cliente.to_dict())
    raise HTTPException(status_code=404, detail="Cliente no creado")

@app.patch('/clientes/', tags=["Clientes"])
async def editar_cliente(datos: ModeloCliente):
    if db.Clientes.buscar(datos.dni):
        cliente = db.Clientes.editar(datos.dni, datos.nombre, datos.apellido)
        if cliente:
            return JSONResponse(content= cliente.to_dict())
        raise HTTPException(status_code=404, detail="Cliente no editado")
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

@app.delete('/clientes/{dni}/', tags=["Clientes"])
async def borrar_cliente(dni: str):
    if db.Clientes.buscar(dni):
        cliente = db.Clientes.borrar(dni)
        if cliente:
            return JSONResponse(content= cliente.to_dict())
        raise HTTPException(status_code=404, detail="Cliente no borrado")
    raise HTTPException(status_code=404, detail="Cliente no encontrado")