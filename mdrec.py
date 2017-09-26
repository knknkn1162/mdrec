import six, grip

import pytablewriter
from pandas import DataFrame, Series
from pathlib import Path

from IPython.display import display_markdown  # show とか、 record_md など使える

from collections.abc import Iterable
from misc import src2base64
import logging
import shutil

logger = logging.getLogger(__name__)


class MDRec():
    def __init__(self, *, save_file=None, refresh=True):
        self.path = Path(save_file) if save_file is not None else Path('./md/test.md')
        self.refresh = refresh
        self.counter = 0

    @staticmethod
    def _append_new_line(data):
        return data + "\n\n"

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
            res += self.df2md(data, h=h, title=title)
        elif isinstance(data, str):
            hmapping = ["#" * i + " "*(i>0) for i in range(7)]
            res += self._append_new_line("{}{}".format(hmapping[h or 0], data))
        elif isinstance(data, Iterable):  # except type of str
            for d in data:
                res += self._append_new_line("+ {}".format(d))
        else:
            res += self._append_new_line(str(data))

        if display_notebook:
            display_markdown(res, raw=True)

        return self._save(res)

    """
    1. foo
    2. hoge
    3. ...
    """
    def enum(self, lst):
        pass

    def img2md(self, src, *, alt=None, title=None):
        src_path = Path(src)
        stem = src_path.stem
        parent = self.path.parent

        # dst is on the src_dir
        dst_img_path = Path("img") / src_path.name

        src = parent / str(dst_img_path)

        if src_path != src:
            shutil.copyfile(str(src_path), str(src))
        alt = alt or stem
        title = title or stem

        res = '''![{}]({} "{}")'''.format(alt, dst_img_path, title)
        return self._save(self._append_new_line(res))

    def quote(self, s):
        res = "\n".join(["> {}".format(t) for t in s.split("\n")])
        return self._save(self._append_new_line(res))

    def df2md(self, df, *,
              h=None, title=None):

        if h is None: h = 2
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

        res = self._logging(writer)
        return res

    def _save(self, res):
        mode = "w" if (self.counter == 0 and self.refresh == True) else "a"
        with self.path.open(mode=mode, encoding='utf8', errors='ignore') as f:
            f.write(res)
        self.counter += 1
        return res

    def _to_data_url(self, url, type):
        pass

    def _logging(self, writer):
        writer.stream = six.StringIO()
        writer.write_table()
        return writer.stream.getvalue()

    def to_html(self, *,
                username=None, password=None, render_inline=True, title=None):
        if [username, password] == [None, None]:
            logger.warning(
                "you may fail to convert {} to html because of rate limiting of github API..".format(self.path)
            )
        grip.export(self.path,
                    username=username, password=password, title=title, render_inline=render_inline)

