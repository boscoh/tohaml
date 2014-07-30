from  test_helper import *

class HtmlToHamlPyTest(unittest.TestCase):
    def test_no_tag_name_for_div_if_class_or_id_is_present(self):
        self.assertEqual('#foo', render('<div id="foo"> </div>'))
        self.assertEqual('.foo', render('<div class="foo"> </div>'))
    def test_multiple_class_names(self):
        self.assertEqual('.foo.bar.baz', render('<div class=" foo bar baz "></div>'))
    def test_should_have_pretty_attributes(self):
        self.assertEqual('%input{type:"text",name:"login"}', render('<input type="text" name="login" />'))
        self.assertEqual('%meta{content:"text/html",http-equiv:"Content-Type"}', render('<meta http-equiv="Content-Type" content="text/html" />'))
    def test_id_with_dot_and_hash(self):
        self.assertEqual('%div{id:"foo.bar"}', render("<div id='foo.bar'></div>"))
        self.assertEqual('%div{id:"foo#bar"}', render("<div id='foo#bar'></div>"))
    def test_class_with_dot_and_hash(self):
        self.assertEqual('%div{class:"foo.bar"}', render("<div class=' foo.bar '></div>"))
        self.assertEqual('%div{class:"foo#bar"}', render("<div class=' foo#bar '></div>"))
        self.assertEqual('.foo.bar{class:"foo#bar foo.bar"}', render("<div class='foo foo#bar bar foo.bar'></div>"))
    def test_self_closing_tag(self):
        self.assertEqual("%img", render("<img />"))
    def test_inline_text(self):
        #FIXME
        self.assertEqual("%p\n  foo", render("<p>foo</p>"))
if __name__ == '__main__':
    unittest.main()
