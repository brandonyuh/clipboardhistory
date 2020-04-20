import pyperclip
import threading
import time

check_delay = 1


def main():
    tread = threading.Thread(target=periodic_check)
    tread.start()


def periodic_check():
    clipboard_value = ""
    while True:
        clipboard_value = check_changed(clipboard_value)

        time.sleep(check_delay)


def check_changed(clipboard_value):
    new_clipboard_value = pyperclip.paste()
    if clipboard_value != new_clipboard_value:
        clipboard_value = new_clipboard_value
        # TODO record value

    return clipboard_value


if __name__ == "__main__":
    main()
