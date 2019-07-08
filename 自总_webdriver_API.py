from selenium import webdriver
import time

'''
---------------------Selenium 1.0---------------------
1．Selenium IDE
Selenium IDE 是嵌入到 Firefox 浏览器中的一个插件，实现简单的浏览器操作的录制与回放功能。
2．Selenium Grid
Selenium Grid 是一种自动化的测试辅助工具，Grid 通过利用现有的计算机基础设施，能加快 Web-App 的
功能测试。利用 Grid 可以很方便地实现在多台机器上和异构环境中运行测试用例。
3．Selenium RC
Selenium RC（Remote Control）是 Selenium 家族的核心部分。Selenium RC 支持多种不同语言编写的自动
化测试脚本，通过 Selenium RC 的服务器作为代理服务器去访问应用，从而达到测试的目的。
Selenium RC 分为 Client Libraries 和 Selenium Server。Client Libraries 库主要用于编写测试脚本，用来控制
Selenium Server 的库。Selenium Server 负责控制浏览器行为。总的来说，Selenium Server 主要包括三个部分：
Launcher、Http Proxy 和 Core。其中，Selenium Core 是被 Selenium Server 嵌入到浏览器页面中的。其实 Selenium
Core 就是一堆 JavaScript 函数的集合，即通过这些 JavaScript 函数，我们才可以实现用程序对浏览器进行操作。
Launcher 用于启动浏览器，把 Selenium Core 加载到浏览器页面当中，并把浏览器的代理设置为 Selenium Server
的 Http Proxy。

--------------------Selenium 2.0-----------------------
搞清了 Selenium 1.0 的家族关系，再来看看 Selenium 2.0。Selenium 2.0 就是把 WebDriver 加入到了这个
家族中，简单用公式表示为：
Selenium 2.0 = Selenium 1.0 + WebDriver
需要强调的是，在Selenium 2.0中主推的是WebDriver，可以将其看作Selenium RC 的替代品。因为Selenium
为了保持向下的兼容性，所以在 Selenium 2.0 中并没有彻底地抛弃 Selenium RC。
----------Selenium RC 与 WebDriver 有什么区别呢？-------
Selenium RC 是在浏览器中运行 JavaScript 应用，使用浏览器内置的 JavaScript 翻译器来翻译和执行
selenese 命令（selenese 是 Selenium 命令集合）。
WebDriver 是通过原生浏览器支持或者浏览器扩展来直接控制浏览器。WebDriver 针对各个浏览器而开发，
取代了嵌入到被测 Web 应用中的 JavaScript，与浏览器紧密集成，因此支持创建更高级的测试，避免了 JavaScript
安全模型导致的限制。除了来自浏览器厂商的支持之外，WebDriver 还利用操作系统级的调用，模拟用户输入。
selenium驱动浏览器原理：
Selenium RC 是在浏览器中运行 JavaScript 应用，使用浏览器内置的 JavaScript 翻译器来翻译和执行
selenese 命令（selenese 是 Selenium 命令集合）。
WebDriver 是通过原生浏览器支持或者浏览器扩展来直接控制浏览器。WebDriver 针对各个浏览器而开发，
取代了嵌入到被测 Web 应用中的 JavaScript，与浏览器紧密集成，因此支持创建更高级的测试，避免了 JavaScript
安全模型导致的限制。除了来自浏览器厂商的支持之外，WebDriver 还利用操作系统级的调用，模拟用户输入。

------------------------------Selenium 3.0---------------------------
2016 年 7 月，Selenium3.0 悄悄发布第一个 beta 版。Selenium 3.0 做了一些不大不小的更新：
1、终于去掉了 RC，简单用公式表示为：
Selenium 3.0 = Selenium 2.0 - Selenium RC（Remote Control）  即用weddriver替代了Selenium RC
2、Selenium3.0 中的火狐浏览器驱动独立了，以前装完 selenium2 就可以驱动 Firefox 浏览器了，现在
和 Chrome 一样，必须下载和设置浏览器驱动。geckodriver.exe，双击查看浏览器驱动版本
3、MAC OS 集成 Safari 的浏览器驱动。默认在/usr/bin/safaridriver 目录下。
4、Selenium3.0 只支持 Java8 版本以上。
5、只支持 IE 9.0 版本以上;只支持火狐47以上

'''

