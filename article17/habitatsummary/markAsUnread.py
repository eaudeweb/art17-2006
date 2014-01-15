# Script (Python)
# /article17/habitatsummary/markAsUnread
# params: 'id, user'
## Script (Python) "markAsUnread"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=id, user
##title=
##
context.sql_methods.set_comments_unread(id_comment=id, reader_user_id=user)
return id
