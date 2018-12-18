import psycopg2

class SQLHandler:

	def __init__(self, user_name, user_password, db_name):
		
		self.user_name = user_name
		self.user_pwd = user_password
		self.db_name = db_name

	def dbConnect(self):

		print(self.user_name, self.user_pwd, self.db_name)

		self.conn = psycopg2.connect(
			host = "localhost",
			port = 5432,
			database = "sample",
			user = "postgres",
			password = "sample"
		)

		# self.conn = psycopg2.connect(
		# 	host = "127.0.0.1",
		# 	port = 5432,
		# 	database = self.db_name,
		# 	user = self.user_name,
		# 	password = self.user_pwd
		# )

		# if self.conn.is_connected():
		# 	print("connect success")
		# 	self.cursor = self.conn.cursor()
		# else:
		# 	print("not connection")

		# cursor = connect.cursor() # カーソル取得

	def createTable(self, table_name):
		
		# テーブルの作成
		"""
		Cursorクラスのexecute()によりSQLの実行が可能
		"""

		cursor.execute("create table users (user_id int(20), user_name varchar(200), email varchar(200))")
		connect.commit()

	def insertItem(self, insert_item = []):
		
		# 作成したテーブルにデータを保存する
		self.cursor.execute("insert into users values(%s, %s, %s)", (insert_item[0], insert_item[1], insert_item[2]))
		self.conn.commit()

	def deleteItem(self, sql):

		self.cursor.execute(sql)
		self.conn.commit()

	def updateItem(self, sql):
		
		self.cursor.execute(sql)
		self.conn.commit()

	def selectItem(self, sql):

		#cursor.execute()でSQLを実行できます。
		self.cursor.execute(sql)
		#cursorは実行しただけでは、取り出せないのでcursor.fetchall()が必要です。
		result = self.cursor.fetchall()

		return result

	def dbClose():
		
		# 接続を閉じる
		connect.close()

if __name__ == "__main__":

	db_connect = SQLHandler("postgres ", "sample", "sample")

	db_connect.dbConnect()

	sql = 'select * from users'
	item = [1, "example", "example@example.co.jp"]

	# db_connect.insertItem(item)
	# result = db_connect.selectItem(sql)

	# print(result)