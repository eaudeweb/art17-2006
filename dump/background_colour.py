# Script (Python)
# /article17/speciessummary/background_colour
# params: 'value, extraclasses, conclusions'
## Script (Python) "background_colour"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=value, extraclasses, conclusions
##title=
##
#from Products.PythonScripts.standard import html_quote

if value == 'XU' and not (context.acl_manager.has_etc_role() or context.acl_manager.has_adm_role()):
    value = 'XX'

#if value and value.endswith('?') and not (context.acl_manager.has_etc_role() or context.acl_manager.has_adm_role()):
#    value = value[:-1]

classes = {
    'FV':'FV',
    'U1':'U1',
    'U1-':'U1M',
    'U1+':'U1P',
    'U2':'U2',
    'U2-':'U2M',
    'U2+':'U2P',
    'XX':'XX',
    'NA':'NA',
    'XU':'XU',
    'U2?':'U2U',
    'U1?':'U1U',
    'FV?':'FVU',
    'XX?':'XXU',
    'XU?':'XUU',
    }

country_assessments = {
    'FV':  'Favourable (FV)',
    'U1':  'Inadequate (U1)', 
    'U1-': 'Inadequate and deteriorating (U1-)', 
    'U1+': 'Inadequate but improving (U1+)', 
    'U2':  'Bad (U2)', 
    'U2-': 'Bad and deteriorating (U2-)', 
    'U2+': 'Bad but improving (U2+)', 
    'XX':  'Unknown (XX)',
    'NA':  'Imposible to be assesed'} 

title = conclusions.get(value, None)
if title is None:
    title = country_assessments.get(value, 'Not provided')

return {'class': '%s %s' % (extraclasses, classes.get(value,'')), 'title': title}
