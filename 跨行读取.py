#可能Python会提示缺少模块，请在命令行使用“pip install 模块名”安装
#下面的路径改为转换成十六进制txt文件的路径，Windows用户特别注意斜杠是/而不是\
#因为这个命令是在Ubuntu下运行的，所以没有盘符，请根据自身情况调整
import linecache,re,os,time
file_path = '/media/olaf/OLAF/output_DNA.txt'
def get_line_context(file_path, line_number):
    return linecache.getline(file_path, line_number).strip()

#for循环的“3860540”改为十六进制文件的总行数+1
#801为步长，这里我以十六进制总行数除以视频总帧率，得到的就是步长
for line_number in range(1,3860540,801):
    str_line = get_line_context(file_path, line_number)
    print(str_line)
    str_line = get_line_context(file_path, line_number + 1)
    print(str_line)
    str_line = get_line_context(file_path, line_number + 2)
    print(str_line)
    str_line = get_line_context(file_path, line_number + 3)
    print(str_line)
#上面为每个步长显示4行，可以根据需要按照格式补充/删减代码
#下面是显示完每行的休眠时间，删除timesleep行则不休眠
#如果是录视频推荐调整为0.1或更慢
    time.sleep(0.04)
#清屏命令。只在命令行模式运行有效
#如果你是Windows用户，请改为cls
#Linux用户不需要修改
#macOS用户未测试，应该和Linux一样
    os.system("clear")
#显示完所有行的休眠时间，可以删除
time.sleep(2)
