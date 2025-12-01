from flask import Flask, request, jsonify

app = Flask(__name__)

database = []

#  CREATE 
@app.route("/add", methods=["POST"])
def add_item():
    data = request.get_json()
    database.append(data)
    return jsonify({"message": "Item added successfully", "data": data}), 201


#  READ ALL 
@app.route("/items", methods=["GET"])
def get_items():
    return jsonify({"items": database}), 200


# READ SINGLE 
@app.route("/item/<int:item_id>", methods=["GET"])
def get_item(item_id):
    if 0 <= item_id < len(database):
        return jsonify(database[item_id]), 200
    return jsonify({"error": "Item not found"}), 404


#  UPDATE 
@app.route("/update/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    if 0 <= item_id < len(database):
        new_data = request.get_json()
        database[item_id].update(new_data)
        return jsonify({"message": "Item updated", "item": database[item_id]}), 200
    return jsonify({"error": "Item not found"}), 404


#  DELETE 
@app.route("/delete/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    if 0 <= item_id < len(database):
        removed = database.pop(item_id)
        return jsonify({"message": "Item deleted", "deleted_item": removed}), 200
    return jsonify({"error": "Item not found"}), 404


#  ROOT 
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Flask REST API is running"})


if __name__ == "__main__":
    app.run(debug=True)
