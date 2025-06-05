class Student():
	def __init__(self):
		# xsxx=学生信息 xscj=学生成绩
		self.xuehao = 1000000
		self.xsxx = []
		self.xscj = []

	def add_student(self, xingming, xingbie, nianling):
		if not student.xsxx:
			self.xuehao = self.xuehao + 1
			tmp_stu = {"xuehao":self.xuehao, "xingming":xingming, "xingbie":xingbie, "nianling":nianling}
			self.xsxx.append(tmp_stu)
			self.luru_chengji(self.xuehao)
			print(f"学号为：{self.xuehao}，姓名为：{tmp_stu["xingming"]}，性别为：{tmp_stu["xingbie"]}，年龄为：{tmp_stu["nianling"]}的学员信息已成功添加。")
		else:
			for stu in self.xsxx:
				if stu["xingming"] == xingming and stu["xingbie"] == xingbie and stu["nianling"] == nianling:
					print(f"姓名为：{xingming}，性别为：{xingbie}，年龄为：{nianling}的学员信息已经存在，无需再次添加。")
				else:
					#tmp_stu = self.xsxx[-1]
					self.xuehao = int(self.xsxx[-1]["xuehao"]) + 1
					tmp_stu = {"xuehao":self.xuehao, "xingming":xingming, "xingbie":xingbie, "nianling":nianling}
					self.xsxx.append(tmp_stu)
					self.luru_chengji(self.xuehao)
					print(f"学号为：{self.xuehao}，姓名为：{tmp_stu["xingming"]}，性别为：{tmp_stu["xingbie"]}，年龄为：{tmp_stu["nianling"]}的学员信息已成功添加。")
				return

	def show_student(self):
		if not self.xsxx:
			print(f"没有学生信息，系统为空。")
		else:
			for index,tmp_stu in enumerate(self.xsxx, start=1):
				print(f"{index}. [学号]：{tmp_stu["xuehao"]}\t[姓名]：{tmp_stu["xingming"]}\t[性别]：{tmp_stu["xingbie"]}\t[年龄]：{tmp_stu["nianling"]}",end="\n")
			print(f"------------------所有学员信息都已列出----------------------")

	def show_student_all(self):
		if not self.xsxx and not self.xscj:
			print(f"没有学生信息，系统为空。")
		else:
			for index01,tmp_stu in enumerate(self.xsxx, start=1):
				for index02,tmp_cj in enumerate(self.xscj, start=1):
					if int(tmp_stu["xuehao"]) == int(tmp_cj["xuehao"]):
						print(f"{index02}. [学号]：{tmp_stu["xuehao"]}\t[姓名]：{tmp_stu["xingming"]}\t[性别]：{tmp_stu["xingbie"]}\t[年龄]：{tmp_stu["nianling"]}\t[语文]:{tmp_cj["yuwen"]}\t[数学]:{tmp_cj["shuxue"]}\t[英语]:{tmp_cj["shuxue"]}",end="\n")
						break
			print(f"------------------所有学员信息都已列出----------------------")

	def xiugai_student_xuehao(self, tmp, tmp_xuehao, xiugai_canshu):
		#print(f"{tmp, tmp_xuehao, xiugai_canshu}")
		if tmp == 1:
			for tmp_stu in student.xsxx:
				if int(tmp_stu["xuehao"]) == int(tmp_xuehao):
					tmp_stu["xingming"] = xiugai_canshu
					print(f"学员姓名信息已修改。")
					return
			print(f"1. 没有找到指定学号的学员，无法执行修改操作。")
		elif tmp == 2:
			for tmp_stu in student.xsxx:
				if int(tmp_stu["xuehao"]) == int(tmp_xuehao):
					tmp_stu["xingbie"] = xiugai_canshu
					print(f"学员性别信息已修改。")
					return
			print(f"2. 没有找到指定学号的学员，无法执行修改操作。")
		elif tmp == 3:
			for tmp_stu in student.xsxx:
				if int(tmp_stu["xuehao"]) == int(tmp_xuehao):
					tmp_stu["nianling"] = xiugai_canshu
					print(f"学员年龄信息已修改。")
					return
			print(f"3. 没有找到指定学号的学员，无法执行修改操作。")
		else:
			print(f"输入错误，无法执行修改操作。")

	def xiugai_student_xingming(self, tmp, tmp_xingming, xiugai_canshu):
		#print(f"{tmp, tmp_xuehao, xiugai_canshu}")
		if tmp == 1:
			for tmp_stu in student.xsxx:
				if tmp_stu["xingming"] == tmp_xingming:
					tmp_stu["xingming"] = xiugai_canshu
					print(f"学员姓名信息已修改。")
					return
			print(f"1. 没有找到指定学号的学员，无法执行修改操作。")
		elif tmp == 2:
			for tmp_stu in student.xsxx:
				if tmp_stu["xingming"] == tmp_xingming:
					tmp_stu["xingbie"] = xiugai_canshu
					print(f"学员性别信息已修改。")
					return
			print(f"2. 没有找到指定学号的学员，无法执行修改操作。")
		elif tmp == 3:
			for tmp_stu in student.xsxx:
				if tmp_stu["xingming"] == tmp_xingming:
					tmp_stu["nianling"] = xiugai_canshu
					print(f"学员年龄信息已修改。")
					return
			print(f"3. 没有找到指定学号的学员，无法执行修改操作。")
		else:
			print(f"输入错误，无法执行修改操作。")

	def remove_student(self, tmp, shanchu_canshu):
		print(f"3 开始执行删除操作")
		if tmp == 1:
			for tmp_stu in student.xsxx:
				if int(tmp_stu["xuehao"]) == int(shanchu_canshu):
					self.xsxx.remove(tmp_stu)
					print(f"学号为:{tmp_stu["xuehao"]} 的学员信息已删除。")
					return
			print(f"没有找到指定学号的学员，无法执行删除操作。")
		elif tmp == 2:
			for tmp_stu in student.xsxx:
				if tmp_stu["xingming"] == shanchu_canshu:
					self.xsxx.remove(tmp_stu)
					print(f"姓名为:{tmp_stu["xingming"]} 的学员信息已删除。")
					return
			print(f"没有找到指定姓名的学员，无法执行删除操作。")
		else:
			print(f"错误输入，无法执行删除操作。")

	def find_stadent(self, tmp, chaxun_canshu):
		if tmp == 1:
			for tmp_stu in student.xsxx:
				if int(tmp_stu["xuehao"]) == int(chaxun_canshu):
					print(f"学号为{tmp_stu["xuehao"]}的学员已找到，学员信息如下：")
					print(f"学号为：{tmp_stu["xuehao"]}，姓名为：{tmp_stu["xingbie"]}，性别为：{tmp_stu["xingbie"]}，年龄为{tmp_stu["nianling"]}。")
					return
			print(f"没有找到学号为{chaxun_canshu}的学员信息。")
		elif tmp == 2:
			for tmp_stu in student.xsxx:
				if tmp_stu["xingming"] == chaxun_canshu:
					print(f"姓名为{tmp_stu["xingming"]}的学员已找到，学员信息如下：")
					print(f"学号为：{tmp_stu["xuehao"]}，姓名为：{tmp_stu["xingbie"]}，性别为：{tmp_stu["xingbie"]}，年龄为{tmp_stu["nianling"]}。")
					return
			print(f"没有找到姓名为{chaxun_canshu}的学员信息。")
		else:
			print(f"{tmp} 输入错误，没有找到查询结果。")

	def luru_chengji(self, xuehao):
		yuwen = shuxue = yingyu = 0
		tmp_cj = {"xuehao":xuehao,"yuwen":yuwen,"shuxue":shuxue,"yingyu":yingyu}
		student.xscj.append(tmp_cj)
		print(f"学员为：{xuehao}的学员成绩已录入，所有成绩默认为0。")

	def xiugai_chengji(self, tmp, xuehao, chengji):
		for tmp_cj in student.xscj:
			if int(tmp_cj["xuehao"]) == int(xuehao):
				if tmp == 1:
					tmp_cj["yuwen"] = chengji
					print(f"学员语文成绩已经修改成功。")
				elif tmp == 2:
					tmp_cj["shuxue"] = chengji
					print(f"学员数学成绩已经修改成功。")
				elif tmp == 3:
					tmp_cj["yingyu"] = chengji
					print(f"学员英语成绩已经修改成功。")
				return
		print(f"输入错误，无法执行修改成绩操作。")

	def xiugai_chengji_all(self, xuehao, yuwen, shuxue, yingyu):
		for tmp_cj in student.xscj:
			if int(tmp_cj["xuehao"]) == int(xuehao):
				tmp_cj["yuwen"] = int(yuwen)
				tmp_cj["shuxue"] = int(shuxue)
				tmp_cj["yingyu"] = int(yingyu)
				print(f"学员成绩已经修改成功。")
				return
		print(f"输入错误，无法执行修改成绩操作。")

	def chakan_chengji(self):
		if not self.xscj:
			print(f"没有学员成绩，成绩系统为空。")
		else:
			for index,tmp_cj in enumerate(self.xscj, start=1):
				print(f"{index}. [学号]:{tmp_cj["xuehao"]}\t[语文]:{tmp_cj["yuwen"]}\t[数学]:{tmp_cj["shuxue"]}\t[英语]:{tmp_cj["yingyu"]}",end="\n")
			print(f"所有学员成绩已列出。")