# -------------------------操作[元素]基本方法----------------------
# 2.1 ------操作[浏览器]基本方法------
driver = webdriver.Chrome()    # 打开谷歌浏览器
driver.get("https://www.baidu.com/")   # 访问某网址
time.sleep(3)  # 设置休眠，单位秒，可以是小数
driver.refresh()    # 刷新页面
driver.back()  # 页面后退
driver.forward() # 页面前进
driver.set_window_size(540,960)  # 设置窗口大小，如手机分辨率为540*960
driver.maximize_window()  # 最大化窗口
driver.get_screenshot_as_file("d:\\test\\aa.jpg")  # 截图，定义文件位置名称
# 获取当前window的截图，出现IOError时候返回False,截图成功返回True。
test.img = driver.get_screenshot_as_base64()
driver.close()  # 关闭当前窗口
driver.quit()   # 关闭所有窗口，退出浏览器进程

# 2.2 -------常用18种元素定位------
# 定位单个元素，8种
webdriver.find_element_by_id("")
webdriver.find_element_by_name("")
webdriver.find_element_by_class_name("")
webdriver.find_element_by_tag_name("")
webdriver.find_element_by_link_text("")
webdriver.find_element_by_partial_link_text("")
webdriver.find_element_by_css_selector("")
webdriver.find_element_by_xpath("")
# 定位一组元素，返回对象列表  8种
webdriver.find_elements_by_id("") # id复数定位
webdriver.find_elements_by_name("")  # name复数定位
webdriver.find_elements_by_class_name("") # class复数定位
webdriver.find_elements_by_tag_name("") # teg复数定位
webdriver.find_elements_by_link_text("")  # link复数定位
webdriver.find_elements_by_partial_link_text("") # partial_link复数定位
webdriver.find_elements_by_css_selector("")  # css_selector 复数定位
webdriver.find_elements_by_xpath("")       # xpath复数定位
# 这两种是参数化的方法，对上面各8种的总结
webdriver.find_element(by='id', value="")
webdriver.find_elements(by='id', value="")
'''
1、xpath语法：
指明标签 //*或者 //input[@id="kw"]
根据@属性定位，id name class 或其他属性
逻辑运算and or not，用的最多的是and，同时满足两个属性，//*[@id="kw" and @name="aa"]
层级定位/，
索引定位，从1开始，input[1],多个相同标签，用索引定位
模糊匹配：标签对之间的文本信息的模糊匹配//*[contains(text(),"hao123)]
        模糊匹配某个属性//*[contains(@id,"kw")]
        模糊匹配以什么开头//*[starts-with(@id,"kw")]
        模糊匹配以什么结尾//*[ends-with(@id,"kw")]
        还支持最强的正则表达式 //*[match(text(),"kw")]  后边是我的猜测//*[match(@id,"^kw")]

2、css选择器语法：官方说法，css定位更快，语法更简洁，但是xpath更直观，更好理解一些。
指明标签  input find_elements_by_css_selector("input")
id定位 #id值  input find_element_by_css_selector("#kw")
class定位 .class值  input find_element_by_css_selector(".slp")
根据元素属性定位   [属性名="属性值"]
标签+属性定位  input[id="kw"]  input[name="aa"]
逻辑运算与，满足两个属性值  input[id="kw"][name="aa"]
层级定位>   div>li
索引定位 重复的标签名:nth-child(1) 索引从1开始
例如select下边有三个option select#nr>option:nth-child(1)
'''

# 2.6--------操作元素（键盘和鼠标事件）--------
# 2.6.1简单操作
webdriver.find_element_by_id("").click()  # 点击元素按钮
webdriver.find_element_by_id("").clear()  # 清空输入框
webdriver.find_element_by_id("").send_keys("")  # 输入字符串
# 2.6.2submit提交表单
webdriver.find_element_by_id("").submit() # 提交表单，一般用于模拟回车键
# 2.6.3键盘操作
from selenium.webdriver.common.keys import Keys
webdriver.find_element_by_id("").send_keys(Keys.ENTER)   # 模拟按enter键
webdriver.find_element_by_id("").send_keys(Keys.F1)   # 模拟按键F1到F12
webdriver.find_element_by_id("").send_keys(Keys.CONTROL, "c") # 组合键 Control+C复制 Keys.TAB 制表键Tab
# 2.6.4鼠标事件
from selenium.webdriver.common.action_chains import ActionChains
element = webdriver.find_element_by_id("")
ActionChains(driver).move_to_element(element).perform()  # 鼠标悬停
ActionChains(driver).context_click().perform()    # 鼠标右击
ActionChains(driver).double_click().perform()     # 鼠标双击
ActionChains(driver).drag_and_drop().perform()   # 拖动某元素

