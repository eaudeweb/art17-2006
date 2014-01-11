# Script (Python)
# /article17/speciessummary/canPostComments
# params: 'comments, concl_owner, user, action'
## Script (Python) "canPostComments"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=comments, concl_owner, user, action
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE

acl = context.acl_manager
can_add = False

if acl.has_sta_role(user) or acl.has_nat_role(user):
    if acl.has_sta_role(concl_owner):
        can_add = True
    if acl.has_nat_role(concl_owner) and concl_owner == user:
        can_add = True
else:
    can_add = True

if can_add:
    authors = [ comm['author'] for comm in comments ]
    if user in authors:
        if action == 'edit':
            return True
        else:
            return False
    else:
        return True
