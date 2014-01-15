# Script (Python)
# /article17/habitatsummary/getHabitatsAndRegions
# params: 'habitat, group'
## Script (Python) "getHabitatsAndRegions"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=habitat, group
##title=
##
habitats = context.getGroupHabitats(group)
regions = context.getHabitatRegions(habitat)

return "%s###%s" % (habitats, regions)
