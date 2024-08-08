from parsel import Selector


class Parser:
    def __init__(self, rules, html: str) -> None:
        self.rules = rules
        self.html = html
        self.parser = Selector(text=html)

    def get(self):
        data = {}
        if "prepare" in self.rules:
            self.parser = self.parser.css(self.rules["prepare"])
        for key in self.rules:
            if key == "prepare":
                continue
            if "selector" in self.rules[key]:
                data[key] = self._get_content_by_css(self.rules[key]["selector"])
            elif "jmespath" in self.rules[key]:
                data[key] = self._get_content_by_jmespath(self.rules[key]["jmespath"])
            else:
                raise TypeError("selector not found")
        return data

    def get_rss(self):
        data = []
        articles = self.parser.css(self.rules["list"]).getall()
        for article in articles:
            item = {}
            for key in self.rules["item"]:
                item[key] = (
                    Selector(text=article)
                    .css(self.rules["item"][key]["selector"])
                    .get()
                )
            data.append(item)
        return data

    def _get_content_by_css(self, selector: str, parser=None) -> str:
        if parser is None:
            parser = self.parser
        elems = parser.css(selector).getall()
        if elems is not None and len(elems) > 0:
            return "\n".join(elems)
        return ""

    def _get_content_by_jmespath(self, selector: str) -> str:
        elems = self.parser.jmespath(selector).getall()
        if elems is not None and len(elems) > 0:
            return "\n".join(elems)
        return ""
