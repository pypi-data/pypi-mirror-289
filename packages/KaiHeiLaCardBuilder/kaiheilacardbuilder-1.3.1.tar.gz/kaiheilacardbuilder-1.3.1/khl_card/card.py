import json
from collections.abc import Sequence
from typing import List, Iterator, TypeVar
from typing import Optional, Union

from .color import Color
from .modules import _Module
from .types import ThemeTypes, SizeTypes, NamedColor

__all__ = ['Card', 'CardMessage']

_T_co = TypeVar("_T_co", covariant=True)


class Card(Sequence):
    """
    构建卡片
    """
    type: str = 'card'
    theme: str
    size: str
    color: Optional[str]
    modules: List[_Module]

    def __init__(self, *modules: _Module, theme: Union[str, ThemeTypes] = ThemeTypes.PRIMARY,
                 size: Union[str, SizeTypes] = SizeTypes.LG, color: Union[Color, NamedColor, str, None] = None) -> None:
        """
        构建卡片

        :param modules: 卡片模块列表
        :param theme: 卡片主题
        :param size: 目前只支持sm与lg。 lg仅在PC端有效, 在移动端不管填什么，均为sm。
        :param color: 卡片颜色 ex: #55ffff or NamedColor.XXX
        """
        self.modules = list(modules)
        self.theme = theme if isinstance(theme, str) else theme.value
        self.size = size if isinstance(size, str) else size.value
        if color is None:
            self.color = None
        elif isinstance(color, str):
            self.color = color
        elif isinstance(color, Color):
            self.color = color.__str__()
        elif isinstance(color, NamedColor):
            self.color = color.value.__str__()
        else:
            raise ValueError('incorrect color value: ' + self.color)

    def __getitem__(self, item: int) -> _Module:
        return self.modules[item]

    def __setitem__(self, key: int, value: _Module):
        self.modules[key] = value

    def __len__(self):
        return len(self.modules)

    def __iter__(self) -> Iterator[_T_co]:
        return self.modules.__iter__()

    def __contains__(self, value: object) -> bool:
        return self.modules.__contains__(value)

    def __reversed__(self) -> Iterator[_T_co]:
        return self.modules.__reversed__()

    def __repr__(self):
        return 'Card(' + ', '.join([module.__repr__() for module in self.modules]) + ')'

    def count(self, value: _Module) -> int:
        return self.modules.count(value)

    def index(self, value: _Module, start: int = ..., stop: int = ...) -> int:
        return self.modules.index(value, start, stop)

    def append(self, module: _Module):
        self.modules.append(module)

    def build(self) -> dict:
        """
        :return: 构造后卡片
        """
        ret = {'type': self.type, 'theme': self.theme, 'size': self.size, 'modules': []}
        if self.color is not None:
            ret['color'] = self.color
        for i in self.modules:
            ret['modules'].append(i.build())
        return ret

    def build_to_json(self) -> str:
        return json.dumps(self.build(), indent=4, ensure_ascii=False)

    def clear(self) -> 'Card':
        self.modules.clear()
        return self

    def set_theme(self, theme: Union[str, ThemeTypes]) -> 'Card':
        self.theme = theme if isinstance(theme, str) else theme.value
        return self

    def set_size(self, size: Union[str, SizeTypes]) -> 'Card':
        self.size = size if isinstance(size, str) else size.value
        return self

    def set_color(self, color: Union[str, Color, NamedColor, None]) -> 'Card':
        if color is None:
            self.color = None
        elif isinstance(color, str):
            self.color = color
        elif isinstance(color, Color):
            self.color = color.__str__()
        elif isinstance(color, NamedColor):
            self.color = color.value.__str__()
        else:
            raise ValueError('incorrect color value: ' + self.color)
        return self


class CardMessage(Sequence):
    card_list: List[Card]

    def __init__(self, *card: Card) -> None:
        self.card_list = list(card)

    def __getitem__(self, item: int) -> Card:
        return self.card_list[item]

    def __setitem__(self, key: int, value: Card):
        self.card_list[key] = value

    def __len__(self):
        return len(self.card_list)

    def __iter__(self) -> Iterator[_T_co]:
        return self.card_list.__iter__()

    def __contains__(self, value: object) -> bool:
        return self.card_list.__contains__(value)

    def __reversed__(self) -> Iterator[_T_co]:
        return self.card_list.__reversed__()

    def __repr__(self):
        return 'CardMessage(' + ', '.join([card.__repr__() for card in self.card_list]) + ')'

    def index(self, value: Card, start: int = ..., stop: int = ...) -> int:
        return self.card_list.index(value, start, stop)

    def count(self, value: Card) -> int:
        return self.card_list.count(value)

    def append(self, card: Card):
        self.card_list.append(card)

    def build(self):
        return [card.build() for card in self.card_list]

    def build_to_json(self) -> str:
        return json.dumps(self.build(), indent=4, ensure_ascii=False)
