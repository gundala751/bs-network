from flask import Blueprint, request, jsonify
from datetime import datetime

mining_bp = Blueprint('mining', __name__)

# Simulated mining data
mining_data = {}

@mining_bp.route('/start', methods=['POST'])
def start_mining():
    """Start mining for a user"""
    user_id = request.json.get('user_id')
    
    if not user_id:
        return jsonify({'message': 'User ID required'}), 400
    
    mining_data[user_id] = {
        'started_at': datetime.now().isoformat(),
        'status': 'mining',
        'reward': 0
    }
    
    return jsonify({'message': 'Mining started', 'data': mining_data[user_id]}), 200

@mining_bp.route('/stop/<user_id>', methods=['POST'])
def stop_mining(user_id):
    """Stop mining and claim rewards"""
    if user_id not in mining_data:
        return jsonify({'message': 'No active mining session'}), 404
    
    # Calculate reward (simplified)
    reward = 10.5  # CBS reward
    mining_data[user_id]['status'] = 'completed'
    mining_data[user_id]['reward'] = reward
    
    return jsonify({'message': 'Mining stopped', 'reward': reward}), 200

@mining_bp.route('/status/<user_id>', methods=['GET'])
def get_mining_status(user_id):
    """Get mining status for user"""
    if user_id not in mining_data:
        return jsonify({'message': 'No mining data found'}), 404
    
    return jsonify(mining_data[user_id]), 200
