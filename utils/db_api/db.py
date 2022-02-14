import sqlite3


class SQLestate:

    def __init__(self, database):
        """Подключаемся к БД и сохраняем курсор соединения"""
        self.connection = sqlite3.connect(database)
        self.cursor = self.connection.cursor()

    def add_my_ad_fsm(self, tg_id, brand, model_year, mileage, cost, number_phone, allow=True, allow_admin=False):
        """Добавляем обьявление аренды"""
        with self.connection:
            return self.cursor.execute(
                "INSERT INTO `ad` (`brand`,`model_year`,`mileage`,"
                "`cost`,`number_phone`,`allow`, `allow_admin`, `tg_id`) VALUES(?,?,?,?,?,?,?,?)",
                (brand, model_year, mileage, cost, number_phone, allow, allow_admin, tg_id))

    def show_all_add_(self):
        """Показать все объявления для юзеров"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `ad` WHERE `allow_admin` = ? and `allow` = ?",
                                       (True, True,)).fetchall()

    def show_all_inline_(self, brand):
        """Показать все объявления для юзеров"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `ad` WHERE `allow_admin` = ? and `allow` = ? and `brand` = ?",
                                       (True, True, brand,)).fetchall()

    def show_all_add_my(self, tg_id):
        """Показать все объявления для владельца"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `ad` WHERE `tg_id` = ?",
                                       (tg_id,)).fetchall()

    def show_all_add_adm(self):
        """Показать все объявления для админа"""
        with self.connection:
            return self.cursor.execute("SELECT * FROM `ad` WHERE `allow_admin` = ?",
                                       (False,)).fetchall()

    # SQL USERS ONLY

    def check_subscriber(self, tg_id):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users` WHERE `tg_id` = ?', (tg_id,)).fetchall()
            return bool(len(result))

    def check_confirm(self, tg_id):
        """Проверяем, дал ли согласие юзер"""
        with self.connection:
            result = self.cursor.execute('SELECT `confirm` FROM `users` WHERE `tg_id` = ?', (tg_id,)).fetchall()
            return bool(len(result))

    def subscriber_exists(self):
        """Проверяем, есть ли уже юзер в базе"""
        with self.connection:
            result = self.cursor.execute('SELECT * FROM `users`', ).fetchall()
            return len(result)

    def add_subscriber(self, tg_id, confirm=True, admin=False):
        """Добавляем нового юзера"""
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`id`,`tg_id`, `confirm`, `admin`) VALUES(?,?,?,?)",
                                       (int(self.subscriber_exists()) + 1, tg_id, confirm, admin))

    def get_admin(self, user_id, allow_admin) -> list:
        """Выдача админки"""
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `admin` = ? WHERE `tg_id` =?", (allow_admin, user_id))

    def adm_successful_confirmation(self, id_ad) -> list:
        """админ подтверждает объявлегние"""
        with self.connection:
            return self.cursor.execute("UPDATE `ad` SET `allow_admin` = ? WHERE `id` =?", (True, id_ad,))

    def user_info_stor_start(self, id_ad, allow) -> list:
        """Изменить статус объявления"""
        with self.connection:
            return self.cursor.execute("UPDATE `ad` SET `allow` = ? WHERE `id` =?", (allow, id_ad,))

    def how_status_ad(self, id) -> bool:
        """Проверка на объявление"""
        with self.connection:
            return self.cursor.execute("SELECT `allow` FROM `ad` WHERE `id` =?", (id,)).fetchone()[0]

    def why_get_admin(self, user_id) -> bool:
        """Проверка на админку"""
        with self.connection:
            return self.cursor.execute("SELECT `admin` FROM `users` WHERE `tg_id` =?", (user_id,)).fetchone()[0]

    def adm_dell_ad(self, id_ad):
        """Админ удаляет объявление"""
        with self.connection:
            return self.cursor.execute("DELETE FROM `ad` WHERE `id` =?", (id_ad,))

    def close(self):
        """Закрываем соединение с БД"""
        self.connection.close()
