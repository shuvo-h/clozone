# from app_name_one.user_module.user_route import user_bp
from src.app_server.app_name_one.frontend_module.frontend_route import app_1_frontend_bp


def register_all_frontend_bluprint(app):
    app.register_blueprint(app_1_frontend_bp,url_prefix='')