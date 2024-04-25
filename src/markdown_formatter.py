import re

from htmlnode import HTMLNode

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered list"
block_type_ordered_list = "ordered list"

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def markdown_to_blocks(markdown):
    string_blocks = markdown.split("\n\n")
    stripped_strings = []
    for block in string_blocks:
        if block == "":
            continue
        block = block.strip()
        stripped_strings.append(block)
    return stripped_strings

def block_to_block_type(markdown_block):
    if (
        markdown_block.startswith("# ")
        or markdown_block.startswith("## ")
        or markdown_block.startswith("### ")
        or markdown_block.startswith("#### ")
        or markdown_block.startswith("##### ")
        or markdown_block.startswith("###### ")
    ):
        return block_type_heading
    elif markdown_block.startswith('```') and markdown_block.endswith('```'):
        return block_type_code
    lines = markdown_to_blocks(markdown_block)
    for line in lines:
        if all([line.startswith('>')]):
            return block_type_quote
        elif all([line.startswith('* ') or line.startswith('- ')]):
            return block_type_unordered_list
        elif all([line[0].isdigit()]):
            return block_type_ordered_list
    return block_type_paragraph

def paragraph_to_html_node(paragraph):
    type = block_to_block_type(paragraph)
    if type == block_type_paragraph:
        return HTMLNode('p', paragraph)
    return None
