from json import dump, loads
from tkinter import Button, Entry
from canvas import window, frame
from shop import display_products
from helpers import clean_screen


def render_entry():
    register_button = Button(
        window,
        text="Register",
        bg="#7a99f5",
        fg="#1b1c1f",
        borderwidth=0,
        width=20,
        height=3,
        command=register
    )

    login_button = Button(
        window,
        text="Login",
        bg="#7a99f5",
        fg="#1b1c1f",
        borderwidth=0,
        width=20,
        height=3,
        command=login
    )

    def login_hover(e):
        login_button['background'] = '#6e6ccc'

    def login_dehover(e):
        login_button['background'] = '#7a99f5'

    def register_hover(e):
        register_button['background'] = '#6e6ccc'

    def register_dehover(e):
        register_button['background'] = '#7a99f5'

    frame.create_window(400, 250, window=register_button)
    frame.create_window(400, 320, window=login_button)
    register_button.bind('<Enter>', register_hover)
    register_button.bind('<Leave>', register_dehover)
    login_button.bind('<Enter>', login_hover)
    login_button.bind('<Leave>', login_dehover)



def get_users_data():
    info_data = []

    with open("db/users_info.txt", "r") as users_file:
        # For each line of text, convert text to dict, using json and add it to info_data as element
        # loads - take a string and turn it to an object, load - take an object and turn it to a string
        # Here we need json loads
        for line in users_file:
            info_data.append(loads(line))

    return info_data


def login():
    clean_screen()

    frame.create_text(300, 200, text="Username:")
    frame.create_text(300, 250, text="Password:")

    frame.create_window(400, 200, window=username_box)
    frame.create_window(400, 250, window=password_box)

    def register_hover(e):
        login_button['background'] = "#6e6ccc"

    def register_dehover(e):
        login_button['background'] = "#7a99f5"
    login_button.bind('<Enter>', register_hover)
    login_button.bind('<Leave>', register_dehover)

    frame.create_window(400, 300, window=login_button)


def logging():
    if check_logging():
        display_products()
    else:
        frame.create_text(370, 400, text="Invalid username or password!", fill="red")


def check_logging():
    info_data = get_users_data()

    user_username = username_box.get()
    user_password = password_box.get()

    for record in info_data:
        record_username = record["Username"]
        record_password = record["Password"]

        if user_username == record_username and user_password == record_password:
            return True

    return False




def register():
    clean_screen()

    frame.create_text(250, 200, text="First name:")
    frame.create_text(250, 250, text="Last name:")
    frame.create_text(250, 300, text="Username:")
    frame.create_text(250, 350, text="Password:")

    frame.create_window(350, 200, window=first_name_box)
    frame.create_window(350, 250, window=last_name_box)
    frame.create_window(350, 300, window=username_box)
    frame.create_window(350, 350, window=password_box)



    register_button = Button(
        window,
        text="Register",
        bg="#7a99f5",
        fg="#1b1c1f",
        borderwidth=0,
        width=20,
        height=2,
        command=registration
    )

    def hover(e):
        button['background'] = "#6e6ccc"

    def dehover(e):
        button['background'] = "#7a99f5"

    button = register_button
    button.bind('<Enter>', hover)
    button.bind('<Leave>', dehover)

    frame.create_window(400, 450, window=register_button)


def registration():
    info_dict = {
        "First name": first_name_box.get(),
        "Last name": last_name_box.get(),
        "Username": username_box.get(),
        "Password": password_box.get(),
    }

    if check_registration(info_dict):
        with open("db/users_info.txt", "a") as users_file:
            # info_dict["Password"] = get_password_hash(info_dict["Password"])
            # From json we use dump, which saves to file dict from string (the user data after validation pass)
            users_file.write("\n")
            dump(info_dict, users_file)
            display_products()


def check_registration(info):
    frame.delete("error")

    for key, value in info.items():
        if not value.strip():
            frame.create_text(
                400,
                500,
                text=f"{key} cannot be empty!",
                fill="red",
                tags="error",
            )

            return False

    info_data = get_users_data()

    for record in info_data:
        if record["Username"] == info["Username"]:
            frame.create_text(
                400,
                500,
                text="Username is already taken!",
                fill="red",
                tags="error",
            )

            return False

    return True
#
#
# def print_event(event):
#     info = [
#         username_box.get(),
#         password_box.get()
#     ]
#
#     for el in info:
#         if not el.strip():
#             login_button["state"] = "disabled"
#             break
#     else:
#         login_button["state"] = "normal"
#
#
first_name_box = Entry(window, bd=0)
last_name_box = Entry(window, bd=0)
username_box = Entry(window, bd=0)
password_box = Entry(window, bd=0, show="*")

login_button = Button(
    window,
    text="Login",
    bg="#7a99f5",
    fg="black",
    width=13,
    height=1,
    borderwidth=0,
    command=logging
)




# login_button["state"] = "disabled"
#
# window.bind("<KeyRelease>", print_event)