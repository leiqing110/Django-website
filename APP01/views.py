from django.shortcuts import HttpResponse,render,redirect#返回完整的html文件
from APP01 import models
from django.db.models import F, Q

def yimi(request):
    #request参数保存了所有和用户浏览器请求相关的数据
    #with open("templates/yimi.html","r",encoding="utf-8")as f:
    #    data = f.read()
   # return HttpResponse(data)
    return render(request,"yimi.html")
def xiaohei(request):
    #request参数保存了所有和用户浏览器请求相关的数据
    return HttpResponse('hello xiaohei,小黑真黑呀')
#保存了路径和函数的对应关系

def login(request):
    #如果你是get请求
    error_msg = ""
    # if request.method == "GET": #这里GET必须是大写
    #     return render(request, "login.html")
    #如果你是Post请求，我就取出提交的数据，做登陆判断
    email= request.POST.get("user_email",None)
    pwd = request.POST.get("user_pwd",None)
    print(email,pwd)
    #做是否登陆成功的判断
    if email == "admin@163.com" and pwd == "123":
        #登陆成功
        #回复一个特殊的响应，请求指定的url
        return redirect("/user_list/")
    else:
        #return return render(request, "login.html")
        error_msg = "邮箱或密码错误"
    #return HttpResponse('ojbk')
    return render(request,"login.html",{"error":error_msg} )


def baobao(request):
    #获取用户提交的数据
    print(request.POST)
    email= request.POST.get("email",None)
    pwd = request.POST.get("pwd",None)
    print(email,pwd)
    #做是否登陆成功的判断
    if email == "alex@oldboyedu.com" and pwd == "123":
        #登陆成功
        return HttpResponse("登陆成功！")
    else:
        return HttpResponse("登陆失败！")
    #return HttpResponse('ojbk')

def user_list(request):
    #去数据库中查询所有的用户
    #利用ORM这个工具去查询数据库，不用自己去查询
    ret = models.UserInfo.objects.all().order_by("id")
   # print(ret[0])#取出第一个对象
   # print(ret[0].id,ret[0].name)
   # print(ret)

    return render(request, "user_list.html", {"user_list":ret})
    #return HttpResponse("执行完毕")

def add_user(request):
    #第一次请求页面的时候就返回一个页面，让用户填写
    err_msg = ""
    if request.method == "POST":

        #用户填写了新的用户名，并发送了POST请求
        new_name = request.POST.get("username",None)
        new_pwd = request.POST.get("userpwd",None)
        if  new_name:
        #通过ORM去数据库中新创建一条记录
            models.UserInfo.objects.create(name=new_name,pwd=new_pwd)
        #添加完成后跳转到用户列表
            return redirect("/user_list/")
        else:
            err_msg = "出版社名字不能为空!"

    return render(request,"add_user.html",{"error":err_msg})

#删除用户
def delete_user(request):
    #删除指定的id
    del_id = request.GET.get("id",None)
    #如果能取到ID值
    if del_id:
        #去数据库删除当前的id值的数据
        #根据id值查找到的数据
        #del_obj = models.UserInfo.objects.get(id=del_id).delete()
        del_obj = models.UserInfo.objects.get(id=del_id)
        #删除
        del_obj.delete()
        # 返回删除后的页面，跳转到出版社的列表页，查看是否删除成功
        return redirect("/user_list/")
    else:
        return HttpResponse("要删除的数据不存在")
    pass

#编辑用户信息
def edit_user(request):
    #用户修改完用户的名字，点击提交按钮，给我发来新的名字
    if request.method == "POST":
        #取新出版社的名字
        #print(request.POST)
        edit_id = request.POST.get("user_id") #这里获取的是表单的内容，必须匹配name
        #根据ID获取要修改的对象\
        #print(edit_id)

        edit_user = models.UserInfo.objects.get(id=edit_id)

        new_name = request.POST.get("user_name")
        new_pwd = request.POST.get("user_pwd")
        edit_user.name = new_name
        edit_user.pwd = new_pwd
        edit_user.save()#把修改提交到数据库
        #挑转到用户列表页，查看是否修改成功
        return redirect("/user_list/")

    edit_id = request.GET.get("id",None)#从请求URl中获取ID参数
    #如果这个ID存在
    if edit_id:
        user_obj = models.UserInfo.objects.get(id=edit_id)
        #将信息传到页面上
        return render(request,"edit_user.html",{"user":user_obj})
    else:
        return HttpResponse("编辑的用户不存在")

