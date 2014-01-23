# Script (Python)
# /article17/habitatsreport/getGroups
# params: ''
## Script (Python) "getGroups"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
records = [group['group'] for group in context.sql_methods.select_groups()]

#first option must be blank
records.append('')

return records
