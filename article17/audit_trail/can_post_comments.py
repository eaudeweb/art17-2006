# Script (Python)
# /article17/wiki_trail/can_post_comments
# params: 'comments, user, action'
## Script (Python) "can_post_comments"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=comments, user, action
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE

auth_user = request.AUTHENTICATED_USER.getUserName()
if user!= auth_user:
    return False

authors = [ comm['author'] for comm in comments ]
if user in authors:
    if action == 'edit':
        return True
    else:
        return False
else:
    return True
