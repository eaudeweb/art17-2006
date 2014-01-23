# Script (Python)
# /article17/speciesreport/attrs_content/td_population_complementary_favourable
# params: 'record, qa_errors'
## Script (Python) "td_population_complementary_favourable"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, qa_errors
##title=
##
population_q = record['complementary_favourable_population_q'] or ''
population = record['complementary_favourable_population']
filled = record['filled_complementary_favourable_population'] or ''

class_names = ['number', 'section-border']
title = []

for err in qa_errors:
    if err['FlagField'] in ['complementary_favourable_population_q', 'complementary_favourable_population', 'filled_complementary_favourable_population']:
        title.append('%s: %s' % (err['FlagText'], err['suspect_value']))
        class_names.append('qa_error')

if filled:
    if population_q or population:
        content = '%s(%s)' % (population_q, context.str2num(population, ''))
    else:
        content = 'N/A'
else:
    if population_q or population:
        content = '%s%s' % (population_q, context.str2num(population, ''))
    else:
        content = 'N/A'

return {'class': ' '.join(class_names), 'title': '<br />'.join(title), 'content': content}
