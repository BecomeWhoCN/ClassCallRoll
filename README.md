## BecomeWhoCN/ClassCallRoll

### 版权声明和其他

<img src="https://img2.imgtp.com/2024/04/04/SP1MAEPi.png" style="float:left;zoom:50%"/>准守MIT协议，你可以自由修改和使用，请注明脚本来自[Github-BecomeWhoCN](https://github.com/BecomeWhoCN)
退出软件将会重置点名记录，为了精简未使用cookies，启动将自动占用5022端口提供服务
其他：阅读使用规范和使用手册（readme.md/readme.html)
使用须知：在根目录中必须要有一个名为`名单.csv`的文件，字符集默认为GBK和UTF-8，支持使用代码编辑器和各类office套件

### 部署说明

前端：Html，JS  
后端：Python 
第三方python库：pandas，numpy，flask

编译后的版本：下载编译的zip文件，解压后请修改`名单.csv`文件即可，启动请点击 `main.exe` 文件，系统会自动读取csv文件中的信息并且启动浏览器。可以根据个人需要修改template模板

源码模式：源码模式需要你本地有python3.6以上的版本并且拥有pandas，numpy，flask第三方库。提前修改根目录下的`名单.csv`，根据需要你可以还需要修改templates中html样式，随后在命令行或者开发环境中运行main.py运行即可。

打包推荐命令：`pyinstaller --noconfirm --log-level=WARN --clean --add-data "./templates;templates" --icon=./templates/ClassCallRoll.ico main.py`

##### 点名记录消失的情况

- 手动关闭程序或者flask窗口		
- 在浏览器中点击更新csv文件或者清除数据

### 可移植性说明

 `名单.csv`文件: csv文件存储了班级中的人员信息，在每次运行代码的时候会提取文件作为抽奖的资源。你也可以在代码运行的时候做热更新，在功能栏中。但是我依然推荐更新后再开启软件，热更新作为对数据微调。
字段介绍：包括id:自增字段，name:人名，chance:概率。name存储的同学名字，chance是概率，最低为1，100%。如填5则为500%的概率抽中。
修改html模板，你可以定位到项目中的templates，index.html中存放的是首页信息，这里推荐修改head中的title信息和body下的h1标签。其他的可以根据需要酌情进行修改。

### 其他

关于group页面：针对于小组点名使用，例如模板中总共有63人来自于10个小组，系统会自动读取csv文件中的分组信息列出所有可用得小组人员信息，不需要手动填写。

readme.html: 此文件的声明文件和使用前必读。

404.html：页面导向
