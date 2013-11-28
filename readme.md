
# tohaml

converts HTML to HAML for the HamlPy compiler

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

Alternatively, for shits and giggles, `tohaml` can fetch straight from a URL:

    >> tohaml http://python.org python.html

If you want to work this into a workflow in Python scripts, then, let's say you already have `index.html`:

    import StringIO
    import codecs

    import tohaml

    # read unicode characters - covers most cases :/
    in_stream = codecs.open('index.html', encoding='utf-8')

    out_stream = StringIO.StringIO()
    tohaml.print_haml(in_stream, out_stream)
    print out_stream.getvalue()

## This flavor of HAML

There are a few different varieties of HAML, of which, `tohaml` targets the variety used by the python [HamlPy compiler](https://github.com/jessemiller/HamlPy).

In particular, `<style>` elements are preserved in indented blocks using the `:css` filter. As well, tag attributes are stored in the `{}` notation of Python dictionaries.

Unicode characters are automatically escaped into HTML entities. A couple of characters that are crucial to HamlPy (`-`, `#`, `%`) are also escaped if they are at the beginning of a block.

Alas, due to the nature of HAML, not all white-space between tags can be faithfully interpreted: either white space are inserted between both start/close tags, or no spaces at all.

## Future Ideas

- some examples

Copyright (c) 2013 Bosco Ho. 

