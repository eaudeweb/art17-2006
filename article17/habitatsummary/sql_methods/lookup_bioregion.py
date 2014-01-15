# Script (Python)
# /article17/habitatsummary/sql_methods/lookup_bioregion
# params: ''
## Script (Python) "lookup_bioregion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
# The list bio regions for the habitats directive
return {
    'ALP': 'Alpine',
    'ATL': 'Atlantic',
    'BOR': 'Boreal',
    'CON': 'Continental',
    'MED': 'Mediterranean',
    'MAC': 'Macaronesian',
    'PAN': 'Pannonian',
# Marine
    'MATL': 'Marine-Atlantic region',
    'MBAL': 'Marine-Baltic region',
    'MMAC': 'Marine-Macaronesian region',
    'MMED': 'Marine-Mediterranean region'
}
