# Script (Python)
# /article17/habitatsreport/sql_methods/lookup_bioregion
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
    'MATL': 'Atlantic ocean',
    'MBAL': 'Baltic sea',
    'MMAC': 'Macaronesian/Atlantic ocean',
    'MMED': 'Mediterranean Sea'
}
