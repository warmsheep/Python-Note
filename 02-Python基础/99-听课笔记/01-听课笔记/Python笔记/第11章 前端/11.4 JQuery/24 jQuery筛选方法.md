## jQuery筛选方法

| 方法 | 概念 | 语法 | 代码 |
|:-- |:-- |:-- |:-- |
| eq | 获取第N个元素 | eq(index) |  $('p').eq(0) |
| first | 获取第一个元素 | first() | $('p').first() |
| last | 获取最后一个元素 | last() |
| hasClass | 检查当前的元素是否含有某个特定的类，如果有，则返回true | ('li').hasClass('li1') |
| children | 取得一个包含匹配元素集合中每一个元素的所有子元素的元素集合 | children() | $('div').children() |
| parent | 取得一个包含着所有匹配元素的唯一父元素的元素集合 | parent() | $('p').parent() |
| prev | 取得一个包含匹配的元素集合中每一个元素紧邻的前一个同辈元素的元素集合 | prev() | $('p').prev() |
| preAll | 查找当前元素之前所有的同辈元素 | preAll() | $('div:last').preAll().addClass('before') |
| siblings | 筛选给定的同胞同类元素(不包括给定元素本身) | siblings(元素) | $('#leftBoxli').eq(0).siblings('li').addClass('active') |
