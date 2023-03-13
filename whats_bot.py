from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from wiki import wiki_queries
from weather_req.wether_api import query_weather
from genius_lysrics import search

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello'


@app.route('/sms', methods=['POST'])
def sms_reply():
    """Responding incoming message with simple text"""
    # Fetch the message
    msg = request.form.get('Body')

    # Create a reply
    resp = MessagingResponse()
    if 'info'.capitalize() in msg:
        resp.message(body='Hello user *This is service bot made by Levi*.\n\n'
                          '```This is an independent service powered by twilio and its in trial phase. '
                          'Be informed that, developer has no Whatsapp API authorisation this is why, '
                          'you are supposed to be in my SandBox to be able to use this bot. '
                          'If this service is much useful, please you can help me '
                          'to have the Whatsapp API authorisation. Please join my channel here '
                          'chat.whatsapp.com/EOOHG3edGPLGdZqn1Imh4J '
                          'Your feedback is much appreciated.```')

    elif 'wiki'.capitalize() in msg:
        wiki_new = msg.replace('wiki'.capitalize(), '')
        resp.message(body=f'```{wiki_queries(wiki_new)}```')

    elif 'weather'.capitalize() in msg:
        weather_new = msg.replace('weather '.capitalize(), '')
        resp.message(body=f'```{query_weather(weather_new)}```')

    elif msg == 'help'.capitalize():
        resp.message(body='Add a prefix:\n *Wiki* : Before message to get the details of what you want\n'
                          '*lyric* : Before song name and artist name'
                          '*Weather* : Before any valid city name to know weather details\n'
                          '*Help* : To know the usage\n\n*Example*\n\n'
                          '```Wiki members of united nations\n'
                          'Weather Msanje\n'
                          'lyric andy mineo - listen```')

    elif 'lyric'.capitalize() in msg:
        lyric_new = msg.replace('lyric '.capitalize(), '')
        resp.message(body=search(lyric_new))

    else:
        resp.message(body='This is LeeReub Bot made by *Levi*.\n\n'
                          'Add a prefix:\n "wiki" : Before message to search information\n'
                          '*weather* : Before any valid city name to know weather details\n'
                          '*lyric* : Before song name and artist name *(Separate between song name and artist name '
                          'with \'-\' example \'make war - tedashii\')*\n'
                          '*help* : To know the usage')
    return str(resp)


if __name__ == '__main__':
    app.run()
