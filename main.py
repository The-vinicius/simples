from fastapi import FastAPI
import uvicorn

app=FastAPI()

@app.get('/')
async def read():
    return 'hello, world'

if __name__ == '__main__':
    uvicorn.run(app, debug=True) 
