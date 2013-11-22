#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2013, Bosco Ho. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright
# notice, this list of conditions and the following disclaimer in the
# documentation and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import print_function, division, unicode_literals

import sys
import os
import codecs
from htmlentitydefs import codepoint2name

import bs4


def read_text(fname):
  "Reads in utf-8 encoding (includes ascii)"
  with codecs.open(fname, encoding='utf-8') as f:
    text = f.read()
  return text


def write_text(fname, text):
  "Writes text to file in utf-8 and creates directory if needed."
  dirname = os.path.dirname(fname)
  if dirname and not os.path.isdir(dirname):
    os.makedirs(dirname)
  with codecs.open(fname, 'w', encoding='utf-8') as f:
    f.write(text)


def is_tag(elem):
  return isinstance(elem, bs4.element.Tag)


def attr_str(attrs):
  if not attrs:
    return ''
  pieces = []
  for key, val in attrs.items():
    piece = key + ':'
    if isinstance(val, list):
      piece += '\'{}\''.format(' '.join(val))
    else:
      piece += repr(val)
    pieces.append(piece)
  s = '{'
  s += ','.join(pieces)
  s += '}'
  return s


def is_outer_nospace(elem):
  prev_nospace = False
  prev = elem.previous_sibling
  if is_tag(prev) or unicode(prev)[-1] != ' ':
    prev_nospace = True

  next_nospace = False
  next = elem.next_sibling
  if is_tag(next) or unicode(next)[0] != ' ':
    next_nospace = True

  result = prev_nospace and next_nospace
  return result


def is_inner_nospace(elem):
  if len(elem.contents) == 0:
    return True

  first_nospace = False
  first = elem.contents[0]
  if is_tag(first) or unicode(first)[0] != ' ':
    first_nospace = True

  last_nospace = False
  last = elem.contents[-1]
  if is_tag(last) or unicode(last)[-1] != ' ':
    last_nospace = True

  result = first_nospace and last_nospace
  return result


def print_tag(indent_str, elem, stream):
  attrs = elem.attrs
  name = elem.name
  if name == 'style':
    print(indent_str, ':css', file=stream, sep='')
    return
  tag = ''
  if name == 'div':
    if 'id' in attrs:
      tag = '#' + attrs['id']
      del attrs['id']
    if 'class' in attrs:
      for attr_class in attrs['class']:
        tag += '.' + attr_class
      del attrs['class']
  if tag == '':
    tag = '%' + name
  tag += attr_str(attrs)
  if elem.name in ['a', 'span', 'strong', 'em']:
    if is_outer_nospace(elem):
      tag += '>'
    if is_inner_nospace(elem):
      tag += '<'
  print('{}{}'.format(indent_str, tag), file=stream, sep='')


def replace_reserved_first_char(text):
  for i in range(len(text)):
    if text[i] != ' ':
      i_first = i
      break
  else:
    return text
  pairs = [('-', '&minus;'), ('%', '&#37;'), ('#', '%#35')]
  for char, entity in pairs:
    if text[i_first] == char:
      text = text[:i_first] + entity + text[i_first+1:]
  return text


def indented_string(indent, text, full_width=80):
  width = full_width - indent
  lines = text.splitlines()
  result = ''
  for line in lines:
    words = line.split()
    print_line = ''
    line_indent = len(line) - len(line.lstrip())
    print_line += ' '*line_indent
    for word in words:
      if print_line:
        add_word = print_line + ' ' + word
      else:
        add_word = word
      if len(add_word) < full_width:
        print_line = add_word
      else:
        result += ' '*indent + print_line + '\n'
        print_line = word
    if print_line:
      result += ' '*indent + print_line + '\n'
  return result


def clean_quotes(html):
  if html == '&ldquo;' or html == '&rdquo;':
    return '"'
  if html in ['&lsquo;', '&rsquo;', '&sbquo;', '&prime;']:
    return '\''
  if html in ['&hellip;']:
    return '...'
  return html


def unicode_to_entities(text):
  """
  Identifies unicode characters that can be converted to
  HTML-safe html-entities. Also translates smart single and
  double quotes into normal double and single quotes, and 
  turns ellipses into three full-stops.
  """
  new_lines = []
  for line in text.splitlines():
    pieces = []
    for ch in line:
      codepoint = ord(ch)
      if codepoint > 128:
        if codepoint in codepoint2name:
          html = '&' + codepoint2name[codepoint] + ';'
          html = clean_quotes(html)
          pieces.append(html)
        else:
          html = '&#{0};'.format(codepoint)
          pieces.append(html)
      else:
        pieces.append(ch)
    new_lines.append(''.join(pieces))
  return "\n".join(new_lines)


def print_elem(indent, elem, stream):
  indent_str = ' '*indent
  if is_tag(elem):
    print_tag(indent_str, elem, stream)
    for child_elem in elem.contents:
      print_elem(indent+2, child_elem, stream)
  else:
    # navigable string or comment
    raw_string = unicode(elem)
    clean_string = replace_reserved_first_char(raw_string)
    clean_string = unicode_to_entities(clean_string)    
    print_string = indented_string(indent, clean_string)
    if print_string.strip():
      print(print_string, file=stream, end='')


def print_haml(html, stream=sys.stdout):
  html_text = read_text(html)
  soup = bs4.BeautifulSoup(html_text)
  print_elem(0, soup.html, stream)




