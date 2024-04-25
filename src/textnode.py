from htmlnode import LeafNode
from markdown_formatter import extract_markdown_images, extract_markdown_links

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text , text_type, url=None):
        self.text = text 
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text 
        and self.text_type == other.text_type 
        and self.url == other.url)

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    if text_node.text_type == text_type_text:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    elif text_node.text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    elif text_node.text_type == text_type_code:
        return LeafNode("code", text_node.text)
    elif text_node.text_type == text_type_link:
        return LeafNode("a", text_node.text, { 'href':  text_node.url })
    elif text_node.text_type == text_type_image:
        return LeafNode("img", None, { 'src': text_node.url, 'alt': text_node.text })
    else:
        raise Exception("Unexpected type")
        
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue    
        split_nodes = []
        nodes = old_node.text.split(delimiter)
        if len(nodes) % 2 == 0:
            raise ValueError(f"Unmatched {delimiter} in text.")
        for i in range(len(nodes)):
            if nodes[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(nodes[i], text_type_text))
            else:
                split_nodes.append(TextNode(nodes[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        images = extract_markdown_images(text)
        if len(images) == 0:
            new_nodes.append(old_node)
            continue
        for image in images:
            node = text.split(f"![{image[0]}]({image[1]})", 1)
            if len(node) != 2:
                raise ValueError("Invalid markdown, image not closed")
            if node[0] != "":
                new_nodes.append(TextNode(node[0], text_type_text))
            new_nodes.append(TextNode(image[0], text_type_image, image[1]))
            text = node[1]
        if text != "":
            new_nodes.append(TextNode(text, text_type_text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        text = old_node.text
        links = extract_markdown_links(text)
        if len(links) == 0:
            new_nodes.append(old_node)
            continue
        for link in links:
            node = text.split(f"[{link[0]}]({link[1]})", 1)
            if len(node) != 2:
                raise ValueError("Invalid markdown, link section closed")
            if node[0] != "":
                new_nodes.append(TextNode(node[0], text_type_text))
            new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            text = node[1]
        if text != "":
            new_nodes.append(TextNode(text, text_type_text))
    return new_nodes

def text_to_textnodes(text):
    new_node = [TextNode(text, text_type_text)]
    new_node = split_nodes_delimiter(new_node, "**", text_type_bold)
    new_node = split_nodes_delimiter(new_node, "*", text_type_italic)
    new_node = split_nodes_delimiter(new_node, "`", text_type_code)
    new_node = split_nodes_image(new_node)
    new_node = split_nodes_link(new_node)
    return new_node
