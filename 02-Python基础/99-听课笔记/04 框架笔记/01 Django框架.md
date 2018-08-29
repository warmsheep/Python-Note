# Django框架基础知识
基于第三方工具实现的模板渲染
from jinjia2 import Template

1.http无状态，短连接
2.浏览器（socket客户端）
  网站（socket服务端）
3.自己写网站
  a.socket服务端
  b.根据URL不同返回不同的内容
    路由系统:
      URL -> 函数
  c.字符串返回给用户
    模板引擎渲染:
      HTML充当模板（特殊字符）
      自己创造任意数据
    字符串

4.Web框架
  框架种类:
    - a,b,c   --> Tornado
    - [第三方a],b,c  --> wsgiref Django
    - [第三方a],b,[第三方c] ---> flask

  分类:
    - Django（web)
    - 其他

2.Django框架
  pip3 install Django

  django-admin startproject mysite
  cd /Users/yuanjun/mysite
  python(3) manage.py runserver 127.0.0.1:8080(如果什么都不加就是8000端口)

  pycharm:
    。。。
Django程序目录:
  mysite
    settings.py Django配置文件
    url.py 路由系统：url->函数
    wsgi.py 用于定义Django用socket,wsgiref,
    manage.py 对当前Django程序所有操作可以基于python manage.py runserver

render找，settigns templates可以配置

静态文件：css 图片 js


1.创建project
2.配置:
    - 模板路径
      template目录
      TEMPLATES = [
          {
              'BACKEND': 'django.template.backends.django.DjangoTemplates',
              'DIRS': [os.path.join(BASE_DIR, 'templates')]
              ,
              'APP_DIRS': True,
              'OPTIONS': {
                  'context_processors': [
                      'django.template.context_processors.debug',
                      'django.template.context_processors.request',
                      'django.contrib.auth.context_processors.auth',
                      'django.contrib.messages.context_processors.messages',
                  ],
              },
          },
      ]
    - 静态文件路径
      static目录
      STATICFILES_DIRS = (
          os.path.join(BASE_DIR,"sta"),#必须加逗号
      )
3.额外配置
  - 注释掉Csrf
    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        #'django.middleware.csrf.CsrfViewMiddleware',
        注释掉这行代码
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ]

4.url对应关系
  /login/  login
  def login(request):
    request.method
    request.POST -》 请求体
    request.GET -》 请求头的URL中

    GET请求 --》 只有request.GET
    POST请求 --》request.GET和request.POST都有值

    return HttpResponse(...)
    return render(request,"login.html",{...})
    return redirect("要跳转的网址")

5.模板引擎的特殊标记
  login.html
  {{name}}
  return render(request,"login.html",{"name","alex"})

思考题:删除的时候

作业:
    Django+pymysql实现
    - 用户登陆
    - 查看用户列表


学员管理:
    表:
      班级
      学生
      老师

班级表
id    title
1     全栈4期
2     全栈5期


学生表
id    name    班级ID(FK)
1     张三     1

老师表
id    name
1     海峰   
2     egon
3     元昊

老师班级关系表
id    老师ID   班级ID
1       1       1
2       1       2

create table




    单表操作:
      - 增
      - 删
      - 改
      - 查
    一对多操作:
      - 增
      - 删
      - 改
      - 查
    多对多操作:
      - 增
      - 删
      - 改
      - 查

Django基础

内容回顾:
1.web框架本质
  - http协议
    - 头
    - 体
  - 模板引擎的渲染是在服务端进行
  - 字符串
2.Django
  - 安装
  - Django-admin startproject mysite
  - 配置
    - 模板路径
    - 静态文件
    - Csrf注释
  - urls.py
    url -> 函数
  - 函数:
    - 至少有1个参数def index(request):
      - request.POST
      - request.GET
      - return HttpResponse(..)
      - return render(request,"模板路径",..)
      - return redirect("URL")
  - 模板渲染
    def index(request):
        return render(request,"模板路径",
          {
            "k1","v1",
            "k2":[1,2,3],
            })
    index.HTML
        <h1>{{k1}}</h1>
        {% for item in k2 %}
          <h2>{{item}}</h2>
        {% endfor %}

下午作业:
1.班级
  Ajax删除
2.班级
  Ajax编辑

本周作业:
一对多
多对多


内容回顾:
1.创建Django程序
2.新URL方式:
  - 添加
  - 删除
  - 编辑
今日内容:
0.班级管理
  - 添加
  - 删除
  - 编辑
  PS: views中对用户提交的数据进行判断(Form组件)

1.学生管理
  - 添加
  - 删除
  - 编辑

2.模态对话框
  班级管理
    - 添加
      Form表单提交，页面会刷新



3.Ajax
jQuery

