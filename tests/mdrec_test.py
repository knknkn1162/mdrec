import unittest
from mdrec import MDRec
import os
from sample import ja_sample, nested_sample


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

        res = r.link("../src/tes.png", text="testtest", img=False)
        self.assertEqual(res, "[testtest](../../src/tes.png)\n\n")


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


if __name__ == "__main__":
    unittest.main()
