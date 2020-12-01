### 预览项目，运行步骤：

### 开发环境
#### 使用Pipenv
##### 1. 安装
```
$ pip install pipenv
```

##### 2. 创建虚拟环境
```
$ cd dblog  // 切换到项目目录
$ pipenv --three // 使用python3环境
```

##### 3. 安装依赖
```
$ pipenv install
```

##### 4. 进入虚拟环境
```
$ pipenv shell
```

##### 5. 迁移数据库
```
$ python manage.py migrate // 项目默认使用sqlite3
```

#### 使用Virtualenv
##### 1. 安装
```
$ pip install virtualenv
```

##### 2. 创建虚拟环境
```
$ cd dblog // 切换到项目目录
$ virtualenv venv -p python3
```

##### 3. 进入虚拟环境
```
$  .\venv\Scripts\activate  // win
$  source venv/bin/activate // mac、linux
```

##### 4. 安装依赖
```
$ pip install -r requirements.txt
```

##### 5. 数据库迁移
```
$ python manage.py migrate // 项目默认使用sqlite3
```

### 添加假数据以预览样式(可忽略，建立空内容博客)
```
$ python ./scripts/fake.py 

$ python .\scripts\fake.py // win
```

### RunServer
```
$ python manage.py runserver
```
