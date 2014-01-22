# Script (Python)
# /article17/habitatsprogress/process_conclusions
# params: 'conclusion_type, group'
## Script (Python) "process_conclusions"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=conclusion_type, group
##title=
##
from Products.PythonScripts.standard import html_quote
request = container.REQUEST
RESPONSE =  request.RESPONSE

#CONSTANTS 
USER_MAXIM = 'maximiur'
USER_IURIE = 'iurieetcbd'


output = {}
records = context.sql_methods.select_habitat_conclusions(conclusion=conclusion_type, group=group)

for record in records:
    #loading...
    habitat = record['habitatcode']
    region = record['reg_code']
    decision = record['decision']
    conclusion = record['conclusion']
    method = record['method']
    overall = record['method_assessment']
    user = record['user']

    if not output.has_key(habitat):
        #initialize
        output[habitat] = {'ALP':{}, 'ATL':{}, 'BOR':{}, 'CON':{}, 'MAC':{}, 'MED':{}, 'PAN':{}, 'MATL':{}, 'MBAL':{}, 'MMAC':{}, 'MMED':{}}

    dict = output[habitat][region]

    if not dict.has_key('main_decision'):
        dict['main_decision'] = ''
    if not dict.has_key('original_decision'):
        dict['original_decision'] = ''
    if not dict.has_key('method'):
        dict['method'] = ''
    if not dict.has_key('overall'):
        dict['overall'] = ''
    if not dict.has_key('user'):
        dict['user'] = ''
    if not dict.has_key('colour'):
        dict['colour'] = ''
    if not dict.has_key('other_decisions'):
        dict['other_decisions'] = []
    if not dict.has_key('method_details'):
        dict['method_details'] = []
    if not dict.has_key('decision_details'):
        dict['decision_details'] = []
    if not dict.has_key('habitat'):
        dict['habitat'] = ''
    if not dict.has_key('shortname'):
        dict['shortname'] = ''
    if not dict.has_key('group'):
        dict['group'] = ''
    if not dict.has_key('region'):
        dict['region'] = ''

    #if conclusion is accepted
    if decision == 'OK':
        if dict['main_decision'] == 'END':
            dict['other_decisions'].append(decision)
        else:
            if dict['main_decision'] != '':
                dict = context.save_decision(dict)
            dict = context.save_conclusion(dict, decision, record, conclusion_type)
    #if conclusion is not accepted
    else:
        if dict['main_decision'] in ['OK', 'END']:
            dict['other_decisions'].append(decision)
        else:
            if user == USER_MAXIM:
                if dict['main_decision'] != '':
                    if dict['user'] == USER_IURIE and dict['overall'] == 'MTX': #check if the other automatic assesment has MTX value
                        dict['other_decisions'].append(decision)
                    else:
                        dict = context.save_decision(dict)
                        dict = context.save_conclusion(dict, 'A', record, conclusion_type)
                else:
                    dict = context.save_conclusion(dict, 'A', record, conclusion_type)
            elif user == USER_IURIE:
                if dict['main_decision'] != '':
                    if dict['user'] == USER_MAXIM and dict['overall'] == 'MTX': #check if the other automatic assesment has MTX value
                        dict['other_decisions'].append(decision)
                    else:
                        dict = context.save_decision(dict)
                        dict = context.save_conclusion(dict, 'A', record, conclusion_type)
                else:
                    dict = context.save_conclusion(dict, 'A', record, conclusion_type)
            elif decision:
                if dict['main_decision'] != '' and (dict['user'] == USER_MAXIM or dict['user'] == USER_IURIE):
                    dict['other_decisions'].append(decision)
                else:
                    dict = context.save_conclusion(dict, decision, record, conclusion_type)
return output