def movie_list(request):
    all_movie = models.Movies.objects.all()
    # 在html页面完成字符串的替换
    return render(request, "movie_list.html", {"all_movie": all_movie})

def delete_movie(request):
    #删除指定的id
    del_id = request.GET.get("id",None)
    #如果能取到ID值
    if del_id:
        #去数据库删除当前的id值的数据
        #根据id值查找到的数据
        #del_obj = models.UserInfo.objects.get(id=del_id).delete()
        del_obj = models.Movies.objects.get(id=del_id)
        #删除
        del_obj.delete()
        # 返回删除后的页面，跳转到出版社的列表页，查看是否删除成功
        return redirect("/movie_list/")
    else:
        return HttpResponse("要删除的数据不存在")
    pass

def add_movie(request):
    if request.method == "POST":
        # {"book_title":"跟金老板学开车，"publisher_id"：9}
        new_name = request.POST.get("moviename")
        new_intro = request.POST.get("movieintro")
        new_time = request.POST.get("movietime")
        new_yingting = request.POST.get("yingting")
        # #创建新书对象

        models.Movies.objects.create(mname=new_name, intro=new_intro,time=new_time,yingting=new_yingting)
        # #返回到书籍列表页
        return redirect("/movie_list/")
    ret = models.Movies.objects.all()
    return render(request, "add_movie.html", {"movie_list": ret})

def search(request):
    if request.method == "POST":

        edit = request.POST.get("search")  # 这里获取的是表单的内容，必须匹配name
        # 根据ID获取要修改的对象\
        # print(edit_id)
        #print(edit_name)
        edit_movie = models.Movies.objects.filter(Q(mname__icontains=edit))

        return render(request, "movie_list.html", {"all_movie": edit_movie})

def search_huiyuan(request): #会员信息查找函数
    if request.method == "POST":

        edit = request.POST.get("search_huiyuan")  # 这里获取的是表单的内容，必须匹配name

        # print(edit_id)
        #print(edit_name)
        edit_huiyuan = models.Huiyuan.objects.filter(Q(name__icontains=edit)|Q(id=edit))#根据条件筛选

        return render(request, "huiyuan_list.html", {"all_huiyuan": edit_huiyuan})

def search_good(request):#卖品查找
    if request.method == "POST":

        edit = request.POST.get("search_good")  # 这里获取的是表单的内容，必须匹配name
        # 根据ID获取要修改的对象\
        # print(edit_id)
        #print(edit_name)
        edit_good = models.Goods.objects.filter(Q(name__icontains=edit)|Q(type_id__name__icontains=edit)|Q(price=edit)|Q(id=edit))#根据条件筛选

        return render(request, "goods_list.html", {"all_goods": edit_good})
def edit_movie(request):
    #用户修改完用户的名字，点击提交按钮，给我发来新的名字
    if request.method == "POST":
        #取新出版社的名字
        #print(request.POST)
        edit_id = request.POST.get("id") #这里获取的是表单的内容，必须匹配name
        #根据ID获取要修改的对象\
        #print(edit_id)

        edit_movie = models.Movies.objects.get(id=edit_id)

        new_name = request.POST.get("moviename")
        new_intro= request.POST.get("movieintro")
        new_time = request.POST.get("movietime")
        new_yingting = request.POST.get("yingting")
        edit_movie.mname = new_name
        edit_movie.intro = new_intro
        edit_movie.time = new_time
        edit_movie.yingting = new_yingting
        edit_movie.save()#把修改提交到数据库
        #挑转到用户列表页，查看是否修改成功
        return redirect("/movie_list/")

    edit_id = request.GET.get("id",None)#从请求URl中获取ID参数
    #如果这个ID存在
    if edit_id:
        movie_obj = models.Movies.objects.get(id=edit_id)
        #将信息传到页面上
        return render(request,"edit_movie.html",{"movie":movie_obj})
    else:
        return HttpResponse("编辑的用户不存在")

