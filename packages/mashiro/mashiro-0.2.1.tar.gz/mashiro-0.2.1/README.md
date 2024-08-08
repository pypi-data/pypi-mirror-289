# Mashiro
呐，欢迎回到『さくら荘』

![Shiina Mashiro](https://ximg.us.kg/34F037E7C53EB31B616CA42CB3ED9437)

> 一成不变的日子，总觉得索然无味，但是，在夏天，捡了这只纯白色的猫，住进樱花庄后，我发现了，无聊的并不是时间，而是和平凡无奇的自己.

这是我的自用库——Mashiro。因为太~~菜~~懒了只好把几个常用的代码块做成函数打包发布.

## 用法

1. `webget(u, encoding='utf-8')`
获取URL页面内容，返回字符串，可通过encoding指定编码.
自带随机UA.

2. `get(url, outfile)`
下载URL内容到本地（bin）. 返回`bool`.
自带随机UA.

3. `btw(a,b,string)`
获取两个字符串之间的内容，返回`list`.

4. `mkdir(filepath)`
新建文件夹，如果文件夹存在自动跳过.

5. `readJSON(file_path, encoding='utf-8')`
读取JSON文件并加载为对象，可指定编码.

6. `debug(s,k)`
debug模式，用于显示变量内容（好像没什么用？）.

7. `Sakurasou()`
随机返回一句樱花庄语录.

## 写在最后
以上几个函数足以应付普通的爬虫任务. 
emmmmmmmm不知道要写什么巴拉巴拉巴拉