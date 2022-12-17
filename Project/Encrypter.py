import rsa


def encrypt(publickey):
    # Opens log file
    log_file = open(
        r"C:\Users\Badger\Documents\GitHub\Simple_Keylogger\Log\clean_key_log.txt", "r")
    lines = log_file.readlines()

    # Encrypts log line by line and appends to the enc_log
    enc_log = []
    for line in lines:
        encrypted = rsa.encrypt(line.encode(), publickey)
        enc_log.append(encrypted)
    print(enc_log)
    # Save the log
    return enc_log


def save_enc_log(log):
    with open(r'C:\Users\Badger\Documents\GitHub\Simple_Keylogger\Log\encrypted_log.txt', 'w') as f:
        f.write(str(log))


# Create key using rsa library if you not created already (key lenght=1024)
def create_key(size):
    publickey, privatekey = rsa.newkeys(size)
    return publickey, privatekey


def save_priv(priv):
    with open(r'C:\Users\Badger\Documents\GitHub\Simple_Keylogger\Log\private_key.pem', 'w') as f:
        f.write(priv)


def save_pub(pub):
    with open(r'C:\Users\Badger\Documents\GitHub\Simple_Keylogger\Log\public_key.pem', 'w') as f:
        f.write(pub)


def main():
    # Create private and public keys (size=2048)
    publickey, privatekey = create_key(2048)

    # Save keys
    save_priv(str(privatekey))
    save_pub(str(publickey))

    save_enc_log(encrypt(privatekey))


if __name__ == "__main__":
    main()
