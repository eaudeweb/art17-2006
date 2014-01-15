# Script (Python)
# /article17/habitatsummary/updateDecision
# params: 'decision, field'
## Script (Python) "updateDecision"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=decision, field
##title=
##
# Example code:

from DateTime import DateTime

request = container.REQUEST
RESPONSE =  request.RESPONSE

#load request variables
habitat, region, user = field.split('###')

context.sql_methods.update_decision(decision=decision,
                        user_decision=request.AUTHENTICATED_USER.getUserName(),
                        last_update_decision=DateTime().strftime('%Y-%m-%d %H:%M'),
                        region=region,
                        habitatcode=habitat,
                        user=user)

return "%s|||%s" % (decision, field)
