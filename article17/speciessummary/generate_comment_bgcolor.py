# Script (Python)
# /article17/speciessummary/generate_comment_bgcolor
# params: 'isOwner, read_comments, del_comm, id'
## Script (Python) "generate_comment_bgcolor"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=isOwner, read_comments, del_comm, id
##title=
##
# Example code:

if del_comm:
    return 'delete'
if isOwner:
    return 'owner'
if id in read_comments:
    return 'read'
return ''
