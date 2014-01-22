# Script (Python)
# /article17/speciesprogress/shrink_species
# params: 'species'
## Script (Python) "shrink_species"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=species
##title=
##
records = context.sql_methods.lookup_species_name(species=species)
if records:
    priority = int(records[0]['priority'])
else:
    priority = 0

marker = ''
if species.find('(') != -1:
    if priority:
        marker = '*'
    pieces = species.split('(')
    return '%s%s<br />%s' % (pieces[0], marker, pieces[1].replace(')', ''))
else:
    if priority:
        marker = '*'
    return '%s%s' % (species, marker)
