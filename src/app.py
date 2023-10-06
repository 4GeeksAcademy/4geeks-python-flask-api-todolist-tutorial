from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos), 202
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ", position)
    todos.pop(position -1)
    return jsonify(todos)

# int --- It is there to say that it expects an integer
# -1 --- Since list indices start from 0,  position - 1  is used to adjust the position accordingly. 


# These two lines should always be at the end of your app.py file
# if __name__ == '__main__': is for app.run not to be run all the time
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

# pipenv run python src/app.py

# host='0.0.0.0': This specifies the host address on which the application should listen for incoming requests. In this case, '0.0.0.0' means the application will listen on all available network interfaces. This allows the application to be accessible from any IP address.

# port=3245: This sets the port number on which the application should listen for incoming requests. In this case, the application will listen on port 3245. You can choose any available port number that suits your needs.

# debug=True: Enabling debug mode provides additional features during development, such as detailed error messages and automatic reloading of the application when code changes are detected. It is recommended to set debug=True during development but not in production.

# When you execute app.run(), the Flask development server starts and listens for incoming HTTP requests on the specified host and port. Once the server is running, you can access your Flask application by visiting the host address and port number in a web browser or by sending HTTP requests programmatically.