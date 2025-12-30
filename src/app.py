from fastapi import FastAPI

text_posts = {'name':'roshan'}

app = FastAPI()

@app.get("/posts")
def get_all_posts():
    return text_posts