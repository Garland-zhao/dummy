# dummy
homework of Sacntist

# 基于Django3.2 && PG构建API接口和展示页面

* ## 目前支持的功能
    - 用户的注册、登录、登出
    - 管理员查看所有用户信息，用户只能查看自己的信息
    - 用户修改昵称


* ## 在服务启动后，需要手动添加身份数据

```sql
INSERT INTO "public"."auth_group" ("id", "name") VALUES (1, 'admin');
INSERT INTO "public"."auth_group" ("id", "name") VALUES (2, 'customer');
```

* ## 创建管理员用户(用户名需要^admin)
```bash
python manage.py createsuperuser --username=admin_01 --email=admin01@example.com
```

* ## 其它的一些问题
    - 没想到Django已经出到v4.1了，
    - 前后端分离真是好文明。。。
    - 碍于时间限制，无法深入了解其独特的ORM，通用视图也是一个极大优化结构的方面
    - 生产环境下还需要找一些django的三方包，来满足诸如参数校验等常规操作的简单实现