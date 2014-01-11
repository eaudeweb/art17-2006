# Script (Python)
# /article17/speciessummary/insertSTAConclusion
# params: ''
## Script (Python) "insertSTAConclusion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
#imports
from DateTime import DateTime

#CONSTANTS
NOT_NUMERIC_VALUES = "Only numeric values with not more than two decimals are accepted!"
FIELD_MANDATORY = "In order to provide a correction at least one field must be filled!"

request = container.REQUEST
RESPONSE =  request.RESPONSE
auth_user = request.AUTHENTICATED_USER.getUserName()

session = request.SESSION
form = request.form
valid_data = True
enable_warning = form.get('enable-warning', '1')


#
#load data from request
#

#MS
ms = form.get('ms', '')
assesment_speciesname=form.get('assesment_speciesname', '')
region=form.get('region', '')

#range values
range_surface_area = form.get('range_surface_area', '')
method_range = form.get('method_range', '')
conclusion_range = form.get('conclusion_range', '')
range_trend = form.get('range_trend', '')
range_yearly_magnitude = form.get('range_yearly_magnitude', '')
complementary_favourable_range = form.get('complementary_favourable_range', '')

#population values
population_size = form.get('population_size', '')
population_size_unit = form.get('population_size_unit', '')
method_population = form.get('method_population', '')
conclusion_population = form.get('conclusion_population', '')
population_trend = form.get('population_trend', '')
population_yearly_magnitude = form.get('population_yearly_magnitude', '')
complementary_favourable_population = form.get('complementary_favourable_population', '')

#habitat values
habitat_surface_area = form.get('habitat_surface_area', '')
complementary_suitable_habitat = form.get('complementary_suitable_habitat', '')
method_habitat = form.get('method_habitat', '')
conclusion_habitat = form.get('conclusion_habitat', '')
habitat_trend = form.get('habitat_trend', '')

#future values
method_future = form.get('method_future', '')
conclusion_future = form.get('conclusion_future', '')

#assessment values
method_assessment = form.get('method_assessment', '')
conclusion_assessment = form.get('conclusion_assessment', '')

#
# STEP 1: validate form values
#
if not context.validate_field(range_surface_area):
    session.set('range-error', '')   #marker
    session.set('range_surface_area_error', NOT_NUMERIC_VALUES) #error message
    valid_data = False

if not context.validate_field(complementary_favourable_range):
    session.set('range-error', '')
    session.set('complementary_favourable_range_error', NOT_NUMERIC_VALUES)
    valid_data = False

if not context.validate_field(range_yearly_magnitude):
    session.set('range-error', '')
    session.set('range_yearly_magnitude_error', NOT_NUMERIC_VALUES)
    valid_data = False

if not context.validate_field(population_size):
    session.set('population-error', '')
    session.set('population_size_error', NOT_NUMERIC_VALUES)
    valid_data = False

if not context.validate_field(complementary_favourable_population):
    session.set('population-error', '')
    session.set('complementary_favourable_population_error', NOT_NUMERIC_VALUES)
    valid_data = False

if not context.validate_field(population_yearly_magnitude):
    session.set('population-error', '')
    session.set('population_yearly_magnitude_error', NOT_NUMERIC_VALUES)
    valid_data = False

if not context.validate_field(habitat_surface_area):
    session.set('habitat-error', '')
    session.set('habitat_surface_area_error', NOT_NUMERIC_VALUES)
    valid_data = False

if not context.validate_field(complementary_suitable_habitat):
    session.set('habitat-error', '')
    session.set('complementary_suitable_habitat_error', NOT_NUMERIC_VALUES)
    valid_data = False

#
# STEP 2: check if at least one field has been filled
#

if not (range_surface_area or conclusion_range or range_trend or complementary_favourable_range or \
        population_size or population_size_unit or conclusion_population or population_trend or \
        complementary_favourable_population or habitat_surface_area or conclusion_habitat or \
        habitat_trend or complementary_suitable_habitat or conclusion_future or conclusion_assessment):
    session.set('general-error', '')
    session.set('general_method_error', FIELD_MANDATORY)
    valid_data = False

