# Script (Python)
# /article17/habitatsummary/markAsRead
# params: 'id, user'
## Script (Python) "markAsRead"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=id, user
##title=
##
context.sql_methods.insert_comments_read(id_comment=id, reader_user_id=user)
return id
