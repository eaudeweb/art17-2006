# Script (Python)
# /article17/speciesprogress/generate_bgcolour
# params: 'record, extraclasses, conclusions, conclusion, comments, wiki_comments, trail_comments, user_comments, countries, conclusion_types'
## Script (Python) "generate_bgcolour"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, extraclasses, conclusions, conclusion, comments, wiki_comments, trail_comments, user_comments, countries, conclusion_types
##title=
##
colour = record['colour']
species = context.string_decode(record['species'])
if record['main_decision'] == 'OK':
    extraclasses = 'valid_cell %s' % extraclasses

sp_present = []
sp_ocasional = []
concl_type = ''
title = []

classes = {
    'FV':'FV',
    'U1':'U1',
    'U1-':'U1M',
    'U1+':'U1P',
    'U2':'U2',
    'U2-':'U2M',
    'U2+':'U2P',
    'XX':'XX',
    'NA':'NA',
    'XU':'XU',
    'U2?':'U2U',
    'U1?':'U1U',
    'FV?':'FVU',
    'XX?':'XXU',
    'XU?':'XUU',
    }

for concl in conclusion_types:
    if concl['code'] == conclusion:
        concl_type = concl['name']
        break

for i in countries.get(species, ''):
    if i[0] == record['region']:
        if i[2] == 0:
            sp_ocasional.append(i[1])
        else:
            sp_present.append(i[1])

comm = comments.get(species, '')
if comm:
    comm = comm.get(record['region'], 0)
else:
    comm = 0

wiki_comm = wiki_comments.get(species, '')
if wiki_comm:
    wiki_comm = wiki_comm.get(record['region'], 0)
else:
    wiki_comm = 0

user_comm = user_comments.get(species, '')
if user_comm:
    user_comm = user_comm.get(record['region'], 0)
else:
    user_comm = 0

#trail_comm = trail_comments.get(species, '')
#if trail_comm:
#    trail_comm = trail_comm.get(record['region'], 0)
#else:
#    trail_comm = 0

#title = """Species: %s, Region: %s <br />
#           Method: %s <br />
#           Unread sheet comments: %s <br />
#           Unread comments: %s <br />
#           Unread audit comments: %s """ % (species, record['region'], record['method'], comm, wiki_comm, trail_comm)

if record['decision_details'] == 'no decision':
    details = 'Auto'
elif record['decision_details'] is None:
    details = 'Auto'
else:
    details = record['decision_details']


title.append("Species: %s, Region: %s" % (species, record['region']))
if sp_present:
    title.append("Reported as present by : %s" % ', '.join(sp_present))
if sp_ocasional:
    title.append("Reported as ocasional by : %s" % (', '.join(sp_ocasional)))
title.append("Assessment %s: %s" % (concl_type, conclusions.get(colour, None)))
if context.acl_manager.has_etc_role() or context.acl_manager.has_adm_role():
    title.append("Decision: %s (%s)" % (record['main_decision'], details))
title.append("Method: %s (%s)" % (record['method'], record['method_details']))
if context.acl_manager.has_etc_role() or context.acl_manager.has_adm_role():
    title.append("Unread comments for my assessment: %s" % user_comm)
    title.append("Unread comments for all assessments: %s" % comm)
    title.append("Unread comments on data sheet info: %s" % wiki_comm)

return {'class': '%s %s' % (extraclasses, classes.get(colour,'')), 'title': "<br />".join(title)}
