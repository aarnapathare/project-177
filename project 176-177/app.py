templates = [
    {
        "inputs": 5, 
        "category": "Sports", 
        "Word": "Chess"
    }, 
    {
        "inputs": 6, 
        "category":"European Country Name", 
        "word":"France"
    }
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get-template")
def get_template():
    return jsonify({
        "status":"success",
        "word": random.choice(templates)
    })