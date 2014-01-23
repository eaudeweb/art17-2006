# Script (Python)
# /article17/speciesreport/attrs_content/td_species
# params: 'record'
## Script (Python) "td_species"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record
##title=
##
request = container.REQUEST
RESPONSE =  request.RESPONSE

from Products.PythonScripts.standard import html_quote

class_names = ['section-border']
species = record['assesment_speciesname'] or 'N/A.'
title = ''
content = []

if record['speciesname']!=record['assesment_speciesname'] or record['complementary_other_information']!='':
    class_names.append('qa_error')
    content.append('<div title="<q>%s</q><br />%s' % (html_quote(unicode(record['speciesname'], 'utf-8')), html_quote(unicode(record['complementary_other_information'], 'utf-8'))))
    if record['complementary_other_information_english'] is not None:
        content.append('<br /><q>English translation: </q>%s' % html_quote(unicode(record['complementary_other_information_english'], 'utf-8')))
    content.append('<br /><br /><em>Click to open original report in a new window</em>">%s</div>' % species)
elif record['species_type_asses'] == 0:
    class_names.append('qa_error')
    errors = context.sql_methods.lookup_species_type(abbrev=record['species_type'])
    if errors:
        title = errors[0]['SpeciesType']
    else:
        title = record['species_type']
    content.append(species)
else:
    title = "Click to open original report in a new window"
    content.append(species)

return {
    'class': ' '.join(class_names),
    'title': title,
    'content': ''.join(content)
    }
