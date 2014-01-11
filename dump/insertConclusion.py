# Script (Python)
# /article17/speciessummary/insertConclusion
# params: ''
## Script (Python) "insertConclusion"
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
METH_CONCL_MANDATORY = "At leat one method and conclusion must be filled!"
METH_CONCL_PAIR_MANDATORY = "You cannot add a conclusion without a method and nor a method without a conclusion"
METH_CONCL_MISS_MATCHED = "%s miss matched %s"

request = container.REQUEST
RESPONSE =  request.RESPONSE
session = request.SESSION
form = request.form
valid_data = True
enable_warning = form.get('enable-warning', '1')

#
#load data from request
#

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
# STEP 2: check if at least one method and conclusion has been filled
#

if not (method_range and conclusion_range or \
        method_population and conclusion_population or \
        method_habitat and conclusion_habitat or \
        method_future and conclusion_future or \
        method_assessment and conclusion_assessment):
    session.set('general-error', '')
    session.set('general_method_error', METH_CONCL_MANDATORY)
    valid_data = False

#
# STEP 3: check if for all conclusions added there is a corresponding method selected
#

if (method_range and not conclusion_range) or (not method_range and conclusion_range):
    session.set('range-error', '')
    session.set('method_range_error', METH_CONCL_PAIR_MANDATORY)
    valid_data = False

if (method_population and not conclusion_population) or (not method_population and conclusion_population):
    session.set('population-error', '')
    session.set('method_population_error', METH_CONCL_PAIR_MANDATORY)
    valid_data = False


if (method_habitat and not conclusion_habitat) or (not method_habitat and conclusion_habitat):
    session.set('habitat-error', '')
    session.set('method_habitat_error', METH_CONCL_PAIR_MANDATORY)
    valid_data = False


if (method_future and not conclusion_future) or (not method_future and conclusion_future):
    session.set('future-error', '')
    session.set('method_future_error', METH_CONCL_PAIR_MANDATORY)
    valid_data = False


if (method_assessment and not conclusion_assessment) or (not method_assessment and conclusion_assessment):
    session.set('assesment-error', '')
    session.set('method_assessment_error', METH_CONCL_PAIR_MANDATORY)
    valid_data = False

#
# STEP 4: warning
#
if valid_data and enable_warning:
    errors = []
    valid = []
    records = context.sql_methods.lookup_method_conclusions(assesment_speciesname=form.get('assesment_speciesname', ''), region=form.get('region', ''))
    for record in records:
        if method_range == record['assessment_method'] and conclusion_range != record['conclusion_range']:
            errors.append(METH_CONCL_MISS_MATCHED % (method_range, conclusion_range))
        if method_population == record['assessment_method'] and conclusion_population != record['conclusion_population']:
            errors.append(METH_CONCL_MISS_MATCHED % (method_population, conclusion_population))
        if method_habitat == record['assessment_method'] and conclusion_habitat != record['conclusion_habitat']:
            errors.append(METH_CONCL_MISS_MATCHED % (method_habitat, conclusion_habitat))
        if method_future == record['assessment_method'] and conclusion_future != record['conclusion_future']:
            errors.append(METH_CONCL_MISS_MATCHED % (method_future, conclusion_future))
        if method_assessment == record['assessment_method'] and conclusion_assessment != record['conclusion_assessment']:
            errors.append(METH_CONCL_MISS_MATCHED % (method_assessment, conclusion_assessment))

    if method_assessment == 'MTX':
        if method_range not in valid:
            valid.append(method_range)
        if method_population not in valid:
            valid.append(method_population)
        if method_habitat not in valid:
            valid.append(method_habitat)
        if method_future not in valid:
            valid.append(method_future)

    if len(valid)>2 or errors:
        session.set('warning-error', '')
        valid_data = False

if valid_data:
    #insert data in database
    context.sql_methods.insert_manual_assesment(MS='EU25', region=form.get('region', ''), assesment_speciesname=form.get('assesment_speciesname', ''), 
                        range_surface_area=range_surface_area, method_range=method_range, range_trend=range_trend, range_yearly_magnitude=range_yearly_magnitude, complementary_favourable_range=complementary_favourable_range, conclusion_range=conclusion_range,
                        population_size=population_size, population_size_unit=population_size_unit, method_population=method_population, population_trend=population_trend, population_yearly_magnitude=population_yearly_magnitude, complementary_favourable_population=complementary_favourable_population, conclusion_population=conclusion_population, 
                        habitat_surface_area=habitat_surface_area, method_habitat=method_habitat, habitat_trend=habitat_trend, complementary_suitable_habitat=complementary_suitable_habitat, conclusion_habitat=conclusion_habitat, 
                        conclusion_future=conclusion_future, method_future=method_future, 
                        method_assessment=method_assessment, conclusion_assessment=conclusion_assessment, 
                        user=request.AUTHENTICATED_USER, last_update=DateTime().strftime('%Y-%m-%d %H:%M'), deleted_record=form.get('deleted_record', 0), 
                        decision=form.get('decision', ''), user_decision=form.get('user_decision', ''), last_update_decision=form.get('last_update_decision'))
else:
    #put data on session
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
