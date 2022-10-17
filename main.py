import uvicorn
from fastapi import FastAPI

from enums import ModelName


app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
