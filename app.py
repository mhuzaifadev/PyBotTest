from flask import Flask,request,Response
from botbuilder.schema import Activity
from botbuilder.core import BotFrameworkAdapter,BotFrameworkAdapterSettings
import asyncio

from ourbot import ActivityBot
from config import DefaultConfig
app = Flask(__name__)
loop = asyncio.get_event_loop()

ebot = ActivityBot()
CONFIG = DefaultConfig()

#https://docs.microsoft.com/en-us/javascript/api/botbuilder/botframeworkadapter?view=botbuilder-ts-latest
# Microsoft App ID and Microsoft App Password     "33787288-ec92-4419-b42c-363e012629bb","af6dd3ef-d22b-46e2-bbe5-4e1cd038f61c"
botadaptersettings = BotFrameworkAdapterSettings("33787288-ec92-4419-b42c-363e012629bb","aa4302bb-5d4d-4bc9-94db-38a6727131a1")
botadapter = BotFrameworkAdapter(botadaptersettings)

@app.route("/api/messages",methods=["POST"])
def messages():
    if "application/json" in request.headers["content-type"]:
      jsonmessage = request.json
    else:
      return Response(status=415)

    activity = Activity().deserialize(jsonmessage)

    async def turn_call(turn_context):
        await ebot.on_turn(turn_context)

    task = loop.create_task(botadapter.process_activity(activity,"",turn_call))
    loop.run_until_complete(task)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)