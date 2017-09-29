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


    def test_img(self):
        save_file = "./out/test_img.md"
        r = MDRec(save_file=save_file)
        r.img(src="./out/src/test01.png", title="test", alt="sample", ignore=True)

        r.to_html()

        self.assertTrue(os.path.exists("./out/test_img.html"))


if __name__ == "__main__":
    unittest.main()
