import component
import unittest
from sample import df_md_sample, nested_sample, ja_sample


class ComponentTests(unittest.TestCase):

    def test_hedding(self):
        res = component.heading("test", h=2)
        self.assertEqual(res, "## test\n\n")

    def test_enum_ja(self):
        res = component.enum(["あ", "い", "う", {"え" : "お"}])
        self.assertEqual(res, ja_sample)

    def test_enum_list(self):
        res = component.enum([1,2,3])
        self.assertEqual(res, "- 1\n- 2\n- 3\n\n")

    def test_enum_dict(self):
        res = component.enum({"a" : 1, "b" : 2})
        self.assertEqual(res, "- a: 1\n  b: 2\n\n")

    def test_enum_nested(self):
        obj = [1,[1,2],[2,[3],4], [{"a": 100, "b": 234}], {"c" : [3,4,5]}]
        res = component.enum(obj)
        self.assertEqual(res, nested_sample)

    def test_line(self):
        res = component.line()
        self.assertEqual(res, "---\n\n")

    def test_url_link(self):
        res = component.link("http://google.com", text="testtest", md_dir="out", img=False)
        self.assertEqual(res, "[testtest](http://google.com)\n\n")

    def test_static_link(self):
        md_file = "./out/test.md"
        from pathlib import Path
        md_path = Path(md_file)
        res = component.link("./out/src/tes.png", text="testtest", md_dir=md_path.parent, img=False)
        self.assertEqual(res, "[testtest](src/tes.png)\n\n")


    def test_img_default_mdpath(self):
        res = component.link("./out/src/test01.png", title="test_img", text="sample")
        # Note that this writes file in the save_file path
        self.assertEqual(res, '''![sample](img/test01.png "test_img")\n\n''')

    def test_img_custom_mdpath(self):
        md_file = "./out/test.md"
        from pathlib import Path
        md_path = Path(md_file)

        res = component.link("./out/src/test01.png", text="sample", title="test_custom", md_dir=md_path.parent)
        # Note that this writes file in the save_file path
        self.assertEqual(res, '''![sample](img/test01.png "test_custom")\n\n''')


    def test_img(self):
        md_file = "./out/test_img.md"
        from pathlib import Path
        md_path = Path(md_file)

        res = component.link("../test02.png", md_dir=md_path.parent, ignore=True)
        self.assertEqual(res, '''![test02.png](img/test02.png)\n\n''')

    def test_table(self):
        from pandas import DataFrame
        df = DataFrame([[12, 2, 4, 3], [3, 3, 3, 4]], columns=list("abcd"), index=["AB", "BB"])
        res = component.table(df, title="sample")
        self.assertEqual(res, df_md_sample)

if __name__ == "__main__":
    unittest.main()


##    #res = link("./tests/out/src/tes.png", md_dir = "out", img=True) # ![tes.png](img/tes.png)
# res = link("./tests/out/src/tes.png", md_dir= "out", img=False) # [tes.png](../tests/out/src/tes.png)
