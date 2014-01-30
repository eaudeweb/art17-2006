# Script (Python)
# /article17/wiki_trail/activate_wiki_changes
# params: ''
## Script (Python) "activate_wiki_changes"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
request = context.REQUEST
RESPONSE = request.RESPONSE

id = request.form.get('wiki-active', '')
wiki_id = request.form.get('wiki_id', '')
region=request.form.get('region', '')
species=request.form.get('species', '')
habitat=request.form.get('habitat', '')
referer=request.form.get('referer', '')

context.sql_methods.inactivate_wiki_changes(id=wiki_id)
context.sql_methods.activate_wiki_changes(id=id)

return RESPONSE.redirect('%s/wiki_trail/changes_html?id=%s&region=%s&species=%s&habitat=%s' % (referer, wiki_id, region, species, habitat))
