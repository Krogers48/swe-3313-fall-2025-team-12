import datetime
from contextlib import nullcontext
from flask import Flask, jsonify, redirect, request, render_template, session, url_for, Response
import json
from passlib.hash import sha256_crypt
import secrets
import csv
import io
import os
import smtplib
import ssl
from email.message import EmailMessage

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


def save_database(db):
    """Write the entire database back to database.json."""
    with open("database.json", "w") as f:
        json.dump(db, f, indent=4)


def get_inventory():
    """Return the list of inventory items from the database, sorted by cost descending."""
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
                elif len(sorted_inv) - 1 == sorted_inv.index(sorted_item):
                    sorted_inv.append(item)
                    break
    return sorted_inv


def get_available_inventory():
    """
    Return the list of available inventory items from the database.

    Items that appear in orders_inventory_items are considered sold and
    are not returned here.
    """
    cart = get_cart()
    inventory = get_inventory()
    db = load_database()
    order_items = db.get("orders_inventory_items", [])
    available_inv = []
    for item in inventory:
        available = True
        for order_item in order_items:
            if item["item_id"] == order_item["item_id"]:
                # FIX: must be assignment, not comparison
                available = False
                break
        for cart_item in cart:
            if item["item_id"] == cart.get(cart_item).get("item_id"):
                available = False
                break
        if available:
            available_inv.append(item)

    return available_inv


def get_cart():
    """
    Get the cart from the session.

    session['cart'] = {
        "1": {"item_id": 1, "name": "...", "price": 176.53, "quantity": 1, "img": "..."},
        ...
    }
    """
    return session.get("cart", {})


def save_cart(cart):
    """Save the cart back into the session."""
    session["cart"] = cart


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


