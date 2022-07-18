from fastapi import FastAPI
from db import initialize_db
from customers import Customers
import models
import schemas

app = FastAPI()

dyn_resource = initialize_db()

@app.put("/")
async def root(request: schemas.Customer):
    #print(**request.dict())
    dicionario = {'id':'1','name':'TESTE1'}
    #new_customer = models.Customer(dicionario)
    #customer = Customers.add_customer(dyn_resource,"title", 2020, "plot", 3.5)
    #table = dyn_resource.Table('Customers')
    response = dyn_resource.Table("Customers").put_item(Item=dicionario)
    return {"message": f"Hello World {response}"}