$ajax({
  URL:'要提交的地址',
  type:'POST'//GET提交方式
  data:{"k1":"v1"}//提交的数据
  success:function(data){
    //当服务端处理完毕后，自动执行的回调函数
    //data:返回的数据
  }
  })

其他:
  1.模板语言if条件语句
  2.form表单提交页面会刷新
  3.ajax提交页面不刷新
  4.js实现页面跳转
    location.href = "要跳转的地址"
本周作业:多对多
  5.模态对话框
    - 少量的输入框
    - 数据少

    新URL方式
    - 数据大
    - 操作多
下午作业:
1.班级:
  删除用ajax
2.班级编辑
  ajax编辑


S4day67
内容回顾:
1.Web框架本质
  客户端(socket):
    2.发送IP和端口
      GET:
        请求头:
          http1.1 /index?p=123/
        请求体(无内容)
      POST:
        请求头http1.1 /index?p=123/
        请求体(有值)


  服务器(socket):
  1.启动并监听IP和端口，等待用户连接
  3.接收请求进行处理，并返回
    普通返回:
      响应头:
      ...
      响应体:
    重定向返回:
      响应头:
        location:
        ...
  4.接收响应:
    普通响应:页面直接显示
    重定向相应:再发起一次http请求

2.DjangoWeb框架
  a.创建Project
    django-admin startproject mysite
  b.配置
    i.TEMPLATES
    ii.静态文件，加逗号
    iii.csrf
  c.路由关系
    url --> 函数
  d.视图函数
    def index(request):
        request.method
        request.POST.get()
        request.GET.get()

        li = request.POST.getlist("多选下拉框")

        return HttpResponse("字符串")
        return redirect("URL")
        return render(request,"模板路径",字典)
        render本质
        1.获取模板+数据，渲染
        2.HttpResponse(...)
    e.模板渲染
        {{k1}}
        {{k1.0}}

        {% for i in result%}
        {% endfor%}

        {%if 1>2%}
        {%else%}
        {%endif%}
3.ajax
$.ajax({
  url:,
  type:,
  data:,
  success:fuction(arg){

  }

  })

其他:
1.模板语言if条件语句
2.form表单提交，页面会刷新
3.ajax提交页面不刷新
4.js实现页面跳转:
  location.href = '要跳转的地址'
5.对话框:一般与ajax绑定
  新URL:
    - 对于大量的数据以及操作适用
今日内容:
  1.对话框
    单表
      添加
      编辑
      删除
      PS：
        a.阻止默认事件的发生：两个都需要return
        b.location.reload()
        c.HttpResponse(json.dumps())
        d.JSON.parse()
    一对多
      PS:
      a.jQuery时间阻止默认事件发生
      $(function () {
        $("#addModel").click(function () {
            alert(123);
            return false
        })
    })


  2.多对多
  - 新URL方式
    - 添加
    - 编辑
  - 对话框
    - 增加
    - 编辑
    - 添加（左右移动）

  3.Bootstrap 基本样式
  4.fontawesome 图标

day68
今日内容:
1.学员管理多对多
2.插件
3.用户登陆

今日任务:
作业:
后台管理页面
  - 用户登录
  - 学员管理
    - 单表
    - 一对多
    - 多对多
1.HTTP请求的生命周期:
发送get请求，请求头，没有请求体
后台拿到请求头，将请求头中的url拿到，先去路由东西里匹配
如果有匹配则执行相应函数，函数中数据到相应模板，模板渲染出字符串，返回给用户，返回也有响应头，响应体
请求头 -》提取URL-》路由关系匹配——》函数（模板+数据渲染）-》返回用户（响应头+响应体）

2.def index(request):
      request.GET.get()
      requets.POST.get()
      request.method()
      request.getlist()
return render() render本身其实也是httpresponse,不过内部多了渲染功能
  redirect()
  return HttpResponse()
  模板的渲染是在后台执行

3.for
  if
  索引.
  {{}}

4.js序列号
  dataType:JSON,
  JSON.parsw()
  阻止默认事件
  js:<a onclick='return func();'></a>
  jquery:<a onclick='func();'></a> 直接在函数中return false即可

  $.ajax({
    url:"",
    type:"",
    dataType:,
    data:{},
    success:function(arg){

    },
    })

今日内容:
1.学员管理多对多
  - 新URL方式
    - 增加
    - 编辑
  - 对话框
    - 增加
    - 编辑:[11,22,33].indexOf(222)
    - 遗留
      - select 左右移动
2.插件
  - bootstrap(一)
    - 看图拷贝
    - 常用标签
    - 响应式
    - js
  - font awesome
3.用户登录

