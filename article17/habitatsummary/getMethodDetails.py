# Script (Python)
# /article17/habitatsummary/getMethodDetails
# params: 'method_id'
## Script (Python) "getMethodDetails"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=method_id
##title=
##
methods = context.sql_methods.get_method_details(method=method_id)
if methods:
    return methods[0]['details']
