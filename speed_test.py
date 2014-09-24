import re
import timeit

def get_element_class_00(attrs):
  if 'class' in attrs:
    tag = ''
    for attr_class in filter(lambda x: len(x) > 0 and not re.match(r'.*[#|\.].*', x), attrs['class']):
      tag += '.' + attr_class
    if any(map(lambda c: re.match(r'.*[#|\.].*', c), attrs['class'])):
       attrs['class'] = filter(lambda x: re.match(r'.*[#|\.].*', x), attrs['class'])
    else:
      del attrs['class']
    return tag
  return ''    


def get_element_class_01(attrs):
  if 'class' in attrs:
    re_comp = re.compile(r'.*[#|\.].*')
    tag = ''
    for attr_class in filter(lambda x: len(x) > 0 and not re_comp.match(x), attrs['class']):
      tag += '.' + attr_class
    if any(map(lambda c: re_comp.match(c), attrs['class'])):
       attrs['class'] = filter(lambda x: re_comp.match(x), attrs['class'])
    else:
      del attrs['class']
    return tag
  return ''


def get_element_class_02(attrs):
  if 'class' in attrs:
    tag = ''
    for attr_class in filter(lambda x: len(x) > 0 and not re.match(r'.*[#\.].*', x), attrs['class']):
      tag += '.' + attr_class
    if any(map(lambda c: re.match(r'.*[#\.].*', c), attrs['class'])):
       attrs['class'] = filter(lambda x: re.match(r'.*[#\.].*', x), attrs['class'])
    else:
      del attrs['class']
    return tag
  return ''    


def get_element_class_03(attrs):
  if 'class' in attrs:
    tag = ''
    check = ('#', '.')
    bad_class_names = [j for i in check for j in attrs['class'] if i in j]
    for attr_class in filter(lambda x: len(x) > 0 and x not in bad_class_names, attrs['class']):
      tag += '.' + attr_class
    if len(bad_class_names):
       attrs['class'] = bad_class_names
    else:
      del attrs['class']
    return tag
  return ''


def get_element_class_04(attrs):
  if 'class' in attrs:
    tag = ''
    for attr_class in filter(lambda x: len(x) > 0 and not re.match(r'.*(?:#|\.|\{\{|\{%).*', x), attrs['class']):
      tag += '.' + attr_class
    if any(map(lambda c: re.match(r'.*(?:#|\.|\{\{|\{%).*', c), attrs['class'])):
       attrs['class'] = filter(lambda x: re.match(r'.*(?:#|\.|\{\{|\{%).*', x), attrs['class'])
    else:
      del attrs['class']
    return tag
  return ''


def get_element_class_05(attrs):
  if 'class' in attrs:
    re_comp = re.compile(r'.*(?:#|\.|\{\{|\{%).*')
    tag = ''
    for attr_class in filter(lambda x: len(x) > 0 and not re_comp.match(x), attrs['class']):
      tag += '.' + attr_class
    if any(map(lambda c: re_comp.match(c), attrs['class'])):
       attrs['class'] = filter(lambda x: re_comp.match(x), attrs['class'])
    else:
      del attrs['class']
    return tag
  return ''


def get_element_class_06(attrs):
  if 'class' in attrs:
    tag = ''
    check = ('#', '.', '{{', '{%')
    bad_class_names = [j for i in check for j in attrs['class'] if i in j]
    for attr_class in filter(lambda x: len(x) > 0 and x not in bad_class_names, attrs['class']):
      tag += '.' + attr_class
    if len(bad_class_names):
       attrs['class'] = bad_class_names
    else:
      del attrs['class']
    return tag
  return ''

CHECK = ('#', '.', '{{', '{%')

def get_element_class_07(attrs):
  if 'class' in attrs:
    tag = ''
    bad_class_names = (j for i in CHECK for j in attrs['class'] if i in j)
    for attr_class in filter(lambda x: len(x) > 0 and x not in bad_class_names, attrs['class']):
      tag += '.' + attr_class
    bad_class_names = list(bad_class_names)
    if len(bad_class_names):
       attrs['class'] = list(bad_class_names)
    else:
      del attrs['class']
    return tag
  return ''

