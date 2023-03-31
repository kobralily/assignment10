"""basic Flask app - demo of using a variable in a route"""
from flask import Flask, render_template
app = Flask(__name__)

import csv

def convert_to_dict(filename):
    # open a CSV file - note - must have column headings in top row
    datafile = open(filename, newline='')

    # create DictReader object
    my_reader = csv.DictReader(datafile)

    # create a regular Python list containing dicts
    list_of_dicts = list(my_reader)

    # close original csv file
    datafile.close()

    # return the list
    return list_of_dicts

cards_list = convert_to_dict('mtg_one.csv')

pairs_list = []
for card in cards_list:
    pairs_list.append( (card['id'], card['cardName']) )

@app.route('/')
def index():
    return render_template('index.html', pairs=pairs_list)

@app.route('/cardName/<num>')
def cardName(num):
    card = cards_list[int(num) - 1]
    return render_template('card.html', card=card)

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=4999, debug=True)

# if you need to avoid using port 5000 - some Mac users -
# delete the first app.run() line above and
# un-comment the second app.run() line. Then use localhost:4999