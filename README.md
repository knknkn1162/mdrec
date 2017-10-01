# MDRec : Markdown Recorder from python

MDRec creates markdown file easily from python object.
You can also convert this to html file at once.

## Installation

+ this library is under development..

```bash
pip install mdrec
```

## Example

Here is example code, output result and raw_file respectively.

### Code

```python
from mdrec import MDRec

save_file = "./out/test_txt.md"
# set markdown file. (You may also try not to set this option.)
r = MDRec(save_file=save_file)

# suppoort header. write "#### testtest\n\n" in designated save_file.
r.rec("testtest", h=4)

# plain txt
r.rec("this is example below")

# express itemization via Iterable object
r.rec([1,2,3])

# draw vertical line
r.line()

# support ja
r.rec(["あ", "い", "う", {"え" : "お"}])

# you should draw a vertical line explicitly
r.line()

# support nested list, dict or Iterable. 
r.rec([1,[1,2],[2,[3],4], [{"a": 100, "b": 234}], {"c" : [3,4,5]}])

## support quote
r.increase_quote_level()
## If you set raw option to be False, suppress markdown output in jupyter notebook.
r.rec("testtest", h=2, raw=False)

r.increase_quote_level()
r.rec(["z", 'x'])

r.reset_quote_level()

from pandas import DataFrame
# support DataFrame or Series ((NOT support list of list)
df = DataFrame([[12, 2, 4, 3], [3, 3, 3, 4]], columns=list("abcd"), index=["AB", "BB"])

# display table with title
r.rec(df, title="test", h=3)

# set link. support both url and local file path.
r.link(src="./test01.png", title="test", text="sample")

# image link with markdown syntax. To display image in jupyter notebook syncronously, set copy_sync=True
r.img(src="./test01.png", title="test", text="sample", copy_sync=True)

# export markdown file to html via github API. (You can set your username and password in ~/.grip/settings.py.)
r.to_html()
```

### Output

`<start>`

#### testtest

this is example below

- 1
- 2
- 3

---

- あ
- い
- う
- え: お

---

- 1
- - 1
  - 2
- - 2
  - - 3
  - 4
- - a: 100
    b: 234
- c:
  - 3
  - 4
  - 5

> ## testtest
> 
>> - z
>> - x
>> 
### test
|   |  a  |  b  |  c  |  d  |
|---|----:|----:|----:|----:|
|AB |   12|    2|    4|    3|
|BB |    3|    3|    3|    4|


[sample](../test01.png "test")

![sample](img/test01.png "test")



`<end>`

### Raw 

```markdown
#### testtest

this is example below

- 1
- 2
- 3

---

- あ
- い
- う
- え: お

---

- 1
- - 1
  - 2
- - 2
  - - 3
  - 4
- - a: 100
    b: 234
- c:
  - 3
  - 4
  - 5

> ## testtest
> 
>> - z
>> - x
>> 
### test
|   |  a  |  b  |  c  |  d  |
|---|----:|----:|----:|----:|
|AB |   12|    2|    4|    3|
|BB |    3|    3|    3|    4|


[sample](../test01.png "test")

![sample](img/test01.png "test")
```

## Usage

+ By default, results are also displayed in jupyter notebook, so if you switch off the option, let `r.rec(obj, raw=False)`.

## Configuration

+ If you use `MDRec.to_html`, note that this call [Grip](https://github.com/joeyespo/grip) and github API implicitly. To set github username and password, see the link, https://github.com/joeyespo/grip#configuration.
