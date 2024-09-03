import sqlite3

def get_user(user_id):
    with sqlite3.connect('services.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
        return cursor.fetchone()

def add_user(user_id, username):
    with sqlite3.connect('services.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (user_id, username) VALUES (?, ?)", (user_id, username))
        conn.commit()

def add_service(user_id, name, description, price):
    with sqlite3.connect('services.db') as conn:
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO services (user_id, name, description, price, approved) VALUES (?, ?, ?, ?, NULL)",
            (user_id, name, description, price))
        conn.commit()

def get_services(user_id):
    with sqlite3.connect('services.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT name, description, price, approved FROM services WHERE user_id=?", (user_id,))
        return cursor.fetchall()

def get_pending_services():
    with sqlite3.connect('services.db') as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, name FROM services WHERE approved IS NULL")
        return cursor.fetchall()

def approve_service(service_id):
    with sqlite3.connect('services.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE services SET approved = 1 WHERE id = ?", (service_id,))
        conn.commit()

def reject_service(service_id, reject_reason, user_id):
    with sqlite3.connect('services.db') as conn:
        cursor = conn.cursor()
        cursor.execute("UPDATE services SET approved = 0 WHERE id = ?", (service_id,))
        cursor.execute("SELECT user_id, name FROM services WHERE id = ?", (service_id,))
        service = cursor.fetchone()
        user_id, service_name = service
        cursor.execute("INSERT INTO rejections (service_id, reason) VALUES (?, ?)", (service_id, reject_reason))
        conn.commit()
        # Отправка сообщения пользователю об отказе в услуге
        from bot import bot
        bot.send_message(user_id, f"Ваша услуга '{service_name}' была отклонена. Причина: {reject_reason}")
