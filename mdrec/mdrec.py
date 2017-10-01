import grip

from . import component
from pandas import DataFrame, Series
from pathlib import Path

from IPython.display import display_markdown
from collections.abc import Iterable

import logging
logger = logging.getLogger(__name__)


class MDRec():
    def __init__(self, *, save_file=None, refresh=True):
        self.path = Path(save_file) if save_file is not None else None
        self.refresh = refresh
        self._quote_level = 0

    def increase_quote_level(self):
        self._quote_level += 1

    def decrease_quote_level(self):
        self._quote_level = max(0, self._quote_level-1)

    def reset_quote_level(self):
        self._quote_level = 0

    def generate_quote(self):
        return ">"*self._quote_level + " "*(self._quote_level>0)

    """
    depending on type of data argument, change output.
        DataFrame : to markdown_formatted table
        Series : to markdown_formatted table
        list : to itemize
        str : as it is
        otherwise : to str
    """
    def rec(self, data, *, h=None, title=None, raw=True):
        res = ""
        if any(list(map(lambda t: isinstance(data, t), [DataFrame, Series]))):
            default_h = h or 2
            res += component.table(data, h=default_h, title=title)
        elif isinstance(data, Iterable) and (not isinstance(data, str)):  # except type of str
            res += component.enum(data)
        else:
            res += component.header(data, h=h)

        quote = self.generate_quote()
        res = "".join([quote + line for line in res.splitlines(keepends=True)])

        display_markdown(res, raw=raw)

        return self._save(res)

    """insert image in markdown file"""
    def img(self, src, *, text="", title=None, copy=True, ignore=False, raw=True, copy_sync=False):
        res = component.link(src=src, md_dir=self.path.parent,
            text=text, img=True, title=title, copy=copy, ignore=ignore, new_line=True,
        )
        if raw:
            display_res = component.link(src=src, md_dir=".",
                text=text, title=title, copy=False, ignore=True, copy_sync=copy_sync,
            )

            display_markdown(display_res, raw=raw)

        return self._save(res)

    """write horizontal line in the save_file"""
    def line(self, raw=True):
        res = component.line()
        display_markdown(res, raw=raw)

        return self._save(res)

    """generate link path"""
    def link(self, src, *, text="", title=None, copy=True, ignore=False, new_line=True, raw=True):
        res = component.link(src=src, md_dir=self.path.parent,
            text=text, img=False, title=title, copy=copy, ignore=ignore, new_line=new_line
        )
        if raw:
            display_res = component.link(src=src, md_dir=".",
                text=text, img=False, title=title, copy=False, ignore=True, new_line=new_line
            )
            display_markdown(display_res, raw=raw)

        return self._save(res)

    """convert markdown file to html"""
    def to_html(self, *, render_inline=True, title=None):
        if self.path is not None:
            return grip.export(self.path, title=title, render_inline=render_inline)
        else:
            logging.warning("save_file is None")

    def _save(self, res):
        mode = "w" if self.refresh else "a"
        if self.path is not None:
            with self.path.open(mode=mode, encoding='utf8', errors='ignore') as f:
                f.write(res)
        self.refresh = False
        return res

