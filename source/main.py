import datetime
from contextlib import nullcontext
from flask import Flask, jsonify, redirect, request, render_template, session, url_for
import json
from passlib.hash import sha256_crypt
import secrets

# Trying out the datatime module for recording when orders are placed
# date = str(datetime.date.today())
# split_date = date.split("-")
# new_date = split_date[1] + "/" + split_date[2] + "/" + split_date[0]
# print(f"Was {date}, is now {new_date}")

# secret key for the flask session
secret_key = secrets.token_hex(32)

# creating the flask app
app = Flask(__name__)
app.config["DEBUG"] = True
app.secret_key = secret_key

# --- Shopping cart configuration ---

TAX_RATE = 0.07       # 7% sales tax (change if needed)
SHIPPING_FLAT = 0.00  # flat shipping for now; can tweak later


def load_database():
    """Load the entire database.json file."""
    with open("database.json", "r") as f:
        return json.load(f)

def get_inventory():
    """Return the list of inventory items from the database."""
    db = load_database()
    unsorted_inv = db.get("inventory", [])
    sorted_inv = []
    for item in unsorted_inv:
        if sorted_inv == []:
            sorted_inv.append(item)
        else:
            for sorted_item in sorted_inv:
                if item["cost"] > sorted_item["cost"]:
                    sorted_inv.insert(sorted_inv.index(sorted_item), item)
                    break
                elif len(sorted_inv)-1 == sorted_inv.index(sorted_item):
                    sorted_inv.append(item)
                    break
    return sorted_inv

def get_available_inventory():
    """Return the list of available inventory items from the database."""
    inventory = get_inventory()
    db = load_database()
    order_items = db.get("orders_inventory_items", [])
    available_inv = []
    for item in inventory:
        available = True
        for order_item in order_items:
            if item["item_id"] == order_item["item_id"]:
                available == False
                break
        if available:
            available_inv.append(item)

    return available_inv


def get_cart():
    """
    Get the cart from the session.

    Structure:
    session['cart'] = {
        "1": {"item_id": 1, "name": "...", "price": 176.53, "quantity": 2, "img": "..."},
        ...
    }
    """
    return session.get("cart", {})


def save_cart(cart):
    """Save the cart back into the session."""
    session["cart"] = cart


