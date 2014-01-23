# Script (Python)
# /article17/habitatsreport/attrs_content/td_coverage_grid_area
# params: 'record, conclusions, qa_errors'
## Script (Python) "td_coverage_grid_area"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, conclusions, qa_errors
##title=
##
return {
    'content':context.str2num(record['percentage_distribution_grid_area']),
    'title': '',
    'class': 'center section-border',
    }
