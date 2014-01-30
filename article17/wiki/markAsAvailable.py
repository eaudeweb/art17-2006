# Script (Python)
# /article17/wiki/markAsAvailable
# params: 'id, user'
## Script (Python) "markAsAvailable"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=id, user
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE

auth_user = request.AUTHENTICATED_USER.getUserName()
if user!= auth_user:
    return False
else:
    context.sql_methods.undelete_wiki_comments(id=id)
return id
