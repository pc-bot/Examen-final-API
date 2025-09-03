from fastapi import FastAPI
from starlette.responses import Response
from pydantic import BaseModel

app = FastAPI()

class Characteristics(BaseModel):
    ram_memory : int
    rom_memory : int

class PhonesInfo(BaseModel):
    id : str
    brand : str
    model : str
    characteristics : Characteristics

phoneLists = list[PhonesInfo] = []

@app.get("/health")
async def getHealth():
    return Response(media_type="text/plain",content="OK", status_code=200)

@app.post("/phones",response_model=list[PhonesInfo])
async def createPhones(Phone : PhonesInfo):
    phoneLists.append(Phone.model_dump())
    return Response(content="Phone added",status_code= 200)

@app.get("/phones")
async def getPhones():
    return Response(status_code=200,content=phoneLists, media_type="application/json")

@app.get("/phones/{id}",response_model=PhonesInfo)
async def getPhoneyId(id : int, Phones : PhonesInfo):
    for idx, phones in phoneLists:
        if id == PhonesInfo.id :
            phoneLists[idx] = phones
            return phones
    return Response(content={"error": "Id not found"}, status_code=404)


    


