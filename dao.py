import sqlite3

# Connect to database
db = sqlite3.connect('url_shortener.db')
cursor = db.cursor()


class DAO:
    def create_database(self):
        # Creating table
        table = '''CREATE TABLE IF NOT EXISTS shortened_urls (id INTEGER PRIMARY KEY AUTOINCREMENT, original_url 
        VARCHAR(255) NOT NULL, new_url CHAR(25) NOT NULL, generated_code CHAR(5) NOT NULL); '''
        db.execute(table)

    def insert_data(self, original_url, new_url, generated_code):
        self.create_database()
        cursor.execute('INSERT INTO shortened_urls (original_url, new_url, generated_code) VALUES ( ?, ?, ? );', (original_url, new_url, generated_code))
        db.commit()
        return cursor.rowcount

    def select_data(self, code_url):
        self.create_database()
        data = cursor.execute('SELECT * FROM shortened_urls WHERE generated_code = ?', (code_url,))
        return data
