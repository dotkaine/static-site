import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_to_html(self):
        node = LeafNode("This is a paragraph", "p", props={"class": "bold"})
        self.assertEqual(node.to_html(), '<p class="bold">This is a paragraph</p>')

    def test_to_html_without_tag(self):
        node = LeafNode("This is a paragraph")
        self.assertEqual(node.to_html(), 'This is a paragraph')

if __name__ == "__main__":
    unittest.main()
