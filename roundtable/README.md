```bash
# 创建项目
django-admin startproject roundtable
python manage.py startapp lancelot

# 初始化数据库
python manage.py makemigrations lancelot
python manage.py migrate

# 启动服务
python manage.py runserver
```

## 待完成的内容

1 基于类的视图

2 中间件替代自定义装饰器

3 model添加字段注释说明

4 