# 2.7----------多窗口、句柄（handle）-----------
driver.current_window_handle()  # 获取当前窗口的句柄
driver.window_handles    # 获取打开的所有窗口的句柄，是一个列表，应该会按照打开顺序的先后，返回一个句柄列表
# 切换窗口方法一
current_window = driver.current_window_handle
all_handle = driver.window_handles
for i in all_handle:
    if i != current_window:
        driver.switch_to.window()
        title = driver.title   # 判断窗口是否切换成功
# 切换窗口方法二
all_handle = driver.window_handles  # 返回句柄列表，应该是按打开窗口的先后顺序返回，后打开的排后
driver.switch_to.window(all_handle[1])  # 切换到第二个窗口
title = driver.title      # 判断窗口是否切换成功

# 2.25------------js处理多窗口-------------
# 打开页面链接时，打开新窗口，页面间切换麻烦，所以修改target属性，在当前窗口打开新页面
# 修改target="_blank"属性为target=""
# 注意：并不是所有的链接都适用于本方法，本篇只适用于有这个target="_blank"属性链接情况
js = "document.getElementByClassName('').target=''"
driver.execute_script(js)

'''
python中sort，sorted，reverse,reversed的区别
简单的说以上四个内置函数都是排序。按大小排序和反转排序
对于sort和reverse都是list列表的内置函数，一般不传参数，没有返回值，会改变原列表的值。
而sorted和reversed是python内置函数，需要传参数，参数可以是字符串，列表，字典，元组，
不管传的参数是什么sorted返回的都是列表，reversed返回的都是迭代器，原参数的值不会发生改变。
'''

# 2.9----------iframe （多表单切换？）----------
# 在 Web 应用中经常会遇到 frame/iframe 表单嵌套页面的应用，WebDriver 只能在一个页面上对元素识别与
# 定位，对于 frame/iframe 表单内嵌页面上的元素无法直接定位。这时就需要通过 switch_to.frame()方法将当前
# 定位的主体切换为 frame/iframe 表单的内嵌页面中。

# 将定位器切换到iframe上
driver.switch_to.frame("iframe_id")     # 通过iframe的id定位
driver.switch_to.frame("iframe_name")   # 通过iframe的name定位
iframe = webdriver.find_element_by_tag_name("")   # 没有id或者name为空，先定位到iframe
driver.switch_to.frame(iframe)      # 通过iframe对象定位

#释放iframe
driver.switch_to.parent_frame()  # 定位器跳回到上级页面
driver.switch_to.default_content()   # 定位器跳到最外层

# 2.10----------定位select下拉框的选项-----------
'''
<select id="nr" name="NR">
        <option selected="" value="10">每页显示10条</option>
        <option value="20">每页显示20条</option>
        <option value="50">每页显示50条</option>
</select>
'''
# 二次定位：先定位select框，再定位select里的选项 
s = driver.find_element_by_id("nr")
s.find_element_by_xpath("//option[@value='20']").click()  # 选择第二个选项
#或者driver.find_element_by_id("nr").find_element_by_xpath("//option[@value='20']").click()

# 直接定位
driver.find_element_by_xpath("//select[@id='nr']/option[2]").click()   # 选择第二个选项

# 通过select模块定位，不用click点击
from selenium.webdriver.support.select import Select
s = driver.find_element_by_id("nr")  # 先定位到select对象

Select(s).select_by_index(0)   # 通过索引定位选项，从0开始计数
Select(s).select_by_value("20")  # 通过选项标签的value值 定位选项
Select(s).select_by_visible_text("每页显示20条") # 通过选项文本定位

