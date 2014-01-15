# Script (Python)
# /article17/habitatsummary/canAddConclusion
# params: 'region,habitat,user'
## Script (Python) "canAddConclusion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=region,habitat,user
##title=
##
conclusions = context.sql_methods.lookup_user_conclusions(region=region, habitatcode=habitat, user=user)

if conclusions or user == 'Anonymous User':
    return False
return True
