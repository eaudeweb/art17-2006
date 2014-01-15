# Script (Python)
# /article17/habitatsummary/filter_conclusions
# params: ''
## Script (Python) "filter_conclusions"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
output = []
conclusions = context.sql_methods.select_conclusions()

for conclusion in conclusions:
    if conclusion['conclusion'].strip() == 'XU':
        if context.acl_manager.has_etc_role() or context.acl_manager.has_adm_role():
            output.append(conclusion)
    elif not conclusion['conclusion'].endswith('?'):
        output.append(conclusion)
return output
