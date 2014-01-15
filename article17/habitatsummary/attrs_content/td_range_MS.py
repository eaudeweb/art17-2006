# Script (Python)
# /article17/habitatsummary/attrs_content/td_range_MS
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
title = ''
content = []

if record['complementary_other_information']!='':
    class_names.append('qa_error')
    content.append("""<div title="%s""" % html_quote(unicode(record['complementary_other_information'], 'utf-8')))
    if record['complementary_other_information_english'] is not None:
        content.append("""<br /><q>English automatic translation: </q>%s""" % html_quote(unicode(record['complementary_other_information_english'], 'utf-8')))
    if record['habitattype_type_asses'] == 0:
        errors = context.sql_methods.lookup_habitat_type(abbrev=record['habitattype_type'])
        if errors:
            content.append("""<br /><br />%s""" % errors[0]['SpeciesType'])
        else:
            content.append("""<br /><br />%s""" % record['habitattype_type'])
    content.append("""<br /><br /><em>Click to open original report in a new window</em>">%s</div>""" % eu_country_code)
elif record['habitattype_type_asses'] == 0:
    class_names.append('qa_error')
    errors = context.sql_methods.lookup_habitat_type(abbrev=record['habitattype_type'])
    if errors:
        title = errors[0]['SpeciesType']
    else:
        title = record['habitattype_type']
    content.append(eu_country_code)
else:
    title = "Click to open original report in a new window"
    content.append(eu_country_code)

return {
    'class': ' '.join(class_names),
    'title': title,
    'content': ''.join(content)
    }