上节回顾:
  1.SQLhelper
  2.Traditonal:true ajax发送列表的数据，但是不支持字典，只支持列表，可以将字典序列化再发送
  data:{'k1':[1,2,3,4],'k2':JSON.stringify({k1:v1,k2:v2})}
今日内容概要:
1.bootstrap
2.后台管理布局
3.Cookie
4.Django
  - 母版
  - 路由

目标:完善学院管理

1.bootstrap
一个包含css js的代码库
- 样式
- 响应式(@media关键字)
  - 导航条
  - 栅格
@media(max-width: 700px){
   .pg-header{
    background-color:royalblue;
    height:48px;
    }
}


2.完善学院管理系统
- 后台管理布局
- Django母版
母版:存放所有页面公用
子版:继承母版
  - 自定义当前页面私有
3.cookie
a.保存在浏览器端的"键值对"
b.服务端可以向用户浏览器端写cookie
c.客户端每次发请求时，会携带cookie去
d.一般用来用户登录
set_cookie
  key
  value
  max_age=None
  expires = None
  path = '/'
  domain = None
  secure = False #HTTPS
  httponly=False#只能从HTTP请求中传入，js代码无法获取到，但是并不是绝对的
自定制签名
装饰器

内容整理:
1.Bootstrap响应式布局: @media()
2.栅格
3.表格
4.导航条
5.路径导航
6.font-awesome
7.布局:占满品目position:absolute;溢出overflow:scroll/auto;
8..xx:hover .g{}当鼠标移动到xx样式的标签上时，其子标签.g应用下面的属性
9.Django母版
  母版:
    <html>
      <% block s1%><% endblock %>
    </html>
  子版:
    {% extends 'layout.html'%}
    {% block s1%}<><>{% endblock%}
10.用户登陆
- cookie: 保存在浏览器端“键值对”，设置超时时间
  - 发送HTTP请求，在请求头中携带当前所有可访问的cookie
  - 响应头
- 写cookie
@xzzz
def index(request):
    obj = HttpResponse('ok')
    obj.set_cookie(....)
    request.COOKIES.get(...)
    obj.set_signed_cookie(...)
    request.get_signed_cookie(...)
- 自定义cookie签名
- 装饰器装饰views的函数

今日作业:
  1.布局+代码
  2.登陆+cookie+装饰器
  3.布局页面HTML+CSS

坦白:
  project
    - app01 自己创建的目录
      - views.py
    - SQLhelper 封装SQL操作

  Django
    - 路由
    - 视图
    - 模板
    - 自带ORM(类-表；对象-行：pymysql连接数据库)

  Tornado
    - 路由
    - 视图
    - 模板
    - 自由：pymysql;sqlAchemy

  Flask:
    - 路由
    - 视图
    - 模板(第三方的组件)
    - 自由：pymysql;sqlAchemy

1.创建app
2.数据库操作

今日内容:

  django-admin startproject mysite;
  cd mysite
  python manage.py startapp app01;

  project
    - app01
      - admin: django自带
      - modal:写类，根据类创建数据库表
      - test:单元测试
      - views:业务处理，但是不一定只有一个，可以建立一个views的文件夹

    - app02
    - app03
  1.路由系统
    url -> 函数
    a.一一对应 /login/ -> def login 静态路由
    b./add-user/(\d+)/ -> def add_user(request,a1) 动态路由
    c./add-user/(?P<a1>\d+)/ -> def add_user(request,a1)
    d.路由分发
     urls.py
      url(r"^app01/",include('app01.urls')),
     app01.urls.py
      url(r"^index.html$",vies.index),
    e./add-user/(\d+)/ -> def add_user(request,a1) name=n1
      根据名称反向生成URL
      1.在python代码中
        from django.urls import reverse
        v = reverse('n1',kwargs={"a1":1111})#arg想要生成几就是几
        print(v)
      2.url(r'^login/',views.login,name='m1'),
        {% url "m1"%}
徐峥：
 n1
 n2
 n3

def index(request):
    url_list = [
      "n1",
      "n2",
      "n3"
    ]
    temp = []
    for i in url_list:
        url = reverse(i)
        temp.append(url)
    return render(...,temp)



    伪静态:

  2.视图函数 CBV,FBV


  3.ORM操作
    Http请求:
      url -> 视图(模板+数据)

  1.创建数据库
  2.settings配置数据库连接
  DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME':'tb2',
    'USER': 'root',
    'PASSWORD': '',
    'HOST': 'localhost',
    'PORT': '3306',
    }
  }
  3.__init__.py
  import pymysql
  pymysql.install_as_MySQLdb()

4.
from django.db import models
class UserInfo(models.Model):
    # nid = models.AutoField()#自增类型
    nid = models.BigAutoField(primary_key=True)如果不写，也会自动生成，且自增且为主键，名称为id
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

