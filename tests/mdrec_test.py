import unittest
from pandas import DataFrame
from mdrec import MDRec

class MDRecTests(unittest.TestCase):

    def test_rec(self):

        save_file = "./out/test.md"
        r = MDRec(save_file=save_file)

        res = r.rec("test", h=1)
        newline = "\n\n"
        self.assertEqual(res, "# test"+newline)

        msg = "teststeststests"
        res = r.rec(msg)
        self.assertEqual(res, msg + newline)

        res = r.rec(["bbbi", "ddn", 3])
        self.assertEqual(res, "+ bbbi{}+ ddn{}+ 3{}".format(newline, newline, newline))

        r.img2md(src="./out/img/test01.png")
        # display_test
        df = DataFrame([[12, 2, 4, 3], [3, 3, 3, 4]], columns=list("abcd"), index=["AB", "BB"])
        r.rec(df, title="sample")

        r.to_html()


    def test_img(self):
        save_file = "./out/test.md"
        r = MDRec(save_file=save_file)

        r.img2md("./out/img/test01.png", embeded=True)

        r.to_html()

if __name__ == "__main__":
    unittest.main()
