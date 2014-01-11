# Script (Python)
# /article17/speciessummary/sql_methods/test
# params: ''
## Script (Python) "test"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
res = context.get_map_restricted_species(assesment_speciesname='parnassius apollo')
return [r['assesment_speciesname'] for r in res]
