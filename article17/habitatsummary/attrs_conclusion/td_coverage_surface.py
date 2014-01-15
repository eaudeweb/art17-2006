# Script (Python)
# /article17/habitatsummary/attrs_conclusion/td_coverage_surface
# params: 'record'
## Script (Python) "td_coverage_surface"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record
##title=
##
return {
    'class': 'number',
    'content': context.str2num(record['coverage_surface_area'], '')
    }
