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

    if "" == new_clipboard_value:
        save_image()
    elif clipboard_value != new_clipboard_value:
        save_text()

    clipboard_value = new_clipboard_value
    return clipboard_value


def save_text():
    print("TODO save text to file")
    pass


def save_image():
    print("TODO save image to file")
    pass


if __name__ == "__main__":
    main()
