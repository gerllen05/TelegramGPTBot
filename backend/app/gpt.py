import openai

from app.models import MessageItem


def chat_gpt_query(session, gpt_key, user, content_amount, debug):
    last_msgs = get_last_messages(session, user, content_amount)
    if debug:
        print(last_msgs)
    openai.api_key = gpt_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=last_msgs,
    )
    if debug:
        print(response)
    return (response.choices[0].message.content, response.usage)

def get_last_messages(session, user, amount):
    msgs = session.query(MessageItem).filter(MessageItem.userId == user.id).order_by(MessageItem.id.desc()).limit(amount).cte()
    reversed_msgs = session.query(msgs).order_by(msgs.c.id).all()
    messages = format_messages(reversed_msgs)
    return messages

def format_messages(messages):
    formatted_msgs = []
    for msg in messages:
        if not msg.isForgotten:
            dict = {
                "role": msg.role,
                "content": msg.content
                }
            formatted_msgs.append(dict)
    return formatted_msgs