Select(s).deselect_by_index()  # 取消对应index选项
Select(s).deselect_by_value()  # 取消对应value选项
Select(s).deselect_by_visible_text()  # 取消对应value选项
Select(s).deselect_all()  # 取消所有选项
Select(s).first_selected_option()   # 返回第一个选项
Select(s).all_selected_options()  # 返回所有选项
s.click()  # 加这句的目的是，由于使用这种方式定位select，会导致失去焦点，
            # 后续的操作可能会有问题，比如提示框弹不出来，加这句就可以解决了

# 2.11--------alert\confirm\prompt--------
# 处理 JavaScript 所生成的 alert、confirm 以及 prompt
alert = driver.switch_to.alert()   # 先获取提示框对象，即定位到提示框
alert.text        # 获取提示框的文本信息
alert.accept()    # 点击确认按钮
alert.dismiss()   # 解散/关闭提示框
alert.send_keys() # 向prompt输入框输入内容
# 遇到的问题：提示框未能弹出来，因为上边操作了select，导致页面失去焦点
# 解决办法：在用Select类选择完选项后，点击下select自己
s = driver.find_element_by_id("nr")
Select(s).select_by_visible_text("每页显示20条")
s.click()

# 2.29-----------练习题1:去掉页面动态(弹出)窗---------------------
# js自带的提示框不美观，现在很多是自定义的弹出框
# 思路是用js将弹出框的样式对象的display属性置为none，不可见
js = "document.getElementById('弹出框id').style.display='none'"
driver.execute_script(js)

# 2.12--------单选框和复选框（radiobox、checkbox）--------
'''单选框radio代码：input的type是radio，name值相同
    <label value="radio">男</label>   
    <input name="sex" value="male" id="boy" type="radio"><br>  
    <label value="radio1">女</label>  
    <input name="sex" value="female" id="girl" type="radio">
'''
driver.find_element_by_id("boy").is_selected()  # 先判断是否被选中，是返回True，否返回False
driver.find_element_by_id("boy").click()   # 直接定位单选框并点击

# 复选框，input标签的type类型是checkbox，文本值在标签对里
# <input id="c3"type="checkbox">appium<br>  
# 单选复选框
c = driver.find_element_by_id("c3")
if not c.is_selected():  # 先判断是否被选中，是返回True，否返回False
    c.click()      # 直接定位复选框并点击

# 全选复选框
checkboxs = driver.find_elements_by_xpath("//*[@type='checkbox']")   # 定位到所有的复选框，一组
for i in checkboxs:
    if not i.is_selected():    # 先判断是否被选中，没有的话，点击选择，\
        i.click()                # 因为万一选中的话，点一下就取消选择了

#2.13-----------table表格定位-----------------
'''
<table border="1" id="myTable">  
                <tr>  
                    <th>QQ群</th>
                    <th>QQ号</th>   
                </tr>  
                <tr>  
                    <td>selenium自动化</td>  
                    <td>232607095</td>  
                </tr>  
            </table>  

'''
# 用xpath或者css层级定位,获取其文本内容，做判断
cell = driver.find_element_by_xpath("//*[@id='myTable']/tr[2]/td[1]")
# 定位的格式是固定的，只需改tr和td后面的数字就可以了.如第二行第一列tr[2]td[1].
cell.text   # 获取元素的文本内容，做判断

#2.14------------加载Firefox/Chrome浏览器配置-------------
# 加载Firefox浏览器配置，包括插件，包括窗口打开方式，保存的表单信息，已登录账号？等
profile_directory = r'C:\Users\xxx\AppData\Roaming\Mozilla\Firefox\
                    Profiles\1x41j9of.default'  # 浏览器配置文件，在帮助-故障排除信息--配置
                    # 文件夹--显示文件夹--复制该路径
