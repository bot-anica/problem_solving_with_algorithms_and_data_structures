# 11. Другой пример, в котором может возникнуть проблема соответствия скобок,
# приходит из гипертекстового языка разметки (или HTML).
# В HTML у каждого тега существуют открывающая и закрывающая формы,
# которые должны быть сбалансированы, чтобы адекватно описывать веб-документ.
#
# Вот пример очень простого веб-документа:
#
# <html>
#    <head>
#       <title>
#          Example
#       </title>
#    </head>
#
#    <body>
#       <h1>Hello, world</h1>
#    </body>
# </html>

from data_structures import Stack


def validate_html(html: str):
    html_lines = html.split("\n")

    for i in range(len(html_lines)):
        html_lines[i] = html_lines[i].strip()

    # Некоторые строки могут содержать и открывающий и закрывающий теги,
    # поэтому для удобства минимизирую html, приведя его в 1 строку
    minified_html = "".join(html_lines)

    tag_stack = Stack()

    prev_spec_symbol = ''
    current_tag = ''

    for i in range(len(minified_html)):
        if minified_html[i] == "<":
            prev_spec_symbol = "<"
        elif prev_spec_symbol == "<" and minified_html[i] == ">":
            if current_tag:
                tag_stack.push(current_tag)
                current_tag = ""
                prev_spec_symbol = ""
            else:
                raise ValueError(f"HTML has empty open tag <>")
        elif prev_spec_symbol == "<" and minified_html[i] == "/":
            prev_spec_symbol = "/"
        elif prev_spec_symbol == "/" and minified_html[i] != ">":
            current_tag += minified_html[i]
        elif prev_spec_symbol == "/" and minified_html[i] == ">":
            if current_tag:
                if tag_stack.peek() == current_tag:
                    current_tag = ""
                    tag_stack.pop()
                else:
                    raise ValueError(f"HTML includes {tag_stack.peek()} open tag and next one {current_tag} close tag")
            else:
                raise ValueError(f"HTML has empty close tag </>")
        elif prev_spec_symbol in ["<", "/"] and not minified_html[i] in "/>":
            current_tag += minified_html[i]

    return tag_stack.is_empty()


html_as_text = """
<html>
   <head>
      <title>
         Example
      </title>
   </head>

   <body>
      <h1>Hello, world</h1>
   </body>
</html>
"""

print(validate_html(html_as_text))