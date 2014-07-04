from  test_helper import *

class HtmlToHamlPyTest(unittest.TestCase):
    def test_multiple_class_names(self):
        self.assertEqual('.foo.bar.baz', tohaml.render_tag('<div class=" foo bar baz "></div>'))
if __name__ == '__main__':
    unittest.main()