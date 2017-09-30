import pytablewriter, six
from pandas import DataFrame, Series
from pathlib import Path
from os.path import relpath
import shutil
import yaml, mimetypes
from collections.abc import Mapping
from urllib.parse import urlsplit

import logging
logger = logging.getLogger(__name__)

"""draw horizontal line"""
def line():
    return _end("---")

"""
return text including h tag
"""
def header(data, h):
    hmapping = ["#" * i + " " * (i > 0) for i in range(7)]
    res = "{}{}".format(hmapping[h or 0], str(data))
    return _end(res)

"""
switch itemize or enumerate with numbering argument
"""
def enum(data):
    def preprocess(dat):
        if isinstance(dat, Mapping):
            return [dat]
        return dat

    res = yaml.dump(preprocess(data), default_flow_style=False, allow_unicode=True)
    return res + "\n"

"""convert dataframe to markdown using pytablewriter module"""
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
    writer.stream = six.StringIO()
    writer.write_table()
    return writer.stream.getvalue() + "\n"


"""
split prev or next sentence
"""
def _end(data):
    return data + "\n\n"

"""generate links or images on markdown"""
def link(src, *, text="", img=True,
         md_dir=".", title=None, copy = True, ignore=False, new_line=True, copy_sync=False):

    # if path is url
    if (urlsplit(src).netloc != ""):
        link_path = src
    else: # if local path
        Path(md_dir).mkdir(exist_ok=True)
        # judge image file or not
        src_path = Path(src)
        mimetypes.init()
        image_flag = mimetypes.types_map[src_path.suffix].startswith("image")

        if (not img) or (not copy) or (not image_flag):
            src_path = relpath(src_path, md_dir)
            link_path = src_path
        else:
            copy_dir = "img"
            src_dir = Path(md_dir) / copy_dir
            src_path = src_dir / src_path.name
            link_path = Path(copy_dir) / src_path.name
            # copy file
            src_dir.mkdir(exist_ok=True)
            if (not Path.samefile(src_path.parent, Path(src).parent)) and (not ignore):
                # copy file synchronously or not
                if copy_sync:
                    with open(str(src), 'rb') as f1, open(str(src_path), 'wb') as f2:
                        shutil.copyfileobj(f1, f2)
                else:
                    shutil.copyfile(str(src), str(src_path))

    img_sign = "!" if img else ""

    text = text or Path(src).name
    if title is not None:
        title = ''' "{}"'''.format(title)
    else:
        title=""

    res = '''{}[{}]({}{})'''.format(img_sign, text, link_path, title)
    return _end(res) if new_line else res
