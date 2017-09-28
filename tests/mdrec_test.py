import unittest
from pandas import DataFrame
from mdrec import MDRec

class MDRecTests(unittest.TestCase):

    def test_hedding(self):
        res = MDRec.heading("test", h=2)
        self.assertEqual(res, "## test\n\n")

    def test_enum(self):
        res = MDRec.enum([1,2,3], numbering=True)
        self.assertEqual(res, "1. 1\n1. 2\n1. 3\n\n")

    def test_horizontal(self):
        res = MDRec.horizontal()
        self.assertEqual(res, "---\n\n")

    def test_img(self):
        save_file = "./out/test_img.md"
        r = MDRec(save_file=save_file)
        res = r.img(src="./out/src/test01.png", title="test", alt="sample")
        # Note that this writes file in the save_file path
        self.assertEqual(res, '''![sample](img/test01.png "test")\n\n''')


    def test_img_with_ignore(self):
        save_file = "./out/test_ignore.md"
        r = MDRec(save_file=save_file)
        res = r.rec_img(src="./dummy/tes.png", title="test", alt="sample", ignore=True)
        # Note that this writes file in the save_file path
        self.assertEqual(res, '''![sample](img/tes.png "test")\n\n''')


    def test_table(self):
        df = DataFrame([[12, 2, 4, 3], [3, 3, 3, 4]], columns=list("abcd"), index=["AB", "BB"])
        res = MDRec.table(df, title="sample")
        self.assertEqual(res, df_md_sample)

    def test_non_name(self):
        r = MDRec()
        res = r.rec_img(src="./out/src/test02.png", title="test", alt="sample")
        # Note that this writes file in the save_file path
        self.assertEqual(res, '''![sample](img/test02.png "test")\n\n''')



df_md_sample = \
"""## sample
|   |  a  |  b  |  c  |  d  |
|---|----:|----:|----:|----:|
|AB |   12|    2|    4|    3|
|BB |    3|    3|    3|    4|


"""

if __name__ == "__main__":
    unittest.main()
