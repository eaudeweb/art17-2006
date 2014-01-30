# Script (Python)
# /article17/wiki/edit_wiki
# params: ''
## Script (Python) "edit_wiki"
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

region=request.form.get('region', '')
species=request.form.get('species', '')
habitat=request.form.get('habitat', '')
body=request.form.get('body', '')
referer=request.form.get('referer', '')
editor = request.AUTHENTICATED_USER.getUserName()

#check if exists
if habitat:
    active_wiki = context.sql_methods.select_active_wiki(region=region, habitat=habitat)
if species:
    active_wiki = context.sql_methods.select_active_wiki(region=region, assesment_speciesname=context.string_decode(species))

if active_wiki:
    if (active_wiki[0]['body'] != body) and (body.strip() != ''):
        #update wiki changes
        context.sql_methods.inactivate_wiki_changes(id=active_wiki[0]['id'])
        #save wiki changes
        context.sql_methods.insert_wiki_changes(id=active_wiki[0]['id'], body=body, editor=editor, active=1)
else:
    if body:
        #insert in wiki table
        last_inserted = context.sql_methods.insert_wiki(region=region, assesment_speciesname=context.string_decode(species), habitatcode=habitat)
        #save wiki changes
        context.sql_methods.insert_wiki_changes(id=last_inserted[0]['newid'], body=body, editor=editor, active=1)

return RESPONSE.redirect('%s/wiki?region=%s&species=%s&habitat=%s' % (referer, region, species, habitat))
