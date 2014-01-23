# Script (Python)
# /article17/speciesreport/shrink_species
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
if species.find('(') != -1:
    pieces = species.split('(')
    return '%s<br />%s' % (pieces[0], pieces[1].replace(')', ''))
else:
    return species
