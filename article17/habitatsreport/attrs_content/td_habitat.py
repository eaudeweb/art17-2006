# Script (Python)
# /article17/habitatsreport/attrs_content/td_habitat
# params: 'record'
## Script (Python) "td_habitat"
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
habitatcode = record['habitatcode'] or 'N/A'
habitat_names = context.sql_methods.lookup_habitat_name(habitatcode=habitatcode)


if habitat_names[0]['priority'] == 1:
    marker = '*'
else:
    marker = ''


habitat_name = "%s%s - %s" % (habitatcode, marker, habitat_names[0]['shortname'])
title = ''
content = []

if record['complementary_other_information']!='':
    class_names.append('qa_error')
    content.append('<div title="%s' % html_quote(unicode(record['complementary_other_information'], 'utf-8')))
    if record['complementary_other_information_english'] is not None:
        content.append('<br /><q>English translation: </q>%s' % html_quote(unicode(record['complementary_other_information_english'], 'utf-8')))
    content.append('<br /><br /><em>Click to open original report in a new window</em>">%s</div>' % habitat_name)
else:
    title = "Click to open original report in a new window"
    content.append(habitat_name)

return {
    'class': ' '.join(class_names),
    'title': title,
    'content': ''.join(content)
    }
