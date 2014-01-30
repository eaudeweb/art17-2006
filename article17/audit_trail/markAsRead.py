# Script (Python)
# /article17/wiki_trail/markAsRead
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
context.sql_methods.insert_wiki_comments_read(comment_id=id, reader_id=user)
return id
