from flask import Flask, render_template, request, make_response, jsonify


# create an instance for your flask app
app = Flask(__name__)


# Ice cream shop orders
order = {
    "order1": {
        "Size": "Small",
        "Flavour": "Chocolate",
        "Container": "Cup"
    },
    "order2": {
        "Size": "Medium",
        "Flavour": "Coffee",
        "Container": "Crisp Cone"
    }
}


@app.route("/orders")
def get_order():
    response = make_response(jsonify(order), 200)
    return response


"""
Get order details using order id
"""
@app.route("/orders/<orderid>")
def get_order_details(orderid):
    if orderid in order:
        response = make_response(jsonify(order[orderid]), 200)
        return response
    return "Order not found"


"""
Get order items using order id
"""
@app.route("/orders/<orderid>/<items>")
def get_item_details(orderid, items):
    item = order[orderid].get(items)
    if item:
        response = make_response(jsonify(item), 200)
        return response
    return "Item not found"


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)