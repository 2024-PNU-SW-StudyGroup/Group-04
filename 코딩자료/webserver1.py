from flask import Flask, request, jsonify

app = Flask(__name__)

# 기본 페이지
@app.route('/')
def home():
    return "Hello, Flask!"

# GET 요청을 처리하는 예제
@app.route('/greet', methods=['GET'])
def greet():
    name = request.args.get('name', 'Guest')
    return f"Hello, {name}!"

# POST 요청을 처리하는 예제
@app.route('/data', methods=['POST'])
def data():
    data = request.json
    return jsonify({"received": data})

# 웹서버 실행
if __name__ == '__main__':
    app.run(debug=True)
