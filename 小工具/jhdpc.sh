#! /bin/bash


#---------------------------------------------------
# jhdpc.sh
# 作者：hans
#----------------------------------------------------
##### 用户配置区 开始 #####

# 功能：指定文件夹，导入该文件夹内jar包，再进行编译

# _HADOOP_HOME：hadoop的安装目录 例如：/home/hadoop/app/hadoop-2.9.2
# _HADOOP_HOME=

##### 用户配置区 结束 #####


HADOOP_JAR=""
PATTERN=".jar"
_PATH=${_HADOOP_HOME}/share/hadoop

function read_dir(){
for file in `ls $1`
do
 if [ -d $1"/"$file ]
 then
  read_dir $1"/"$file
 elif [[ $file =~ $PATTERN ]]
 then
  HADOOP_JAR=${HADOOP_JAR}:$1"/"$file
 fi
done
} 
read_dir $_PATH
javac -classpath $HADOOP_JAR $1
