# Script (Python)
# /article17/habitatsummary/getGroupHabitats
# params: 'group'
## Script (Python) "getGroupHabitats"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=group
##title=
##
group = context.string_decode(group)
records = ['%s@@@%s' % (habitat['habitatcode'], habitat['shortname']) for habitat in context.sql_methods.select_group_habitats(group=group)]

#first option must be blank
records.append(' @@@ ')
records.sort()
records.reverse()

return ';'.join(records)
