"""
drawsvg_helper_micro provides a wrapper class for drawsvg when you have
a known list of coordinates and want to offload the coordinate calculations

```python
from py_svghelper_micro import DrawingHandler

dh = DrawingHandler([(1,1),(10,5)], 800, 600)
```

"""


from .drawsvg_helper import DrawingHandler

DrawingHandler
