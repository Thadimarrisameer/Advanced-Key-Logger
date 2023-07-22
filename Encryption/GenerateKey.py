from cryptography.fernet import Fernet


key = Fernet.generate_key()
file = open("e:\\Collage\\BTECH-SEMESTER-6\\Network Secutity\\Project\\python-advanced-keylogger-crash-course\\Cryptography\\encryption_key.txt", 'wb')
file.write(key)
file.close()
