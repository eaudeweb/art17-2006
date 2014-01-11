# Script (Python)
# /article17/speciessummary/convertCursorToList
# params: 'cursor, arg'
## Script (Python) "convertCursorToList"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=cursor, arg
##title=
##
return [ res[arg] for res in cursor ]
