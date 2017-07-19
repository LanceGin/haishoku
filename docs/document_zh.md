# Haishoku

> `haishoku` 是一个日语词, 意思是 `配色`.

Haishoku 是一个用来获取图片主色调和主要配色方案的python库，依赖于`python3`和`pillow`。

### 功能

1. 获取图片的 `主色调`

2. 获取图片的 `配色方案`

3. 从`v1.1.3`版本开始，可以直接从网络url生成Haishoku对象

### 示例
![demo](http://wx2.sinaimg.cn/large/89243dfbly1ffoekfainzj20dw05k0u7.jpg)

( 原图来源: dribbble )

### 安装

```shell
pip3 install haishoku
```

如果提示没有pip3，可能需要按以下方式安装：

```shell
python3 -m pip install haishoku
```

### Api

#### • loadHaishoku( image )

```python
from haishoku.haishoku import Haishoku
haishoku = Haishoku.loadHaishoku(image)
```

接口会返回一个`Haishoku`实例，你可以通过实例属性`haishoku.dominant` 和 `haishoku.palette`直接获取到对应的`主色调` 和 `配色方案`

> 当然，也提供了更加直接的接口用来获取对应颜色的值以及临时预览颜色，如下：

#### • getDominant( image )

```python
from haishoku.haishoku import Haishoku
dominant = Haishoku.getDominant(image)
```

返回结构为 (R, G, B) 的一个 `元组`

#### • showDominant( image )

```python
from haishoku.haishoku import Haishoku
Haishoku.showDominant( image )
```

接口会打开一个临时文件用来预览主色调的颜色。（不会保存在本地）

#### • getPalette( image )

```python
from haishoku.haishoku import Haishoku
palette = Haishoku.getPalette( image )
```

返回一个结构为： [(percentage, (R, G, B)), (percentage, (R, G, B)), ...] 最大长度为8的`数组`

#### • showPalette( image )

```python
from haishoku.haishoku import Haishoku
Haishoku.showPalette( image )
```

接口会打开一个临时文件用来预览图片配色方案。（不会保存在本地）

### Document

 [Document](../README.md)


