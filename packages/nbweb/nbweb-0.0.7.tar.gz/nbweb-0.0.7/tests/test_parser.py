from nbweb.parser import Parser


def test_parser() -> None:
    html = """
    <html>
        <body>
            <h1>dummy title</h1>
            <div class="article-content">
                <p>line 1</p>
                <p>line 2</p>
            </div>
            <img data-src="dummy-src">
        </body>
    </html>"""
    rules = {
        "title": {"selector": "h1::text"},
        "img": {"selector": "img::attr(data-src)"},
        "content": {"selector": "div.article-content > p::text"},
    }
    p = Parser(rules, html)
    data = p.get()

    assert data is not None
    assert len(data) == 3
    assert "title" in data
    assert "content" in data
    assert data["title"] == "dummy title"
    assert data["content"] == "line 1\nline 2"
    assert data["img"] == "dummy-src"


def test_parser_rss():
    html = """
    <html>
    <body>
        <ul class="articles">
            <li><a href="/link#1">article 1</a></li>
            <li><a href="/link#2">article 2</a></li>
            <li><a href="/link#3">article 3</a></li>
        </ul>
    </body>
    </html>
    """
    rules = {
        "list": "ul.articles > li",
        "item": {
            "title": {"selector": "a::text"},
            "link": {"selector": "a::attr(href)"},
        },
    }
    p = Parser(rules, html)
    data = p.get_rss()
    assert data is not None
    assert len(data) == 3
    assert data[0]["title"] == "article 1"
    assert data[0]["link"] == "/link#1"
    assert data[1]["title"] == "article 2"
    assert data[1]["link"] == "/link#2"
    assert data[2]["title"] == "article 3"
    assert data[2]["link"] == "/link#3"