#
# STEP 3: check if already exists a conclusion for the same MS
#

conclusions = context.sql_methods.lookup_user_conclusions(bioregion=region, speciesname=assesment_speciesname, username=auth_user)
for concl in conclusions:
    if concl['MS'] == ms:
        session.set('warning-error', 'You already added a conclusion for %s. <br /> You can only edit the existing one.' % ms)
        valid_data = False
        break

#
# STEP 4: compare
#

if ms == 'EU25':
    if valid_data and enable_warning:
        ok_conclusions = context.sql_methods.lookup_OK_manual_assessment(assesment_speciesname=assesment_speciesname, region=region)
        errors = []
        for record in ok_conclusions:
            #range
            if range_surface_area and range_surface_area == record['range_surface_area']:
                errors.append('Surface (range)')
            if conclusion_range and conclusion_range == record['conclusion_range']:
                errors.append('Conclusion (range)')
            if range_trend and range_trend == record['range_trend']:
                errors.append('Trend (range)')
            if complementary_favourable_range and complementary_favourable_range == record['complementary_favourable_range']:
                errors.append('Ref. (range)')
            #population
            if population_size and population_size == record['population_size']:
                errors.append('Size (population)')
            if population_size_unit and population_size_unit == record['population_size_unit']:
                errors.append('Unit (population)')
            if conclusion_population and conclusion_population == record['conclusion_population']:
                errors.append('Conclusion (population)')
            if population_trend and population_trend == record['population_trend']:
                errors.append('Trend (population)')
            if complementary_favourable_population and complementary_favourable_population == record['complementary_favourable_population']:
                errors.append('Ref. (population)')
            #habitat
            if habitat_surface_area and habitat_surface_area == record['habitat_surface_area']:
                errors.append('Area (habitat)')
            if conclusion_habitat and conclusion_habitat == record['conclusion_habitat']:
                errors.append('Conclusion (habitat)')
            if habitat_trend and habitat_trend == record['habitat_trend']:
                errors.append('Trend (habitat)')
            if complementary_suitable_habitat and complementary_suitable_habitat == record['complementary_suitable_habitat']:
                errors.append('Suitable (habitat)')
            #future prospects
            if conclusion_future and conclusion_future == record['conclusion_future']:
                errors.append('Conclusion (future prosp.)')
            #overall assessment
            if conclusion_assessment and conclusion_assessment == record['conclusion_assessment']:
                errors.append('Conclusion (overall asses.)')
        if errors:
            error_description = "As you selected EU25, you can comment by providing a correction on ETC/BD biogeographical assessments, so the values should be different that those provided by the ETC/BD. The following fields are identical and must be changed:"
            session.set('warning-error', '%s <br /> %s' % (error_description, '<br />'.join(errors)))
            valid_data = False
        else:
            session.set('warning-valid-error', '')
            valid_data = False
