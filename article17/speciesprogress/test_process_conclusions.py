# Script (Python)
# /article17/speciesprogress/test_process_conclusions
# params: ''
## Script (Python) "test_process_conclusions"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
records =  context.sql_methods.select_species_conclusions(conclusion='conclusion_assessment', group='Plants')
print len(records)
return printed
