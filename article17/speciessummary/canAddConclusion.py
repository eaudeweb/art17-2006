# Script (Python)
# /article17/speciessummary/canAddConclusion
# params: 'region, species, user'
## Script (Python) "canAddConclusion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=region, species, user
##title=
##
conclusions = context.sql_methods.lookup_user_conclusions(bioregion=region, speciesname=species, username=user)
if conclusions or not context.acl_manager.checkPermissionAddConclusion():
    return False

return True
