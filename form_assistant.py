# coding=utf-8
import os.path
import time

def formatFilename():  # 自动添加后缀名
    filename = input("输入文件名：")
    if filename[-4:] != '.csv':
        filename = filename + '.csv'
    return filename
def getInputStr(col):  # 检查输入合法性
    strcheck = 0
    while strcheck == 0:
        inputstr = input('第 %d 列：' % col)
        strcheck = 1
        for c in inputstr:
            if c == ',':
                print('数据中不能含有逗号，请重新输入。')
                strcheck = 0
    return inputstr

QUIT_KEY = 'quit'  #退出程序关键字

#print('\n♥♥♥♥♥ 本程序用于方便宝贝儿填表 ♥♥♥♥♥\n')
# 已经分了，此行留作纪念

print('输入的数据将保存为逗号分隔值文件(.csv)')

#判断文件操作模式
nameStatus = 0
while nameStatus == 0:
    filename = formatFilename()
    if os.path.isfile(filename):
        oac = input('文件 ' + filename + ' 已存在，覆盖/追加/放弃 (O/A/C*)？')
        if oac == 'O' or oac == 'o':
            nameStatus = 1 #覆盖
        elif oac == 'A' or oac == 'a':
            nameStatus = 2 #追加
        else:
            pass
    else:
        nameStatus = 1 #新建

#判断坐标信息
if nameStatus == 1:
    fo = open(filename, mode='w+')
    print('已创建文件 ' + filename + '\n')
    coln = int(input('请输入列数：'))
    ln = 1
    col = 1
else:
    fo = open(filename, mode='r')
    lines = fo.readlines()
    fo.close()
    fo = open(filename, mode='a+')
    print('已读取文件 ' + filename + '\n')
    if len(lines) == 0:
        coln = int(input('文件 ' + filename + ' 为空文件，请输入列数：'))
        ln = 1
        col = 1
    elif len(lines) == 1 and lines[0][-1] != '\n':
        col = lines[0].count(',') + 2
        coln = int(input('当前在第 1 行，第 %d 列，列表首行可能未完成，请输入列数（不小于 %d）：' % (col, col-1)))
        ln = 1
    else:
        coln = lines[0].count(',') + 1
        print('当前列表共 %d 列' % coln)
        ln = len(lines)
        if lines[-1][-1] == '\n':
            col = coln + 1
        else:
            col = lines[-1].count(',') + 2
    if len(lines) > 0:
        print('当前位置之前的部分数据：\n')
        if len(lines) > 1:
            print('第 %d 行：' % (ln-1) + lines[-2].strip('\n'))
        print('第 %d 行：' % ln + lines[-1].strip('\n') + '\n')
    if col > coln:
        ln += 1
        col = 1
        if lines[-1][-1] != '\n':
            fo.write('\n')
print('列数：%d，当前位置：第 %d 行，第 %d 列。\n' % (coln, ln, col))

#输入数据
print('输入数据，每行一个，输入 ' + QUIT_KEY + ' 退出：')
while True:
    print('----- 第 %d 行 -----' % ln)
    while col <= coln:
        inputstr = getInputStr(col)
        if inputstr == QUIT_KEY:
            break
        if col != 1:
            fo.write(',')
        fo.write(inputstr)
        col += 1
    if inputstr == QUIT_KEY:
        break
    fo.write('\n')
    ln += 1
    col = 1
fo.close()
print('数据已保存为 ' + filename + '，正在退出……')
time.sleep(0.32)