profile = webdriver.FirefoxProfile(profile_directory)  # 加载浏览器配置
driver = webdriver.Firefox(profile)     #启动浏览器和相关配置
# 加载Chrome浏览器配置
option = webdriver.ChromeOptions()
option.add_agrument(r"--user-data-dir=C:\Users\你的电脑的名字？你的用户名字？"
                    r"不要用中文\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome(chrome_options=option)

# wap（手机网站）测试，使用谷歌的触屏版
option = webdriver.ChromeOptions()
option.add_agrument("--user-agent=iphone")   # 伪装iphone
option.add_agrument("--user--agent=android")  # 伪装android
driver.Chrome(chrome_option=option)

# 2.15-----------富文本（richtext是一个控件，是多行文本的通用说法？
# 在html页面上input的type里并没有richtext这个值，html里也没有这个标签）----------------
'''
1、富文本框的一种实现方式是iframe加内嵌html带有contenteditable="true"的body，最好里边加个P标签
<iframe id="ifr" src="">
<html><head></head>
<body id="tinymce" class="mceContentBody " onload="window.parent.
tinyMCE.get('Editor_Edit_EditorBody').onLoad.dispatch();"
 contenteditable="true">     # 全局属性contenteditable：是一段可编辑的段落

<p>富文本框内容</p>
</body></html>
</iframe>
'''
# 方法1：切换到iframe上，定位到body，然后send_keys()
driver.switch_to.frame("id或者name值或者frame对象")  # 先切换到iframe上
driver.find_element_by_id("body_id").send_keys(Keys.TAB)   # 执行下边一句时，也许会输入不上，先输入一个tab可以解决
driver.find_element_by_id("body_id").send_keys("富文本框内容") # 定位到body上，直接输入内容
# 方法2：不用切换iframe，直接执行js输入内容, js处理iframe问题
text = "富文本内容"
js = "document.getElementById('ifarme的id').contentWindow.document.body.innerHTML='%s'"%text
driver.execute_script(js)

'''
2、另一种是textarea文本域，定义多行的文本输入控件
<textarea id="ta" rows="3" cols="20">
输入的文本域内容
</textarea>
'''
# 只能用js修改元素的value值的方式，不能用send_keys()。定位到输入框，可以直接用value="xxx"方法输入内容
text = "富文本框的值输入内容"
js = "var sum=document.getElementById('id'); sum.value='" + text + "';"
# 我觉的也等价于下边的写法,反正都是修改某元素的属性
# js = "document.getElementById('id').value='" + text + "';"
driver.execute_script(js)

# 2.16-1--------非input文件上传（AutoIt或SendKeys库）-------------------

# 2.16-------input（type="file"）文件上传
# 思路：定位到input控件，直接send_keys(r"文件路径")
# 悠悠的例子是文件上传在一个iframe里，整个页面有俩iframe，所以需要先切换到iframe上去
# iframe的id是变化的，且没有name属性，那么就靠tagname+索引定位iframe元素，用iframe元素切换
iframe = driver.find_elements_by_tag_name('iframe')[1]  # 定位到第二个iframe上
driver.switch_to.frame(iframe)          # 切换到第二个iframe上
# 定位上传文件控件并发送文件路径
driver.find_element_by_name('file').send_keys(r"D:\test\xuexi\test\14.png")

# 2.17-----------获取元素属性和页面信息（获取验证信息--断言用）-----------
driver.title   # 获取当前页面的title
driver.current_url   # 获取当前页面的url
driver.name    # 获取浏览器名称

e = driver.find_element_by_id("")
e.text      # 获取元素的文本，即标签对之间的文本
e.get_attribute("value")   # 获取该元素的value属性的值，或者class，type属性等
            # 获取输入框的内容  。<input type="text" name="firstname" value="aaa">
            # 那么输入框默认的值为aaa；value 属性规定输入字段的初始值，
            # 或者输入框有值后，获取输入框的值，都是用元素.get_attribute(value)获取输入框内容，
            # js语法document.getElementById('').value='' 设置输入框内容
e.size      # 获取元素的尺寸   返回{'width': 500, 'height': 22}
e.is_displayed()         # 元素是否可见，是返回True，否返回False
e.tag_name   # 获取元素的标签

# 2.18----------爬页面源码-------
driver.page_source()   # 获取当前页的源码

# 2.19---------cookie相关操作-----------
driver.get_cookies()     # 获取当前页的所有的cookie，返回字典类型的列表？
driver.get_cookie("cookie的name")    # 获取指定cookie值
driver.add_cookie({})     # 添加一个cookie
driver.delete_all_cookies()     # 清除所有的cookie
driver.delete_cookie("cookie的name")   # 清除某个cookie

# 2.20-----------绕过验证码（add_cookie）-------------
# 绕过验证码，添加cookie，参数是cookie字典，注意抓包时登陆务必勾选【下次自动登录】？
# cookie字典不只包含cookie的值，还要包含domain,expire,path,httpOnly,secure值？这些值抓包看不到，
# 通过get_cookie(name)获取某个cookie的全部属性值
c1 = {u'domain': '.cnblogs.com','name': '.CNBlogsCookie',
      'value': u'xxxx','expiry': 1491887887,'path': u'/','httpOnly': True,'secure': False}
c2 = {u'domain': '.cnblogs.com','name': '.CNBlogsCookie',
      'value': u'xxxx','expiry': 1491887887,'path': u'/','httpOnly': True,'secure': False}
driver.add_cookie(c1) # 添加一个cookie
driver.add_cookie(c2) # 添加一个cookie

# 2.21------------js处理页面滚动条----------
'''
前言
    selenium并不是万能的，有时候页面上操作无法实现的，这时候就需要借助JS来完成了。
常见场景：
当页面上的元素超过一屏后，想操作屏幕下方的元素，是不能直接定位到，会报元素不可见的。
这时候需要借助滚动条来拖动屏幕，使被操作的元素显示在当前的屏幕上。
滚动条是无法直接用定位工具来定位的。selenium里面也没有直接的方法去控制滚动条，
这时候只能借助js了，还好selenium提供了一个操作js的方法:
driver.execute_script()，可以直接执行js的脚本
'''
js = "window.scrollTo(左边距，上边距)"
js = "window.scrollTo(0, 0)"  # 滑动到顶部
driver.execute_script(js)

# ---------------------元素聚焦-----------------
'''
元素聚焦
1.虽然用上面的方法可以解决拖动滚动条的位置问题，但是有时候无法确定我需要操作的元素
在什么位置，有可能每次打开的页面不一样，元素所在的位置也不一样，怎么办呢？
2.这个时候我们可以先让页面直接跳到元素出现的位置，然后就可以操作了。同样需要借助JS去实现。
'''
target = driver.find_element_by_xxxx()
driver.execute_script("arguments[0].scrollIntoView();", target)
# ----------------js定位元素的5种方法-----------------------
'''
除了id是定位到的是单个element元素对象，其它的都是elements返回的是list对象
1、通过id获取：返回单个元素
document.getElementsById(“id”)
2、通过name获取：返回列表,注意是加s
document.getElementsByName("name")
3、通过classname获取：返回列表，注意是加s
document.getElementsByClassName("class name")
4、通过tagname获取：返回列表，注意是加s
document.getElementsByTagName("tagname")
5、通过css选择器获取：返回列表，注意是加s
document.querySelectorAll("css选择器")
'''

# -2.33-----------定位的坑：class属性有空格------------------
# <div id="id" class="aa bb cc">
# class属性中间的空格并不是空字符串，那是间隔符号，表示的是一个元素有多个class的属性名称
# class属性是比较特殊的一个，除了这个有多个属性外，其它的像name,id是没多个属性的

# 方法1：用css定位时，空格用.代替
driver.find_element_by_css_selector("aa.bb.cc")
# 方法2：取class中的一个唯一的类属性做定位，判断类属性唯一：在谷歌f12，搜索类属性，看有几个
driver.find_element_by_class_name("aa")
driver.find_element_by_class_name("bb")
# 方法3：取类属性中的一个，不是唯一也可以，定位到一组，按索引获取元素
driver.find_elements_by_class_name("cc")[0]

# 2.23--------------js处理日历控件（去掉readonly属性）-----------------
# <input id="train_date" class="inp-txt" type="text" value="" 
# name="leftTicketDTO.train_date" autocomplete="off" maxlength="10" readonly="readonly">
# 基本思路：先用js去掉readonly属性，然后直接输入日期文本内容
js = "document.getElementById('id').removeAttribute('readonly')"  # js去掉readonly属性
driver.execute_script(js)

# 用webdriver输入日期
driver.find_element_by_id().clear()  # 清空输入框先务必
driver.find_element_by_id().send_keys("2019-06-19")  # 输入日期，此时会弹出日期控件，点击其他地方以关闭
# 用js输入日期，不会弹出控件框
js = "document.getElementById('').value='2019-06-19'"
driver.execute_script(js)

# 2.24 ---------js处理内嵌div滚动条------------
'''
<div id="yoyoketang" name="yoyo"
class="scroll">这是一个内嵌div</div>
'''
js = "document.getElementById('').scrollTop=10000"   # 纵向底部
js = "document.getElementById('').scrollTop=0"     # 纵向顶部
js = "document.getElementById('').scrollLeft=0"     # 横向左侧
js = "document.getElementById('').scrollLeft=10000"  # 横向右侧
driver.execute_script(js)

# 2.26------------js解决click失效问题-------------
# 有时候元素明明找到了，运行也没有报错，但是点击页面元素没反应，这种就是click事件失效了
# 方法1：点击目标元素的父元素标签，例如操作完下拉框后，点击保存没反应，div里包含保存按钮，可以先点击一次div元素
driver.find_element_by_id("父元素id")  # 先点击一次保存按钮的父元素div标签
driver.find_element_by_id("目标按钮id")  # 再点击按钮
# 方法2：用js直接执行click() 点击事件
js = "document.getElementById('').click()"
driver.execute_script(js)

# --------------设置元素等待----------
# 1、隐式等待
driver.implicitly_wait(10)  # 整个测试过程，共等待10秒，不针对某一元素，超过10秒后，还没定位到，抛出异常
# 2、显示等待
'''
在设置时间内，默认每隔一段时间检测一次当前页面元素是否存在，如果超过设置时间检测不到则抛出异常
WebDriverWait(driver, timeout, poll_frequency=0.5, ignored_exceptions=None)
driver ：浏览器驱动。
timeout ：最长超时时间，默认以秒为单位。
poll_frequency ：检测的间隔（步长）时间，默认为 0.5S。
ignored_exceptions ：超时后的异常信息，默认情况下抛 NoSuchElementException 异常。

WebDriverWait()一般由 until()或 until_not()方法配合使用，下面是 until()和 until_not()方法的说明。
 until(method, message=‘ ’)
调用该方法提供的驱动程序作为一个参数，直到返回值为 True。
 until_not(method, message=’’)
调用该方法提供的驱动程序作为一个参数，直到返回值为 False。

在本例中，通过 as 关键字将 expected_conditions 重命名为 EC，并调用 presence_of_element_located()方法
判断元素是否存在。
'''
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
element = WebDriverWait(driver,60,0.5).until(EC.presence_of_element_located(By.ID,"id"))
element.click()

import  unittest,os
from HTMLTestRunner import HTMLTestRunner

# 3.2-------unittest执行顺序-------------
# 一个文件里的执行顺序：0-9，A-Z，a-z，按照ASCII的顺序
# 多文件，多目录也是如此

# 3.3------unittest批量执行------------
case_dir = os.path.join(os.path.getcwd(), "case")  # 用例路径
report = os.path.join(os.path.getcwd(), "report")  #报告路径

discover = unittest.defaultTestLoader.discover(start_dir=case_dir,pattern="test*.py",top_level_dir=None)
# discover加载到的用例是一个list集合
# 用unittest里面的TextTestRunner或者HTMLTestRunner类的run方法去执行
runner = unittest.TextTestRunner()
runner.run(discover)

now = time.strftime("%Y-%m-%d %H %M %S")
report = "d:\\report"+now+".html"
f = open(report, "wb")
runner = HTMLTestRunner(stream=f,title="自动化测试报告",description="报告描述")
runner.run(discover)

# 3.4 unittest之装饰器（@classmethod）
# 即setUpClassl里的cls.driver，等于self.driver；cls应该是代表self，可能在装饰器里做了修改，
# 将cls变为了self？类方法的第一个参数是代表类对象本身，带self的属性是全类里都可以访问的
class Testaa(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome() # 注意这里是cls.driver
        cls.driver.get("https://www.baidu.com/")
        print("只在类前执行一次")

    def test_aa(self):
        self.driver.find_element_by_id("kw").send_keys("悠悠")  # 注意这里是self.driver

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("只在类后执行一次")
# 3.7--------unittest之断言----------
self.assertEqual
self.assertTrue



