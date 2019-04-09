import sublime
import sublime_plugin
import os
import subprocess


class rushCommand(sublime_plugin.TextCommand):
    
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
        	



