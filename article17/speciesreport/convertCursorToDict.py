# Script (Python)
# /article17/speciesreport/convertCursorToDict
# params: 'cursor, key'
## Script (Python) "convertCursorToDict"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cursor, key
##title=
##
out = {}
for res in cursor:
    out['%s_%s' % (res[key], res['eu_country_code'])] = res['show_data']
return out
