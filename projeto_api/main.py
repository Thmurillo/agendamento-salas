from fastapi import FastAPI
from routes import user, block, room, reservation


app = FastAPI()
app.include_router(user.router)
app.include_router(block.router)
app.include_router(room.router)
app.include_router(reservation.router)

# @app.get ("/")
# def helloWorld():
#     return "Hello world"


