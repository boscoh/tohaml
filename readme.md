
# tohaml

An HTML to HAML converter, targeting the Python HamlPy compiler.

## Installation

To install:

    >> pip install tohaml

The only dependency is BeautifulSoup4 if you install it yourself:

    >> python setup.py install

## Usage

If you've downloaded an HTML file `index.html` then 

    >> tohaml index.html 

will output to screen; and

    >> tohaml index.html index.haml

will write to `index.haml`.

In Python scripts, let's say you already have `index.html`:

    ```python
    import tohaml
    import StringIO

    html = 'index.html'
    output = StringIO.StringIO()
    tohaml.print_haml(html, stream=output)
    print output.getvalue()
    ```

## Flavor of HAML

There are a few different varieties of HAML. `tohaml` targets the variety used by the python [HamlPy compiler](https://github.com/jessemiller/HamlPy).

In particular, CSS and Javascript are preserved in indented blocks using the `:css` and `:javascript` tags. As well, tag attributes are stored in the `{}` notation of Python dictionaries.

Unicode characters are automatically escaped into HTML entities.

Alas, due to the nature of HAML, not all white-space between tags can be faithfully interpreted: either white space between both start/close tags, or no spaces at all.

Copyright (c) 2013 Bosco Ho.

