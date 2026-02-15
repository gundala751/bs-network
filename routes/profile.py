from flask import Blueprint, request, jsonify

# Initialize a Blueprint for user profile management
profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/profile', methods=['GET'])
def get_profile():
    """Endpoint to get user profile information."""
    # Logic to retrieve user profile goes here
    return jsonify({'message': 'User profile retrieved successfully'}), 200

@profile_bp.route('/profile', methods=['POST'])
def update_profile():
    """Endpoint to update user profile information."""
    data = request.json
    # Logic to update user profile goes here
    return jsonify({'message': 'User profile updated successfully'}), 200

@profile_bp.route('/profile/password', methods=['POST'])
def change_password():
    """Endpoint to change user password."""
    data = request.json
    # Logic to change user password goes here
    return jsonify({'message': 'User password changed successfully'}), 200