import unittest
import tohaml
import io
import bs4
def render(string):
  output = io.StringIO()
  soup  = bs4.BeautifulSoup(string)
  for child in soup.children:
    tohaml.print_elem(0, child, output)
  return output.getvalue().rstrip('\n')
