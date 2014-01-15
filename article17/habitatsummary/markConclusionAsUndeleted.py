# Script (Python)
# /article17/habitatsummary/markConclusionAsUndeleted
# params: 'id'
## Script (Python) "markConclusionAsUndeleted"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=id
##title=
##
from DateTime import DateTime

request = container.REQUEST
RESPONSE =  request.RESPONSE

habitat, region, user, ms = request.get('id').split('###')

context.sql_methods.update_undelete_conclusion(region=region,
                            habitatcode=habitat,
                            user=user,
                            ms=ms,
                            last_update=DateTime().strftime('%Y-%m-%d %H:%M'))
return id
