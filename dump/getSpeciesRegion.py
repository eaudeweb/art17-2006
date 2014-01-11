# Script (Python)
# /article17/speciessummary/getSpeciesRegion
# params: 'species'
## Script (Python) "getSpeciesRegion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=species
##title=
##
records = [rec['region'] for rec in context.sql_methods.lookup_species_bioregion(assesment_speciesname=context.string_decode(species))]
regions = ['%s,%s' % (context.lookup_bioregion().get(r,''), r) for r in records]

#first option must be blank
regions.append('All bioregions,')
regions.sort()
regions.reverse()

return ';'.join(regions)
