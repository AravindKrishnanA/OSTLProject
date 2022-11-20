import json
from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2

conn = psycopg2.connect(host="localhost",
                        database="flappybird",
                        user="postgres",
                        password="postgres")

cur = conn.cursor()

app = Flask(__name__)
cors = CORS(app)
cors = CORS(app, resources={
    "/*": {
        "origins" : "*"
    }
})

app.config['CORS-HEADERS'] = 'Content-type'

@app.route('/highscoreList', methods=['GET'])
def get_highscore_list():
    cur.execute('SELECT * FROM highscore ORDER BY highscore DESC')
    hslist = cur.fetchall()
    info = []
    for array in hslist[:5]:
        info.append(array)

    return jsonify(info)

@app.route('/highscoreList', methods=['POST'])
def post_highscore_list():
    content = request.json
    username = content['username']
    score = content['highscore']

    #print(username , ',' , str(score))
    print(type(username) , ',' , type(score))

    cur.execute("SELECT highscore from highscore WHERE username = \'{}\' ".format(username))
    highscore = cur.fetchall()
    #print(type(highscore[0][0]))
    if(highscore):
        if(score>highscore[0][0]):
            highscore = score
            cur.execute("UPDATE highscore SET highscore = {} WHERE username = \'{}\'".format(highscore, username))
            conn.commit()
    else:
        cur.execute("INSERT INTO highscore (username, highscore) VALUES(\'{}\', {})".format(username, score))
        conn.commit()
    return("posted 200")



    
if __name__ == "__main__":
    app.run(debug = False, port = "5000")