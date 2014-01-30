# Script (Python)
# /article17/wiki/get_wiki_text
# params: 'region, species, habitat'
## Script (Python) "get_wiki_text"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=region, species, habitat
##title=
##
wiki = context.sql_methods.select_active_wiki(region=region, assesment_speciesname=context.string_decode(species), habitat=habitat)
if wiki:
    return wiki[0]['body']
else:
    return ''