def goods_list(request):
    all_goods= models.Goods.objects.all()
    # 在html页面完成字符串的替换
    return render(request, "goods_list.html", {"all_goods": all_goods})

def add_goods(request):
    if request.method == "POST":
        new_good_name = request.POST.get("good_name")
        new_good_intro = request.POST.get("good_intro")
        new_good_price = request.POST.get("good_price")
        new_good_type_id = request.POST.get("good_type")
        models.Goods.objects.create(name=new_good_name, intro=new_good_intro,price=new_good_price,type_id_id=new_good_type_id)
        # #返回到书籍列表页
        return redirect("/goods_list/")
    ret = models.Goods_type.objects.all()
    return render(request, "add_goods.html", {"good_type_list": ret})

def delete_goods(request):
    # 从URL里获取要删除书籍的id

    delete_id = request.GET.get("id")
    # 去数据库中删除指点id的书
    models.Goods.objects.get(id=delete_id).delete()
    # 返回书籍列表页，查看是否删除成功
    return redirect("/goods_list")

def edit_goods(request):

    if request.method =="POST":
        new_id = request.POST.get("id")
        new_name = request.POST.get("good_name")
        new_intro = request.POST.get("good_intro")
        new_price = request.POST.get("good_price")
        new_type_id = request.POST.get("good_type")

        edit_good_obj = models.Goods.objects.get(id=new_id)#根据ID获取数据库对象
        #提交到数据库
        edit_good_obj.name = new_name
        edit_good_obj.intro = new_intro
        edit_good_obj.price = new_price
        edit_good_obj. type_id_id = new_type_id
        edit_good_obj.save()
        #返回到列表页查看是否编辑成功
        return redirect("/goods_list/")

    edit_id = request.GET.get("id")
    edit_good_obj = models.Goods.objects.get(id=edit_id)
    ret = models.Goods_type.objects.all()
    return render(request,"edit_goods.html",{"good_obj":edit_good_obj,"good_type":ret})

def huiyuan_list(request):

    all_huiyuan = models.Huiyuan.objects.all()
    # 在html页面完成字符串的替换
    return render(request, "huiyuan_list.html", {"all_huiyuan": all_huiyuan})

def edit_huiyuan(request):
    if request.method =="POST":
        new_id = request.POST.get("id")
        new_name = request.POST.get("huiyuan_name")
        new_pwd = request.POST.get("huiyuan_pwd")
        new_price = request.POST.get("huiyuan_price")
        edit_huiyuan_obj = models.Book.objects.get(id=new_id)#根据ID获取数据库对象
        edit_huiyuan_obj.name = new_name
        edit_huiyuan_obj.pwd = new_pwd
        edit_huiyuan_obj.price = new_price
        #提交到数据库
        edit_huiyuan_obj.save()
        #返回到列表页查看是否编辑成功
        return redirect("/huiyuan_list/")
    #返回一个页面让用户编辑会员信息
    #取到编辑的会员的ID值
    edit_id = request.GET.get("id")
    #根据id去数据库中把具体的书籍对象拿到
    edit_huiyuan_obj = models.Huiyuan.objects.get(id=edit_id)
    return render(request,"edit_huiyuan.html",{"huiyuan_obj":edit_huiyuan_obj})

def delete_huiyuan(request):
    # 从URL里获取要删除书籍的id

    delete_id = request.GET.get("id")
    # 去数据库中删除指点id的书
    models.Huiyuan.objects.get(id=delete_id).delete()
    # 返回书籍列表页，查看是否删除成功
    return redirect("/huiyuan_list")

def add_huiyuan(request):

    if request.method == "POST":

        new_name = request.POST.get("huiyuan_name")
        new_pwd= request.POST.get("huiyuan_pwd")
        new_price =  request.POST.get("huiyuan_price")
        models.Huiyuan.objects.create(name=new_name, pwd=new_pwd,price=new_price)
        return redirect("/huiyuan_list/")
    ret = models.Huiyuan.objects.all()
    return render(request, "add_huiyuan.html", {"huiyuan": ret})

