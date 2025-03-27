from fastapi import FastAPI
#importar modelos das suas respectivas pastas
#from admin.routers import router as admin_router
#from app.modules.admin.routers import router as admin_router
from app.modules.admin.controllers import router as admin_router
#from app.modules.auth.routers import router as auth_router
from app.modules.auth.controllers import router as auth_router
#from app.modules.todos.routers import router as todos_router
from app.modules.todos.controllers import router as todos_router
from app.modules.users.controllers import router as users_router
#from app.modules.users.routers import router as users_router
from .database import engine
from .database import Base
#importar routers respectivos


app = FastAPI()

Base.metadata.create_all(bind = engine)

@app.get("/")
def main():
    return {"Message": "Hello World!"}

@app.get("/check")
def check():
    return {"status": "Tudo ok por aqui"}


app.include_router(admin_router)
app.include_router(auth_router)
app.include_router(todos_router)
app.include_router(users_router)