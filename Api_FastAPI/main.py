from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from typing import List


class Tea(BaseModel):
    id :int
    name : str
    orgin : str




app = FastAPI()
#teas = []
# leater data store list type | follow the base class 
teas : list[Tea] = []
#-----------------------------------------------------------
@app.get("/")
async def root():
    return {"message": "Hello World, how are "}


#-----------------------------------------------------------  
@app.get("/getteas")
def get_teas():
    return teas

@app.post("/addtes")
def add_tea(tea: Tea):
    teas.append(tea)
    return tea


#-----------------------------
@app.put("/updatetea/{tea_id}")
def update_tea(tea_id: int, update_tea: Tea):
    for index, tea in enumerate(teas):
        if tea.id == tea.id:
            teas[index] = update_tea
            return update_tea
    return {"err"  : "tea is not found !"}

@app.delete("/deletetea/{tea_id}")
def delete_tea(tea_id: int):
    for index, tea in enumerate(teas):
        if tea.id == tea_id:
            delete_tea = teas.pop(index)
            return delete_tea
        return { "error" : "Tea is not fourn"}


#==============================
if __name__ == "__main__":
    #uvicorn.run(app,host="0.0.0.0", port=8081, reload= True)
    uvicorn.run("main:app",host="0.0.0.0", port=8081, reload= True) # app is object | main is file
# api testing to swear api 