from flask import jsonify

def send_res(status=200,data=None,meta=None,message='Request successful',err=None,success=True):
    return jsonify({
        'status':status,
        'success':success,
        'message':message,
        'data':data,
        'meta':meta,
        'error':err,

    }), status

