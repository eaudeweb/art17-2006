# Script (Python)
# /article17/speciesprogress/save_decision
# params: 'dict'
## Script (Python) "save_decision"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=dict
##title=
##
if dict['main_decision'] == 'A' and dict['original_decision']:
    dict['other_decisions'].append(dict['original_decision'])
else:
    dict['other_decisions'].append(dict['main_decision'])
return dict
