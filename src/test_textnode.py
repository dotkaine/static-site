import unittest

from htmlnode import LeafNode
from textnode import (
        TextNode,
        text_type_text,
        text_type_bold,
        text_type_italic,
        text_type_code,
        text_type_link,
        text_type_image,
        text_node_to_html_node,
        split_nodes_delimiter
)

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", text_type_bold, "google.com")
        node2 = TextNode("This is a text node", text_type_bold, "google.com")
        self.assertEqual(node, node2)

    def test_eq_with_url(self):
        node = TextNode("This is a text node", text_type_bold, None)
        node2 = TextNode("This is a text node", text_type_bold, None)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", text_type_bold)
        node2 = TextNode("This is not equal", text_type_bold)
        self.assertNotEqual(node, node2)

    def test_repr(self):
        node = TextNode("This is a text node", text_type_bold, "https://www.boot.dev")
        self.assertEqual(
            "TextNode(This is a text node, bold, https://www.boot.dev)", repr(node)
        )

    def test_conversion_text(self):
        node = TextNode("This is some text", text_type_text)
        expectedLeafNode = LeafNode(None, "This is some text", None)
        self.assertEqual(expectedLeafNode, text_node_to_html_node(node))

    def test_conversion_bold(self):
        node = TextNode("This is bold", text_type_bold)
        expectedLeafNode = LeafNode("b", "This is bold", None) 
        self.assertEqual(expectedLeafNode, text_node_to_html_node(node))

    def test_conversion_italic(self):
        node = TextNode("This is italic", text_type_italic)
        expectedLeafNode = LeafNode("i", "This is italic", None) 
        self.assertEqual(expectedLeafNode, text_node_to_html_node(node))

    def test_conversion_code(self):
        node = TextNode("This is some code", text_type_code)
        expectedLeafNode = LeafNode("code", "This is some code", None) 
        self.assertEqual(expectedLeafNode, text_node_to_html_node(node))

    def test_conversion_link(self):
        node = TextNode("This is a link", text_type_link, "http://test.com")
        expectedLeafNode = LeafNode("a", "This is a link", {'href': 'http://test.com'}) 
        self.assertEqual(expectedLeafNode, text_node_to_html_node(node))

    def test_conversion_image(self):
        node = TextNode("An example image", text_type_image, 'http://example.com/image.jpg')
        expectedLeafNode = LeafNode("img", None, {'src': 'http://example.com/image.jpg', 'alt': 'An example image' }) 
        self.assertEqual(expectedLeafNode, text_node_to_html_node(node))

    def test_node_delimiter_code(self):
        node = TextNode("An example `code block`", text_type_text)
        expectedLeafNode = [
            TextNode("An example ", text_type_text),
            TextNode("code block", text_type_code),
        ]
        self.assertEqual(expectedLeafNode, split_nodes_delimiter([node], '`', text_type_code))

    def test_node_delimiter_italic(self):
        node = TextNode("An example piece of *italic text*", text_type_text)
        expectedLeafNode = [
            TextNode("An example piece of ", text_type_text),
            TextNode("italic text", text_type_italic),
        ]
        self.assertEqual(expectedLeafNode, split_nodes_delimiter([node], "*", text_type_italic))

    def test_node_delimiter_bold(self):
        node = TextNode("An example piece of **bold text**", text_type_text)
        expectedLeafNode = [
            TextNode("An example piece of ", text_type_text),
            TextNode("bold text", text_type_bold),
        ]
        self.assertEqual(expectedLeafNode, split_nodes_delimiter([node], "**", text_type_bold))

    def test_node_delimiter_invalid_markdown(self):
        node = TextNode("An example piece of *italic text", text_type_text)
        expectedLeafNode = [
            TextNode("An example piece of ", text_type_text),
            TextNode("italic text", text_type_italic),
        ]
        self.assertEqual(expectedLeafNode, split_nodes_delimiter([node], "*", text_type_italic))

if __name__ == "__main__":
    unittest.main()
