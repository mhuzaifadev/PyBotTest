  
from botbuilder.core import TurnContext,ActivityHandler
from botbuilder.schema import ActivityTypes,ChannelAccount
from nltk.chat.util import Chat, reflections

class ActivityBot(ActivityHandler):


        pairs = [
            ['(Hi|How are you|Is anyone there?|Hello|Good day|hey)',['Hello, thanks for visiting', 'Good to see you again', 'Hi there, how can I help?','??????','???? ??']],
            ['(Thanks|Thank you|Thats helpful|thankyou|thanks bro)' ,["Happy to help!", "Any time!", "My pleasure"]],   
            ]

        async def on_message_activity(self,turn_context:TurnContext):
            chat = Chat(self.pairs)
            print(type(turn_context.activity.text))
            await turn_context.send_activity(chat.respond(turn_context.activity.text))
        async def on_members_added_activity(self,member_added : ChannelAccount,turn_context:TurnContext):
            for member in member_added:
                await turn_context.send_activity(member.name)  