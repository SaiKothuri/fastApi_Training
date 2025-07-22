from fastapi import FastAPI
app = FastAPI()


@app.get("/")
def gradious():
   # return {"message": "Hello, Gradious family!"}
   return {'data': {'name' : 'SaiManikata'}}

@app.get("/about")
def about():
   return {'data': {'age': '28', 'city': 'Rajahmundry', 'country': 'India'}}
