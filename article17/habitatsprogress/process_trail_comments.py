# Script (Python)
# /article17/habitatsprogress/process_trail_comments
# params: 'user_id'
## Script (Python) "process_trail_comments"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=user_id
##title=
##
results = context.sql_methods.select_trail_comments(user_id=user_id)
if results:
    return context.eval_string(results[0]['thecount'])
else:
    return {}