# Used this to populate the database and test hashing
# with open("database.json", 'r') as f:
#     database = json.load(f)
#
#     users = []
#
#     user = {}
#
#     user["user_id"] = 1
#     user["first_name"] = "Jerry"
#     user["last_name"] = "Seinfeld"
#     user["username"] = "admin"
#     password = "admin123!"
#     hashed_pw = sha256_crypt.hash(password)
#     user["password"] = hashed_pw
#     user["is_admin"] = True
#     address = {}
#     address["street"] = "123 Apple Street"
#     address["city"] = "New York"
#     address["state"] = "NY"
#     address["zip"] = "12345"
#     user["address"] = address.copy()
#     user["phone"] = "4405786974"
#     users.append(user.copy())
#
#     user["user_id"] = 2
#     user["first_name"] = "John"
#     user["last_name"] = "Badon"
#     user["username"] = "User001"
#     password = "strngp@55w0rd"
#     hashed_pw = sha256_crypt.hash(password)
#     user["password"] = hashed_pw
#     user["is_admin"] = False
#     address = {}
#     address["street"] = "1 Main Street"
#     address["city"] = "Newark"
#     address["state"] = "NJ"
#     address["zip"] = "54321"
#     user["address"] = address.copy()
#     user["phone"] = "6784568871"
#     users.append(user.copy())
#
#     user["user_id"] = 3
#     user["first_name"] = "Chase"
#     user["last_name"] = "McCoy"
#     user["username"] = "User002"
#     password = "un6355@ble"
#     hashed_pw = sha256_crypt.hash(password)
#     user["password"] = hashed_pw
#     user["is_admin"] = False
#     address = {}
#     address["street"] = "55 Oak Tree Lane"
#     address["city"] = "Nowhere"
#     address["state"] = "OK"
#     address["zip"] = "82945"
#     user["address"] = address.copy()
#     user["phone"] = "918456735"
#     users.append(user.copy())
#
#     database["users"] = users
#
#     inventory = []
#
#     inventory_item = {}
#     inventory_item["item_id"] = 1
#     inventory_item["name"] = "IWRL6432AOP"
#     inventory_item["description"] = ("Category: Industrial\n \
#                                      Op Temp (°C): -40 to 105\n \
#                                      Pin Count: 101\n \
#                                      Package Area (mm^2): 73.03")
#     inventory_item["cost"] = float("{:.2f}".format(176.53))
#     inventory_item["img"] = ("https://www.ti.com/content/dam/ticom/images/products/ic/radar/evm-board/iwrl6432aopevm-angled.png")
#
#     inventory.append(inventory_item.copy())
#
#     print(database["inventory"][0])
#
#     inventory_item["item_id"] = 2
#     inventory_item["name"] = "AWR2944P"
#     inventory_item["description"] = ("Category: Automotive\n \
#                                          Op Temp (°C): -40 to 140\n \
#                                          Pin Count: 266\n \
#                                          Package Area (mm^2): 1728.00")
#     inventory_item["cost"] = float("{:.2f}".format(1122.17))
#     inventory_item["img"] = ("https://www.mouser.com/images/texasinstruments/hd/AWR2944PEVM_SPL.jpg")
#
#     inventory.append(inventory_item.copy())
#
#     inventory_item["item_id"] = 3
#     inventory_item["name"] = "AWRL6844"
#     inventory_item["description"] = ("Category: Automotive\n \
#                                              Op Temp (°C): -40 to 140\n \
#                                              Pin Count: 207\n \
#                                              Package Area (mm^2): 82.81")
#     inventory_item["cost"] = float("{:.2f}".format(299.00))
#     inventory_item["img"] = ("https://www.ti.com/content/dam/ticom/images/products/ic/radar/evm-board/awrl6844evm-angled.png")
#
#     inventory.append(inventory_item.copy())
#
#     inventory_item["item_id"] = 4
#     inventory_item["name"] = "AWR2544"
#     inventory_item["description"] = ("Category: Automotive\n \
#                                                  Op Temp (°C): -40 to 140\n \
#                                                  Pin Count: 248\n \
#                                                  Package Area (mm^2): 148.8")
#     inventory_item["cost"] = float("{:.2f}".format(661.45))
#     inventory_item["img"] = ("https://www.mouser.co.il/images/texasinstruments/hd/AWR2544LOPEVM_SPL.JPG")
#
#     inventory.append(inventory_item.copy())
#
#     inventory_item["item_id"] = 5
#     inventory_item["name"] = "IWRL1432"
#     inventory_item["description"] = ("Category: Industrial\n \
#                                                      Op Temp (°C): -40 to 105\n \
#                                                      Pin Count: 102\n \
#                                                      Package Area (mm^2): 41.60")
#     inventory_item["cost"] = float("{:.2f}".format(337.36))
#     inventory_item["img"] = ("https://www.ti.com/content/dam/ticom/images/products/ic/radar/evm-board/iwrl1432boost-bsd-angled.png")
#
#     inventory.append(inventory_item.copy())
#
#     inventory_item["item_id"] = 6
#     inventory_item["name"] = "AWRL1432"
#     inventory_item["description"] = ("Category: Automotive\n \
#                                                          Op Temp (°C): -40 to 125\n \
#                                                          Pin Count: 102\n \
#                                                          Package Area (mm^2): 41.60")
#     inventory_item["cost"] = float("{:.2f}".format(481.38))
#     inventory_item["img"] = ("https://www.ti.com/content/dam/ticom/images/products/ic/radar/evm-board/awrl1432boost-bsd-angled.png")
#
#     inventory.append(inventory_item.copy())
#     database["inventory"] = inventory
#
#     orders = []
#
#     order = {}
#
#     order["order_id"] = 1
#     order["purchaser_id"] = 2
#     order["date"] = "8/8/2025"
#     order["sub_total"] = float("{:.2f}".format(673.53))
#     order["tax"] = float("{:.2f}".format(40.41))
#     order["shipping"] = float("{:.2f}".format(19.00))
#     order["total"] = float("{:.2f}".format(732.94))
#
#     orders.append(order.copy())
#
#     order["order_id"] = 2
#     order["purchaser_id"] = 3
#     order["date"] = "9/21/2025"
#     order["sub_total"] = float("{:.2f}".format(176.53))
#     order["tax"] = float("{:.2f}".format(10.59))
#     order["shipping"] = float("{:.2f}".format(29.00))
#     order["total"] = float("{:.2f}".format(216.12))
#
#     orders.append(order.copy())
#     database["orders"] = orders
#
#     orders_inventory_items = []
#
#     orders_inventory_item = {}
#     orders_inventory_item["order_id"] = 1
#     orders_inventory_item["item_id"] = 7
#
#     orders_inventory_items.append(orders_inventory_item.copy())
#
#     orders_inventory_item["order_id"] = 1
#     orders_inventory_item["item_id"] = 8
#
#     orders_inventory_items.append(orders_inventory_item.copy())
#
#     orders_inventory_item["order_id"] = 2
#     orders_inventory_item["item_id"] = 9
#
#     orders_inventory_items.append(orders_inventory_item.copy())
#     database["orders_inventory_items"] = orders_inventory_items
#
# with open("database.json", 'w') as f:
#     json.dump(database, f, indent=4)
#
# with open("database.json", 'r') as f:
#     database = json.load(f)
#     users = database["users"]
#     for i in range(len(users)):
#         user_one = database["users"][i]
#         print(f"\n\n{user_one['username']}\n")
#         print(f"Is the password 'password'? {sha256_crypt.verify('password', user_one['password'])}")
#         print(f"Is the password 'admin123!'? {sha256_crypt.verify('admin123!', user_one['password'])}")
#         print(f"Is the password 'Admin123!'? {sha256_crypt.verify('Admin123!', user_one['password'])}")
#         print(f"Is the password 'strngp@55w0rd'? {sha256_crypt.verify('strngp@55w0rd', user_one['password'])}")
#         print(f"Is the password 'un6355@ble'? {sha256_crypt.verify('un6355@ble', user_one['password'])}")


