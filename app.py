from flask import Flask,request,Response
from botbuilder.schema import Activity
from botbuilder.core import BotFrameworkAdapter,BotFrameworkAdapterSettings
import asyncio

from ourbot import ActivityBot

app = Flask(__name__)
loop = asyncio.get_event_loop()

ebot = ActivityBot()

#https://docs.microsoft.com/en-us/javascript/api/botbuilder/botframeworkadapter?view=botbuilder-ts-latest
# Microsoft App ID and Microsoft App Password
botadaptersettings = BotFrameworkAdapterSettings("","")
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
    app.run('localhost',3978)