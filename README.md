# py_chinese_encoding
一个编码转换模块，在python2中用以猜测中文文本编码并提供输入、输出的兼容。

## 使用方法

```python
from cn_encoding import CnEncoding

ce = CnEncoding(st, encoding)
# 读取st的内容，并标记为encoding指定的编码。如果不写第二个参数，或encoding为空字符串''，则自动猜测中文编码
print str(ce), unicode(ce), ce.to_encode('gbk')
# 实现了str(使用原编码), unicode(转换为unicode对象)，to_encode(返回重新转换为指定编码的str对象)
```
