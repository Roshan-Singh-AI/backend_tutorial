from fastapi import FastAPI
import pandas as pd
from typing import List
from src.models import Post as PostModel
import requests

app = FastAPI()

@app.get("/posts", response_model=List[PostModel])
def get_all_posts():
    text_posts = pd.read_csv("fake_data/posts.csv").reset_index(drop=True).to_dict(orient='records')
    validated_posts = [PostModel(**post) for post in text_posts]
    return validated_posts

@app.get("/posts/{post_id}", response_model=List[PostModel] )
def get_single_post(post_id: int):
    response = requests.get("http://127.0.0.1:8000/")
    text_posts = pd.read_csv("fake_data/posts.csv").reset_index(drop=True).to_dict(orient='records')
    posts = []
    for post in text_posts:
        if post["id"] == post_id:
            posts.append(PostModel(**post))
    return posts