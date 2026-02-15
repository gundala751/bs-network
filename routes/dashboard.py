from flask import Blueprint, jsonify

# Dashboard Blueprint

routes = Blueprint('dashboard', __name__)

@routes.route('/dashboard', methods=['GET'])
def get_dashboard_statistics():
    # Placeholder for actual dashboard statistics data
    data = {
        'users': 100,
        'active_sessions': 75,
        'current_load': '50%',
    }
    return jsonify(data)

@routes.route('/platform/statistics', methods=['GET'])
def get_platform_statistics():
    # Placeholder for actual platform statistics data
    data = {
        'total_requests': 1000,
        'successful_requests': 950,
        'failed_requests': 50,
    }
    return jsonify(data)