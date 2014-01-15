# Script (Python)
# /article17/speciessummary/calculate_ref
# params: 'current, qualifier, favourable'
## Script (Python) "calculate_ref"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=current, qualifier, favourable
##title=Calculate favourable reference value
##
shortquals = {
'Much more than': '>>',
'Approximately equal to': '~',
'More than': '>',
'Less than': '<'
}

if qualifier == '':
    return favourable
else:
    return shortquals.get(qualifier,'?') + current
