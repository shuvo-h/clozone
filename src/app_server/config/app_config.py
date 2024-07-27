from flask import Flask, jsonify
# from app_server.app_name_one.bluprint_registerer import register_all_frontend_bluprint
from src.app_server.app_name_one.bluprint_registerer import register_all_frontend_bluprint

# create a combined single ap and call all blueprints here to register
def create_combined_app():
    # app = Flask(__name__, static_folder='src/app_client/dist', template_folder='src/app_client/dist')
    app = Flask(__name__, static_folder='../../app_client/dist', template_folder='../../app_client/dist')


    # configure app to add all secret from env
    # Call middleware configuration functions
    # configure_cors(app)
    # configure_logging(app)
    # configure_csrf(app)
    # configure_xss(app)
    # configure_secure_cookies(app)
    # configure_request_rate_limiting(app)
    # configure_csp(app)

    # call config method and pass the app there
    # db_connect(app)

    # register all blueprints here
    register_all_frontend_bluprint(app=app)
    # app.register_blueprint(food_bp,url_prefix='/api/v1/foods')
    # register_all_users_bluprint(app)
    # register_all_food_bluprint(app)
    # register_tinyapp_blueprints(app)

    # add the frontend and vue/react app build files


     # handle custom error page
    # handle invalid url
    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({'success':False,"message":"URL not found:("}),404
    # Internal server error handler
    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify({'success':False,"message":"Internal server error"}),500


    # Configure versioning
    # configure_versioning(app)

    # Configure cache
    # configure_cache(app)

    # Configure background tasks
    # configure_background_tasks(app)

    return app