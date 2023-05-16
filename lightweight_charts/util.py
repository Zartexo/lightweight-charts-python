from typing import Literal


class MissingColumn(KeyError):
    def __init__(self, message):
        super().__init__(message)
        self.msg = message

    def __str__(self):
        return f'{self.msg}'


LINE_TYPE = Literal['solid', 'dotted', 'dashed', 'large_dashed', 'sparse_dotted']

POSITION = Literal['above', 'below', 'inside']

SHAPE = Literal['arrow_up', 'arrow_down', 'circle', 'square']

CROSSHAIR_MODE = Literal['normal', 'magnet']

PRICE_SCALE_MODE = Literal['normal', 'logarithmic', 'percentage', 'index100']


def _line_type(lt: LINE_TYPE):
    return {
        'solid': 'Solid',
        'dotted': 'Dotted',
        'dashed': 'Dashed',
        'large_dashed': 'LargeDashed',
        'sparse_dotted': 'SparseDotted',
        None: None,
    }[lt]


def _position(p: POSITION):
    return {
        'above': 'aboveBar',
        'below': 'belowBar',
        'inside': 'inBar',
        None: None,
    }[p]


def _shape(shape: SHAPE):
    return {
        'arrow_up': 'arrowUp',
        'arrow_down': 'arrowDown',
        'circle': 'Circle',
        'square': 'Square',
        None: None,
    }[shape]


def _crosshair_mode(mode: CROSSHAIR_MODE): return mode.title() if mode else None


def _js_bool(b: bool): return 'true' if b is True else 'false' if b is False else None


def _price_scale_mode(mode: PRICE_SCALE_MODE):
    return 'IndexedTo100' if mode == 'index100' else mode.title() if mode else None