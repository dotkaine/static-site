class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        if self.props is None:
            return ""
        attributes = []
        if self.props:
            for key, value in self.props.items():
                attributes.append(f' {key}="{value}"')
        return ''.join(attributes)


    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def __eq__(self, other):
        return (self.tag == other.tag 
        and self.value == other.value
        and self.props == other.props)

    def to_html(self):
        if not self.value:
            raise ValueError("Value required")
        if self.tag is None:            
            return self.value
        return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'

    def __repr__(self):
        return f'LeafNode({self.tag}, {self.value}, {self.props})'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if not self.tag:
            raise ValueError("Tag required")
        if not self.children:
            raise ValueError("Children required")
        htmlString = ""
        for child in self.children:
            htmlString += child.to_html()
        return f'<{self.tag}{self.props_to_html()}>{htmlString}</{self.tag}>'
    
    def __repr__(self):
        return f'ParentNode({self.tag}, children: {self.children}, {self.props}'
