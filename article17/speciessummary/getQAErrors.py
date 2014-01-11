# Script (Python)
# /article17/speciessummary/getQAErrors
# params: 'qa_errors, fieldname'
## Script (Python) "getQAErrors"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=qa_errors, fieldname
##title=
##
fields = [ r['FlagField'] for r in qa_errors ]
if fieldname in fields:
    return [(r['error_description'], r['suspect_value']) for r in qa_errors ][0]