RE_COMP = re.compile(r'.*[#|\.].*')

def get_element_class_08(attrs):
  if 'class' in attrs:
    tag = ''
    for attr_class in filter(lambda x: len(x) > 0 and not RE_COMP.match(x), attrs['class']):
      tag += '.' + attr_class
    if any(map(lambda c: RE_COMP.match(c), attrs['class'])):
       attrs['class'] = filter(lambda x: RE_COMP.match(x), attrs['class'])
    else:
      del attrs['class']
    return tag
  return ''

RE_COMP2 = re.compile(r'.*(?:#|\.|\{\{|\{%).*')

def get_element_class_09(attrs):
  if 'class' in attrs:
    tag = ''
    for attr_class in filter(lambda x: not RE_COMP2.match(x), attrs['class']):
      tag += '.' + attr_class
    if any(map(lambda c: RE_COMP2.match(c), attrs['class'])):
       attrs['class'] = filter(lambda x: RE_COMP2.match(x), attrs['class'])
    else:
      del attrs['class']
    return tag
  return ''
  
#attrs = {'class': ['cls1', "{% cycle 'odd' 'even' %}", "cls.2", 'cls3', 'c#ls4', '{{ cls5 }}', 'cls6_with_log_name_to_check_does_it_hurts_or_not?', 'cls7', 'cls7', 'cls7', 'cls7', 'cls7', 'cls7', 'cls7', 'cls7', 'cls7', 'cls7']}
#
# Results:
#
# get_element_class_09(attrs): 00000000000.10148000717163085938
# get_element_class_08(attrs): 00000000000.10403800010681152344
# get_element_class_07(attrs): 00000000000.18428802490234375000
# get_element_class_03(attrs): 00000000001.17161202430725097656
# get_element_class_06(attrs): 00000000001.42884802818298339844
# get_element_class_01(attrs): 00000000004.11601805686950683594
# get_element_class_05(attrs): 00000000004.17100691795349121094
# get_element_class_02(attrs): 00000000006.54944682121276855469
# get_element_class_00(attrs): 00000000006.56750798225402832031
# get_element_class_04(attrs): 00000000006.64313292503356933594

# attrs = {'class': ['cls1']}
#
# Results:
#
# get_element_class_08(attrs): 00000000000.10082101821899414062
# get_element_class_04(attrs): 00000000000.10089898109436035156
# get_element_class_09(attrs): 00000000000.10171818733215332031
# get_element_class_02(attrs): 00000000000.10249805450439453125
# get_element_class_00(attrs): 00000000000.10443401336669921875
# get_element_class_01(attrs): 00000000000.14670896530151367188
# get_element_class_05(attrs): 00000000000.14689993858337402344
# get_element_class_03(attrs): 00000000000.14864897727966308594
# get_element_class_06(attrs): 00000000000.14908695220947265625
# get_element_class_07(attrs): 00000000000.17654490470886230469

#attrs = {'class': ['cls.4']}
#
# Results:
#
# get_element_class_09(attrs): 00000000000.10305905342102050781
# get_element_class_08(attrs): 00000000000.10341691970825195312
# get_element_class_07(attrs): 00000000000.17693901062011718750
# get_element_class_03(attrs): 00000000001.00884008407592773438
# get_element_class_06(attrs): 00000000001.17103600502014160156
# get_element_class_01(attrs): 00000000002.91070699691772460938
# get_element_class_05(attrs): 00000000002.96019983291625976562
# get_element_class_02(attrs): 00000000003.81945681571960449219
# get_element_class_04(attrs): 00000000003.84111118316650390625
# get_element_class_00(attrs): 00000000003.84169507026672363281

if __name__ == '__main__':
    times_to_run = 1000000
    test_number = 10
    times = [(i, timeit.Timer('get_element_class_%02d(attrs)' % i, 'from __main__ import attrs, get_element_class_%02d' % i).timeit(times_to_run)) for i in xrange(test_number)]
    sorted_times = sorted(times, key=lambda i: i[1])

    for i, time in sorted_times:
        print 'get_element_class_{0:02d}(attrs): {1:032.020f}'.format(i, time)
