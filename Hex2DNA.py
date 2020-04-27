#可能Python会提示缺少模块，请在命令行使用“pip install 模块名”安装
import linecache,re,os,time

#下面的路径改为转换成十六进制txt文件的路径，Windows用户特别注意斜杠是/而不是\
file_path = 'F:/dontstop.txt'

def get_line_context(file_path, line_number):
    return linecache.getline(file_path, line_number).strip()

total_bin = ''

#for循环的“3860540”改为十六进制文件的总行数+1
for line_number in range(1,3860540):
    str_line = get_line_context(file_path, line_number)
    list_line = str_line.split(" ")
    print(list_line)
#这里是二进制数补齐，不要修改这里的for循环数值
#除非你的十六进制文件不是以LinuxVIM生成的，则将‘8’改为一行的十六进制组数量+1
    for i in range(0,8):
        bin_source = str(bin(int(list_line[i],16)))
        bin_final = str(bin_source[2:])
        if int(len(bin_final)) != 16:
            gap = 16 - int(len(bin_source))
            for x in range(0,int(gap) + 2):
                bin_final = str("0") + str(bin_final)
        else:
            pass
        total_bin += bin_final
    print(total_bin)
    pattern = re.compile('.{2}')
    cut = (' '.join(pattern.findall(total_bin)))
#这里是DNA规则，你可以自定义修改，默认按视频的说明
    cut = cut.replace("00","A")
    cut = cut.replace("01","G")
    cut = cut.replace("10","C")
    cut = cut.replace("11","T")
#下面路径请改为输出路径，包括文件名
#文件名可以不存在，但必须保证路径存在
#同样，Windows用户要注意/
    command = ("echo " + cut + " >> F:/output_DNA.txt")
    print(command)
    os.system(command)
    total_bin = ''
