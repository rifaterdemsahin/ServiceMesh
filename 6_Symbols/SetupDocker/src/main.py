from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    response = """
    <h1>Hello, Service Mesh! 🌐</h1>
    <p>Welcome to the world of microservices! 🚀</p>
    <ul>
        <li>Service 1 (Frontend): ✅</li>
        <li>Service 2 (Backend): ✅</li>
        <li>Service 3 (Database): ✅</li>
        <li>Service 4 (Cache): ✅</li>
    </ul>
    """
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)