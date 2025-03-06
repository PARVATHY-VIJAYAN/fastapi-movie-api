from fastapi import FastAPI, Request
import requests
from typing import List,Dict
app = FastAPI()

movies_dict : List[Dict[str,str]] = [
                                        {"id": "1",
                                         "title": "Inception",
                                         "director": "Christopher Nolan"
                                        }
                                    ]

#view all
@app.get("/movies")
async def index():
   return movies_dict

#Retrieve one movie
@app.get("/movies/{id}")
async def index(r:Request,id:str) -> dict:
    print(id)
    '''
        id = r._query_params.__dict__['_dict']['id']
    '''
    for movie in movies_dict:
      if movie.get("id") == id:
         return movie
    return {"message": "Movie not found!"}

#add a movie
@app.put("/movies/{id}")
async def index(r:Request,id:str):
   data = await r.json()
   newdict = {"id": id}
   for movie in movies_dict:
      if movie.get("id") == id:
         movie["title"] = data["title"]
         movie["director"] = data["director"]
   return {"message": "Movie added successfully!"}

@app.post("/movies")
async def index(r:Request):
   movies_dict.append(await r.json())
   return "item added\n",movies_dict
   
@app.delete("/movies/{id}")
async def index(r:Request,id:str):
   print(id)
   for movie in movies_dict:
      indexvalue = movies_dict.index(movie)
      if movie["id"]==id:
         movies_dict.pop(indexvalue)
   print(movies_dict)
   return {"message": "Movie removed successfully!"}