def edit_huiyuan(request):
    if request.method =="POST":
        new_id = request.POST.get("id")
        new_name = request.POST.get("huiyuan_name")
        new_pwd = request.POST.get("huiyuan_pwd")
        new_price = request.POST.get("huiyuan_price")
        edit_huiyuan_obj = models.Huiyuan.objects.get(id=new_id)#根据ID获取数据库对象
        edit_huiyuan_obj.name = new_name
        edit_huiyuan_obj.pwd = new_pwd
        edit_huiyuan_obj.price = new_price
        #提交到数据库
        edit_huiyuan_obj.save()
        #返回到列表页查看是否编辑成功
        return redirect("/huiyuan_list/")
    edit_id = request.GET.get("id")
    #根据id去数据库中把具体的会员对象拿到
    edit_huiyuan_obj = models.Huiyuan.objects.get(id=edit_id)
    return render(request,"edit_huiyuan.html",{"huiyuan_obj":edit_huiyuan_obj})

def test(request):
    print(request.GET)
    print(request.GET.get("name"))
    return HttpResponse("ok")

def publisher_list():
    pass
#展示书的列表


def book_list(request):
    #去数据库中查询所有的书籍
    all_book =models.Book.objects.all()
    #在html页面完成字符串的替换
    return render(request,"book_list2.html",{"all_book":all_book})

def add_book(request):
    #取到所有的出版社
    if request.method == "POST":
        #{"book_title":"跟金老板学开车，"publisher_id"：9}
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        # #创建新书对象
        print("afaf "+new_publisher_id)
        models.Book.objects.create(title=new_title,publisher_id_id =new_publisher_id)
        # #返回到书籍列表页
        return redirect("/book_list/")
    ret = models.Publisher.objects.all()
    return render(request,"add_book.html",{"publisher_list":ret})

from django.views import View
#CBV版添加出版社
class Addbook(View):
    def get(self,request):
        return render(request, "add_book.html")
    def post(self,request):
        # {"book_title":"跟金老板学开车，"publisher_id"：9}
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        # #创建新书对象
        print("afaf " + new_publisher_id)
        models.Book.objects.create(title=new_title, publisher_id_id=new_publisher_id)
        # #返回到书籍列表页
        return redirect("/book_list/")


def delete_book(request):
    #从URL里获取要删除书籍的id

    delete_id = request.GET.get("id")
    #去数据库中删除指点id的书
    models.Book.objects.get(id=delete_id).delete()
    #返回书籍列表页，查看是否删除成功
    return redirect("/book_list")

def edit_book(request):
    if request.method =="POST":
        new_id = request.POST.get("id")
        new_title = request.POST.get("book_title")
        new_publisher_id = request.POST.get("publisher")
        edit_book_obj = models.Book.objects.get(id=new_id)#根据ID获取数据库对象
        edit_book_obj.title = new_title
        edit_book_obj.publisher_id_id = new_publisher_id
        #提交到数据库
        edit_book_obj.save()
        #返回到列表页查看是否编辑成功
        return redirect("/book_list/")
    #返回一个页面让用户编辑书籍信息
    #取到编辑的书的ID值
    edit_id = request.GET.get("id")
    #根据id去数据库中把具体的书籍对象拿到
    edit_book_obj = models.Book.objects.get(id=edit_id)
    ret = models.Publisher.objects.all()
    return render(request,"edit_book.html",{"publisher_list":ret,"book_obj":edit_book_obj})

#处理上传文件的函数
def upload(request):
    if request.method =="POST":
        #从请求的FILES中获取上传文件的文件名，file为页面上type=files类型
        filename = request.FILES["upload_file"].name
        #在项目目录下新建一个文件
        with open(filename,"wb") as f:
            #从上传的文件对象中一点一点读
            for chunk in request.FILES["upload_file"].chunks():
                #写入本地文件
                f.write(chunk)
        return HttpResponse("上传OK")

