import unittest
from mdrec import MDRec
import os
from sample import ja_sample, nested_sample, df_md_sample


class MDRecTests(unittest.TestCase):

    def test_txt(self):
        save_file = "./out/test_txt.md"
        r = MDRec(save_file=save_file)

        res = r.rec("testtest", h=3, display=False)
        self.assertEqual(res, "### testtest\n\n")

        res = r.rec(["あ", "い", "う", {"え" : "お"}])
        self.assertEqual(res, ja_sample)

        res = r.rec([1,[1,2],[2,[3],4], [{"a": 100, "b": 234}], {"c" : [3,4,5]}])
        self.assertEqual(res, nested_sample)

        from pandas import DataFrame
        df = DataFrame([[12, 2, 4, 3], [3, 3, 3, 4]], columns=list("abcd"), index=["AB", "BB"])
        res = r.rec(df, title="sample")
        self.assertEqual(res, df_md_sample)

        res = r.link("../src/tes.png", text="testtest", img=False)
        self.assertEqual(res, "[testtest](../../src/tes.png)\n\n")

        self.assertTrue(os.path.exists(save_file))

    def test_img(self):
        save_file = "./out/test_img.md"
        r = MDRec(save_file=save_file)
        try:
            r.img(src="./test01.png", title="test", text="sample")
        except:
            self.assertRaises(IOError)

        res = r.img(src="./out/src/test01.png", title="test", text="sample", ignore=True)
        self.assertEqual(res, '''![sample](img/test01.png "test")\n\n''')
        r.to_html()

        self.assertTrue(os.path.exists("./out/test_img.html"))


    def test_quote(self):
        r = MDRec(save_file="tt.md")
        r.increase_quote_level()
        res = r.rec("testtest", h=2)
        self.assertEqual(res, "> ## testtest\n> \n")

        r.increase_quote_level()
        res = r.rec(list("abc"))
        self.assertEqual(res, ">> - a\n>> - b\n>> - c\n>> \n")

        r.reset_quote_level()
        res = r.rec(list("abcd"))
        self.assertEqual(res, "- a\n- b\n- c\n- d\n\n")

        r.to_html()

if __name__ == "__main__":
    unittest.main()
