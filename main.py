import os
from dotenv import load_dotenv
from src.app_server.config.app_config import create_combined_app

# app = Flask(__name__, static_folder='dist/static', template_folder='dist')

# app = Flask(__name__, static_folder='src/app_client/dist', template_folder='src/app_client/dist')


# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/<path:path>')
# def static_proxy(path):
#     try:
#         return send_from_directory(app.static_folder, path)
#     except Exception as e:
#         print(f"Error: {e}")
#         return render_template('index.html')

# @app.route('/api/v1/users', methods=['GET'])
# def get_users():
#     # Sample data, replace with actual data retrieval logic
#     users = [
#         {'id': 1, 'name': 'Alice'},
#         {'id': 2, 'name': 'Bob'},
#         {'id': 3, 'name': 'Charlie'}
#     ]
#     return jsonify(users)

# app run start

# Load environment variables from .env file
load_dotenv()

combined_app = create_combined_app()


if __name__ == '__main__':
    # Get port numbers from environment variables or use defaults
    # this port only works for command "python main.py", for command use "FLASK_RUN_PORT" in .env
    appPort = int(os.getenv('PORT_ONE', 5000))
    print(appPort)
      # run only one app at a time, not two
    combined_app.run(debug=True, port=appPort)