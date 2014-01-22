# Script (Python)
# /article17/speciesprogress/process_countries
# params: ''
## Script (Python) "process_countries"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
results = context.sql_methods.select_countries()
if results:
    return context.eval_string(results[0]['thecount'])
else:
    return {}
