from quart import Quart, render_template, websocket
import asyncio
import time

app = Quart(__name__)


@app.route("/", methods=['GET'])
async def hello():
    return await render_template('index.html')


@app.route('/api')
async def json():
    time.sleep(5)
    return {"hello": "world"}


@app.websocket('/ws')
async def ws():
    while True:
        data = await websocket.receive()
        await websocket.send(f"received: {data}")

# if __name__ == "__main__":
#     app.run()


if __name__ == "__main__":
    app.run(use_reloader=True)
