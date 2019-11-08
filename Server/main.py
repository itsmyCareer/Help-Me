from flask import Flask, jsonify, request
import pymysql
import pymysql.cursors

db = pymysql.connect(host='localhost', port=3306, user='itsmysurport', passwd='Wordp@ss5479', db='testdb', charset='utf8mb4')
app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def test():
    a = request.json['username']
    try:
        with db.cursor() as cursor:
            sql = 'INSERT INTO users (username) VALUES (%s)'
            cursor.execute(sql, (a))
        db.commit()
        print(cursor.lastrowid)
        # 1 (last insert id)
    finally:
        db.close()
    return 'success'

if __name__ == '__main__':
    app.run(debug=True)