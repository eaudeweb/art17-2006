# Script (Python)
# /article17/speciessummary/getSpeciesAndRegion
# params: 'upper_group, species'
## Script (Python) "getSpeciesAndRegion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=upper_group, species
##title=
##
spec = context.getGroupSpecies(upper_group)
bio = context.getSpeciesRegion(species)

return "%s###%s" % (spec, bio)
