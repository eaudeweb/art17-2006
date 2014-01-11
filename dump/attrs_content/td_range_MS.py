# Script (Python)
# /article17/speciessummary/attrs_content/td_range_MS
# params: 'record'
## Script (Python) "td_range_MS"
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

class_names = ['center', 'section-border']
eu_country_code = record['eu_country_code'] or 'N/A'
buffer = []
content = ''
title = ''


if record['speciesname']!=record['assesment_speciesname'] or record['complementary_other_information']!='':
    class_names.append('qa_error')
    buffer.append('<q>%s</q><br />%s' % (unicode(record['speciesname'], 'utf-8'), unicode(record['complementary_other_information'], 'utf-8')))
    if record['complementary_other_information_english'] is not None:
        buffer.append('<br /><q>English automatic translation: </q>%s' % unicode(record['complementary_other_information_english'], 'utf-8'))
    if record['species_type_asses'] == 0:
        errors = context.sql_methods.lookup_species_type(abbrev=record['species_type'])
        if errors:
            buffer.append('<br /><br />%s' % errors[0]['SpeciesType'])
        else:
            buffer.append('<br /><br />%s' % record['species_type'])
    buffer.append('<br /><br /><em>Click to open original report in a new window</em>')
    content = """<div title="%s">%s</div>""" % (html_quote(''.join(buffer)), eu_country_code)
elif record['species_type_asses'] == 0:
    class_names.append('qa_error')
    errors = context.sql_methods.lookup_species_type(abbrev=record['species_type'])
    if errors:
        title = errors[0]['SpeciesType']
    else:
        title = record['species_type']
    content = eu_country_code
else:
    title = "Click to open original report in a new window"
    content = eu_country_code

return {
    'class': ' '.join(class_names),
    'title': title,
    'content': content
    }
