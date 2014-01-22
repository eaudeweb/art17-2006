# Script (Python)
# /article17/speciesprogress/save_conclusion
# params: 'dict, decision, record, conclusion_type'
## Script (Python) "save_conclusion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=dict, decision, record, conclusion_type
##title=
##
if conclusion_type == 'conclusion_assessment':
    if record['method'] == 'MTX':
        dict['method'] = record['method_range']
    else:
        dict['method'] = record['method']
else:
    dict['method'] = record['method']
dict['main_decision'] = decision
dict['original_decision'] = record['decision']
dict['colour'] = record['conclusion']
#dict['method'] = record['method']
dict['overall'] = record['method_assessment']
dict['user'] = record['user']
dict['group'] = context.string_encode(record['group'])
dict['species'] = context.string_encode(record['assesment_speciesname'])
dict['region'] = record['region']
dict['method_details'] = record['method_details']
dict['decision_details'] = record['decision_details']


return dict
