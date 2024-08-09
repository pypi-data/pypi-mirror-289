from flask import Flask, request, jsonify
import logging
from .config import db_config, API_KEY
from .models import ExceptionLogger  # Import ExceptionLogger from models
import mysql.connector

def create_app():
    app = Flask(__name__)

    # Logger setup
    logging.basicConfig(level=logging.INFO)

    @app.before_request
    def verify_api_key():
        if request.headers.get("API-Key") != API_KEY:
            return jsonify({"error": "Unauthorized"}), 401

    @app.route('/log_exception', methods=['POST'])
    def log_exception():
        try:
            data = request.get_json()

            if not data or 'message' not in data or 'stack_trace' not in data:
                return jsonify({"error": "Invalid exception data"}), 400

            message = data['message']
            stack_trace = data['stack_trace']

            # Use ExceptionLogger class
            logger = ExceptionLogger()
            logger.log_exception(message, stack_trace)

            logging.info("Exception logged successfully")
            return jsonify({"message": "Exception logged successfully"}), 200

        except mysql.connector.Error as err:
            logging.error(f"Database error: {err}")
            return jsonify({"error": f"Database error: {err}"}), 500

        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            return jsonify({"error": f"Unexpected error: {e}"}), 500

    return app

# Entry point for Flask CLI
if __name__ == '__main__':
    create_app().run(debug=True)
