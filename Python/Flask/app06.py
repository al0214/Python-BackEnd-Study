from flask import Flask, make_response
app = Flask(__name__)

@app.route('/response')
def response_example():
    # 응답 객체를 생성합니다. "Hello with header"는 응답 바디이며, 200은 HTTP 상태 코드입니다.
    resp = make_response("Hello with header", 200)

    # 'Custom-Header'라는 이름의 사용자 정의 헤더를 설정하고 'custom-value' 값을 지정합니다.
    resp.headers['Custom-Header'] = 'custom-value'
    
    # 설정한 헤더와 함께 응답 객체를 반환합니다.
    return resp
    
@app.route('/direct')
def direct_response():
    headers = {'X-Example' : 'DirectHeader'}
    return make_response("Direct Response", 200, headers)

@app.route('/custom')
def custom_response():
    response = make_response("Custom Response", 202)
    response.headers['X-Example'] = 'CustomHeader'
    return response

if __name__ == '__main__':
    app.run(debug=True)