def save_to_file(student):
	try:
		if not student.xsxx and not student.xscj:
			print(f"没有新增学生信息，无需保存。")
		else:
			xsxx_file = "xsxx.txt"
			xscj_file = "xscj.txt"
			with open(xsxx_file, "w", encoding="utf-8") as file:
				for tmp_stu in student.xsxx:
					file.write(f"{tmp_stu["xuehao"]}\t{tmp_stu["xingming"]}\t{tmp_stu["xingbie"]}\t{tmp_stu["nianling"]}\n")
			with open(xscj_file, "w", encoding="utf-8") as file:
				for tmp_cj in student.xscj:
					file.write(f"{tmp_cj["xuehao"]}\t{tmp_cj["yuwen"]}\t{tmp_cj["shuxue"]}\t{tmp_cj["yingyu"]}\n")
			print(f"学生信息已保存。")
	except Exception as e:
		print(f"保存文件时出错，错误内容为：{e}")

def load_from_file(student):
	try:
		xsxx_file = "xsxx.txt"
		xscj_file = "xscj.txt"
		print(f"正在加载学员信息......")
		with open(xsxx_file, "r", encoding="utf-8") as file:
			for line in file:
				xuehao,xingming,xingbie,nianling = line.strip().split("\t")
				tmp_stu={"xuehao":xuehao,"xingming":xingming,"xingbie":xingbie,"nianling":nianling}
				student.xsxx.append(tmp_stu)
		with open(xscj_file, "r", encoding="utf-8") as file:
			for line in file:
				xuehao,yuwen,shuxue,yingyu = line.strip().split("\t")
				tmp_cj = {"xuehao":xuehao,"yuwen":yuwen,"shuxue":shuxue,"yingyu":yingyu}
				student.xscj.append(tmp_cj)
		print(f"所有学员信息都已加载。")
	except FileNotFoundError:
		print(f"没有找到配置文件，讲加载空文件。")
	except Exception as e:
		print(f"加载文件时出错，错误内容为：{e}")

