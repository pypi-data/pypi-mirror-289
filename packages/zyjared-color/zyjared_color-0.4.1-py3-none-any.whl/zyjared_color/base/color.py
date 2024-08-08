from ..core import Style, create_style_method_meta
from .styles import STYLES
import re


class Color(Style, metaclass=create_style_method_meta(STYLES)):

    def _compose_style(self):
        return f'\033[{';'.join([str(i) for i in self.style.values()])}m{self.text}\033[0m'

    def _calc_extra_len(self):
        if self.style:
            return len(f'\033[{';'.join([str(i) for i in self.style.values()])}m\033[0m')
        else:
            return 0

    def __format__(self, format_spec: str):

        # 无 format_spec
        if not format_spec:
            return f'{self._to_str():{format_spec}}'

        ns = re.findall(r'\d+', format_spec)

        # 无效 format_spec
        if not ns:
            return f'{self._to_str():{format_spec}}'

        # -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

        text = self._to_str()

        if self.children:
            true_len = 0
            for child in self.children:
                if child.text:
                    true_len += len(child.text)
        else:
            true_len = len(self.text)

        extra_n = len(text) - true_len

        if extra_n <= 0:
            return f'{text:{format_spec}}'
        else:
            _spec = format_spec.replace(
                ns[0],
                f'{int(ns[0]) + extra_n}'
            )
            return f'{text:{_spec}}'
