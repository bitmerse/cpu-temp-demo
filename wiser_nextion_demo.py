from gpiozero import CPUTemperature
from nextion import Nextion
import time
import asyncio

#temperature variable
tempGraph=0
#setup connection
client = Nextion('/dev/ttyUSB0', 9600, None)
async def update_nextion():
    global client
    await client.connect()

    while True:
        tempGraph = int(CPUTemperature().temperature)
        print("tempGraph: ",tempGraph)
        await client.set('NtempGraph.val', tempGraph)
        time.sleep(0.05)

loop = asyncio.get_event_loop()
asyncio.ensure_future(update_nextion())
loop.run_forever()