# Script (Python)
# /article17/wiki_trail/get_read_comments
# params: 'auth_user'
## Script (Python) "get_read_comments"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=auth_user
##title=
##
comments = context.sql_methods.select_wiki_comments_read(reader_id=auth_user)
return [ comm['comment_id'] for comm in comments ]
