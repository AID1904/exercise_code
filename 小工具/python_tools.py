"""
python_tools.py
python小工具
"""
def ergodic(path,condition_func,operation_func):
    """
    遍历系统指定文件夹 获取指定特征的文件名 自定义操作
    兼容linux和windows
    :param path: 文件夹路径
    :param condition_func: 条件控制函数
    :param operation_func: 操作函数
    :return:
    """
    import os
    dirs_list = os.listdir('%s'%path)
    for p in dirs_list:
        file_path = "%s/%s"%(path,p)
        if os.path.isdir(file_path):
            ergodic(file_path,condition_func,operation_func)
        elif condition_func(p):
            operation_func()
