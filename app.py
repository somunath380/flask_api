from flask import Flask
import sqlite3
import json
app = Flask(__name__)

@app.route('/')
def entry_page():
    return '<h1>Flask is Running</h1>'

@app.route('/ifsc/<ifsc>', methods=['GET'])
def bank_details_by_ifsc(ifsc):
   conn = sqlite3.connect('testdb.db')
   curr = conn.cursor()
   _sql = 'select * from banks where ifsc=\'{}\''.format(ifsc)
   curr.execute(_sql)
   res = curr.fetchall()
   return json.dumps(res)

@app.route('/details/<bank_name>/<city>',methods=['GET'])
def branch_details(bank_name,city):
        conn = sqlite3.connect('testdb.db')
        curr = conn.cursor()
        _sql = 'select * from banks where bank_name=\'{}\' and city=\'{}\''.format(bank_name,city)
        curr.execute(_sql)
        res = curr.fetchall()
        return json.dumps(res)


if __name__ == "__main__":
    app.run(debug=True)