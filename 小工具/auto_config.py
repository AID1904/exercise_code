"""
auto_config.py

致力于解决配置的苦恼，将所有配置脚本化！

"""
import os



class EclipseNewJavaProject:
    """
    自动配置 java 的 eclipse project，适用于 vscode 开发

    搭配 vscode 的 remote ssh,  java extension pack 使用更佳
    """
    def __init__(self, path):
        self.path = path
        self.name = path.split("/")[-1]
        self.status = True
        self.entry()

    def initial(self):
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

    def import_jars(self, jars_path):
        dst = "%s/lib" % self.path
        self.ergodic(jars_path, lambda p: p[len(p) - 4:len(p)] == ".jar",
                     lambda p, file_path: self.copy_file(file_path, "%s/%s" % (dst, p)))
        self.new_classpath()

    @staticmethod
    def ergodic(path, condition_func, operation_func, *args, **kwargs):
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
                EclipseNewJavaProject.ergodic(file_path, condition_func, operation_func)
            elif condition_func(p, *args, **kwargs):
                operation_func(p, file_path, *args, **kwargs)

    @staticmethod
    def copy_file(file_path, dst):
        fr = open(file_path, "rb")
        fw = open(dst, "wb")
        r = fr.read()
        fw.write(r)
        fw.close()
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
        fo.write("\t<classpathentry kind = \"src\" path = \"src\" / >\n")
        fo.write("\t<classpathentry kind = \"output\" path = \"bin\" / >\n")
        self.ergodic("%s/lib" % self.path, lambda p: p[len(p) - 4:len(p)] == ".jar",
                     lambda p, file_path: fo.write("\t<classpathentry kind=\"lib\" path=\"lib/%s\"/>\n" % (p)))
        fo.write("</classpath>")
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
        fw.write("</projectDescription>\n")
        fw.close()
        

    def entry(self):
        """
        逻辑待完善
        :return:
        """
        if os.path.exists(self.path):
            self.status = False
        if self.status:
            while True:
                self.initial()
                c = input("创建项目成功，是否导入相关jar包？[y/n]：")
                if c == "y":
                    jars_path = input("请输入源路径：")
                    self.import_jars(jars_path)
                    break
                elif c == "n":
                    self.help()
                    break
        while True:
            c = input("项目已存在，是否覆盖？[y/n]")
            if c == "y":
                self.initial()
                break
            elif c == "n":
                self.help()
                break

    def help(self):
        """
        帮助界面待完善
        :return:
        """
        print("对象方法：")
        print("import_jars(jars_path)  导入jar包")
        print("import_jars(jars_path)  导入jar包")

    def manifest(self):
        """
        定义主清单
        """
        pass
