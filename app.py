from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

'Setup connection'
app.config['MYSQL_HOST'] = 'bmfztcf4tmnnovqlzbhh-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'utepxjwtj4a0teox'
app.config['MYSQL_PASSWORD'] = 'ynVYHlzbSV3AiYeQjIRU'
app.config['MYSQL_DB'] = 'bmfztcf4tmnnovqlzbhh'

mysql = MySQL(app)


@app.route('/')  # Use the route decorator to specify the URL for the view function
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM products')
    data = cur.fetchall()
    cur.close()
    return jsonify(data)
    ''' return render_template('index.html', data1=data)'''




if __name__ == '__main__':
    app.run(debug=True)
