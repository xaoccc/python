def show_success_message(success, success_message):
    success = "Successfully executed " + success + "."
    print(success)
    print("=" * len(success))
    print(f"{success_message}.\n")


def show_warning_message(warning):
    warning = "Warning: " + warning + "."
    print(warning)
    print("=" * len(warning) + "\n")


def show_error_message(error_message, reason, error_code):
    error_message = "Error: Failed to execute " + error_message + "."
    print(error_message)
    print("=" * len(error_message))
    print(f"Reason: {reason}.")
    print(f"Error code: {error_code}.\n")
    

def read_and_process_message():
    for i in range(int(input())):
        message_type = input()
        if message_type == "success":
            show_success_message(input(), input())
        elif message_type == "warning":
            show_warning_message(input())
        elif message_type == "error":
            show_error_message(input(), input(), input())


read_and_process_message()
