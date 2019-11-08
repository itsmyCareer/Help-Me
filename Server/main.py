from flask import Flask, jsonify, request
import pymysql
import pymysql.cursors

class ItemFounded(Exception):
    pass

db = pymysql.connect(host='localhost', port=3306, user='itsmysurport', passwd='Wordp@ss5479', db='testdb', charset='utf8mb4')
app = Flask(__name__)

try:
    @app.route('/', methods = ['POST', 'GET'])
    def test():
        a = request.json['username']
        
        with db.cursor() as cursor:
            sql = 'SELECT * FROM users'
            cursor.execute(sql)
            result = cursor.fetchall()
        try:
            for i in range(0, len(result)):
                print(result[i][1], a)
                if result[i][1] == a:
                    raise ItemFounded

            with db.cursor() as cursor:
                sql = 'INSERT INTO users (username) VALUES (%s)'
                cursor.execute(sql, (a))
            db.commit()
            print(cursor.lastrowid)
            # 1 (last insert id)
            
            return 'success'
        except:
            print('Hello.')
            return 'success'

    @app.route('/help', methods = ['POST'])
    def helpme():
        help_location = request.json['location']
        help_time = request.json['time']
        help_device_id = request.json['device_id']
        with db.cursor() as cursor:
            sql = 'INSERT INTO helpdatas (location, time, device_id) VALUES (%d, %s, %s)'
            cursor.execute(sql, (help_location, help_time, help_device_id))
        db.commit()

    @app.route('/read')
    def hosting():
        a = ''
        with db.cursor() as cursor:
            sql = 'SELECT * FROM helpdatas'
            cursor.execute(sql)
            result = cursor.fetchall()
            print(result)
            for i in range(0, len(result[-1])):
                a += (str(result[-1][i]) + ':')
        return a

    if __name__ == '__main__':
        app.run(debug=True)

finally:
    db.close()