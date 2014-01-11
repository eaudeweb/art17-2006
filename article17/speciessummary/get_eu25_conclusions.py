# Script (Python)
# /article17/speciessummary/get_eu25_conclusions
# params: 'assesment_speciesname, region'
## Script (Python) "get_eu25_conclusions"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=assesment_speciesname, region
##title=
##
ok_conclusions = context.sql_methods.select_ok_conclusions(assesment_speciesname=assesment_speciesname, bioregion=region)
if not ok_conclusions:
    auto_conclusions = context.sql_methods.select_auto_conclusions(assesment_speciesname=assesment_speciesname, bioregion=region)
    if auto_conclusions:
        return True
    else:
        return False
return True
