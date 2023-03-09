from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

conn = pymysql.connect(
    host='loans.c7fjnowdxab2.af-south-1.rds.amazonaws.com',
    user='testing',
    password='loan@ev&%*&53',
    db='loans'
)

@app.route('/data', methods=['GET'])
def get_data():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Summary')
    data = cursor.fetchall()
    cursor.close()
    return jsonify(data)

if __name__ == '__main__':
    app.run()