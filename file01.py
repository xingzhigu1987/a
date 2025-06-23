# 编写一个Python程序，要求用户输入多行文字（每行按回车，输入“exit”结束），并把这些内容写入到一个名为`file01.txt`的文件中。
# 写入完成后，再从文件中读取所有内容并打印到屏幕上。

file = open("file01.txt", mode="a", encoding="utf-8")
while True:
	tmp = input("输入内容：").strip() 
	if tmp != "exit":
		file.write(tmp+"\n")
		continue
	else:
		file.close()
		print("用户输入结束语句，程序结束。")
		break
# file = open("file01.txt", "r")
# read = file.read()
# file.close()
# print(read)
with open("file01.txt", "r", encoding="utf-8") as file:
	read = file.read()
	print(read)

# 有一个名为`numbers.txt`的文本文件，文件中每一行都是一个整数（假设数据已给好）。
# 编写程序读取这个文件，将所有整数求和，并把结果写入`result.txt`。

from random import randint
file = open("numbers.txt", "w", encoding="utf-8")
for i in range(randint(5, 20)):
	num = str(randint(5, 100))
	file.write(num + "\n")
file.close()

sum = 0
num_list = []
with open("numbers.txt", "r", encoding="utf-8") as file:
	for line in file:
		num = int(line.strip())
		num_list.append(num)

for i in num_list:
	sum += i

file = open("result.txt", "w")
file.write(str(sum))
file.close()

print(f"本次计算元素包含：{num_list}")
print("sum = " + str(sum))

# 要求用户输入若干个学生的信息（每个学生包括姓名、年龄、成绩），
# 将这些信息逐行保存到`students.txt`中，每个学生一行，用逗号分隔。
# 然后读取文件内容，并把学生信息按如下格式输出：  `姓名：XXX，年龄：XX，成绩：XX`
def save_to_stuinfo(stu_data, filename="stu_info.txt"):
	f = open(filename, "a", encoding="utf-8")
	print(stu_data)
	for user, stu in stu_data.items():
		tmp_stu =",".join(stu) + "\n"
		f.write(tmp_stu)
	f.close()
	print("学员信息已经保存到配置文件中。")

def load_from_stuinfo(filename="stu_info.txt"):
	stu_dict = {}
	f = open(filename, "r", encoding="utf-8")
	for line in f:
		stu_list = []
		use_name, use_age, use_grades = line.strip().split(",")
		print(f"学员信息： 姓名：{use_name} 年龄：{use_age} 成绩：{use_grades} ")
		stu_list.append(use_name)
		stu_list.append(use_age)
		stu_list.append(use_grades)

		stu_dict[use_name] = stu_list
	f.close()
	return stu_dict

def add_stu():
	stu_name = input("输入学生姓名：").strip()
	# if stu_name == 
	stu_age = input("输入学生年龄：")
	stu_grades = input("输入学生成绩：")
	return stu_name, stu_age, stu_grades

stu_info = {}
while True:
	print('''----学生信息管理系统----
1. 添加学生信息
2. 保存学生信息
3. 加载学生信息
4. 退出系统
''')
	choices = input("输入操作项：").strip()

	if choices == "1":
		for i in range(5):
			stu_tmp = []
			print(f"第{i+1}个学生".center(50,"-"))
			name, age, grades = add_stu()
			stu_tmp.append(name)
			stu_tmp.append(age)
			stu_tmp.append(grades)
			stu_info[name] = stu_tmp
		print("已添加5个学员信息，请及时保存。")
	elif choices == "2":
		save_to_stuinfo(stu_info)
	elif choices == "3":
		stu_info = load_from_stuinfo()
	elif choices == "4" or choices == "":
		exit("正在退出系统，再见。")
	else:
		print("无效输入，请重新输入操作项。")




# 读取一个名为`note.txt`的文本文件，将其中所有出现的“Python”改为“小蛇”，并将修改后的内容保存到新文件`note_new.txt`中.

f1 = open("note.txt", "r", encoding="utf-8")
f2 = open("note_new.txt", "w", encoding="utf-8")
old_str = "Python"
new_srt = "小蛇"

f1_data = f1.read()
f2_data = f1_data.replace(old_str, new_srt)
f2.write(f2_data)
f1.close()
f2.close()
print("内容替换完成，请注意查看新的文件文件")

# 编写程序，将一个指定文件（如`numbers.txt`）的内容完整复制到另一个文件（如`copy.txt`）。

f1 = open("numbers.txt", "r")
f2 = open("copy.txt", "w")
for line in f1:
	str = line.strip() + "\n"
	f2.write(str)
f1.close()
f2.close()
print("文件复制完成")