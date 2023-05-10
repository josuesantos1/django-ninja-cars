from django.shortcuts import render

from ninja import Router

class VehicleView():
    router = Router()

    router.post("/")
    def create(self):
        pass
    
    router.get("/")
    def view(self):
        return {"result": "carsSerialized"}
    
    router.put("/")
    def update(self):
        pass
    
    router.delete("/")
    def delete(self):
        pass 
    
