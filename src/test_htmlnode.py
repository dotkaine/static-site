import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(props={"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    #LeafNode tests
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph", props={"class": "bold"})
        self.assertEqual(node.to_html(), '<p class="bold">This is a paragraph</p>')

    def test_to_html_without_tag(self):
        node = LeafNode(None, "This is a paragraph")
        self.assertEqual(node.to_html(), 'This is a paragraph')

    #ParentNode tests
    def test_to_html_with_tag_and_children(self):
        leafNode = LeafNode("p", "This is a paragraph")
        node = ParentNode(tag="div", children=[leafNode])
        self.assertEqual(node.to_html(), "<div><p>This is a paragraph</p></div>")
    
    def test_to_html_with_nested_children(self):
        leafNode2 = LeafNode("p", "Leafnode2")
        leafNode = ParentNode("span", [leafNode2])
        node = ParentNode(tag="div", children = [leafNode])
        self.assertEqual(node.to_html(), "<div><span><p>Leafnode2</p></span></div>")

if __name__ == "__main__":
    unittest.main()
