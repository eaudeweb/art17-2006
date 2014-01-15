# Script (Python)
# /article17/habitatsummary/manageComment
# params: ''
## Script (Python) "manageComment"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE

from DateTime import DateTime

region=request.form.get('region', '')
habitat=request.form.get('habitat', '')
user=request.form.get('user', '')
ms=request.form.get('ms', '')
author = request.AUTHENTICATED_USER

if request.has_key('add_button'):
    #insert comment details in database
    results = context.sql_methods.insert_comment(region=region, 
                        habitat=habitat, 
                        user=user, 
                        ms=ms, 
                        comment=request.form.get('comment', ''), 
                        author=author, 
                        post_date=DateTime().strftime('%Y-%m-%d %H:%M'))
    context.sql_methods.insert_comments_read(id_comment=results[0]['newid'], reader_user_id=author)
elif request.has_key('edit_button'):
    #update comment details in database
    context.sql_methods.update_comment(id=request.form.get('comment_id', ''),
                        comment=request.form.get('comment', ''),
                        post_date=DateTime().strftime('%Y-%m-%d %H:%M'))
    context.sql_methods.delete_comments_read(id=request.form.get('comment_id', ''), user=author)
return RESPONSE.redirect('%s/comments_html?region=%s&amp;habitat=%s&amp;user=%s&amp;ms=%s' % (context.absolute_url(), region, habitat, user, ms))
