# Script (Python)
# /article17/habitatsummary/view_conclusions
# params: 'conclusions, auth_roles'
## Script (Python) "view_conclusions"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=conclusions, auth_roles
##title=
##
ok_concl = [record for record in conclusions if record['decision'] in ['OK', 'END']]

#has role 'administrator' or 'expert'
if auth_roles['administrator'] or auth_roles['expert']:
    return [(concl['region'], concl['habitatcode'], concl['user'], concl['MS']) for concl in conclusions]

#is anonymous user or has role 'stakeholder' or 'nat'
else:

    #check if the decision status is OK or END
    if ok_concl:
        buffer = []
        buffer = [(concl['region'], concl['habitatcode'], concl['user'], concl['MS']) for concl in ok_concl]
        #check if the record was inserted by a STA
        for rec in conclusions:
            user_roles = context.acl_manager.getSpecificUserRoles(rec['user'])
            if not user_roles['administrator'] and not user_roles['expert']:
                buffer.append((rec['region'], rec['habitatcode'], rec['user'], rec['MS']))
        return buffer

    #if no decision with OK or END is found then display the 'automatic' conclusions
    else:
        buffer = []
        buffer = [(concl['region'], concl['habitatcode'], concl['user'], concl['MS']) for concl in conclusions if concl['user'] in ['maximiur', 'iurieetcbd']]
        #check if the record was inserted by a STA
        for rec in conclusions:
            user_roles = context.acl_manager.getSpecificUserRoles(rec['user'])
            if not user_roles['administrator'] and not user_roles['expert']:
                buffer.append((rec['region'], rec['habitatcode'], rec['user'], rec['MS']))
        return buffer
return []