# function that creates the user, mostly just to de-clutter code
def create_user(first_name, last_name, users, username, password):
    new_user = {}
    new_user['user_id'] = users[-1]['user_id'] + 1
    new_user['first_name'] = first_name
    new_user['last_name'] = last_name
    new_user['username'] = username
    hashed_pw = sha256_crypt.hash(password)
    new_user['password'] = hashed_pw
    new_user['is_admin'] = False
    new_user['address'] = {}
    new_user['phone'] = ""
    return new_user


# default route, redirects to login
@app.route('/')
def beginning():
    return redirect(url_for('login'))


# login
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # when the login form is filled out, we go here
        # getting username and password for verification
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()
        with open("database.json", 'r') as f:
            database = json.load(f)
            users = database['users']
            match = {}
            for user in users:
                # looking for an existing account that matches the entered
                # username
                if user['username'] == username:
                    match = user
                    break
            if match == {}:
                # Re-renders the login page with "No account with that username."
                # error message if no account is associated with the username
                return render_template('login.html', message="No account with that username.", msg_color="red")
            if not sha256_crypt.verify(password, match['password']):
                # Re-renders the login page with "Incorrect password." error
                # message if the entered password doesn't match the one associated
                # with the account.
                return render_template('login.html', message="Incorrect password.", msg_color="red")

            # if the username is valid and the password is correct, the user
            # gets logged in by adding some account values to the session
            session['is_admin'] = match['is_admin']
            session['user_id'] = match['user_id']
            session['first_name'] = match['first_name']
            session['username'] = match['username']
            session['address'] = match['address']
            session['phone'] = match['phone']

        # clearing sensitive info
        database = None
        users = None
        # redirecting to the main page
        return redirect(url_for('main'))

    else:
        # all other methods simply render the login page with the standard message
        return render_template('login.html', message="Great to See You Again!", msg_color="light-grey")


