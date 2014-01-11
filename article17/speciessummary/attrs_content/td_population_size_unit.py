# Script (Python)
# /article17/speciessummary/attrs_content/td_population_size_unit
# params: 'record, qa_errors'
## Script (Python) "td_population_size_unit"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, qa_errors
##title=
##
min_size = record['population_minimum_size'] or ''
max_size = record['population_maximum_size'] or ''
filled = record['filled_population'] or 'N/A'
size_unit = record['population_size_unit'] or 'N/A'

class_names = ['number']
title = []

if filled == 'Min':
    min_size = '(%s)' % min_size
if filled == 'Max':
    max_size = '(%s)' % max_size


if min_size or max_size:
    size_unit_value = '%s - %s' % (min_size, max_size)
else:
    size_unit_value = 'N/A'

for err in qa_errors:
    if err['FlagField'] in ['population_minimum_size', 'population_maximum_size', 'filled_population', 'population_size_unit']:
        title.append('%s: %s' % (err['FlagText'], err['suspect_value']))
        class_names.append('qa_error')

return {
    'class': ' '.join(class_names),
    'title': '<br />'.join(title),
    'content': '%s %s' % (context.str2num(size_unit_value), size_unit)
    }
