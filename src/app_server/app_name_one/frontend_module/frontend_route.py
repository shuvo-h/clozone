from flask import Blueprint,request,jsonify, send_from_directory,render_template
import os


# Determine the base directory
base_dir = os.path.abspath(os.path.dirname(__file__))
# Construct the paths
static_folder = os.path.join(base_dir, '../../../app_client/dist')
template_folder = os.path.join(base_dir, '../../../app_client/dist')

app_1_frontend_bp = Blueprint('app_1_frontend_bp',__name__,static_folder=static_folder, template_folder=template_folder)


@app_1_frontend_bp.route('/')
def index():
    return render_template('index.html')

# render vue build "dist" as template
# configure the static file path when app=Flask(static_folder,template_folder)
@app_1_frontend_bp.route('/<path:path>')
def static_proxy(path):
    try:
        return send_from_directory(app_1_frontend_bp.static_folder,path)
    except Exception as e:
        print(f"Error::==:: {e}")
        # return jsonify({"message":"Page Not found"}),404
        return render_template('index.html')