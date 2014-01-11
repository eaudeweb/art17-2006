# Script (Python)
# /article17/speciessummary/getGroupSpecies
# params: 'upper_group'
## Script (Python) "getGroupSpecies"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=upper_group
##title=
##
if context.string_decode(upper_group) == 'not-defined':
    records = ['%s,%s' % (rec['speciesname'], context.string_encode(rec['speciesname'])) for rec in context.sql_methods.list_species_not_in_group()]
else:
    upper_group = context.string_decode(upper_group)
    records = ['%s,%s' % (rec['assesment_speciesname'], context.string_encode(rec['assesment_speciesname'])) for rec in context.sql_methods.list_group_species(group=upper_group)]

#first option must be blank
records.append(',')
records.sort()
records.reverse()

return ';'.join(records)
