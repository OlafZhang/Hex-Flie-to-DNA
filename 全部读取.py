#可能Python会提示缺少模块，请在命令行使用“pip install 模块名”安装
#下面的路径改为转换成十六进制txt文件的路径，Windows用户特别注意斜杠是/而不是\
#因为这个命令是在Ubuntu下运行的，所以没有盘符，请根据自身情况调整
import linecache,re,os,time
file_path = ('/media/olaf/OLAF/output_DNA.txt')
def get_line_context(file_path, line_number):
    return linecache.getline(file_path, line_number).strip()

#for循环的“3860540”改为十六进制文件的总行数+1
for line_number in range(1,3860540):
    str_line = get_line_context(file_path, line_number)
    print(str_line)
#显示完每行的休眠时间，删除timesleep行则不休眠
#如果是录视频推荐调整为0.1或更慢
    time.sleep(0.001)
#显示完所有行的休眠时间，可以删除
time.sleep(2)
