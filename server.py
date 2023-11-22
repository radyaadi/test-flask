from waitress import serve
from app import app  # Replace 'predict' with the actual name of your Flask app file

if __name__ == '__main__':
    serve(app, host='127.0.0.1', port=5000)