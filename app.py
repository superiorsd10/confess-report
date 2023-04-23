import sys
sys.path.insert(0, '/Users/sachin/Desktop/Python Academics/Confess Report/venv/lib/python3.11/site-packages/profanity_check')
from profanity_check import predict_prob

from flask import Flask,request,jsonify


app = Flask(__name__) 


@app.route('/api',methods=['GET'])
def report():
	d = {}
	Query = str(request.args['query'])
	d['result'] = str(predict_prob([Query]))
	return jsonify(d)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
