# Script (Python)
# /article17/habitatsummary/get_eu25_conclusions
# params: 'habitatcode, region'
## Script (Python) "get_eu25_conclusions"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=habitatcode, region
##title=
##
ok_conclusions = context.sql_methods.select_ok_conclusions(habitatcode=habitatcode, bioregion=region)
if not ok_conclusions:
    auto_conclusions = context.sql_methods.select_auto_conclusions(habitatcode=habitatcode, bioregion=region)
    if auto_conclusions:
        return True
    else:
        return False
return True
