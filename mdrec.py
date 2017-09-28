import grip

import component
from pandas import DataFrame, Series
from pathlib import Path

from IPython.display import display_markdown  # show とか、 record_md など使える

from collections.abc import Iterable
import logging
import uuid

logger = logging.getLogger(__name__)


class MDRec():
    def __init__(self, *, save_file=None, refresh=True):
        self.path = Path(save_file) if save_file is not None else Path('./_cache_{}.md'.format(uuid.uuid4()))
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
    def rec(self, data, *, h=None, title=None, display_notebook=True):
        res = ""
        if any(list(map(lambda t: isinstance(data, t), [DataFrame, Series]))):
            res += component.table(data, h=h, title=title)
        elif isinstance(data, str):
            res += component.heading(data, h=h)
        elif isinstance(data, Iterable):  # except type of str
            res += component.enum(data)
        else:
            res += component.heading(data, h=h)

        if display_notebook:
            display_markdown(res, raw=True)

        return self._save(res)

    """insert image in markdown file"""
    def img(self, src, *, alt=None, title=None, ignore=False):
        return self._save(component.img(src, md_file=self.path, alt=alt, title=title, ignore=ignore))

    """write horizontal line in the save_file"""
    def line(self):
        return self._save(component.line())

    """convert markdown file to html"""
    def export_html(self, *, render_inline=True, title=None):
        return grip.export(self.path, title=title, render_inline=render_inline)

    def _save(self, res):
        mode = "w" if (self.counter == 0 and self.refresh == True) else "a"
        with self.path.open(mode=mode, encoding='utf8', errors='ignore') as f:
            f.write(res)
        self.counter += 1
        return res

