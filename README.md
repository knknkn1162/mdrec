# MDRec : Markdown Recorder from python

This library creates markdown file easily from python object.
You can also convert this to html file.

## Installation

+ this library is under development..

```bash
pip install -e git+ssh://git@github.com/knknkn1162/mdrec.git@dev_seed#egg=mdrec-0.1dev
```

## Example

Here is example code, output result and raw_file respectively.

### Code

```python
save_file = "./out/test_txt.md"
r = MDRec(save_file=save_file)

r.rec("testtest", h=4, display=False)

# support ja
r.rec(["あ", "い", "う", {"え" : "お"}])
# support nested list, dict or Iterable. 
r.rec([1,[1,2],[2,[3],4], [{"a": 100, "b": 234}], {"c" : [3,4,5]}])

from pandas import DataFrame
# support DataFrame or Series ((NOT support list of list)
df = DataFrame([[12, 2, 4, 3], [3, 3, 3, 4]], columns=list("abcd"), index=["AB", "BB"])
r.rec(df, title="sample", h=4)

# generate link (you can set img=True to generate images)
r.link("./src/tes.png", text="testtest", img=False)

# draw vertical line
r.line()

# export markdown to html.
r.to_html()
```

### Output

Run this code and you can get the markdown file below:

#### testtest

- あ
- い
- う
- え: お

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

#### sample
|   |  a  |  b  |  c  |  d  |
|---|----:|----:|----:|----:|
|AB |   12|    2|    4|    3|
|BB |    3|    3|    3|    4|


[testtest](./src/tes.png)

---

`<end>`

### Raw 

```markdown
#### testtest

- あ
- い
- う
- え: お

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

#### sample
|   |  a  |  b  |  c  |  d  |
|---|----:|----:|----:|----:|
|AB |   12|    2|    4|    3|
|BB |    3|    3|    3|    4|


[testtest](./src/tes.png)

---
```

## Usage

+ By default, results are also displayed in jupyter notebook, so if you switch off the option, let `r.rec(obj, display_notebook=False)`.

## Configuration

+ If you use `MDRec.to_html`, note that this call [Grip](https://github.com/joeyespo/grip) and github API implicitly. To set github username and password, see the link, https://github.com/joeyespo/grip#configuration.
