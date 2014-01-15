# Script (Python)
# /article17/habitatsummary/details/background_colour
# params: 'value'
## Script (Python) "background_colour"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=value
##title=
##
colors = ('#9CB34D','#D16E43','#D16E43','#D16E43','#C22C15','#C22C15','#C22C15','#6F6C66','#FFFFFF')
assessments = ('FV','U1','U1-','U1+','U2','U2-','U2+','XX','')

RGBS = dict(zip(assessments,[x for x in colors]))
colour = RGBS.get(value,'')
if colour:
    return colour[1:]
else:
    return ''
