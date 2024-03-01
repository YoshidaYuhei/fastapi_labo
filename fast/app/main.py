from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routers import system, auth, user, ticket

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

############################################################
# Routers
############################################################
app.include_router(system.router, tags=["システム"], prefix='/system')
app.include_router(auth.router, tags=["認証"], prefix='/auth')
app.include_router(user.router, tags=["ユーザー"], prefix='/user')
# app.include_router(ticket.router, tags=["チケット"], prefix='/ticket')
