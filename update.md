# 更新日志

## 更新计划  

[https://mubu.com/doc2I2skpgW9o](https://mubu.com/doc2I2skpgW9o)

## 1.8.2.1
+ 新增: 点击样式按钮后, 可以使用 Alt+ Shift+ Z 快速设置正文样式, Alt+ Shift+ S 设置带缩进的正文样式
+ 更改: 引导助手升级到1.2版本
+ 更改: 安装程序引导文字改为中文

## 1.8.2.0
+ 新增: 支持wps个人版
+ 新增: 支持以记事本方式修改默认配置文件, 避免因word更新被重置. 但是存在风险,尤其是系统字号和word字号需要换算. 开启方法很隐蔽--"双击赞赏码".
+ 更改: 引导助手只有安装时才出现, 不再重复出现.
+ 更改: 清理和完善了代码,
+ 移除: 去掉了安装包附带的公文模板,不再集成提供.

## 1.8.1.3
+ 修复: 1810重写代码页脚边距未设置的bug 
+ 修复: 1810重写代码导致取消勾线精准排版控制后, 无法再次开启的bug

## 1.8.1.1
+ 修复:  重新的添加外侧页码的代码不兼容wps的bug

## 1.8.1.0
+ 新增: 删除选定范围内的空行
+ 新增: 公文部件插入装订线
+ 更改: 页面设置独立行间距选项
+ 修复: 文档中包含word97/2003旧版分节符时, 添加页码出错.重新了添加外侧页码的实现方法.
+ 修复: 文档中包含word97/2003旧版分节符时,设置页面出错

## 1.8.0.3
+ 修复: wps下删除所有空白报错的bug
+ 修复: 页面2010及以下版本无法第二次弹出对话框的bug.

## 1.8.0.1
+ 修复: 1-4级标题的图标在黑色模式下显示不清的问题
+ 新增: 公文模板(新建->个人)

## 1.8.0.0
+ 更改: 页面设置窗体不再置顶显示. 
+ 更改: 语音朗读窗体可移动.
+ 修复: 中文字体更改偶现无效的bug 
+ 修复: 插入的函用文武线不水平 

## 1.7.9.0
+ 新增: 页码新增"光标处"插入,折中解决横页页码问题. 
+ 新增: "朗读"新增高级功能,可以控制语速和选择发音人. 
+ 修复: 删除所有空行会误删非嵌入式图片的bug.

## 1.7.8.0
+ 新增: 字体更改新增字体替换功能.
+ 新增: 字体更改对话框支持帮助按钮提示
+ 修复: 修复"打开文档第一步操作是替换操作会崩溃"的bug

## 1.7.7.0
+ 新增: 西文字体更改支持保存设置.
+ 更改: 由于wps兼容性问题,wps下隐藏文档加密菜单项.
+ 更改: 调整了函线的宽度为170mm,居中
+ 更改: 初次安装为图文引导提示, 避免了之前版本在资源管理器预览文档时弹出提示的情况
+ 更改: 公文操作完美的实现一键撤销/重做. Word支持中文提示. 
+ 更改: 安装包更改了外观,修复和卸载功能更好的兼容不同分辨率
+ 修复: 先插入横页再调整页面设置,会改成纵向a4并报错.v177 感谢@1206858659 提供的思路
+ 修复: 打开字体对话框出错时会导致崩溃的bug v177

## 1.7.6.1
+ 新增: 页面设置窗口: 行数页数增设开关.新增提示图标,可点击
+ 新增: 插入公文部件: 版头、横线 
+ 新增: 插入页码: 新增右侧页码
+ 更改: 检查更新: 发现新版下载可用时, 再次点击会自动打开浏览器下载
+ 更改: 插入版记线自动位于页面最底部   感谢@1206858659
+ 更改: 朗读: 未选择内容时,自动选择光标至段尾的文字
+ 更改: 重写1-4级标题编号,wps和word存在差异,重写, 让文档保持一致
+ 更改: 重写公文样式的1-4级编号
+ 修复: 中英文之间插入空格丢字
+ 修复: 用户删除默认编号库可能导致的标题序列错误
+ 修复: 插入版记移除了wps2016不支持(Tables.AllowPageBreaks )的命令

## 1.7.4.1
+ 新增: 公文样式新增带缩进的正文样式
+ 新增: 页码自定义也支持粗体和斜体
+ 更改: 公文样式基础样式从正文改为无格式.
+ 更改: 外侧页码前后缩进1字符 感谢@琥珀的囚徒 提供的思路
+ 修复: 公文样式二级标题为全角括号
+ 修复: 公文样式不支持粗/斜体的bug
+ 修复: 转换带圈数字序列时大于20报错.
+ 修复: 所有的自定义字体都未能正确支持粗体斜体的bug
+ 修复: 高DPI下关于对话框按钮显示不全的bug
+ 修复: 设置正文时未取消大纲级别的bug

## 1.7.3
+ 新增: 字体更改菜单新增西文字体更改功能.

## 1.7.2.2
+ 修复: 文档以保护视图打开时,按钮未禁用的bug

## 1.7.2.1 
+ 修复: WPS下关于角标无法调出隐藏功能
+ 修复: WPS下副本菜单大图标显示不正确的bug

## 1.7.2 测试版
+ 新增: 强制重建公文样式功能,用于改乱后恢复样式表.--点击前请先清除格式,再重建
+ 新增: 高级功能对话框支持帮助按钮
+ 新增: 插入符号新增数字转换为带圈数字序号.支持1-20.
+ 更改: 二级标题()改为全角（）
+ 更改: 副本下拉菜单改为大图标显示
+ 修复: 高级功能对话框闪烁问题
+ 修复: 公文样式表创建速度慢的问题
+ 修复: 标题按钮没有1-4级大纲的问题
+ 修复: Word2007-2010按钮文字显示错位的问题

## 1.7.1 测试版
+ 新增: 页码字体格式支持自定义.
+ 新增: 公文样式支持1-4级大纲

## 1.7.0 测试版
+ 新增: 万众期待的公文格式自定义终于来了 ,支持字体大小/是否粗体,斜体.
+ 更改: 关于对话框->高级功能, 对公文格式进行自定义设置.
+ 更改: 在线帮助更改到幕布. 支持脑图显示.

## 1.6 测试版
+ 新增: 生成jpg图片副本
+ 新增: 当前页面存为图片支持原尺寸jpg+ 原尺寸png

## 1.5 测试版
+ 新增: 标题/正文支持自定义字体功能(目前请自行修改 公文排版.dll.config, 后期会有写入功能)
+ 新增: 标题和样式支持大纲级别
+ 新增: 点击页面设置标题栏问号?按钮可以显示在线帮助
+ 新增: 页面设置支持行间距(固定值)设置
+ 修复: 页面设置按钮可打开多个窗口的bug
+ 更改: 使用了全新安装程序,减少安装问题.

## 1.0.8.3
+ 更改: WPS用户的福音,标题设置完整支持wps,不再混乱.
+ 新增: 关于对话框支持”检测新版本”.考虑到有内网用户,所以没有自动下载更新功能.

## 1.0.8.1
+ 新增: 页面设置”重置”按钮右键点击可以删除配置文件.[隐藏功能]
+ 新增: 点击公文标签”每个区块的右下角”有惊喜(wps部分支持).
+ 更改: 关于插件对话框可以复制系统信息,以便更好的反馈问题.
+ 更改: 建议反馈以网站发帖形式获取帮助,不再发送邮件.
+ 更改: 页面设置中”行间距(磅)”改为”每行字数”.
+ 更改: 默认设置精确实现了公文标准”每页27行,每行28字”.
+ 更改: 新的安装程序,减少安装问题.

## 1.0.8.0
+ 新增: WPS用户的福音,终于可以显示图标了.不过由于WPS2019解析的问题,图标没有最新版Office365版本好看.
+ 新增: ”当前页面存为图片”功能支持tiff格式原尺寸高精度,在保存对话框选择图片类型即可 .
+ 修复: 页面设置保存时行数和行间距互换的bug
+ 修复: 横页文档保存图片时变形挤压成竖向.
+ 修复: 连续多次使用”当前页面存为图片”功能导致内存溢出.
+ 修复: ”删除空行”会错误删除smarART内容的bug.

## 1.0.7.4
+ 更改: 字体列表载入实现方法
+ 更改: 增强代码健壮性,减少了极端情况下可能出现的报错提示.
+ 更改: 使用了全新证书和强签名,增强了软件安全性和完整性以及执行效率.减少新用户安装难度.

## 1.0.7.1
+ 更改: 字体更换功能由仅支持中文字符改为支持中文和西文字符.

## 1.0.7.0
+ 新增: 离线安装版(尺寸较大,102Mb,适合内网用户)
+ 新增: 页面设置可以保存了.
+ 更改: 建议反馈时,邮件自动附加系统信息.

## 1.0.6.0
+ 更改: 字体载入提示,支持Word2019和wps2019(wps部分兼容).
+ 新增: 下载链接里提供了单exe安装程序,可以避免zip包遇到的一些安装问题.

## 1.0.5.9
+ 更改：语音加载模块失败后不再提示，朗读按钮自动禁用。

## 1.0.5.8
+ 更改: 优化了精简版系统导致的语音模块无法加载的出错提示.

## 1.0.5.7
+ 新增: 增加在线帮助
+ 修复: 删除空格(选定范围): 只能删除1个空格的bug.
+ 修复: 保存为图片时,小内存电脑可能提示”GDI+  中发生一般性错误。”

## 1.0.5.6
+ 新增：文字替换功能。
+ 修复:  公文样式中方正小标宋字体名称的错误.

## 1.0.5.5
+ 新增: 插入符号功能菜单新增[]和【】转换为六角括号.

## 1.0.5.4
+ 新增: 副本功能新增将当前页面单独保存成 PNG 图片.

## 1.0.5.3
+ 新增: 公文样式功能,可以对当前文档生成公文专用的样式,可以方便的在样式面板选择并设置格式.
+ 更改: 更改了4级标题的实现方法,兼容性更好.
+ 更改: 更改了关于插件的图标和大小.

## 1.0.5.2
+ 新增: 副本功能增加文字转成图片,可以按页面方式生成PNG格式图片.
+ 更改: 对NetFrame runtime的需求从4.6降低到4.0, win8.1和win10安装时将无需下载更新NetFrame.
+ 修复: 执行”删除所选内容空格”后屏幕不更新的bug.

## 1.0.5.1
+ 更改: 关于对话框支持显示office类型和windows系统版本.
+ 修复: 4级标题(1)无法指定序列的bug.

## 1.0.5.0
+ 新增: 在存档目录生成同名副本,支持pdf和doc(word97-2003格式)
+ 新增: 快速调用文档加密和限制编辑,在已知密码的前提下,可以快速清除文档打开和修改密码.
+ 新增: 朗读选定内容功能.单击朗读,再次单击停止.
+ 新增: 插入公章图片.支持连接方式和嵌入方式.默认为连接方式.
+ 新增: 更多可插入符号
+ 新增: 给选定文字设置着重号
+ 新增: 给选定文字设置隐藏格式(适合打印试卷)
+ 新增: 删除选定范围内的空格
+ 新增: 标点符号的中英互换
+ 新增: 中英文之间加空格
+ 更改: 设置标题文字由按钮模式改为下拉菜单的半自动模式.  第一次自动编号,再次可以指定编号序列,
+ 更改: 为了更好的兼容性,页面设置侧栏改为页面设置对话框.
+ 更改: 优化了大量按钮的屏幕提示.
+ 修复: 仅一页时插入外侧页码出错 修复: 保护视图下,文档不可编辑时,按钮可用导致出错. 修复: 其它可能出现的bug

## 1.0.0.6
+ 新增: 插入红色分割线(反线)的功能.
+ 修复: 安装时访问网站的bug;
+ 修复: 页面设置面板开关显示的bug
+ 移除: 删除行首空格功能

## 1.0.0.4
首次发布