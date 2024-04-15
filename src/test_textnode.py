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
        text_node_to_html_node
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

    def test_conversion(self):
        node = TextNode("This is some text", text_type_text)
        expectedLeafNode = "LeafNode(None, This is some text, None)"
        self.assertEqual(expectedLeafNode, text_node_to_html_node(node))

    def test_conversion2(self):
        node = TextNode(None, text_type_bold)
        self.assertEqual(
            "LeafNode(b, bold, None)", text_node_to_html_node(node)
        )


if __name__ == "__main__":
    unittest.main()
