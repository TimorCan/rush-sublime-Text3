import sublime
import sublime_plugin,time
import os
import subprocess


class rushCommand(sublime_plugin.TextCommand):
    def is_visible(self):
        file_name = self.view.file_name()
        if file_name.endswith(".rush"):
            return True
        else:
            return False    



    def run(self,edit):
        file_name = self.view.file_name()
        # file_path = os.path.dirname(file_name)
        #完整的文件路径
        # complete_path = file_path + file_name
        # print("complete_path is *********************")
        # print(file_name)
        #next-->执行命令行
        command_path = '/AppleInternal/Library/Frameworks/Rush.framework/bin/rush ' + file_name
        if command_path.endswith('.rush'):
            #这里可以执行下 rush ~/..../file.rush
            out = subprocess.check_output(command_path, shell=True)
            print(str(out,encoding='utf-8'))
        else:
            return




class zsCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        #当前视图
        view = self.view
        #当前选择的区域
        sels = view.sel()
        selContent = ''
        if len(sels) > 0 :
            #获取以一个选中区域
            sels = sels[0]
        #获取选中区域内容
        regionStr = view.substr(sels)
        #重新拼接字符串--前面插入一个tab
        for s in regionStr.split('\n'):
            selContent += '\t' + s + '\n';
        #剪切掉当前选中的内容
        view.run_command('cut')
        #获取当前时间
        curtime = time.strftime('%Y-%m-%d %X',time.localtime(time.time()))
        content = ' #  @athor #作者\n  # @desc #描述\n  # @date ' + curtime + '\n'
        content = content + selContent;
        view.insert(edit,0,content)
        #清空剪切板
        sublime.set_clipboard('')       


 
        	



