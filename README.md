# MDRec : Markdown Recorder from python

Create markdown file from python object.
You can also convert this to html file.

## Installation

```bash
pip install -e git+ssh://git@github.com/knknkn1162/mdrec.git@dev_seed#egg=mdrec-0.1dev
```

## Example

```python
save_file = "./out/test.md"
r = MDRec(save_file=save_file)

# write `# test` in save_file. 
r.rec("test", h=1)

msg = "teststeststests"
r.rec(msg)


# you can select whether itemize or enumerate by numbering option. By default, numbering=False.
iterable_obj = ["bbbi", "ddn", 3]
r.rec(iterable_obj)

# insert image.
r.img2md(src="./out/img/test01.png")

# you can display dataframe object with table. 
df = DataFrame([[12, 2, 4, 3], [3, 3, 3, 4]], columns=list("abcd"), index=["AB", "BB"])
r.rec(df, title="sample")

# export markdown to html.
r.to_html()
```

## Usage

+ By default, results are also displayed in jupyter notebook, so if you switch off the option, let `r.rec(obj, display_notebook=False)`.

## Configuration

+ If you use `MDRec.to_html`, note that this call [Grip](https://github.com/joeyespo/grip) implicitly. To set username and password, see the link, https://github.com/joeyespo/grip#configuration.
