class Library:
	def __init__(self):
		self.books=[]

	def add_book(self, title, author):
		book = {"title":title,"author":author,"is_borrowed":False}
		self.books.append(book)
		print(f"《{title}》已经添加到图书馆。")

	def display_books(self):
		if not self.books:
			print("图书馆暂无藏书。")
		else:
			print("图书馆现有藏书：")
			for index,book in enumerate(self.books,start=1):
				status="已借出" if book["is_borrowed"] else "可借阅"
				print(f"{index}.《{book['title']}》 - {book['author']} - {status}")

	def borrow_book(self,title):
		for book in self.books:
			if book["title"] ==  title:
				if book["is_borrowed"]:
					print(f"《{title}》已经被借出。")
				else:
					book["is_borrowed"] = True
					print(f"你已成功借阅《{title}》。")
				return
		print(f"未找到《{title}》这本书。")

	def return_book(self, title):
		for book in self.books:
			if book["title"] == title:
				if not book["is_borrowed"]:
					print(f"《{title}》并未被借出，无需归还。")
				else:
					book["is_borrowed"] == False
					print(f"你已成功归还《{title}》。")
				return
		print(f"未找到《{title}》这本书")

	def del_book(self,title):
		if not self.books:
			print("图书馆暂无藏书。")
		else:
			for book in self.books:
				if book["title"] == title:
					self.books.remove(book)
					print(f"《{title}》已经从图书馆删除。")
					return

def save_to_file(library, filename="library.txt"):
	try:
		if not library.books:
			print("没有新增图书。")
		else:
			with open(filename, "w", encoding="utf-8") as file:
				for book in library.books:
					status = "1" if book["is_borrowed"] else "0"
					file.write(f"{book['title']},{book['author']},{status}\n")
			print("数据已保存到文件。")
			return
	except Exception as e:
		print(f"保存文件时出现错误:{e}")

def load_from_file(library, filename="library.txt"):
	try:
		with open(filename, "r", encoding="utf-8") as file:
			for line in file:
				title, author,status = line.strip().split(",")
				is_borrowed = bool(int(status))
				book = {"title":title,"author":author,"is_borrowed":is_borrowed}
				library.books.append(book)
			print("数据已从文件加载。")
	except FileNotFoundError:
		print("未找到保存数据的文件，将使用空图书馆。")
	except Exception as e:
		print(f"加载文件时出现错误：{e}")

if __name__ == "__main__":
	library=Library()
	load_from_file(library)

	while True:
		print("\n图书管理系统菜单：")
		print("1. 添加图书")
		print("2. 显示所有图书")
		print("3. 借阅图书")
		print("4. 归还图书")
		print("5. 删除图书")
		print("6. 保存数据到文件")		
		print("7. 退出系统")

		choice = input("请输入你的选择(1-7)：")

		if choice == "1":
			title = input("请输入图书标题:")
			author = input("请输入图书作者:")
			library.add_book(title,author)
		elif choice == "2":
			library.display_books()
		elif choice == "3":
			title = input("请输入要借阅的图书标题：")
			library.borrow_book(title)
		elif choice == "4":
			title = input("请输入要归还的图书标题：")
			library.return_book(title)
		elif choice == "5":
			title = input("请输入要删除的图书标题：")
			library.del_book(title)
		elif choice == "6":
##			title = input("保存数据到文件")
			save_to_file(library)
		elif choice == "7":
			save_to_file(library)
			print("感谢使用图书管理系统，再见！")
			break
		else:
			print("无效的选择，请重新输入。")