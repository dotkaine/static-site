import unittest

from markdown_formatter import extract_markdown_images, extract_markdown_links, markdown_to_blocks, block_to_block_type, block_type_paragraph, block_type_heading, block_type_code, block_type_quote, block_type_unordered_list, block_type_ordered_list

class TestMarkdownRegex(unittest.TestCase):
    def test_markdown_images(self):
        text = "This is text with an ![image](https://storage.googleapis.com/course_assets/zjjcJKZ.png) and ![another](https://storage.googleapis.com/course_assets/dfsdkjfd.png)"
        expectedOutput = [('image', 'https://storage.googleapis.com/course_assets/zjjcJKZ.png'), ('another', 'https://storage.googleapis.com/course_assets/dfsdkjfd.png')]
        self.assertEqual(expectedOutput,  extract_markdown_images(text))

    def test_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        expectedOutput = [('link', 'https://www.example.com'), ('another', 'https://www.example.com/another')]
        self.assertEqual(expectedOutput,  extract_markdown_links(text))

    def test_markdown_to_blocks(self):
        text = """This is text.

This is on another line.
This should be within the same paragraph.

        This is the final line."""
        expectedOutput = ["This is text.",
                          "This is on another line.\nThis should be within the same paragraph.",
                          "This is the final line."]
        self.assertEqual(expectedOutput,  markdown_to_blocks(text))

    def test_markdown_to_blocks_with_extra_lines(self):
        text = """This is text.

        This is on another line.


        This is the final line."""
        expectedOutput = ["This is text.", "This is on another line.", "This is the final line."]
        self.assertEqual(expectedOutput,  markdown_to_blocks(text))

    def test_block_to_block_paragraph(self):
        text = """This is text.

        This is on the final line."""
        self.assertEqual(block_type_paragraph, block_to_block_type(text))

    def test_block_to_block_heading(self):
        text = """# This is text.

        This is on the final line."""
        self.assertEqual(block_type_heading, block_to_block_type(text))

    def test_block_to_block_code(self):
        text = """```This is text.

        This is on the final line.```"""
        self.assertEqual(block_type_code, block_to_block_type(text))

    def test_block_to_block_quote(self):
        text = """>This is text.

        >This is on the final line."""
        self.assertEqual(block_type_quote, block_to_block_type(text))

    def test_block_to_block_unorderd_list_asterix(self):
        text = """* This is text.

        * This is on the final line."""
        self.assertEqual(block_type_unordered_list, block_to_block_type(text))

    def test_block_to_block_unorderd_list_hyphen(self):
        text = """- This is text.

        - This is on the final line."""
        self.assertEqual(block_type_unordered_list, block_to_block_type(text))

    def test_block_to_block_ordered_list(self):
        text = """1. This is text.

        2. This is on the final line."""
        self.assertEqual(block_type_ordered_list, block_to_block_type(text))

if __name__ == "__main__":
    unittest.main()
