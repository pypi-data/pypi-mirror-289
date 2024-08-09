# Pyf Login

This is a reusable Django login package that includes a JWT-based login view.

## 在 django 中应用

1、下载

```bash
pip install pyf_login
```

2、配置
INSTALLED_APPS 中添加 "pyf_login",

3、在 urls.py 中添加
path("auth/", include("pyf_login.urls")),

4、访问
url 为：auth/login （auth 前如果有前缀，请添加自己的前缀）
