from  test_helper import *

class HtmlToHamlPyTest(unittest.TestCase):
    def test_multiple_class_names(self):
        self.assertEqual('.foo.bar.baz', tohaml.render('<div class=" foo bar baz "></div>'))
    def test_id_with_dot_and_hash(self):
        self.assertEqual('%div{id:"foo.bar"}', tohaml.render("<div id='foo.bar'></div>"))
        self.assertEqual('%div{id:"foo#bar"}', tohaml.render("<div id='foo#bar'></div>"))
if __name__ == '__main__':
    unittest.main()