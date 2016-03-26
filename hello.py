
from flask import request, make_response, Flask, session, redirect
from flask_script import Manager
app = Flask(__name__)

manager = Manager(app)

@app.before_first_request
def get_somethin():
    print request.headers

@app.teardown_request
def response_header(reponse):
    if reponse:
        return app.response_class(response=reponse.args[0]+request.headers.get('User-Agent'))

@app.route('/')
def first_program():
    return app.response_class('<h1>hello<?h1>')


@app.route('/<string:user_name>')
def hello(user_name):
    se_app = app
    # reponse = make_response(request.headers.get('User-Agent'))
    # reponse.set_cookie('answer', '42')
    return redirect('http://www.baidu.com')
    # return app.response_class('<h1>hello %s<h1>' % user_name)


@app.route('/404')
def error_404():
    return '<h1>Bad Request</h1>', 404


if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8080, debug=True)
    manager.run()
