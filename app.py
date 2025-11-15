#create a file using the command notepad app.py and paste the following code

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1 style="color:green;">🔒 SSL Secured Website Demo</h1>
        <p>This site uses HTTPS with a self-signed SSL certificate.</p>
        <p>Developed by {Your Name}</p>
    '''

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8443, ssl_context=('cert.pem', 'key.pem'))
