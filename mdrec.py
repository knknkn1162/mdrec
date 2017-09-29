import grip

import component
from pandas import DataFrame, Series
from pathlib import Path

from IPython.display import display_markdown  # show とか、 record_md など使える

from collections.abc import Iterable
import logging

logger = logging.getLogger(__name__)


class MDRec():
    def __init__(self, *, save_file=None, refresh=True):
        self.path = Path(save_file) if save_file is not None else None
        self.refresh = refresh
        self.counter = 0

    """
    depending on type of data argument, change output.
        DataFrame : to markdown_formatted table
        Series : to markdown_formatted table
        list : to itemize
        str : as it is
        otherwise : to str
    """
    def rec(self, data, *, h=None, title=None, display=True):
        res = ""
        if any(list(map(lambda t: isinstance(data, t), [DataFrame, Series]))):
            res += component.table(data, h=h, title=title)
        elif isinstance(data, str):
            res += component.heading(data, h=h)
        elif isinstance(data, Iterable):  # except type of str
            res += component.enum(data)
        else:
            res += component.heading(data, h=h)

        self._display_md(res, display)

        return self._save(res)

    """insert image in markdown file"""
    def img(self, src, *, text="", title=None, copy=True, ignore=False, display=False):
        res = component.link(src=src, md_dir=self.path.parent,
            text=text, img=True, title=title, copy=copy, ignore=ignore, new_line=True,
        )

        self._display_md(res, display)

        return self._save(res)

    """write horizontal line in the save_file"""
    def line(self, display=True):
        res = component.line()
        self._display_md(res, display)

        return self._save(res)

    """generate link path"""
    def link(self, src, *, text="", img=False, title=None, copy=True, ignore=False, new_line=True, display=True):
        res = component.link(src=src, md_dir=self.path.parent,
            text=text, img=img, title=title, copy=copy, ignore=ignore, new_line=new_line
        )

        self._display_md(res, display)

        return self._save(res)

    """convert markdown file to html"""
    def to_html(self, *, render_inline=True, title=None):
        if self.path is not None:
            return grip.export(self.path, title=title, render_inline=render_inline)
        else:
            logging.warning("save_file is None")

    def _save(self, res):
        mode = "w" if (self.counter == 0 and self.refresh == True) else "a"
        if self.path is not None:
            with self.path.open(mode=mode, encoding='utf8', errors='ignore') as f:
                f.write(res)
        self.counter += 1
        return res

    @staticmethod
    def _display_md(data, display):
        if display:
            display_markdown(data, raw=True)

