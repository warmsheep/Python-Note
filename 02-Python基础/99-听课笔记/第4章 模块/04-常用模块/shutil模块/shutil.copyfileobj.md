## shutil.copyfileobj(fsrc, fdst[, length])

将文件内容拷贝到另一个文件中


**被复制的文件必须存在**


**复制内容的文件如果不存在，就会新建该文件**


```Python
import shutil

shutil.copyfileobj(open('old.xml','r'), open('new.xml', 'w'))
```
