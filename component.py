import pytablewriter, six
from pandas import DataFrame, Series
from pathlib import Path
import shutil
from collections.abc import Mapping, Iterable

"""draw horizontal line"""
def line():
    return _end("---")

"""
return text including h tag
"""
def heading(data, h):
    hmapping = ["#" * i + " " * (i > 0) for i in range(7)]
    res = "{}{}".format(hmapping[h or 0], str(data))
    return _end(res)

"""
switch itemize or enumerate with numbering argument
"""
def enum(iter, numbering=False, depth=0):
    lst = __inner_enum_lst(iter, [], numbering=numbering, depth=depth)
    return _end("\n".join(lst))

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

"""generate markdown formatted img expression"""
def img(src, md_file, *, alt=None, title=None, img_dir = "img", ignore=False):
    src_path = Path(src) #img

    # dst is on the src_dir
    rel_img_dir = Path(img_dir)
    md_path = Path(md_file)

    dst_dir = md_path.parent / rel_img_dir
    dst_path = dst_dir / src_path.name
    md_path.parent.mkdir(exist_ok=True)

    if src_path.exists() or (not ignore):
        dst_dir.mkdir(exist_ok=True)
        if not Path.samefile(src_path.parent, dst_path.parent):
            shutil.copyfile(str(src_path), str(dst_path))
    alt = alt or src_path.stem
    title = title or src_path.stem

    res = '''![{}]({} "{}")'''.format(alt, rel_img_dir / src_path.name, title)
    return _end(res)


"""generate link"""
def link(text, path, *, newline=True):
    res = '''[{}]({})'''.format(text, path)
    return _end(res) if newline else res


def __inner_enum_lst(iter, buf, numbering=False, depth=0):
    mark = "1." if numbering else "+"
    prefix = "  " * depth

    if isinstance(iter, Mapping):
        for key, value in iter.items():
            buf.append("{}{} {} : {}".format(prefix, mark, key, value))
    else:
        for elem in iter:
            if isinstance(elem, Iterable) and (not isinstance(elem, six.string_types)):
                buf = __inner_enum_lst(elem, buf, numbering=numbering, depth=depth+1)
            else:
                buf.append("{}{} {}".format(prefix, mark, elem))
    return buf
