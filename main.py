
from fastapi import FastAPI
from . import models
from api_sm.database import engine
from .routers import posts, users, auth, votes
from .config import settings
from fastapi.middleware.cors import CORSMiddleware




models.Base.metadata.create_all(bind=engine)

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(posts.router)
app.include_router(users.router)
app.include_router(auth.router)
app.include_router(votes.router)

@app.get('/')
async def root():
    return {'message': 'Welcome to my api bro'}


# my_posts = [{'title': 'title post1', 'content': 'content post1', 'id': 1}, {'title': 'title post2', 'content': 'content post2', 'id': 2}]

# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p
# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i

# @app.get('/sqlalchemy')
# def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     print(posts)
#     return {'data': posts}