5.注册APP：settigns.py中INSTALLED_APPS增加一列
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app01',
]

6.创建数据库表
执行命令:
  python manage.py makemigrations
  python manage.py migrate

    ORM操作表
      创建表
      修改表
      删除表
    操作数据行
      增删改查
    ORM利用pymysql第三方工具连接数据库
    默认:
     SQL
    默认: mysql -> mysqldb(修改Django默认连接MySQL方式)


作业:
学院管理(SQL换成ORM)
新URL方式
  1.班级增删改查

今日内容:
1.CBV&FBV
2.Django ORM
  - 正向操作 反向操作
  - 对象，元组，字典，跨表
3.分页
  - Django自带
  def index(request):
    from django.core.paginator import Page,Paginator,PageNotAnInteger,EmptyPage
    current_page = request.GET.get('page')
    user_list = models.UserInfo.objects.all()
    paginator = Paginator(user_list,10)
    try:
        posts = paginator.page(current_page)
    except PageNotAnInteger as e:
        posts = paginator.page(1)
    except EmptyPage as e:
        posts = paginator.page(1)
    return render(request,'index.html',{"posts":posts})

    <div>
    {% if posts.has_previous %}
        <a href="/index.html?page={{ posts.previous_page_number }}">下一页</a>
    {% endif %}
    {% if posts.has_next %}
        <a href="/index.html?page={{ posts.next_page_number }}">下一页</a>
    {% endif %}
    {% for num in posts.paginator.page_range %}
        <a href="/index.html?page={{num }}">{{ num }}</a>
    {% endfor %}
    </div>

    缺点: 只适合做下一页上一页，只适用于Django框架

  - 自定义分页

  分批获取数据
  models.UserInfo.objects.all()[0:10]

上节记录
1.路由系统
  - 静态
  - 动态
    - 别名: url reverse("n1")
    - 无别名: 位置参数
  - 别名
    - 根据别名反生成URL
  - 路由分发(include)
  PS:起始符+终止符 ^$
      伪静态 .html

2.ORM操作
  - settings.DATABASES
  - __init__.py  pymysql.install_as_MySQLdb()
  - 类
    class Foo(models.Model):
        nid = models.AutoField(primary_key=True)
        name = models.CharField(max_length=12)
    class Bar(models.Model):
        title = ...
        f = FK... #数据库中显示为f_id
    models.Foo.objects.create()
    result = Foo.objects.all()
    QuerySet[Foo(),]  
    result = Foo.objects.filter(id=1).first() obj类型
    Foo.objects.filter().update()


3.模板语言
  - 索引
  - 母版
    - {block xx}一般有三个
    - {extends "layout.html"}

4.Cookie
  - 保存在用户浏览器端的键值对
  -

上节回顾:
  1.模板
    layout.AuthenticationMiddleware
    {% block x%}{% endblock%}
    index.html
    {% extends 'layout.html'%}#必须在子版最顶部
    {}

  2.cookie
  浏览器上保存的键值对

  def index(request):
      request.COOKIES
      request.get_signed_cookie('k',salt="ff")

      obj = HttpResponse()
      obj = render()
      obj = redirect()
      obj.set_cookie(k1,v1,max_age)
      obj.set_signed_cookie(k1,v1,max_age)

 4.Bootstrap响应式布局
  - css
  - js(欠)

5.后台布局
  1.position:absolute;
   overflow:hidden;
  2..pg-header:hover .div{}


# ORM操作补充:

正向操作
反向操作
对象
字典
列表

  # 获取多个数据时,这种方式不能跨表
  # 1.[obj,obj,obj]
  # models.UserInfo.objects.all()
  # models.UserInfo.objects.filter(id__gt=1)
  # results = models.UserInfo.objects.all()
  # for item in results:
  #     print(item.name,item.ut.title)

  # 2.[{"id":xx,"name":xx}]
  # models.UserInfo.objects.all().values('id','name')
  # models.UserInfo.objects.all().filter(id__gt=1)
  # result = models.UserInfo.objects.all().values('id', 'name')
  # for item in result:
  #     print(result['id'],result['name'])


  # 3.[("id":xx,"name":xx)]
  # models.UserInfo.objects.all().values_list('id','name')
  # models.UserInfo.objects.all().filter(id__gt=1)

  # result = models.UserInfo.objects.all().values_list('id', 'name')
  # for item in result:
  #     print(item[0],item[1])


results = models.UserInfo.objects.all().values('id','name','ut__title')
for item in results:
    print(item['name'],item['id'],item['ut__title'])
只能连表的时候跨表,不能在查询的时候跨表

3.分页




作业:
  1.学员管理原生sql替换掉
