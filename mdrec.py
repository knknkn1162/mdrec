import six, grip

import pytablewriter
from pandas import DataFrame, Series
from pathlib import Path

from IPython.display import display_markdown  # show とか、 record_md など使える

from collections.abc import Iterable
import logging
import shutil, uuid

logger = logging.getLogger(__name__)


class MDRec():
    def __init__(self, *, save_file=None, refresh=True):
        self.path = Path(save_file) if save_file is not None else Path('./md/{}.md'.format(uuid.uuid4()))
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
    def rec(self, data, *, h=None, title=None, display_notebook=True, numbering=False):
        res = ""
        if any(list(map(lambda t: isinstance(data, t), [DataFrame, Series]))):
            res += self.table(data, h=h, title=title)
        elif isinstance(data, str):
            self.heading(data, h=h)
        elif isinstance(data, Iterable):  # except type of str
            res += self.enum(data, numbering)
        else:
            res += self.heading(data, h=h)

        if display_notebook:
            display_markdown(res, raw=True)

        return self._save(res)

    """insert image in markdown file"""
    def rec_img(self, src, *, alt=None, title=None, ignore=True):
        return self._save(self.img(src, alt=alt, title=title, ignore=ignore))

    """convert markdown file to html"""
    def to_html(self, *, render_inline=True, title=None):
        return grip.export(self.path, title=title, render_inline=render_inline)

    """generate markdown formatted img expression"""
    def img(self, src, *, alt=None, title=None, img_dir = "img", ignore=False):
        src_path = Path(src) #img

        # dst is on the src_dir
        rel_img_dir = Path(img_dir)

        dst_dir = self.path.parent / rel_img_dir
        dst_path = dst_dir / src_path.name
        self.path.parent.mkdir(exist_ok=True)

        if src_path.exists() or (not ignore):
            dst_dir.mkdir(exist_ok=True)
            if not Path.samefile(src_path.parent, dst_path.parent):
                shutil.copyfile(str(src_path), str(dst_path))
        alt = alt or src_path.stem
        title = title or src_path.stem

        res = '''![{}]({} "{}")'''.format(alt, rel_img_dir / src_path.name, title)
        return self._end(res)

    @staticmethod
    def _end(data):
        return data + "\n\n"

    @staticmethod
    def heading(data, h):
        hmapping = ["#" * i + " " * (i > 0) for i in range(7)]
        res = "{}{}".format(hmapping[h or 0], str(data))
        return MDRec._end(res)

    """
    switch itemize or enumerate with numbering argument
    """
    @staticmethod
    def enum(lst, numbering=False):
        mark = "1." if numbering else "+"
        res = []
        for elem in lst:
            res.append(
                "{} {}".format(mark, elem))

        return MDRec._end("\n".join(res))

    """convert dataframe to markdown using pytablewriter module"""
    @staticmethod
    def table(df, *, h=2, title=None):
        if isinstance(df, Series):
            df = DataFrame(df)

        if df.index.name is None:
            df.index.name = ""
        df = df.reset_index()

        writer = pytablewriter.MarkdownTableWriter()
        writer.set_indent_level(h - 1)
        if title is not None:
            writer.table_name = title

        writer.from_dataframe(df)
        # fitted multiple cases
        writer.header_list = ["  {}  ".format(a) for a in df.columns]

        res = MDRec._write(writer)
        return res + "\n"

    def _save(self, res):
        mode = "w" if (self.counter == 0 and self.refresh == True) else "a"
        with self.path.open(mode=mode, encoding='utf8', errors='ignore') as f:
            f.write(res)
        self.counter += 1
        return res

    @staticmethod
    def _write(writer):
        writer.stream = six.StringIO()
        writer.write_table()
        return writer.stream.getvalue()

