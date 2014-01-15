# Script (Python)
# /article17/habitatsummary/getHabitatAnnexes
# params: 'habitatcode'
## Script (Python) "getHabitatAnnexes"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=habitatcode
##title=
##
output = []
records = context.sql_methods.select_habitat_annexes(habitatcode=habitatcode)
if records:
    record = records[0]

    if record['annex']:
        if int(record['priority']):
            output.append('%s*' % record['annex'])
        else:
            output.append(record['annex'])
    return ', '.join(output)
else:
    return ''
