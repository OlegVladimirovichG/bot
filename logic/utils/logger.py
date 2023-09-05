import datetime


# Функция для записи информации о запросах в лог-файл
def log_request(user_id, username, text):
    current_time = datetime.datetime.now()

    log_entry = f"[{current_time}] User ID: {user_id}, Username: {username}, Request: {text}\n"

    with open("bot_log.txt", "a") as log_file:
        log_file.write(log_entry)
