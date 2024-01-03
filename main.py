from fastapi import FastAPI
from src.routes.routes import set_api_routes
from src.middlewares.cors_middleware import set_cors
import uvicorn

app = FastAPI()

# Middlewares
set_cors(app)


@app.get("/")
def read_root():
    return {"data": "Hello there!"}


# Routes
set_api_routes(app)

if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=9002, reload=False)
