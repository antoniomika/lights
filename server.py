import sendsignal
from flask import Flask, render_template, Response, request, jsonify, \
    session, redirect

app = Flask(__name__)
app.secret_key = "TEST"

username = 'test'
password = 'test'


@app.route('/')
def index():
    if 'loggedin' in session:
        return render_template('index.html')
    else:
        return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    if 'username' in request.form and 'pwd' in request.form:
        if (request.form['username'] == username and
                request.form['pwd'] == password):
            session['loggedin'] = True
    return redirect('/')


@app.route('/trigger')
def trigger():
    if 'loggedin' in session:
        if 'color' in request.args and request.args['color'] is not '':
            sendsignal.send(request.args['color'])
    return redirect('/')


@app.route('/logout')
def logout():
    if 'loggedin' in session:
        session.clear()
    return redirect('/')


@app.route('/shutdown')
def shutdown():
    if 'loggedin' in session:
        shutdown_server()
        return jsonify(status=True)
    else:
        return jsonify(status=False)


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080, threaded=True)
