import sqlite3


class DataBase:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def user_exists(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id, )).fetchall()
            return bool(len(result))

    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id, ))

    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `active` = ? WHERE `user_id` = ?", (active, user_id, ))

    def user_money(self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT `money` FROM `users` WHERE `user_id` = ?", (user_id, )).fetchmany(1)
            return int(result[0][0])

    def set_money(self, user_id, money):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `money` = ? WHERE `user_id` = ?", (money, user_id, ))

    def add_check(self, user_id, money, bill_id):
        with self.connection:
            return self.cursor.execute("INSERT or REPLACE INTO `check` (`user_id`, `money`, `bill_id`) VALUES (?,?,?)", (user_id, money, bill_id, ))

    def get_check(self, bill_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `check` WHERE `bill_id` = ?", (bill_id, )).fetchmany(1)
            if not bool(len(result)):
                return False
            else:
                return result[0]

    def delete_check(self, bill_id):
        with self.connection:
            return self.cursor.execute("DELETE FROM `check` WHERE `bill_id` = ?", (bill_id, ))

    def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT `user_id`, `active` FROM `users`").fetchall()