else:
    if valid_data and enable_warning:
        assessment = context.sql_methods.lookup_country_assessment(assesment_speciesname=assesment_speciesname, region=region, eu_country_code=ms)
        errors = []
        for record in assessment:
            #range
            if range_surface_area and range_surface_area == context.str2num(record['range_surface_area']):
                errors.append('Surface (range)')
            if conclusion_range and conclusion_range == record['conclusion_range']:
                errors.append('Conclusion (range)')
            if range_trend and range_trend == record['range_trend']:
                errors.append('Trend (range)')
            if complementary_favourable_range and complementary_favourable_range == '%s%s' % (record['complementary_favourable_range_q'], record['complementary_favourable_range']):
                errors.append('Ref. (range)')
            #population
            if population_size and population_size_unit:
                if '%s %s' % (population_size, population_size_unit) == record['population_size_unit']:
                    errors.append('Size&Unit (population)')
            if conclusion_population and conclusion_population == record['conclusion_population']:
                errors.append('Conclusion (population)')
            if population_trend and population_trend == record['population_trend']:
                errors.append('Trend (population)')
            if complementary_favourable_population and complementary_favourable_population == '%s%s' % (record['complementary_favourable_population_q'], record['complementary_favourable_population']):
                errors.append('Ref. (population)')
            #habitat
            if habitat_surface_area and habitat_surface_area == context.str2num(record['habitat_surface_area']):
                errors.append('Area (habitat)')
            if conclusion_habitat and conclusion_habitat == record['conclusion_habitat']:
                errors.append('Conclusion (habitat)')
            if habitat_trend and habitat_trend == record['habitat_trend']:
                errors.append('Trend (habitat)')
            if complementary_suitable_habitat and complementary_suitable_habitat == context.str2num(record['complementary_suitable_habitat']):
                errors.append('Suitable (habitat)')
            #future prospects
            if conclusion_future and conclusion_future == record['conclusion_future']:
                errors.append('Conclusion (future prosp.)')
            #overall assessment
            if conclusion_assessment and conclusion_assessment == record['conclusion_assessment']:
                errors.append('Conclusion (overall asses.)')

        if errors:
            error_description = "As you selected a certain MS, you can comment by providing a correction on MS biogeographical assessments, so the values should be different that those provided by the MS. The following fields are identical and must be changed:"
            session.set('warning-error', '%s <br /> %s' % (error_description, '<br />'.join(errors)))
            valid_data = False
        else:
            session.set('warning-valid-error', '')
            valid_data = False

if valid_data:
    #insert data in database
    context.sql_methods.insert_manual_assesment(MS=ms, region=region, assesment_speciesname=assesment_speciesname, 
                        range_surface_area=range_surface_area, method_range=method_range, range_trend=range_trend, range_yearly_magnitude=range_yearly_magnitude, complementary_favourable_range=complementary_favourable_range, conclusion_range=conclusion_range,
                        population_size=population_size, population_size_unit=population_size_unit, method_population=method_population, population_trend=population_trend, population_yearly_magnitude=population_yearly_magnitude, complementary_favourable_population=complementary_favourable_population, conclusion_population=conclusion_population, 
                        habitat_surface_area=habitat_surface_area, method_habitat=method_habitat, habitat_trend=habitat_trend, complementary_suitable_habitat=complementary_suitable_habitat, conclusion_habitat=conclusion_habitat, 
                        conclusion_future=conclusion_future, method_future=method_future, 
                        method_assessment=method_assessment, conclusion_assessment=conclusion_assessment, 
                        user=auth_user, last_update=DateTime().strftime('%Y-%m-%d %H:%M'), deleted_record=form.get('deleted_record', 0), 
                        decision=form.get('decision', ''), user_decision=form.get('user_decision', ''), last_update_decision=form.get('last_update_decision'))
else:
    #put data on session
    session.set('ms', ms)
    session.set('range_surface_area', range_surface_area)
    session.set('method_range', method_range)
    session.set('conclusion_range', conclusion_range)
    session.set('range_trend', range_trend)
    session.set('range_yearly_magnitude', range_yearly_magnitude)
    session.set('complementary_favourable_range', complementary_favourable_range)

    session.set('population_size', population_size)
    session.set('population_size_unit', population_size_unit)
    session.set('method_population', method_population)
    session.set('conclusion_population', conclusion_population)
    session.set('population_trend', population_trend)
    session.set('population_yearly_magnitude', population_yearly_magnitude)
    session.set('complementary_favourable_population', complementary_favourable_population)

    session.set('habitat_surface_area', habitat_surface_area)
    session.set('method_habitat', method_habitat)
    session.set('conclusion_habitat', conclusion_habitat)
    session.set('habitat_trend', habitat_trend)
    session.set('complementary_suitable_habitat', complementary_suitable_habitat)

    session.set('conclusion_future', conclusion_future)
    session.set('method_future', method_future)

    session.set('method_assessment', method_assessment)
    session.set('conclusion_assessment', conclusion_assessment)

return RESPONSE.redirect(request.HTTP_REFERER)