def reload_from_file(student):
	student.xsxx = []
	student.xscj = []
	load_from_file(student)

if __name__ == "__main__":
	student = Student()
	load_from_file(student)

	while True:
		print(f"-------------1.正在使用学生管理系统----------------")
		print(f"1. 学生信息管理\t2. 学生成绩管理")
		print(f"3. 查看学生信息\t4. 保存学生信息")
		print(f"5. 重新加载信息\t6. 退出管理系统")
		print(f"7. 查找学生信息\t8. 服务开发中..")
		print(f"-----------------------------------------------")

		choice = input(f"输入操作选项(1-4)：")

		if choice == "1":
			while True:
				print(f"=================2.学生信息管理=================")
				print(f"--1.) 添加学生信息")
				print(f"--2.) 删除学生信息")
				print(f"--3.) 修改学生信息")
				print(f"--4.) 查看学生信息")
				print(f"=======输入回车可返回上一级菜单============")

				choice01 = input(f"输入操作选项(1-4)：")

				if choice01 == "1":
					while True:
						xingming = input(f"输入学生姓名：")
						xingbie = input(f"选择学生性别(男/女)：")
						nianling = input(f"选择学生年龄(10-15)：")

						if not bool(xingbie):
							print(f"无效的学生姓名，重新输入。")
							continue

						if xingbie != "男" and xingbie != "女":
							print(f"无效的学生性别，重新输入。")
							continue

						if (not bool(nianling)) or (10 > int(nianling) or int(nianling) > 15):
							print(f"无效的学生年龄，重新输入。")
							continue

						if bool(xingming) and bool(xingbie) and bool(nianling):
							break
						else:
							print(f"输入错误，检查并确认输入内容，重新输入。")

					student.add_student(xingming, xingbie, nianling)
				elif choice01 == "2":
					while True:
						print(f"------------------3.删除学生信息------------------")
						print(f"---1.) 通过学号删除")
						print(f"---2.) 通过姓名删除")
						print(f"=======输入回车可返回上一级菜单============")

						choice12 = input(f"输入操作选项(1-2)：")

						if choice12 == "1":
							tmp = 1
							while True:
								tmp_xuehao = input(f"输入要删除的学员学号：")

								if bool(tmp_xuehao):
									print(f"1. 开始执行删除操作")
									break
								else:
									print(f"输入错误，重新输入要删除的学员学号。")
									continue

							student.remove_student(tmp, tmp_xuehao)
						elif choice12 == "2":
							tmp = 2
							while True:
								tmp_xingming = input(f"输入要删除的学员姓名：")

								if bool(tmp_xingming):
									print(f"2. 开始执行删除操作")
									break
								else:
									print(f"输入错误，重新输入要删除的学员姓名。")
									continue

							student.remove_student(tmp, tmp_xingming)
						else:
							print(f"返回上级菜单。")
							break
				elif choice01 == "3":
					while True:
						print(f"------------------3.修改学生信息------------------")
						print(f"---1.) 通过学号修改")
						print(f"---2.) 通过姓名修改")
						print(f"=======输入回车可返回上一级菜单============")

						choice03 = input(f"输入操作选项(1-2)：")

						if choice03 == "1":
							while True:
								print(f"------------------4.通过学员学号修改学生信息------------------")
								print(f"----1.) 修改学员姓名")
								print(f"----2.) 修改学员性别")
								print(f"----3.) 修改学员年龄")
								print(f"=======输入回车可返回上一级菜单============")

								choice031 = input(f"输入操作选项(1-3)：")

								if choice031 == "1":
									tmp = 1
									tmp_xuehao = input(f"输入要修改的学员学号：")
									if not bool(tmp_xuehao):
										print(f"输入错误，重新输入学员学号。")
										continue
									xingming = input(f"输入新的学员姓名：")
									if not bool(xingming):
										print(f"无效的学生姓名，重新输入。")
										continue
									student.xiugai_student_xuehao(tmp, tmp_xuehao, xingming)
								elif choice031 == "2":
									tmp = 2
									tmp_xuehao = input(f"输入要修改的学员学号：")
									if not bool(tmp_xuehao):
										print(f"输入错误，重新输入学员学号。")
										continue
									xingbie = input(f"输入新的学员性别(男/女)：")
									if xingbie == "男" or xingbie == "女":
										student.xiugai_student_xuehao(tmp, tmp_xuehao, xingbie)
									else:
										print(f"学员性别输入错误，重新输入。")
										continue
								elif choice031 == "3":
									tmp = 3
									tmp_xuehao = input(f"输入要修改的学员学号：")
									if not bool(tmp_xuehao):
										print(f"输入错误，重新输入学员学号。")
										continue
									nianling = input(f"输入新的学员年龄(10-15)：")
									if not bool(nianling):
										print(f"无效输入，重新输入新的学员年龄(10-15)：")
										continue

									if 10 <= int(nianling) <= 15:
										student.xiugai_student_xuehao(tmp, tmp_xuehao, nianling)
									else:
										print(f"学员年龄输入错误，重新输入。")
										continue
								else:
									print(f"返回上级菜单。")
									break
						elif choice03 == "2":
							while True:
								print(f"------------------4.通过学员姓名修改学生信息------------------")
								print(f"----1.) 修改学员姓名")
								print(f"----2.) 修改学员性别")
								print(f"----3.) 修改学员年龄")
								print(f"=======输入回车可返回上一级菜单============")

								tmp_xingming = input(f"输入要修改的学员姓名：")
								if not bool(tmp_xingming):
									print(f"输入错误，重新输入学员姓名。")
									continue
								choice032 = input(f"输入操作选项(1-3):")

								if choice032 == "1":
									tmp = 1
									xingming = input("输入新的学员姓名：")
									if not bool(xingming):
										print(f"无效的学生姓名，重新输入。")
										continue
									student.xiugai_student_xingming(tmp, tmp_xingming, xingming)
								elif choice032 == "2":
									tmp = 2
									xingbie = input("输入新的学员性别(男/女)：")
									if xingbie == "男" or xingbie == "女":
										student.xiugai_student_xingming(tmp, tmp_xingming, xingbie)
									else:
										print(f"学员性别输入错误，重新输入。")
										continue
								elif choice032 == "3":
									tmp = 3
									nianling = input(f"输入新的学员年龄(10-15)：")
									if not bool(nianling):
										print(f"无效输入，重新输入新的学员年龄(10-15)：")
										continue

									if 10 <= int(nianling) <= 15:
										student.xiugai_student_xingming(tmp, tmp_xingming, nianling)
									else:
										print(f"学员年龄输入错误，重新输入。")
										continue
								else:
									print(f"返回上级菜单。")
									break
						else:
							print(f"返回上级菜单。")
							break
				elif choice01 == "4":
					student.show_student()
				else:
					print(f"返回上级菜单。")
					break
		elif choice == "2":
			while True:
				print(f"=================2. 学生成绩管理=================")
				print(f"1.) 修改学生成绩")
				print(f"2.) 查看学生成绩")
				print(f"=======输入回车可返回上一级菜单============")

				choice02 = input(f"输入操作选项(1-2)：")

				if choice02 == "1":
					while True:
						print(f"=================3. 修改学生成绩=================")
						print(f"1.) 通过学号修改")
						print(f"2.) 通过姓名修改")
						print(f"=======输入回车可返回上一级菜单============")

						choice21 = input(f"输入操作项(1-2)：")

						if choice21 == "1":
							while True:
								print(f"=================4. 修改学生成绩=================")
								print(f"1.) 修改语文成绩")
								print(f"2.) 修改数学成绩")
								print(f"3.) 修改英语成绩")
								print(f"4.) 修改全部成绩")
								print(f"=======输入回车可返回上一级菜单============")

								choice20 = input(f"输入要修改的学员学号：")
								if not bool(choice20):
									print(f"无效输入，重新输入学员学号。")
									continue
								choice22 = input(f"输入修改操作选项(1-4)：")

								if choice22 == "1":
									tmp = 1
									tmp_yuwen = input(f"输入学员语文成绩：")
									if 0 <= int(tmp_yuwen) <= 100:
										student.xiugai_chengji(tmp, choice20, tmp_yuwen)
									else:
										print(f"无效输入，请重新输入。")
										continue
								elif choice22 == "2":
									tmp = 2
									tmp_shuxue = input(f"输入学员数学成绩：")
									if 0 <= int(tmp_shuxue) <= 100:
										student.xiugai_chengji(tmp, choice20, tmp_shuxue)
									else:
										print(f"无效输入，请重新输入。")
										continue
								elif choice22 == "3":
									tmp = 3
									tmp_yingyu = input(f"输入学员英语成绩：")
									if 0 <= int(tmp_yingyu) <= 100:
										student.xiugai_chengji(tmp, choice20, tmp_yingyu)
									else:
										print(f"无效输入，请重新输入。")
										continue
								elif choice22 == "4":
									tmp_yuwen = input(f"输入学员语文成绩：")
									tmp_shuxue = input(f"输入学员数学成绩：")
									tmp_yingyu = input(f"输入学员英语成绩：")
									if (0 <= int(tmp_yuwen) <= 100) and (0 <= int(tmp_shuxue) <= 100) and(0 <= int(tmp_yingyu) <= 100):
										student.xiugai_chengji_all(choice20, tmp_yuwen, tmp_shuxue, tmp_yingyu)
									else:
										print(f"无效输入，请重新输入。")
										continue
								else:
									print(f"返回上级菜单。")
									break
						elif choice21 == "2":
							while True:
								print(f"=================4. 修改学生成绩=================")
								print(f"1.) 修改语文成绩")
								print(f"2.) 修改数学成绩")
								print(f"3.) 修改英语成绩")
								print(f"4.) 修改全部成绩")
								print(f"=======输入回车可返回上一级菜单============")

								choice23 = input(f"输入要修改的学员姓名：")
								if not bool(choice23):
									print(f"无效输入，重新输入学员姓名。")
									continue
								for tmp_stu in student.xsxx:
									print(f"{tmp_stu["xingming"]}")
									print(choice23)
									if tmp_stu["xingming"] == choice23:
										tmp_xuehao = int(tmp_stu["xuehao"])
										break

								choice22 = input(f"输入修改操作选项(1-4)：")

								if choice22 == "1":
									tmp = 1
									tmp_yuwen = input(f"输入学员语文成绩：")
									if 0 <= int(tmp_yuwen) <= 100:
										student.xiugai_chengji(tmp, tmp_xuehao, tmp_yuwen)
									else:
										print(f"无效输入，请重新输入。")
										continue
								elif choice22 == "2":
									tmp = 2
									tmp_shuxue = input(f"输入学员数学成绩：")
									if 0 <= int(tmp_shuxue) <= 100:
										student.xiugai_chengji(tmp, tmp_xuehao, tmp_shuxue)
									else:
										print(f"无效输入，请重新输入。")
										continue
								elif choice22 == "3":
									tmp = 3
									tmp_yingyu = input(f"输入学员英语成绩：")
									if 0 <= int(tmp_yingyu) <= 100:
										student.xiugai_chengji(tmp, tmp_xuehao, tmp_yingyu)
									else:
										print(f"无效输入，请重新输入。")
										continue
								elif choice22 == "4":
									tmp = 4
									tmp_yuwen = input(f"输入学员语文成绩：")
									tmp_shuxue = input(f"输入学员数学成绩：")
									tmp_yingyu = input(f"输入学员英语成绩：")
									if (0 <= int(tmp_yuwen) <= 100) and (0 <= int(tmp_shuxue) <= 100) and(0 <= int(tmp_yingyu) <= 100):
										student.xiugai_chengji(tmp_xuehao, tmp_yuwen, tmp_shuxue, tmp_yingyu)
									else:
										print(f"无效输入，请重新输入。")
										continue
								else:
									print(f"返回上级菜单。")
									break
						else:
							print(f"返回上级菜单。")
							break
				elif choice02 == "2":
					student.chakan_chengji()
				else:
					print(f"返回上级菜单。")
					break
		elif choice == "3":
			student.show_student_all()
		elif choice == "4":
			save_to_file(student)
		elif choice == "5":
			reload_from_file(student)
		elif choice == "7":
			while True:
				print(f"-------------2.学员信息查询----------------")
				print(f"1. 使用学号查询")
				print(f"2. 使用姓名查询")
				print(f"=============输入回车可返回上一级菜单========")

				choice71 = input(f"选择查询方式(1-2)：")

				if choice71 == "1":
					tmp = 1
					chaxun_canshu = input(f"输入要查询的学员学号：")
					if not bool(chaxun_canshu):
						print(f"无效输入，请重新输入。")
						continue
					student.find_stadent(tmp,chaxun_canshu)
				elif choice71 == "2":
					tmp = 2
					chaxun_canshu = input(f"输入要查询的学员姓名：")
					if not bool(chaxun_canshu):
						print(f"无效的学生姓名，重新输入。")
						continue
					student.find_stadent(tmp,chaxun_canshu)
				else:
					print(f"返回上级菜单。")
					break
		elif choice == "8":
			print(f"服务不可用，功能正在开发中.....")
			continue
		elif choice == "6":
			# tcxt ： 退出确认
			tcxt = input(f"正在退出学生信息管理系统，是否确认。（Y/N）")
			if tcxt == "y" or tcxt == "Y":
				save_to_file(student)
				print(f"退出学生信息管理系统。")
				break
			elif tcxt == "n" or tcxt == "N":
				print(f"取消退出学生信息管理系统。")
				continue
			else:
				print(f"无效输入，请重新输入。")
		else:
			print(f"无效输入,请重新输入指定操作选项。")