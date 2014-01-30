# Script (Python)
# /article17/wiki_trail/manage_wiki_comments
# params: ''
## Script (Python) "manage_wiki_comments"
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

wiki_id = request.form.get('wiki_id', '')
comment = request.form.get('comment', '')
comment_id = request.form.get('comment_id', '')
region=request.form.get('region', '')
species=request.form.get('species', '')
habitat=request.form.get('habitat', '')
referer=request.form.get('referer', '')

author = request.AUTHENTICATED_USER

if request.has_key('add_button'):

    #insert comment details in database
    results = context.sql_methods.insert_wiki_comments(wiki_id=wiki_id,comment=comment, author=author)
    context.sql_methods.insert_wiki_comments_read(comment_id=results[0]['newid'], reader_id=author)

elif request.has_key('edit_button'):

    #update comment details in database
    context.sql_methods.update_wiki_comments(id=comment_id, comment=comment)
    context.sql_methods.delete_wiki_comments_read(id=comment_id, user=author)

return RESPONSE.redirect('%s/wiki_trail?id=%s&comm_id=%s&region=%s&species=%s&habitat=%s' % (referer, wiki_id, comment_id, region, species, habitat))
