# prevent to generate __pycache__ folder/file in development for each module
import sys, os
if os.getenv('FLASK_ENV') == 'development':
     sys.dont_write_bytecode = True

from dotenv import load_dotenv
from src.app_server.config.app_config import create_combined_app
from flask_migrate import Migrate

# Load environment variables from .env file
cwd = os.getcwd()
envFilePath = os.path.join(cwd,'.env')
load_dotenv(dotenv_path=envFilePath)

combined_app = create_combined_app()

# connect database
from src.app_server.config.env_config import envs
from src.app_server.config import db_config
migrate = Migrate(app=combined_app,db=db_config.db)


if __name__ == '__main__':
    # Get port numbers from environment variables or use defaults
    # this port only works for command "python main.py", for command use "FLASK_RUN_PORT" in .env
    # appPort = int(os.getenv('PORT_ONE', 5000))
    # print(envs)
      # run only one app at a time, not two
    combined_app.run(debug=True, port=envs['APP_PORT'])