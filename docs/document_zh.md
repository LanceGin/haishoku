# 中文文档

### 安装

```shell
pip3 install haishoku
```

或者你可能需要使用下面的方式

```shell
python3 -m pip install haishoku
```

### 接口

#### • getDominant( image )

```python
from haishoku.haishoku import Haishoku
dominant = Haishoku.getDominant(image)
```

返回: (R, G, B) `元组`

#### • showDominant( image )

```python
from haishoku.haishoku import Haishoku
Haishoku.showDominant( image )
```

该方法会新建一个临时文件用来显示主色调

#### • getPalette( image )

```python
from haishoku.haishoku import Haishoku
palette = Haishoku.getPalette( image )
```

返回: [(R, G, B), (R, G, B), ...] `数组` 个数不超过 8

#### • showPalette( image )

```python
from haishoku.haishoku import Haishoku
Haishoku.showPalette( image )
```

该接口会新建一个临时文件用来显示配色方案