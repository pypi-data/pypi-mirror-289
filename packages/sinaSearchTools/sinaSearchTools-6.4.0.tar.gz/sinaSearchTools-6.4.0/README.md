<!--
 * @Author: qingfeng
 * @Date: 2024-01-18 18:57:12
 * @LastEditTime: 2024-01-18 19:37:06
 * @FilePath: /sinatools/README.md
 * @Description: 
 * 
-->
## 数据质量工具包

通过`pip3 install  sinaTools -U -i http://10.185.31.191/simple/ --trusted-host 10.185.31.191`  
安装sinaTools实现以下功能：
* 这个包是上传到我们自建的仓库，外网不可见，大家可以上传业务相关代码也行
```python
from sinaTools import wenxinTool, logger, sinaTools

log = logger()
st = sinaTools()
wx = wenxinTool(api_key='your_api_key',                  secret_key='your_secret_key')
```
----
### sinaTools类包含以下方法：
| 函数 | 说明 | 参数 | 返回值 |
|:--:|:--:|:----:|:--:|
|get_hot_query|获取热搜词|num|热搜词list|
|get_query|获取普搜词|num|普搜词list|
|send_alarm|发送报警|uid,mid,content,alarm_type|ok|
|get_mid_by_query|从ac拉到query相关的mid|query,num|midlist|
|get_weibo_from_hbase|从hbase查询博文|mid|博文字典dic|
|get_ip_list|获取ip列表|faclonURL里面的tree_id|ip列表|
|get_weibo_from_summary|从hbase获取ip列表|tree_id|ip列表|
|get_weibo_from_bs|从bs获取weibo|tree_id|weibo 字典|
|get_attr_by_mid|获取微博hbase中的字段通过mid|mid,[key]|list|
|get_attribute_from_bowen|获取微博的字段|微博dic,[key]|value|

----
### logger类包含以下方法：
| 函数 | 说明 | 参数 | 返回值 |
|--|--|--|--|
|info|info|msg|返回值|
|error|error|msg|返回值|
|debug|debug|msg|返回值|
|warning|warning|msg|返回值|

* logger类在实例化的时候会创建一个logs文件夹，这个文件夹按照你初始化的参数创建
* 例如：`log = logger(log_path='/home/logs/',log_name='test.log')`

----
### 文心一言api
| 函数 | 说明 | 参数 | 返回值 |
|--|--|--|--|
|cat_wenxing|调用文心一言api|query|返回值|

---
### 发布pip包的方法：
大家想增加自己的功能，可以克隆项目修改，在项目路径执行下面的命令，在执行之前需要注意：
1. 修改setup.py文件中的版本号
3. 修改sinaTools.py文件中的版本号
3. 修改README.md
```shell
python3 -m build
python3 -m twine upload --repository private-pypi dist/sinaTools-0.0.6.1.tar.gz -u "" -p ""
```
想发布自己的包也这么操作。
> 发布完了包之后一定要commit自己的修改到gitlab，同时增加readme中增加自己的方法的说明（在上面的表格中新增行，或者是创建类了之后，新增一个类的表格，方便大家使用你新增的功能）。