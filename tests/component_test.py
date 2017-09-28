import component
import unittest


class ComponentTests(unittest.TestCase):

    def test_hedding(self):
        res = component.heading("test", h=2)
        self.assertEqual(res, "## test\n\n")

    def test_enum(self):
        res = component.enum([1,2,3], numbering=True)
        self.assertEqual(res, "1. 1\n1. 2\n1. 3\n\n")

    def test_link(self):
        res = component.link("testtest", "http://google.com", newline=False)
        self.assertEqual(res, "[testtest](http://google.com)")

    def test_horizontal(self):
        res = component.horizontal()
        self.assertEqual(res, "---\n\n")

    def test_img(self):
        save_file = "./out/test_img.md"
        res = component.img(src="./out/src/test01.png", md_file = save_file, title="test", alt="sample")
        # Note that this writes file in the save_file path
        self.assertEqual(res, '''![sample](img/test01.png "test")\n\n''')

    def test_table(self):
        from pandas import DataFrame
        df = DataFrame([[12, 2, 4, 3], [3, 3, 3, 4]], columns=list("abcd"), index=["AB", "BB"])
        res = component.table(df, title="sample")
        self.assertEqual(res, df_md_sample)

df_md_sample = \
"""## sample
|   |  a  |  b  |  c  |  d  |
|---|----:|----:|----:|----:|
|AB |   12|    2|    4|    3|
|BB |    3|    3|    3|    4|


"""


if __name__ == "__main__":
    unittest.main()