# registration
@app.route('/registration', methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        username = request.form.get('username').strip()
        password = request.form.get('password').strip()
        with open("database.json", 'r') as f:
            database = json.load(f)
            users = database['users']
            for user in users:
                # here we check if the username is already taken
                if user['username'] == username:
                    # Re-renders registration page with the "Username already registered"
                    # error message
                    return render_template('registration.html', message="Username already registered", msg_color="red")
            if len(password) < 6:
                # Re-renders registration page with the "Password must be at least six characters long"
                # error message if the password is under six characters
                return render_template('registration.html', message="Password must be at least six characters long", msg_color="red")

            # Grabs the first and last names
            first_name = request.form.get('first_name').strip()
            last_name = request.form.get('last_name').strip()

            # Creates a new user with the create_user() function
            new_user = create_user(first_name, last_name, users, username, password)

            # adding new user to database
            users.append(new_user)
            database['users'] = users

            # if the username is unique and the password is more than six characters,
            # the user gets logged in by adding some account values to the session.
            # 'is_admin' is False by default as the account is brand new
            session['is_admin'] = False
            session['user_id'] = new_user['user_id']
            session['first_name'] = new_user['first_name']
            session['username'] = new_user['username']
            session['address'] = new_user['address']
            session['phone'] = new_user['phone']

        with open("database.json", 'w') as f:
            # adding new user to database
            json.dump(database, f, indent=4)
        database = None
        users = None
        return redirect(url_for('main'))

    else:
        return render_template('registration.html', message="Welcome to Circuit Breakers!", msg_color="light-grey")


@app.route('/main', methods=["GET", "POST"])
def main():
    # Load inventory and cart so the main page can show the shop section
    inventory = get_available_inventory()
    cart = get_cart()
    cart_count = sum(item["quantity"] for item in cart.values())

    if session['is_admin']:
        is_disabled = "false"
        state = "active"
        is_visible = "visible"
    else:
        is_disabled = "true"
        state = "disabled"
        is_visible = "hidden"

    if request.method == "POST":
        return render_template(
            'main.html',
            is_admin=session["is_admin"],
            first_name=session["first_name"],
            username=session["username"],
            is_disabled=is_disabled,
            state=state,
            inventory=inventory,
            cart_count=cart_count,
            is_visible=is_visible,
            any_results=True,
        )
    else:
        return render_template(
            'main.html',
            is_admin=session["is_admin"],
            first_name=session["first_name"],
            username=session["username"],
            is_disabled=is_disabled,
            state=state,
            inventory=inventory,
            cart_count=cart_count,
            is_visible=is_visible,
            any_results=True,
        )


@app.route('/search', methods=["GET", "POST"])
def search():
    inventory = get_available_inventory()
    cart = get_cart()
    cart_count = sum(item["quantity"] for item in cart.values())

    if session['is_admin']:
        is_disabled = "false"
        state = "active"
        is_visible = "visible"
    else:
        is_disabled = "true"
        state = "disabled"
        is_visible = "hidden"

    if request.method == "POST":
        query = request.form.get('query').strip()
        query = query.lower()
        query_list = query.split()

        search_results = []
        for query in query_list:
            for item in inventory:
                if query in item["name"].lower() or query in item["description"].lower():
                    if query_list.index(query) == 0:
                        search_results.append(item)
                elif item in search_results:
                    search_results.remove(item)

        if search_results != []:
            any_results = True
        else:
            any_results = False

        return render_template(
            'main.html',
            is_admin=session["is_admin"],
            first_name=session["first_name"],
            username=session["username"],
            is_disabled=is_disabled,
            state=state,
            inventory=search_results,
            cart_count=cart_count,
            is_visible=is_visible,
            any_results=any_results,
            search=True,
            query=request.form.get('query').strip(),
        )

    else:
        return render_template(
            'main.html',
            is_admin=session["is_admin"],
            first_name=session["first_name"],
            username=session["username"],
            is_disabled=is_disabled,
            state=state,
            inventory=inventory,
            cart_count=cart_count,
            is_visible=is_visible,
            any_results=True,
        )

@app.route('/admin', methods=["GET", "POST"])
def admin():
    return render_template('admin.html', is_admin=session["is_admin"])


# --- Shop / Cart routes ---

def shop():
    """
    Display inventory items with 'Add to Cart' buttons.
    """
    inventory = get_inventory()
    cart = get_cart()
    cart_count = sum(item["quantity"] for item in cart.values())

    return render_template(
        "shop.html",
        inventory=inventory,
        cart_count=cart_count,
        username=session.get("username"),  # optional
    )


@app.route("/add_to_cart/<int:item_id>", methods=["POST"])
def add_to_cart(item_id):
    """
    Add a single item to the cart by item_id.
    """
    inventory = get_inventory()
    cart = get_cart()

    # Find the item in inventory
    item = next((i for i in inventory if i["item_id"] == item_id), None)
    if item is None:
        # If item_id invalid, just go back to the shop
        return redirect(url_for("shop"))

    key = str(item_id)

    if key in cart:
        cart[key]["quantity"] += 1
    else:
        cart[key] = {
            "item_id": item["item_id"],
            "name": item["name"],
            "price": float(item["cost"]),
            "quantity": 1,
            "img": item["img"],
        }

    save_cart(cart)

    # Redirect back to the page they were on, or the shop
    return redirect(request.referrer or url_for("shop"))


@app.route("/cart", methods=["GET", "POST"])
def cart():
    """
    Show the shopping cart and allow quantity updates / removals.

    - GET: display cart
    - POST: process quantity changes and removals
    """
    cart = get_cart()

    if request.method == "POST":
        # Update quantities / removals
        for key, item in list(cart.items()):
            qty_str = request.form.get(f"qty_{key}")
            remove = request.form.get(f"remove_{key}")

            if remove:
                del cart[key]
                continue

            if qty_str is not None:
                try:
                    qty = int(qty_str)
                    if qty <= 0:
                        del cart[key]
                    else:
                        item["quantity"] = qty
                except ValueError:
                    # Ignore bad input and keep old quantity
                    pass

        save_cart(cart)

    # Build a list for the template and calculate totals
    items = []
    for key, item in cart.items():
        line_total = item["price"] * item["quantity"]
        temp = item.copy()
        temp["key"] = key        # used for form field names
        temp["line_total"] = line_total
        items.append(temp)

    subtotal = sum(i["line_total"] for i in items)
    tax = round(subtotal * TAX_RATE, 2)
    shipping = SHIPPING_FLAT if items else 0.0
    total = round(subtotal + tax + shipping, 2)
    cart_count = sum(i["quantity"] for i in items)

    return render_template(
        "cart.html",
        items=items,
        subtotal=subtotal,
        tax=tax,
        shipping=shipping,
        total=total,
        cart_count=cart_count,
        username=session.get("username"),
    )



# Optional: if you want to run with `python main.py`
if __name__ == "__main__":
    app.run()
