from asyncore import loop
from typing import Union

from fastapi import FastAPI
import datetime
import time


def time_printer():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func time :', ts)


app = FastAPI()


def loop_monitor():
    while True:
        time_printer()
        time.sleep(5)


@app.get("/")
def read_root():
    time_printer()
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


# loop_monitor()

if __name__ == '__main__':
    # loop_monitor()
    # 在5000端口启动服务
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=5000)
