from flask import Flask, jsonify, request
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)

# In-memory storage for transactions and user points
transactions = []
user_points = {}

@app.route('/')
def home():
    return jsonify({"message": "CORS-enabled Flask backend!"})

@app.route('/add', methods=['POST'])
def add_transaction():
    data = request.get_json()
    if not data or 'payer' not in data or 'points' not in data or 'timestamp' not in data:
        return jsonify({"error": "Invalid request data"}), 400

    # Create a transaction entry
    transaction = {
        "payer": data['payer'],
        "points": data['points'],
        "timestamp": datetime.fromisoformat(data['timestamp'].replace("Z", "+00:00"))  # Convert to datetime
    }

    # Store the transaction
    transactions.append(transaction)

    # Update user points
    if data['payer'] not in user_points:
        user_points[data['payer']] = 0
    user_points[data['payer']] += data['points']

    return '', 200

@app.route('/spend', methods=['POST'])
def spend_points():
    data = request.get_json()
    if not data or 'points' not in data:
        return "Invalid request data", 400

    points_to_spend = data['points']
    total_points = sum(user_points.values())

    if points_to_spend > total_points:
        return "User doesn't have enough points", 400

    spent_points = {}
    remaining_points = points_to_spend

    # Sort transactions by timestamp to spend the oldest points first
    sorted_transactions = sorted(transactions, key=lambda x: x['timestamp'])

    # Temporary dictionary to track the deductions from each payer
    payer_deductions = {}

    for transaction in sorted_transactions:
        payer = transaction['payer']
        transaction_points = transaction['points']

        # If payer not in deductions, initialize it
        if payer not in payer_deductions:
            payer_deductions[payer] = 0

        # Calculate available points to spend from this transaction
        available_points = transaction_points + payer_deductions[payer]

        if available_points <= 0:
            # If this transaction or the payer has no points to spend, skip
            if transaction_points < 0:
                remaining_points += abs(transaction_points)
                payer_deductions[payer] += abs(transaction_points)
                spent_points[payer] += abs(transaction_points)

            continue

        if remaining_points > available_points:
            # Deduct all available points from this payer
            #spent_points.append({"payer": payer, "points": -available_points})
            if payer in spent_points:
                spent_points[payer] -= available_points
            else:
                spent_points[payer] = -available_points

            remaining_points -= available_points
            payer_deductions[payer] -= available_points
        else:
            # Spend only the remaining points needed from this payer
            #spent_points.append({"payer": payer, "points": -remaining_points})
            if payer in spent_points:
                spent_points[payer] -= remaining_points
            else:
                spent_points[payer] = -remaining_points
            payer_deductions[payer] -= remaining_points
            remaining_points = 0
            break

    # If there are still remaining points after trying to spend, it means we ran out of points
    if remaining_points > 0:
        return "User doesn't have enough points", 400

    # Apply deductions to user points
    for payer in spent_points:
        #payer = deduction['payer']
        #user_points[payer] += deduction['points']  # deduction['points'] is negative, so this subtracts
        user_points[payer] += spent_points[payer]

    return jsonify(spent_points), 200


@app.route('/balance', methods=['GET'])
def get_balance():
    # Always returns a 200 with the user points
    return jsonify(user_points), 200

if __name__ == '__main__':
    app.run(port=8000, debug=True)