

from decimal import Decimal

import drawsvg as draw

class DrawingHandler():
    d: draw.Drawing
    x_adjust: Decimal
    y_adjust: Decimal
    max_x: Decimal
    max_y: Decimal
    width: int
    height: int
    border: Decimal

    def __init__(
            self,
            coord_list: list[tuple[Decimal, Decimal]],
            width: int = 1000,
            height: int = 1000,
            border: Decimal = 1.1
    ):
        self.d = draw.Drawing(width, height, origin=(0, 0))
        self.width = width
        self.height = height

        lats = [x[0] for x in coord_list]
        self.x_adjust = min(lats) * -1

        lons = [x[1] for x in coord_list]
        self.y_adjust = min(lons) * -1

        self.max_x = max(lats) - min(lats)
        self.max_y = max(lons) - min(lons)

        self.border = border

    def adjust_coord(self, coord: tuple[Decimal, Decimal]) -> tuple[Decimal, Decimal]:
        x = ((coord[0] + self.x_adjust) / self.max_x) * self.width
        y = ((coord[1] + self.y_adjust) / self.max_y) * self.height
        return (x, y)
