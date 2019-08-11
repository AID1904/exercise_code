studyInTarena
===
## AID1904 开源小空间
### 2019.08.11 版本
改变该代码管理器的职能，现在功能是大家代码的开源空间  
开发流程：  
1.在本地创建一个空的文件夹，在该文件夹创建git工程   
git init  
2.添加该远程仓库，取名为aid1904   
git remote add aid1904 https://github.com/AID1904/exercise_code.git  
3.下载远程仓库的代码  
git pull aid1904 master  
4.做完修改后，保存至本地暂存区  
git add [files]  
5.将暂存区的内容保存至本地仓库  
git commit [file] -m [message]  
6.将本地仓库的内容与远程仓库同步  
git push aid1904 master  
(这里需要输入远程仓库的用户名和密码，见QQ群)  
  
### 2019.06.26 版本
目前只想到存放课堂练习的代码（按照日期存放），有待大家开发更多用途。
