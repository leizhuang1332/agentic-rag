import time

from fastapi import FastAPI
from fastapi.responses import StreamingResponse

from chat.ds_chat import call_llm

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/chat")
async def root(input):
    return {"message": input}


def gen_stream(prompt):
    for chunk in range(1000):
        yield str(chunk) + " "
        time.sleep(0.05)


@app.get("/stream")
async def stream_response(input):
    return StreamingResponse(call_llm(input), media_type="text/event-stream")
