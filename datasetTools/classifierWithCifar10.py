# coding: utf-8
# author: @AbsentM
# Date: 2016-07-13 21:00:19
# Doc: readme.md

import csv
import os
import shutil
import sys

# 获取文件名（除去后缀）
def getImageFilePre(filename):
	if filename.endswith(".png"):
		temp = filename.split(".")
		filePre = temp[0]
		return filePre

# string 转 int
def str2Int(stringValue):
	return int(stringValue)

# int 转 string
def int2Str(intValue):
	return str(intValue)

# 文件重命名
def fileRename(dirPath):
	# 三个参数：分别返回
	# 1.父目录
	# 2.所有文件夹名字（不含路径）
	# 3.所有文件名字
	for parent, dirnames, filenames in os.walk(dirPath):
		for dirname in  dirnames:                       #输出文件夹信息
			count = 1
			newTmpPath = os.path.join(dirPath, dirname)
			os.chdir(newTmpPath)
			fileContents = os.listdir(newTmpPath)

			for curFile in fileContents:
				if curFile.endswith(".png"):
					newName = dirname + "."+ int2Str(count) + ".png"
					count = count + 1
					shutil.move(curFile, newName)
					print curFile + " -> " + newName + " ------> OK!"

def main():
	# 读取标签文件内容
	csvfile = file('trainLabels.csv', 'rb')
	reader = csv.reader(csvfile)
	reader = list(reader) # 转化为list列表

	# 读取目录下文件列表
	dirPath = "~\\data_origin\\train_200"
	os.chdir(dirPath)
	dirContents = os.listdir(dirPath)
	dirContents.sort(key=lambda x:int(x[:-4])) #按文件名排序

    totalFiles = 50001
	for num in range(1, totalFiles):  # 0-199
		labelContent = reader[num]
		labelID = reader[num][0]
		labelName = reader[num][1]
		imageFilename = dirContents[num-1]
		tmpFilePre = getImageFilePre(dirContents[num-1])

		if str2Int(labelID) == str2Int(tmpFilePre):
			print "labelID == filePre !!!"
			baseDirPath = "~\\data_origin\\train_with_class"
			new_dir_name = labelName
			new_dir_path = os.path.join(baseDirPath, new_dir_name)

			isExists = os.path.isdir(new_dir_path)
			if not isExists:
				os.makedirs(new_dir_path)
				print new_dir_path + " 创建成功！"
			else:
				print new_dir_path + "目录已存在！"

			shutil.copy(imageFilename, new_dir_path)

		print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

	csvfile.close()

	rootPath = "~\\data_origin\\train_with_class"
	fileRename(rootPath)

if __name__ == '__main__':
	main()
