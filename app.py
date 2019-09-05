from random import choice
from flask import Flask, request

app = Flask(__name__)

compliments = ['coolio', 'smashing', 'neato', 'fantabulous']
days = ['amazing','great','fast','awesome']

@app.route('/compliment')
def get_compliment():
    name = request.args.get('name')
    compliment = choice(compliments)
    return(f'Hello there, {name}! You are so {compliment}!')

def get_horoscope():
    day = choice(days)
    return(f'Your day will go {day}!')

@app.route('/')
def index():
    return  """
    <form action = '/compliment'>
        What is your name??
        <input type = "text" name = "name"></input>
        <button type = "submit">Submit!</button>
    </form>
    """
    
#-------------------------#
if __name__ == "__main__":
    app.run(debug=True)
#-------------------------#