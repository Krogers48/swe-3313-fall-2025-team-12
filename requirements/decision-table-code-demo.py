from dataclasses import dataclass

@dataclass
class Conditions:
    # auth / access
    account_exists: bool = True
    password_correct: bool = True
    role_is_admin: bool = False
    page_is_admin_only: bool = False
    # inventory visibility / search
    item_is_sold: bool = False
    search_term_present: bool = False
    query_matches: bool = True
    # checkout
    cart_empty: bool = True
    pay_now_clicked: bool = False
    fields_complete: bool = False   # payment + shipping
    confirm_clicked: bool = False   # in this merged model, confirm = finalize
    # admin operations (request flags)
    run_sales_report: bool = False
    add_inventory: bool = False
    convert_user_to_admin: bool = False

def evaluate_actions(c: Conditions):
    """Return a sorted list of action strings based on the merged rules."""
    actions = set()

    # ---- LOGIN / ACCESS ----
    if not c.account_exists:
        actions.add("offer_self_register")
    elif c.password_correct:
        actions.add("allow_login")
        actions.add("route_to_main")
        if c.role_is_admin and c.page_is_admin_only:
            actions.add("allow_admin_pages")
        if (not c.role_is_admin) and c.page_is_admin_only:
            actions.add("deny_admin_pages")
    else:
        # bad password -> no allow_login
        pass

    # ---- INVENTORY VISIBILITY / SEARCH ----
    show_item = False
    if c.item_is_sold:
        actions.add("hide_item")
    else:
        if not c.search_term_present:
            show_item = True
        else:
            show_item = c.query_matches
        if show_item:
            actions.add("show_item_in_list")
        else:
            actions.add("hide_item")

    # ---- CHECKOUT FLOW ----
    if not c.cart_empty:
        actions.add("enable_checkout_button")
        actions.add("show_checkout")
        if c.pay_now_clicked:
            actions.add("open_payment")
            if not c.fields_complete:
                actions.add("block_proceed")
            else:
                actions.add("show_confirm_page")
                if c.confirm_clicked:
                    actions.add("create_sale_mark_items_empty_cart_show_receipt")
                else:
                    actions.add("keep_cart_unchanged")

    # ---- ADMIN OPERATIONS ----
    admin_op_requested = c.run_sales_report or c.add_inventory or c.convert_user_to_admin
    if admin_op_requested:
        if c.role_is_admin:
            if c.run_sales_report: actions.add("show_sales_report")
            if c.add_inventory:    actions.add("add_item_to_inventory")
            if c.convert_user_to_admin: actions.add("convert_user_to_admin")
        else:
            actions.add("deny_action")

    return sorted(actions)

# ------------------ demo scenarios ------------------

def demo():
    scenarios = {
        "R1 new user (no account)": Conditions(account_exists=False),
        "R4 customer hits admin page": Conditions(account_exists=True, password_correct=True,
                                                 role_is_admin=False, page_is_admin_only=True),
        "R6 sold item": Conditions(item_is_sold=True),
        "R8 search match": Conditions(item_is_sold=False, search_term_present=True, query_matches=True),
        "R12 pay now but incomplete fields": Conditions(cart_empty=False, pay_now_clicked=True,
                                                       fields_complete=False),
        "R13 confirm to finalize": Conditions(cart_empty=False, pay_now_clicked=True,
                                              fields_complete=True, confirm_clicked=True),
        "R14 back out at confirm": Conditions(cart_empty=False, pay_now_clicked=True,
                                              fields_complete=True, confirm_clicked=False),
        "R15 admin runs report": Conditions(account_exists=True, password_correct=True,
                                            role_is_admin=True, run_sales_report=True),
        "R18 non-admin tries report": Conditions(role_is_admin=False, run_sales_report=True),
        "R20 non-admin tries convert": Conditions(role_is_admin=False, convert_user_to_admin=True),
    }

    for name, cond in scenarios.items():
        acts = evaluate_actions(cond)
        print(f"\n== {name} ==")
        for a in acts:
            print(f"- {a}")

def _parse_bool(s: str):
    s = s.strip().lower()
    if s in {"y","yes","true","t","1"}:
        return True
    if s in {"n","no","false","f","0"}:
        return False
    return None

def _ask_bool(label: str, default: bool | None = None) -> bool:
    suffix = " [y/n]" if default is None else (" [Y/n]" if default else " [y/N]")
    while True:
        raw = input(f"{label}{suffix}: ").strip()
        if not raw and default is not None:
            return default
        val = _parse_bool(raw)
        if val is not None:
            return val
        print("Please enter y/n or true/false.")

def prompt_conditions() -> Conditions:
    """
    Ask user T/F for every condition.
    You can press Enter to accept the shown default (where provided).
    """
    print("\nEnter True/False for each condition (y/n also works).")
    return Conditions(
        # auth / access
        account_exists=_ask_bool("Account exists", True),
        password_correct=_ask_bool("Password correct", True),
        role_is_admin=_ask_bool("Role is Admin", False),
        page_is_admin_only=_ask_bool("Page requested is Admin-only", False),

        # inventory visibility / search
        item_is_sold=_ask_bool("Item is Sold", False),
        search_term_present=_ask_bool("Search term present", False),
        query_matches=_ask_bool("Query matches (if search present)", True),

        # checkout
        cart_empty=_ask_bool("Cart empty", True),
        pay_now_clicked=_ask_bool("Pay Now clicked", False),
        fields_complete=_ask_bool("All payment & shipping fields complete", False),
        confirm_clicked=_ask_bool("Confirm Order clicked", False),

        # admin operations requested
        run_sales_report=_ask_bool("Run Sales Report (requested)", False),
        add_inventory=_ask_bool("Add Inventory (requested)", False),
        convert_user_to_admin=_ask_bool("Convert User to Admin (requested)", False),
    )

def interactive_once():
    print("\n== Interactive Condition Entry ==")
    cond = prompt_conditions()
    actions = evaluate_actions(cond)
    print("\nActions fired:")
    if actions:
        for a in actions:
            print(f"- {a}")
    else:
        print("- (none)")

# ------------------ entry point ------------------

if __name__ == "__main__":
    while True:
        print("\n=== Decision Table Tester ===")
        print("[1] Run canned demos")
        print("[2] Enter conditions manually (interactive)")
        print("[Q] Quit")
        choice = input("> ").strip().lower()
        if choice == "1":
            demo()
        elif choice == "2":
            interactive_once()
        elif choice in {"q","quit","exit"}:
            break
        else:
            print("Unknown choice.")