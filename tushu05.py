class Library():
	def __init__(self):
		self.books = []

	def add_book(self, title, author):
		book = {}
		if not self.books:
			book = {"title":title, "author":author, "is_borrowed":False}
		else:
			for book in self.books:
				if book["title"] == title:
					if book["author"] == author:
						print(f"图书标签为：{title}，图书作者为：{author}的图书已经存在，无需再次添加。")
						return
			book = {f"title":title, "author":author, "is_borrowed":False}
		self.books.append(book)
		print(f"图书标签为：{title}，图书作者为：{author}的图书已经成功添加。")

	def display_book(self):
		if not self.books:
			print(f"图书系统为空。")
		else:
			for index,book in enumerate(self.books, start=1):
				status = "已借出" if book["is_borrowed"] else "可借阅"
				print(f"{index}. {book["title"]} - {book["author"]} - {status}",end="\n")
			print(f"所有图书内容都已全部列出。")

	def borrow_book(self, title, author):
		if not self.books:
			print(f"图书系统为空。")
		else:
			for book in self.books:
				if book["title"] == title:
					if book["author"] == author:
						if book["is_borrowed"]:
							print(f"图书标签为：{title}，图书作者为：{author}的图书正在借阅中，无法再次借阅。")
						else:
							book["is_borrowed"] = True
							print(f"图书标签为：{title}，图书作者为：{author}的图书已成功借阅，借阅周期为30天。")
						return
			print(f"图书标签为：{title}，图书作者为：{author}的图书不存在，请联系图书管理员。")

	def return_book(self, title, author):
		if not self.books:
			print(f"图书系统为空。")
		else:
			for book in self.books:
				if book["title"] == title:
					if book["author"] == author:
						if book["is_borrowed"]:
							book["is_borrowed"] = False
							print(f"图书标签为：{title}，图书作者为：{author}的图书已成功归还，可重新借阅。")
						else:
							print(f"图书标签为：{title}，图书作者为：{author}的图书没有借阅记录，无需归还。")
						return
			print(f"图书标签为：{title}，图书作者为：{author}的图书不存在，请联系图书管理员。")

	def remove_book(self, title, author):
		if not self.books:
			print(f"图书系统为空。")
		else:
			for book in self.books:
				if book["title"] == title:
					if book["author"] == author:
						if book["is_borrowed"]:
							print(f"图书标签为：{title}，图书作者为：{author}的图书正在借阅中，无法执行删除操作。")
						else:
							self.books.remove(book)
							print(f"图书标签为：{title}，图书作者为：{author}的图书已经成功删除。")
						return
			print(f"图书标签为：{title}，图书作者为：{author}的图书不存在，请联系图书管理员。")

def save_to_file(library, filename="tushu05.txt"):
	try:
		if not library.books:
			print(f"没有新增图书。")
		else:
			with open(filename, "w", encoding="utf-8") as file:
				for book in library.books:
					status = "1" if book["is_borrowed"] else "0"
					file.write(f"{book["title"]}\t{book["author"]}\t{status}\n")
				print(f"图书内容已全部保存。")
	except Exception as e:
		print(f"保存图书出错，报错内容为：{e}")

def load_from_file(library, filename="tushu05.txt"):
	try:
		print(f"正在加载图书内容......")
		with open(filename, "r", encoding="utf-8") as file:
			for line in file:
				title, author, status = line.strip().split("\t")
				is_borrowed = bool(int(status))
				book = {"title":title, "author":author, "is_borrowed":is_borrowed}
				library.books.append(book)
			print(f"图书内容已全部加载。")
	except Exception as e:
		print(f"加载图书文件报错，报错内容为：{e}")

def reload_from_file(library, filename="tushu05.txt"):
	library.books = []
	load_from_file(library)

if __name__ == "__main__":
	library = Library()
	load_from_file(library)

	while True:
		print(f"------------------------------")
		print(f"1. 添加图书\t2. 列出图书")
		print(f"3. 借阅图书\t4. 归还图书")
		print(f"5. 删除图书\t6. 保存图书")
		print(f"7. 重新加载\t8. 退出系统")
		print(f"------------------------------")

		choice = input(f"输入操作索引ID(1-8)：")

		if choice == "1":
			while True:
				title = input(f"输入要添加的图书标签：")
				author = input(f"输入要添加的图书作者：")

				if bool(title) and bool(author):
					break
				else:
					print(f"无效输入，重新输入图书标签和图书作者，不允许为空值。")
			library.add_book(title, author)
		elif choice == "2":
			library.display_book()
		elif choice == "3":
			while True:
				title = input(f"输入要借阅的图书标签：")
				author = input(f"输入要借阅的图书作者：")

				if bool(title) and bool(author):
					break
				else:
					print(f"无效输入，重新输入图书标签和图书作者，不允许为空值。")
			library.borrow_book(title, author)
		elif choice == "4":
			while True:
				title = input(f"输入要归还的图书标签：")
				author = input(f"输入要归还的图书作者：")

				if bool(title) and bool(author):
					break
				else:
					print(f"无效输入，重新输入图书标签和图书作者，不允许为空值。")
			library.return_book(title, author)
		elif choice == "5":
			while True:
				title = input(f"输入要删除的图书标签：")
				author = input(f"输入要删除的图书作者：")

				if bool(title) and bool(author):
					break
				else:
					print(f"无效输入，重新输入图书标签和图书作者，不允许为空值。")
			library.remove_book(title, author)
		elif choice == "6":
			save_to_file(library)
		elif choice == "7":
			reload_from_file(library)
		elif choice == "8":
			save_to_file(library)
			print(f"退出图书系统。")
			break
		else:
			print(f"无效输入，请重新输入操作索引ID。")