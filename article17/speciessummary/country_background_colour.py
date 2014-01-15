# Script (Python)
# /article17/speciessummary/country_background_colour
# params: 'species_name_different, complementary_other_information'
## Script (Python) "country_background_colour"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=species_name_different, complementary_other_information
##title=
##
if species_name_different >-1 or complementary_other_information != '':
    return '%s' % 'country_different'
