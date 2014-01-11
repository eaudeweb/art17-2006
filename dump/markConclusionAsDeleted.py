# Script (Python)
# /article17/speciessummary/markConclusionAsDeleted
# params: 'id'
## Script (Python) "markConclusionAsDeleted"
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

species, region, user, ms = request.get('id').split('###')

context.sql_methods.update_delete_conclusion(region=region,
                            assesment_speciesname=context.string_decode(species),
                            user=user,
                            ms=ms,
                            last_update=DateTime().strftime('%Y-%m-%d %H:%M'))
return id
