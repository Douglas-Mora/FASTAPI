# Python API Development -- Guide

**Steps I followed**

*Outside VSCode and on terminal*

|Steps|Code|
|---|---|
|Create a Github repo, and clone it locally|`git clone <url>`|
|Create a virtual environment|`py -3 -m venv <venv_name>`|
|Activate the venv|`.venv\Scripts\Activate.ps1`|
|Install FastApi|`pip install fastapi[all]`|
||``|

Into the `main.py` file:
```
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
async def root():
    return {"message": "Hello, World"}
```

To activate the local server, run:

`uvicorn main:app`

Which is 'uvicorn <file_name>:<app_name>'