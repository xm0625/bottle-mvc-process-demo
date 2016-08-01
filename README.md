bottle-mvc-process-demo
===
  bottle框架的mvc项目demo
  
简介
---
  基于bottle(0.13-dev)设计的一个mvc框架,这是一个不需要额外依赖即可运行的很棒的web server.

特点
---
  1.多进程web server  
  2.cors跨域支持  
  3.全局异常处理  
  4.不需要安装额外依赖  
  
环境需求
---
  Python2.6+
  
如何运行
---
  1.下载项目源码  
  2.进入项目源码文件夹  
  3.执行 python app.py  
  4.访问http://127.0.0.1:8000/xxxx(详见demo中的api定义)  

参考项目
---
[salimane/bottle-mvc][1]  
[bottlepy/bottle][2]  
[muayyad-alsadi/python-PooledProcessMixIn][3]  

如何升级bottle
---
  因为bottle是单文件的微型python web框架,所以只需要从bottle官网下载bottle.py并替换project目录下的bottle.py即可.  
  升级bottle后  
    1.原有demo中的view模板(.tpl文件)可能需要根据新版bottle语法进行更新.  
    2.原有的demo api 可能由于语法变更而失效,删除皆可  

文档
---
  参见[Bottle: Python Web Framework][4]

License
---
  MIT license. 

  [1]: https://github.com/salimane/bottle-mvc
  [2]: https://github.com/bottlepy/bottle
  [3]: https://github.com/muayyad-alsadi/python-PooledProcessMixIn
  [4]: http://www.bottlepy.org/docs/dev/index.html
