from django import template


class EvaluateNode(template.Node):
    html_codes = (('"', "&quot;"),)

    def __init__(self, variable):
        self.variable = template.Variable(variable)

    def unescape_symbols(self, string):
        for code in self.html_codes:
            string = string.replace(code[1], code[0])
        return string

    def render(self, context):
        content = self.unescape_symbols(self.variable.resolve(context))
        tpl = template.Template(content)
        return tpl.render(context)
