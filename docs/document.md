# Document

### Installation

```shell
pip3 install haishoku
```

or maybe you should use

```shell
python3 -m pip install haishoku
```

### Api

#### • getDominant( image )

```python
from haishoku.haishoku import Haishoku
dominant = Haishoku.getDominant(image)
```

returns: (R, G, B) `tuple`

#### • showDominant( image )

```python
from haishoku.haishoku import Haishoku
Haishoku.showDominant( image )
```

it will open a temp image to show the dominant color.

#### • getPalette( image )

```python
from haishoku.haishoku import Haishoku
palette = Haishoku.getPalette( image )
```

returns: [(R, G, B), (R, G, B), ...] `Array` length <= 8

#### • showPalette( image )

```python
from haishoku.haishoku import Haishoku
Haishoku.showPalette( image )
```

it will open a temp image to show the palette.