# Script (Python)
# /article17/speciessummary/getSpeciesAnnexes
# params: 'species'
## Script (Python) "getSpeciesAnnexes"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=species
##title=
##
output = []
records = context.sql_methods.lookup_annex(assesment_speciesname=species)
if records:
   record = records[0]

   if record['annex_II']:
       if int(record['priority']):
           output.append('%s*' % record['annex_II'])
       else:
           output.append(record['annex_II'])

   if record['annex_IV']:
       output.append(record['annex_IV'])

   if record['annex_V']:
       output.append(record['annex_V'])

return ', '.join(output)
