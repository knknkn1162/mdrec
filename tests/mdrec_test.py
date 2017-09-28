import unittest
from mdrec import MDRec
import os

class MDRecTests(unittest.TestCase):


    def test_img(self):
        save_file = "./out/test.md"
        r = MDRec(save_file=save_file)
        r.img(src="./out/src/test01.png", title="test", alt="sample", ignore=True)

        r.export_html()

        self.assertTrue(os.path.exists("./out/test.html"))


if __name__ == "__main__":
    unittest.main()
