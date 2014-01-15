# Script (Python)
# /article17/speciessummary/attrs_content/td_habitat_complementary_suitable
# params: 'record, qa_errors'
## Script (Python) "td_habitat_complementary_suitable"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, qa_errors
##title=
##
class_names = ['number', 'section-border']
title = []

for err in qa_errors:
    if err['FlagField'] == 'complementary_suitable_habitat':
        title.append('%s: %s' % (err['FlagText'], err['suspect_value']))
        class_names.append('qa_error')

return {
    'class': ' '.join(class_names),
    'title': '<br />'.join(title),
    'content': context.str2num(record['complementary_suitable_habitat'])
    }
