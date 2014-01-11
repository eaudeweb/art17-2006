# Script (Python)
# /article17/speciessummary/details/getRegions
# params: 'species'
## Script (Python) "getRegions"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=species
##title=
##
regions = ['^%s' % rec['region'] for rec in context.sql_methods.lookup_species_bioregion(assesment_speciesname=context.string_decode(species))]
return '|'.join(regions)
