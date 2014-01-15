# Script (Python)
# /article17/habitatsummary/attrs_conclusion/td_decision_title
# params: 'record, auth_user'
## Script (Python) "td_decision_title"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=record, auth_user
##title=
##
user_roles = context.acl_manager.getSpecificUserRoles(auth_user)

if user_roles['expert']:
    if record['user_decision']:
        user_name = context.acl_manager.getUserFullName(record['user_decision'])
        return "added by %s <br /> on %s" % (user_name, record['last_update_decision'])
    else:
        return ''
else:
    info = context.sql_methods.lookup_decision_details(decision=record['decision'])
    if info:
        return info[0]['details']
    else:
        return ''
