# MDRec Markdown Recorder from python

## Installation



## Example

```python
save_file = "./out/test.md"
r = MDRec(save_file=save_file)

# write `# test` in save_file. 
r.rec("test", h=1)

msg = "teststeststests"
r.rec(msg)
iterable_obj = ["bbbi", "ddn", 3]

# you can select whether numbering or not
r.rec(iterable_obj)

r.img2md(src="./out/img/test01.png")

# display_test
df = DataFrame([[12, 2, 4, 3], [3, 3, 3, 4]], columns=list("abcd"), index=["AB", "BB"])
r.rec(df, title="sample")

# export markdown => html using grip, https://github.com/joeyespo/grip
r.to_html()
```

## Usage

+ By default, results are also displayed in jupyter notebook, so if you switch off the option, let `r.rec(obj, display_notebook=False)`.
