from flask import Flask, jsonify, render_template_string
from logger import ExceptionLogger
from dotenv import load_dotenv
import traceback


load_dotenv()

app = Flask(__name__)

@app.route('/')
def welcome():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Flask App</title>
    </head>
    <body>
        <h1>Welcome to the Flask App!</h1>
        <ul>
            <li><a href="/trigger_exception">Trigger Exception</a></li>
            <li><a href="/trigger_custom_exception">Trigger Custom Exception</a></li>
            <li><a href="/trigger_type_error">Trigger Type Error</a></li>
            <li><a href="/trigger_key_error">Trigger Key Error</a></li>
        </ul>
    </body>
    </html>
    """
    return render_template_string(html_content)

@app.route('/trigger_exception')
def trigger_exception():
    try:
        # This will raise a ZeroDivisionError
        1 / 0
    except Exception as e:
        # Capture the exception and stack trace
        message = str(e)
        stack_trace = traceback.format_exc()

        # Log the exception
        with ExceptionLogger() as logger:
            logger.log_exception(message, stack_trace)

        return jsonify({"error": "An exception occurred and was logged."}), 500

@app.route('/trigger_custom_exception')
def trigger_custom_exception():
    try:
        # This will raise a custom exception
        raise ValueError("This is a custom exception")
    except Exception as e:
        # Capture the exception and stack trace
        message = str(e)
        stack_trace = traceback.format_exc()

        # Log the exception
        with ExceptionLogger() as logger:
            logger.log_exception(message, stack_trace)

        return jsonify({"error": "A custom exception occurred and was logged."}), 500

@app.route('/trigger_type_error')
def trigger_type_error():
    try:
        # This will raise a TypeError
        result = 'string' + 10
    except Exception as e:
        # Capture the exception and stack trace
        message = str(e)
        stack_trace = traceback.format_exc()

        # Log the exception
        with ExceptionLogger() as logger:
            logger.log_exception(message, stack_trace)

        return jsonify({"error": "A TypeError occurred and was logged."}), 500

@app.route('/trigger_key_error')
def trigger_key_error():
    try:
        # This will raise a KeyError
        my_dict = {'key': 'value'}
        value = my_dict['non_existent_key']
    except Exception as e:
        # Capture the exception and stack trace
        message = str(e)
        stack_trace = traceback.format_exc()

        # Log the exception
        with ExceptionLogger() as logger:
            logger.log_exception(message, stack_trace)

        return jsonify({"error": "A KeyError occurred and was logged."}), 500

if __name__ == '__main__':
    app.run(debug=True)