def send_receipt_email(to_email, order, items, purchaser_name, shipping_address, card_last4):
    print("DEBUG: send_receipt_email() called")

    smtp_server = os.environ.get("SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.environ.get("SMTP_PORT", "587"))
    smtp_user = os.environ.get("SMTP_USER")
    smtp_password = os.environ.get("SMTP_PASSWORD")
    smtp_from = os.environ.get("SMTP_FROM", smtp_user)

    print("DEBUG: to_email =", to_email)
    print("DEBUG: smtp_server =", smtp_server)
    print("DEBUG: smtp_user =", smtp_user)

    if not smtp_user or not smtp_password:
        print("ERROR: SMTP_USER or SMTP_PASSWORD not set; skipping email send.")
        return

    # Build the plain-text email body
    lines = []
    lines.append(f"Hello {purchaser_name},")
    lines.append("")
    lines.append("Thank you for your purchase from Circuit Breakers!")
    lines.append("")
    lines.append(f"Order ID: {order['order_id']}")
    lines.append(f"Order Date: {order['date']}")
    lines.append("")
    lines.append("Shipping Address:")
    if shipping_address:
        lines.append(f"  {shipping_address.get('street', '')}")
        city = shipping_address.get("city", "")
        state = shipping_address.get("state", "")
        zip_code = shipping_address.get("zip", "")
        lines.append(f"  {city}, {state} {zip_code}")
    else:
        lines.append("  (no address on file)")
    lines.append("")

    if card_last4:
        lines.append(f"Payment Method: Card ending in {card_last4}")
    else:
        lines.append("Payment Method: Card (last four digits unavailable)")
    lines.append("")

    lines.append("Items Purchased:")
    if items:
        for item in items:
            # One of each item; just show name + price
            line_price = f"{item['price']:.2f}"
            lines.append(f"  - {item['name']}  ${line_price}")
    else:
        lines.append("  (no items found)")

    lines.append("")
    lines.append(f"Subtotal: ${order['sub_total']:.2f}")
    lines.append(f"Tax:      ${order['tax']:.2f}")
    lines.append(f"Shipping: ${order['shipping']:.2f}")
    lines.append(f"Total:    ${order['total']:.2f}")
    lines.append("")
    lines.append("This is an automated receipt from Circuit Breakers.")
    lines.append("Thank you for shopping with us!")

    body = "\n".join(lines)

    msg = EmailMessage()
    msg["Subject"] = f"Your Circuit Breakers Receipt - Order #{order['order_id']}"
    msg["From"] = smtp_from
    msg["To"] = to_email
    msg.set_content(body)

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.send_message(msg)

    print(f"DEBUG: Receipt email sent successfully to {to_email}")


# default route, redirects to login
@app.route('/')
def beginning():
    return redirect(url_for('login'))


# login
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # getting username and password for verification
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        db = load_database()
        users = db.get('users', [])
        match = {}
        for user in users:
            if user['username'] == username:
                match = user
                break

        if match == {}:
            return render_template('login.html', message="No account with that username.", msg_color="red")

        if not sha256_crypt.verify(password, match['password']):
            return render_template('login.html', message="Incorrect password.", msg_color="red")

        # log user in
        session['is_admin'] = match['is_admin']
        session['user_id'] = match['user_id']
        session['first_name'] = match['first_name']
        session['username'] = match['username']
        session['address'] = match.get('address', {})
        session['phone'] = match.get('phone', "")

        return redirect(url_for('main'))

    else:
        return render_template('login.html', message="Great to See You Again!", msg_color="light-grey")


# registration
@app.route('/registration', methods=["GET", "POST"])
def registration():
    if request.method == "POST":
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        db = load_database()
        users = db.get('users', [])

        for user in users:
            if user['username'] == username:
                return render_template('registration.html', message="Username already registered", msg_color="red")

        if len(password) < 6:
            return render_template(
                'registration.html',
                message="Password must be at least six characters long",
                msg_color="red"
            )

        # Grabs the first and last names
        first_name = request.form.get('first_name', '').strip()
        last_name = request.form.get('last_name', '').strip()

        # Creates a new user with the create_user() function
        new_user = create_user(first_name, last_name, users, username, password)

        # adding new user to database
        users.append(new_user)
        db['users'] = users
        save_database(db)

        # log them in
        session['is_admin'] = False
        session['user_id'] = new_user['user_id']
        session['first_name'] = new_user['first_name']
        session['username'] = new_user['username']
        session['address'] = new_user['address']
        session['phone'] = new_user['phone']

        return redirect(url_for('main'))

    else:
        return render_template('registration.html', message="Welcome to Circuit Breakers!", msg_color="light-grey")


@app.route('/main', methods=["GET", "POST"])
def main():
    # Load inventory and cart so the main page can show the shop section
    inventory = get_available_inventory()
    cart = get_cart()
    cart_count = sum(item["quantity"] for item in cart.values())

    if session.get('is_admin'):
        is_disabled = "false"
        state = "active"
        is_visible = "visible"
    else:
        is_disabled = "true"
        state = "disabled"
        is_visible = "hidden"

    # Always render main; any_results=True by default
    return render_template(
        'main.html',
        is_admin=session.get("is_admin", False),
        first_name=session.get("first_name", ""),
        username=session.get("username", ""),
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

    if session.get('is_admin'):
        is_disabled = "false"
        state = "active"
        is_visible = "visible"
    else:
        is_disabled = "true"
        state = "disabled"
        is_visible = "hidden"

    if request.method == "POST":
        raw_query = request.form.get('query', '').strip()
        if raw_query == "":
            return render_template(
                'main.html',
                is_admin=session.get("is_admin", False),
                first_name=session.get("first_name", ""),
                username=session.get("username", ""),
                is_disabled=is_disabled,
                state=state,
                inventory=inventory,
                cart_count=cart_count,
                is_visible=is_visible,
                any_results=True,
            )
        query_lower = raw_query.lower()
        query_list = query_lower.split()

        search_results = []
        for q in query_list:
            for item in inventory:
                if q in item["name"].lower() or q in item["description"].lower():
                    if item not in search_results:
                        search_results.append(item)

        any_results = bool(search_results)

        return render_template(
            'main.html',
            is_admin=session.get("is_admin", False),
            first_name=session.get("first_name", ""),
            username=session.get("username", ""),
            is_disabled=is_disabled,
            state=state,
            inventory=search_results if any_results else [],
            cart_count=cart_count,
            is_visible=is_visible,
            any_results=any_results,
            search=True,
            query=raw_query,
        )

    # GET: just show normal inventory
    return render_template(
        'main.html',
        is_admin=session.get("is_admin", False),
        first_name=session.get("first_name", ""),
        username=session.get("username", ""),
        is_disabled=is_disabled,
        state=state,
        inventory=inventory,
        cart_count=cart_count,
        is_visible=is_visible,
        any_results=True,
    )

@app.route("/user", methods=["GET", "POST"])
def user_settings():
    if "user_id" not in session:
        return redirect(url_for("login"))

    db = load_database()
    users = db.get("users", [])
    user_id = session.get("user_id")

    current_user = next((u for u in users if u["user_id"] == user_id), None)

    if not current_user:
        return redirect(url_for("main"))

    if request.method == "POST":
        # Get updated fields
        first = request.form.get("first_name", "").strip()
        last = request.form.get("last_name", "").strip()
        street = request.form.get("street", "").strip()
        city = request.form.get("city", "").strip()
        state = request.form.get("state", "").strip()
        zipcode = request.form.get("zip", "").strip()
        phone = request.form.get("phone", "").strip()

        # Optional password change
        new_pw = request.form.get("new_password", "").strip()
        if new_pw:
            current_user["password"] = sha256_crypt.hash(new_pw)

        # Update user
        current_user["first_name"] = first
        current_user["last_name"] = last
        current_user["phone"] = phone
        current_user["address"] = {
            "street": street,
            "city": city,
            "state": state,
            "zip": zipcode
        }

        # Save DB
        db["users"] = users
        save_database(db)

        # Update session
        session["first_name"] = first
        session["address"] = current_user["address"]
        session["phone"] = phone

        return render_template(
            "user.html",
            username=session.get("username"),
            first_name=first,
            updated=True,
            user=current_user,
        )

    return render_template(
        "user.html",
        username=session.get("username"),
        first_name=session.get("first_name"),
        user=current_user,
        updated=False
    )


@app.route('/admin', methods=["GET"])
def admin():
    # Admin dashboard: view users, inventory, and orders.
    if not session.get("is_admin"):
        return redirect(url_for("main"))

    db = load_database()
    users = db.get("users", [])
    inventory = db.get("inventory", [])
    orders = db.get("orders", [])

    # Attach purchaser_username to each order for display
    for order in orders:
        purchaser = next((u for u in users if u["user_id"] == order["purchaser_id"]), None)
        order["purchaser_username"] = purchaser["username"] if purchaser else "Unknown"

    return render_template(
        'admin.html',
        is_admin=True,
        username=session.get("username"),
        users=users,
        inventory=inventory,
        orders=orders,
    )


@app.route("/admin/export_sales", methods=["GET"])
def export_sales():
    # Export sales data to CSV (simulated for the admin).
    if not session.get("is_admin"):
        return redirect(url_for("main"))

    db = load_database()

    users = {u["user_id"]: u for u in db.get("users", [])}
    inventory = {item["item_id"]: item for item in db.get("inventory", [])}
    orders = db.get("orders", [])
    order_items = db.get("orders_inventory_items", [])

    # Map order_id -> list of item_ids
    items_by_order = {}
    for oi in order_items:
        oid = oi.get("order_id")
        iid = oi.get("item_id")
        if oid is None or iid is None:
            continue
        items_by_order.setdefault(oid, []).append(iid)

    # Build CSV in memory
    output = io.StringIO()
    writer = csv.writer(output)

    # Header row
    writer.writerow([
        "order_id",
        "purchaser_username",
        "date",
        "items",
        "subtotal",
        "tax",
        "shipping",
        "total",
    ])

    # Data rows
    for order in orders:
        oid = order.get("order_id")
        purchaser_id = order.get("purchaser_id")
        purchaser = users.get(purchaser_id)
        username = purchaser["username"] if purchaser else "Unknown"

        item_ids = items_by_order.get(oid, [])
        item_names = []
        for iid in item_ids:
            item = inventory.get(iid)
            if item:
                item_names.append(item.get("name", f"Item {iid}"))

        items_str = "; ".join(item_names)

        subtotal = float(order.get("sub_total", 0))
        tax_val = float(order.get("tax", 0))
        shipping_val = float(order.get("shipping", 0))
        total_val = float(order.get("total", 0))

        writer.writerow([
            oid,
            username,
            order.get("date", ""),
            items_str,
            f"{subtotal:.2f}",
            f"{tax_val:.2f}",
            f"{shipping_val:.2f}",
            f"{total_val:.2f}",
        ])

    csv_data = output.getvalue()
    output.close()

    return Response(
        csv_data,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=sales_report.csv"},
    )


@app.route("/admin/make_admin/<int:user_id>", methods=["POST"])
def make_admin(user_id):
    """Convert a user to admin after password verification."""
    if not session.get("is_admin"):
        return jsonify({"success": False, "error": "Unauthorized"}), 403

    admin_password = request.form.get("admin_password", "").strip()
    if not admin_password:
        return jsonify({"success": False, "error": "Password required"}), 400

    db = load_database()
    users = db.get("users", [])

    # Verify admin's password
    admin_user = next((u for u in users if u["user_id"] == session.get("user_id")), None)
    if not admin_user or not sha256_crypt.verify(admin_password, admin_user["password"]):
        return jsonify({"success": False, "error": "Incorrect password"}), 401

    # Find and update the target user
    target_user = next((u for u in users if u["user_id"] == user_id), None)
    if not target_user:
        return jsonify({"success": False, "error": "User not found"}), 404

    if target_user["is_admin"]:
        return jsonify({"success": False, "error": "User is already an admin"}), 400

    target_user["is_admin"] = True
    db["users"] = users
    save_database(db)

    return jsonify({"success": True, "username": target_user["username"]})


@app.route("/admin/inventory/add", methods=["POST"])
def add_inventory_item():
    """Add a new inventory item."""
    if not session.get("is_admin"):
        return redirect(url_for("main"))

    name = request.form.get("name", "").strip()
    description = request.form.get("description", "").strip()
    cost_str = request.form.get("cost", "").strip()
    img = request.form.get("img", "").strip()

    db = load_database()
    users = db.get("users", [])
    inventory = db.get("inventory", [])
    orders = db.get("orders", [])

    # Attach purchaser_username to each order for display
    for order in orders:
        purchaser = next((u for u in users if u["user_id"] == order["purchaser_id"]), None)
        order["purchaser_username"] = purchaser["username"] if purchaser else "Unknown"

    # Validation per requirements: name max 15 chars, description max 50 chars
    if not name or len(name) > 15:
        return render_template(
            "admin.html",
            is_admin=True,
            username=session.get("username"),
            users=users,
            inventory=inventory,
            orders=orders,
            error="Name is required and must be 15 characters or less.",
        )

    if not description or len(description) > 50:
        return render_template(
            "admin.html",
            is_admin=True,
            username=session.get("username"),
            users=users,
            inventory=inventory,
            orders=orders,
            error="Description is required and must be 50 characters or less.",
        )

    try:
        cost = float(cost_str)
        if cost < 0:
            raise ValueError("Cost must be non-negative")
    except (ValueError, TypeError):
        return render_template(
            "admin.html",
            is_admin=True,
            username=session.get("username"),
            users=users,
            inventory=inventory,
            orders=orders,
            error="Invalid price. Please enter a valid number.",
        )

    inventory = db.get("inventory", [])

    # Generate new item_id
    if inventory:
        next_id = max(item.get("item_id", 0) for item in inventory) + 1
    else:
        next_id = 1

    new_item = {
        "item_id": next_id,
        "name": name,
        "description": description,
        "cost": cost,
        "img": img if img else "",
    }

    inventory.append(new_item)
    db["inventory"] = inventory
    save_database(db)

    return redirect(url_for("admin"))


@app.route("/admin/inventory/edit/<int:item_id>", methods=["GET", "POST"])
def edit_inventory_item(item_id):
    """Edit an existing inventory item."""
    if not session.get("is_admin"):
        return redirect(url_for("main"))

    db = load_database()
    inventory = db.get("inventory", [])

    item = next((i for i in inventory if i["item_id"] == item_id), None)
    if not item:
        return redirect(url_for("admin"))

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        description = request.form.get("description", "").strip()
        cost_str = request.form.get("cost", "").strip()
        img = request.form.get("img", "").strip()

        # Validation
        if not name or len(name) > 15:
            return render_template(
                "admin_edit_item.html",
                item=item,
                error="Name is required and must be 15 characters or less.",
            )

        if not description or len(description) > 50:
            return render_template(
                "admin_edit_item.html",
                item=item,
                error="Description is required and must be 50 characters or less.",
            )

        try:
            cost = float(cost_str)
            if cost < 0:
                raise ValueError("Cost must be non-negative")
        except (ValueError, TypeError):
            return render_template(
                "admin_edit_item.html",
                item=item,
                error="Invalid price. Please enter a valid number.",
            )

        # Update item
        item["name"] = name
        item["description"] = description
        item["cost"] = cost
        item["img"] = img if img else ""

        db["inventory"] = inventory
        save_database(db)

        return redirect(url_for("admin"))

    # GET: show edit form
    return render_template(
        "admin_edit_item.html",
        item=item,
        error=None,
    )


@app.route("/admin/inventory/delete/<int:item_id>", methods=["POST"])
def delete_inventory_item(item_id):
    """Delete an inventory item (only if not sold)."""
    if not session.get("is_admin"):
        return jsonify({"success": False, "error": "Unauthorized"}), 403

    db = load_database()
    inventory = db.get("inventory", [])
    order_items = db.get("orders_inventory_items", [])

    # Check if item is already sold
    is_sold = any(oi.get("item_id") == item_id for oi in order_items)
    if is_sold:
        return jsonify({"success": False, "error": "Cannot delete item that has been sold"}), 400

    # Remove item
    inventory = [i for i in inventory if i["item_id"] != item_id]
    db["inventory"] = inventory
    save_database(db)

    return jsonify({"success": True})


@app.route("/admin/create_admin", methods=["GET", "POST"])
def admin_create_ui():
    """Admin Creation UI with search functionality."""
    if not session.get("is_admin"):
        return redirect(url_for("main"))

    db = load_database()
    users = db.get("users", [])

    search_query = ""
    filtered_users = users

    if request.method == "POST":
        search_query = request.form.get("search_query", "").strip().lower()
        if search_query:
            filtered_users = [
                u for u in users
                if search_query in u.get("username", "").lower()
            ]

    return render_template(
        "admin_create.html",
        username=session.get("username"),
        users=filtered_users,
        search_query=search_query,
    )


# --- Cart / Checkout routes ---


@app.route("/add_to_cart/<int:item_id>", methods=["POST"])
def add_to_cart(item_id):
    """
    Add a single item to the cart by item_id.

    NOTE: You can only have ONE of each item in the cart.
    If the item is already in the cart, we do NOT increment quantity.
    """
    inventory = get_inventory()
    cart = get_cart()

    # Find the item in inventory
    item = next((i for i in inventory if i["item_id"] == item_id), None)
    if item is None:
        # If item_id invalid, just go back to main
        return redirect(url_for("main"))

    key = str(item_id)

    if key not in cart:
        cart[key] = {
            "item_id": item["item_id"],
            "name": item["name"],
            "price": float(item["cost"]),
            "quantity": 1,
            "img": item["img"],
        }
    # else: already there, keep quantity at 1

    save_cart(cart)

    # Redirect back to the page they were on, or main if referrer is missing
    return redirect(request.referrer or url_for("main"))


@app.route("/cart", methods=["GET", "POST"])
def cart():
    # Show the shopping cart and allow removals.
    cart = get_cart()

    if request.method == "POST":
        # Update removals (quantities are effectively locked at 1 in the UI)
        for key, item in list(cart.items()):
            remove = request.form.get(f"remove_{key}")

            if remove:
                del cart[key]
                continue

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


@app.route("/checkout", methods=["GET", "POST"])
def checkout():
    print("DEBUG: entered /checkout, method =", request.method)

    cart = get_cart()
    if not cart:
        print("DEBUG: cart empty, redirecting to /cart")
        return redirect(url_for("cart"))

    db = load_database()
    users = db.get("users", [])
    user_id = session.get("user_id")
    current_user = next((u for u in users if u["user_id"] == user_id), None)

    # Pre-fill address, phone if available
    if current_user:
        address = current_user.get("address", {}) or {}
        phone = current_user.get("phone", "")
    else:
        address = {}
        phone = ""

    # Build a list of items with line totals for display and calculation
    items = []
    for item in cart.values():
        line_total = item["price"] * item["quantity"]
        temp = item.copy()
        temp["line_total"] = line_total
        items.append(temp)

    subtotal = sum(i["line_total"] for i in items)
    tax = round(subtotal * TAX_RATE, 2)
    shipping = SHIPPING_FLAT if items else 0.0
    total = round(subtotal + tax + shipping, 2)

    if request.method == "POST":
        print("DEBUG: handling POST /checkout")

        street = request.form.get("street", "").strip()
        city = request.form.get("city", "").strip()
        state = request.form.get("state", "").strip()
        zip_code = request.form.get("zip", "").strip()
        phone_input = request.form.get("phone", "").strip()

        # email only asked at checkout
        email_input = request.form.get("email", "").strip()
        print("DEBUG: email_input from form =", repr(email_input))

        # Card number for last 4
        card_number_raw = request.form.get("card_number", "").strip()
        card_number = card_number_raw.replace(" ", "")
        if len(card_number) >= 4 and card_number[-4:].isdigit():
            card_last4 = card_number[-4:]
        else:
            card_last4 = ""

        # Build shipping address dict (for receipt + email)
        shipping_address = {
            "street": street,
            "city": city,
            "state": state,
            "zip": zip_code,
        }

        # Save updated address + phone into DB (email is NOT saved in DB)
        if current_user is not None:
            current_user["address"] = shipping_address
            current_user["phone"] = phone_input

        # Save updated users list
        db["users"] = users

        # Create a new order
        orders = db.get("orders", [])
        if orders:
            next_id = max(o.get("order_id", 0) for o in orders) + 1
        else:
            next_id = 1

        today = datetime.date.today()
        date_str = f"{today.month}/{today.day}/{today.year}"

        order = {
            "order_id": next_id,
            "purchaser_id": user_id,
            "date": date_str,
            "sub_total": float(f"{subtotal:.2f}"),
            "tax": float(f"{tax:.2f}"),
            "shipping": float(f"{shipping:.2f}"),
            "total": float(f"{total:.2f}"),
        }
        orders.append(order)
        db["orders"] = orders

        # Link this order to the inventory items in orders_inventory_items
        order_items = db.get("orders_inventory_items", [])
        for item in cart.values():
            # one entry per item * quantity
            for _ in range(item["quantity"]):
                order_items.append({
                    "order_id": next_id,
                    "item_id": item["item_id"],
                })
        db["orders_inventory_items"] = order_items

        # Save the updated database (users, orders, orders_inventory_items)
        save_database(db)
        print("DEBUG: database saved for order", next_id)

        # Clear the cart and remember which order we just placed
        session["cart"] = {}
        session["last_order_id"] = next_id

        # store checkout email ONLY in the session for the receipt
        session["checkout_email"] = email_input

        # store shipping + card last4 for receipt page
        session["last_order_address"] = shipping_address
        session["last_order_card_last4"] = card_last4

        # Try to send a real email (Gmail via app password)
        if email_input:
            purchaser_name = (
                current_user["first_name"]
                if current_user
                else (session.get("username") or "Customer")
            )

            print("DEBUG: calling send_receipt_email for", email_input)
            try:
                send_receipt_email(
                    email_input,
                    order,
                    items,
                    purchaser_name,
                    shipping_address,
                    card_last4,
                )
            except Exception as e:
                print("ERROR: send_receipt_email failed:", repr(e))
        else:
            print("DEBUG: no email entered, skipping send_receipt_email")

        print("DEBUG: redirecting to /receipt")
        return redirect(url_for("receipt"))

    # GET: render the checkout page
    print("DEBUG: rendering checkout.html (GET)")
    return render_template(
        "checkout.html",
        items=items,
        subtotal=subtotal,
        tax=tax,
        shipping=shipping,
        total=total,
        username=session.get("username"),
        address=address,
        phone=phone,
    )


@app.route("/receipt", methods=["GET"])
def receipt():
    db = load_database()
    orders = db.get("orders", [])
    inventory = db.get("inventory", [])
    users = db.get("users", [])

    last_order_id = session.get("last_order_id")

    order = next((o for o in orders if o["order_id"] == last_order_id), None)

    purchaser = None
    if order:
        purchaser = next((u for u in users if u["user_id"] == order["purchaser_id"]), None)

    # Get items for this order
    order_items = db.get("orders_inventory_items", [])
    item_ids = [oi["item_id"] for oi in order_items if oi["order_id"] == last_order_id]
    items = [i for i in inventory if i["item_id"] in item_ids]

    # Pull shipping + card info from session
    shipping_address = session.get("last_order_address", {})
    card_last4 = session.get("last_order_card_last4", "")

    return render_template(
        "receipt.html",
        order=order,
        purchaser=purchaser,
        items=items,
        username=session.get("username"),
        shipping_address=shipping_address,
        card_last4=card_last4,
    )


# Optional: if you want to run with `python main.py`
if __name__ == "__main__":
    app.run()
