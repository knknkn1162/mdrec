import pytablewriter, six
from pandas import DataFrame, Series


"""draw horizontal line"""
def horizontal():
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
def enum(lst, numbering=False):
    mark = "1." if numbering else "+"
    res = []
    for elem in lst:
        res.append(
            "{} {}".format(mark, elem))

    return _end("\n".join(res))

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
