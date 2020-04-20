import datetime
import os

import pyperclip
import threading
import time
from PIL import ImageGrab
from PIL import ImageChops

check_delay = 1
save_directory = "images/"
clipboard_value = ""
clipboard_image = None
last_image_file = ""


def main():
    tread = threading.Thread(target=periodic_check)
    tread.start()


def periodic_check():
    while True:
        check_changed()
        time.sleep(check_delay)


def check_changed():
    new_clipboard_value = pyperclip.paste()
    global clipboard_value

    if "" == new_clipboard_value:
        save_image()
    elif clipboard_value != new_clipboard_value:
        save_text(new_clipboard_value)

    clipboard_value = new_clipboard_value
    return clipboard_value


def save_text(new_clipboard_value):
    print("TODO save " + new_clipboard_value + " to file")
    pass


def save_image():
    im = ImageGrab.grabclipboard()
    global clipboard_image
    if im is not None:
        images_different = False
        if clipboard_image is not None:
            diff = ImageChops.difference(clipboard_image, im)
            if diff.getbbox():
                images_different = True
        if clipboard_image is None or images_different:
            clipboard_image = im
            timestamp = getTimeStamp()
            timestamp = timestamp.replace(":", "-")
            timestamp = timestamp.replace(".", "-")
            if not os.path.exists(save_directory):
                os.makedirs(save_directory)
            im.save(save_directory + timestamp + '.png', 'PNG')


def getTimeStamp():
    return str(datetime.datetime.now().isoformat())


if __name__ == "__main__":
    main()
