# Script (Python)
# /article17/habitatsummary/getReadComments
# params: 'auth_user'
## Script (Python) "getReadComments"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=auth_user
##title=
##
comments = context.sql_methods.select_read_comments(reader_user_id=auth_user)
return [ comm['id_comment'] for comm in comments ]
