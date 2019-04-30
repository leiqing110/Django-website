from django.db import models

# Create your models here.
#ORM相关的只能写在这个文件里，写到别的位置Django找不到
class AdminInfo(models.Model):#系统管理员
    id = models.AutoField(primary_key=True)  # 创建一个自增的主键
    name = models.CharField(max_length=20)  # 创建一个varchar类型的不能为空的字段
    email = models.CharField(max_length=20,default='')
    pwd = models.CharField(max_length=20, default="123")  # 创建用户密码

class UserInfo(models.Model):#用户信息表
    id = models.AutoField(primary_key=True)#创建一个自增的主键
    name = models.CharField(max_length=20)#创建一个varchar类型的不能为空的字段
    pwd = models.CharField(max_length=20,default="123")#创建用户密码

    def __str__(self):
        return "<{}-{}>".format(self.id, self.name)


class Movies(models.Model):
    id = models.AutoField(primary_key=True)#创建一个自增的主键
    mname = models.CharField(max_length=20,null=False)#创建一个varchar类型的不能为空的字段
    intro= models.TextField()
    time = models.CharField(max_length=20,null=False)#创建一个varchar类型的不能为空的字段
    yingting = models.CharField(max_length=20,null=False)#创建一个varchar类型的不能为空的字段


class Goods(models.Model):#商品信息表
    id = models.AutoField(primary_key=True)  # 创建一个自增的主键\
    name = models.CharField(max_length=20,null=False)#创建一个varchar类型的不能为空的字段
    intro =  models.TextField()  #商品的描述信息
    price = models.IntegerField()
    type_id = models.ForeignKey(to="Goods_type", on_delete=models.CASCADE)

class Goods_type(models.Model):#商品类型表
    id = models.AutoField(primary_key=True)  # 创建一个自增的主键
    name = models.CharField(max_length=64,null=False,unique=True) #类型名称

class Huiyuan(models.Model):
     id = models.AutoField(primary_key=True)  # 创建一个自增的主键
     name = models.CharField(max_length=20, null=False)  # 创建一个varchar类型的不能为空的字段
     pwd = models.CharField(max_length=20,default="123")#创建会员密码
#      price = models.IntegerField()  #充值信息
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    #创建一个varchar(64)的唯一的不为空的字段
    name = models.CharField(max_length=64,null=False,unique=True)
    addr = models.CharField(max_length=128,default="三里屯")

class Book(models.Model):
    id = models.AutoField(primary_key=True)#自增的主键字段
    #创建一个varchar(64)的唯一的不为空的字段e
    title = models.CharField(max_length=64,null=False,unique=True)
    #和出版社关联的外键字段
    publisher_id = models.ForeignKey(to="publisher",on_delete=models.CASCADE)

