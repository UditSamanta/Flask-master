from flask import Flask, jsonify, request
app = Flask(__name__)
tasks = [
    {
        'id' : 1, 
        'title' : 'Study Science',
        'description' : 'Chap 5',
        'done' : False,
    }
]
@app.route('/')
def hello_world():
    return 'Welcome to MY task Lists'
    
@app.route('/get-data')
def get_task():
    return jsonify({
        'data' : tasks
    })

@app.route('/add-data', methods = ['POST'])

def add_task():
    if not request.json:
        return jsonify({
            "status" : "ERROR",
            "message" : "Please Provide The DATA"
        })

    task = {
        'id' : tasks[-1]['id'] + 1, 
        'title' : request.json['title'],
        'description' : request.json.get('description', ""),
        'done' : False
    }
    tasks.append(task)
    return jsonify({
        "status" : "SUCCESS",
        "message" : "Task Added Succssfully"
    })

if(__name__ == '__main__'):
    app.run(debug = True)


