from fastapi import FastAPI # Importing FastAPI

app = FastAPI() # Creating an instance of FastAPI

from pydantic import BaseModel # Importing BaseModel from pydantic for data validation

from typing import Optional # Importing Optional for optional type hints

import uvicorn # Importing Uvicorn for running the FastAPI app


@app.get("/") #path operation decorator
def gradious(): # This function will be called when the root URL is acc essed
   # return {"message": "Hello, Gradious family!"}
   return {'data': {'name' : 'SaiManikata'}} # dictonionary

@app.get("/about")
def about():
   return {'data': {'age': '28', 'city': 'Rajahmundry', 'country': 'India'}}

@app.get("/contact")
def contact():
   return {'data': {'email': 'kothurisai1919@gmail.com', 'phone': '+91 9133696647'}}

@app.get("/education")
def education():
   return {'data': {'degree': 'B.Tech', 'branch': 'MECH', 'college': 'Aditya College of Engineering', 'year': '2019'}}

@app.get("/blog")
def blog(limit):
   return {'data': f'{limit}: Blogs are coming soon!'}

@app.get("/blogs")
def blogs(limit: int, published: bool):
   return {'data': {"limit" : f'{limit}Blogs are coming from Database', "published": published}}

@app.post("/contact")
def create_contact(alternate_contact: int):
    return {'data': {'message': 'Alternate Contact created successfully', 'Alternate contact': {alternate_contact}}}

class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post("/blog")
def create_blog(blog: Blog):
    return {'data': {'message': f'Blog created successfully with title as {blog.title}'}}


# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)  # Running the FastAPI app with Uvicorn server"
