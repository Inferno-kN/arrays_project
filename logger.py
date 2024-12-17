def log_action(message):
    with open('log.txt', 'a') as log_file:
        log_file.write(message)
