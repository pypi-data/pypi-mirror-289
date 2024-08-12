# 一个简单的复习命令行工具

## 使用方法

### 添加复习项

```cmd
review review_name position
```

### 查看今天的复习项

```cmd
review
```

## .pypirc格式

```
[pypi]
username = __token__
password = <the token value, including the `pypi-` prefix>
```

## 打包命令

```python setup.py sdist bdist_wheel```

## 上传命令

```twine upload dist/*```

