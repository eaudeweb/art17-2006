# Script (Python)
# /article17/habitatsummary/updateReference
# params: ''
## Script (Python) "updateReference"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
#CONSTANTS
NOT_NUMERIC_VALUES = "Only numeric values or intervals are accepted!"

request = container.REQUEST
RESPONSE =  request.RESPONSE
session = request.SESSION
form = request.form
valid_data = True

#
#load data from request
#

habitat = form.get('habitat', '')
group = form.get('group', '')
region = form.get('region', '')

#range values
complementary_favourable_range = form.get('complementary_favourable_range', '')
complementary_favourable_area = form.get('complementary_favourable_area', '')

#
# STEP 1: validate form values
#
if not context.validate_field(complementary_favourable_range):
    session.set('range-error', '')
    session.set('complementary_favourable_range_error', NOT_NUMERIC_VALUES)
    valid_data = False

if not context.validate_field(complementary_favourable_area):
    session.set('coverage-error', '')
    session.set('complementary_favourable_area_error', NOT_NUMERIC_VALUES)
    valid_data = False

if valid_data:
    #insert data in database
    context.sql_methods.update_manual_reference(region=region, habitatcode=habitat, 
                                complementary_favourable_range=complementary_favourable_range,
                                complementary_favourable_area=complementary_favourable_area,
                                user = form.get('conclusion_owner', ''))
    return RESPONSE.redirect('%s?group=%s&habitat=%s&region=%s' % (context.absolute_url(), group, habitat, region))
else:
    #put data on session
    session.set('complementary_favourable_range', complementary_favourable_range)
    session.set('complementary_favourable_area', complementary_favourable_area)
    return RESPONSE.redirect(request.HTTP_REFERER)
