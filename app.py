import requests
import json

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)


@app.route('/')
def index():
   #print('Request for index page received')
   #return render_template('index.html')
   #response = requests.get("https://reqres.in/api/users")
   #data = json.loads(response.content)
   #html = "<html><body>"
   html += "<table>"
   html += "<tr><th>ID</th><th>Name</th><th>Email</th></tr>"
    #for user in data["data"]:
     #   html += f"<tr><td>{user['id']}</td><td>{user['first_name']} {user['last_name']}</td><td>{user['email']}</td></tr>"
    html += "</table>"
    html += "</body></html>"
   return render_template('index.html', html = html)

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

if __name__ == '__main__':
   app.run()
