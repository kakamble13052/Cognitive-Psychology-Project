from flask import Flask, flash, redirect, render_template, request, session, abort
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template(
        'form1.html')


@app.route('/pos', methods=['POST'])
def get_time_from_client():
    js_data = json.loads(request.data)
    print(js_data)



@app.after_request
def add_header(response):
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == "__main__":
    app.run()
