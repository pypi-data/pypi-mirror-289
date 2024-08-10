# python-svg-helper-micro

drawsvg_helper_micro provides a wrapper class for drawsvg when you have
a known list of coordinates and want to offload the coordinate calculations

```python
from py_svghelper_micro import DrawingHandler

dh = DrawingHandler([(1,1),(10,5)], 800, 600)

# drawsvg Drawing can be access via the d property

dh.d.append(element)

```

# TODO

-   allow choice of square adjustments on a non square image size
