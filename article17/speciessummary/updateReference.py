# Script (Python)
# /article17/speciessummary/updateReference
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
from DateTime import DateTime

request = container.REQUEST
RESPONSE =  request.RESPONSE
session = request.SESSION
form = request.form
valid_data = True

#CONSTANTS
NOT_NUMERIC_VALUES = "Only numeric values or intervals are accepted!"

#
#load data from request
#

#hidden fields
assesment_speciesname = form.get('assesment_speciesname', '')
group = form.get('group', '')
region = form.get('region', '')

complementary_favourable_range = form.get('complementary_favourable_range', '')
complementary_favourable_population = form.get('complementary_favourable_population', '')

#
# STEP 1: validate form values
#
if not context.validate_field(complementary_favourable_range):
    session.set('range-error', '')
    session.set('complementary_favourable_range_error', NOT_NUMERIC_VALUES)
    valid_data = False

if not context.validate_field(complementary_favourable_population):
    session.set('population-error', '')
    session.set('complementary_favourable_population_error', NOT_NUMERIC_VALUES)
    valid_data = False

if valid_data:
    #insert data in database
    context.sql_methods.update_manual_reference(region=region, assesment_speciesname=context.string_decode(assesment_speciesname), 
                        complementary_favourable_range=complementary_favourable_range, complementary_favourable_population=complementary_favourable_population, 
                        user=form.get('conclusion_owner', ''))
    return RESPONSE.redirect('%s?group=%s&species=%s&region=%s' % (context.absolute_url(), group, assesment_speciesname, region))
else:
    #put data on session
    session.set('complementary_favourable_range', complementary_favourable_range)
    session.set('complementary_favourable_population', complementary_favourable_population)

    return RESPONSE.redirect(request.HTTP_REFERER)
