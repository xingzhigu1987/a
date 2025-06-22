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

# 要求用户输入若干个学生的信息（每个学生包括姓名、年龄、成绩），将这些信息逐行保存到`students.txt`中，
# 每个学生一行，用逗号分隔。
# 然后读取文件内容，并把学生信息按如下格式输出：  `姓名：XXX，年龄：XX，成绩：XX`



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