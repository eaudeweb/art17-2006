# Script (Python)
# /article17/speciessummary/generate_conclusion_bgcolor
# params: 'decision, deleted'
## Script (Python) "generate_conclusion_bgcolor"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=decision, deleted
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE

if deleted:
    return 'conclusion_deleted'
if decision in ['OK', 'END']:
    return 'conclusion_ok'
return ''
