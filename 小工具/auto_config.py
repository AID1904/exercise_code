"""
auto_config.py

致力于解决配置的苦恼，将所有配置脚本化！

"""
import os

class EclipseNewJavaProject:
    """
    自动配置 java 的 eclipse project，适用于 vscode 开发

    搭配 vscode 的 remote ssh,  java extension pack 使用更佳

    配置完后，重新运行 vscode 才可生效
    """

    def __init__(self):
        self.status = True
        self.main()

    def __initial(self):
        """
        项目初始化
        :return:
        """
        # 创建项目目录
        os.mkdir(self.path)
        # 创建 bin 目录
        os.mkdir("%s/bin" % self.path)
        # 创建 src 目录
        os.mkdir("%s/src" % self.path)
        # 创建 lib 目录
        os.mkdir("%s/lib" % self.path)
        # 创建 .classpath 文件
        self.new_classpath()
        # 创建 .project 文件
        self.new_project()

    def import_jars(self):
        jars_path = input("请输入源路径：")
        dst = "%s/lib" % self.path
        self.__ergodic(jars_path, lambda p: p[len(p) - 4:len(p)] == ".jar",
                       lambda p, file_path: self.__copy_file(file_path, "%s/%s" % (dst, p)))
        self.new_classpath()
        print("导入完毕")
        return True

    @staticmethod
    def __ergodic(path, condition_func, operation_func, *args, **kwargs):
        """
        兼容linux和windows
        :param path: 文件夹路径
        :param condition_func: 条件控制函数
        :param operation_func: 操作函数
        :return:
        """
        dirs_list = os.listdir('%s' % path)
        for p in dirs_list:
            file_path = "%s/%s" % (path, p)
            if os.path.isdir(file_path):
                EclipseNewJavaProject.__ergodic(file_path, condition_func, operation_func)
            elif condition_func(p, *args, **kwargs):
                operation_func(p, file_path, *args, **kwargs)

    @staticmethod
    def __copy_file(file_path, dst):
        fr = open(file_path, "rb")
        fw = open(dst, "wb")
        r = fr.read()
        fw.write(r)
        fw.close()
        print("已添加%s" % dst)
        fr.close()

    def new_classpath(self):
        """
        创建 .classpath 文件
        :return:
        """
        dst_path = "%s/.classpath" % self.path
        fo = open(dst_path, "w", encoding="utf-8")
        fo.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
        fo.write("<classpath>\n")
        fo.write(
            "\t<classpathentry kind=\"con\" path=\"org.eclipse.jdt.launching.JRE_CONTAINER/org.eclipse.jdt.internal.debug.ui.launcher.StandardVMType/JavaSE-1.8\">\n")
        fo.write("\t\t<attributes>\n")
        fo.write("\t\t\t<attribute name=\"module\" value=\"true\"/>\n")
        fo.write("\t\t</attributes>\n")
        fo.write("\t</classpathentry>\n")
        fo.write("\t<classpathentry kind=\"src\" path=\"src\"/>\n")
        fo.write("\t<classpathentry kind=\"output\" path=\"bin\"/>\n")
        self.__ergodic("%s/lib" % self.path, lambda p: p[len(p) - 4:len(p)] == ".jar",
                       lambda p, file_path: fo.write("\t<classpathentry kind=\"lib\" path=\"lib/%s\"/>\n" % (p)))
        fo.write("</classpath>")
        print(".classpath文件写入成功")
        fo.close()

    def new_project(self):
        """
        创建 .project 文件
        :param PROJECT_NAME: 项目名称
        :param PROJECT_HOME: 项目路径
        :return:
        """
        fw = open("%s/.project" % self.path, "w")
        fw.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n")
        fw.write("<projectDescription>\n")
        fw.write("\t<name>%s</name>\n" % self.name)
        fw.write("\t<comment/>\n")
        fw.write("\t<projects/>\n")
        fw.write("\t<buildSpec>\n")
        fw.write("\t\t<buildCommand>\n")
        fw.write("\t\t\t<name>org.eclipse.jdt.core.javabuilder</name>\n")
        fw.write("\t\t\t<arguments/>\n")
        fw.write("\t\t</buildCommand>\n")
        fw.write("\t</buildSpec>\n")
        fw.write("\t<natures>\n")
        fw.write("\t\t<nature>org.eclipse.jdt.core.javanature</nature>\n")
        fw.write("\t</natures>\n")
        fw.write("</projectDescription>")
        print(".project文件写入成功")
        fw.close()

    def default_entry(self):
        """
        逻辑待完善
        :return:
        """
        if os.path.exists(self.path):
            self.status = False
        if not self.status:
            while True:
                c = input("项目已存在，是否覆盖？[y/n]")
                if c in ("y", "Y"):
                    break
                elif c in ("n", "N"):
                    return self.main()
        while True:
            self.__initial()
            c = input("创建项目成功，是否导入相关jar包？[y/n]：")
            if c not in ("y","Y","n","N"):
                continue
            elif c in ("y","Y"):
                self.import_jars()
            return self.main()

    def main(self):
        print("Eclipse new java project:")
        print("1. 默认初始化")
        print("2. 导入jar包")
        print("3. 重新生成.classpath文件")
        print("4. 重新生成.project文件")
        print("")
        print("退出请输入：q")
        # print("5. 重新生成主清单文件")
        c = input("请输入选择：")
        if c == "q":
            return print("谢谢使用！")
        if self.path == "":
            self.path = input("请输入项目路径：")
            self.name = self.path.split("/")[-1]
        if c == "1":
            self.default_entry()
        elif c == "2":
            self.import_jars()
        elif c == "3":
            self.new_classpath()
        elif c == "4":
            self.new_project()
        else:
            return self.main()

    def new_manifest(self):
        """
        定义主清单
        """
        pass


if __name__ == '__main__':
    EclipseNewJavaProject()
