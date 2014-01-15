# Script (Python)
# /article17/habitatsummary/updateConclusion
# params: ''
## Script (Python) "updateConclusion"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
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

habitat = form.get('habitat', '')
group = form.get('group', '')
region = form.get('region', '')
decision = form.get('decision', '')

#range values
range_surface_area = form.get('range_surface_area', '')
method_range = form.get('method_range', '')
conclusion_range = form.get('conclusion_range', '')
range_trend = form.get('range_trend', '')
range_yearly_magnitude = form.get('range_yearly_magnitude', '')
complementary_favourable_range = form.get('complementary_favourable_range', '')

#coverage values
coverage_surface_area = form.get('coverage_surface_area', '')
method_area = form.get('method_area', '')
conclusion_area = form.get('conclusion_area', '')
coverage_trend = form.get('coverage_trend', '')
coverage_yearly_magnitude = form.get('coverage_yearly_magnitude', '')
complementary_favourable_area = form.get('complementary_favourable_area', '')

#structure values
method_structure = form.get('method_structure', '')
conclusion_structure = form.get('conclusion_structure', '')

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

if not context.validate_field(coverage_surface_area):
    session.set('coverage-error', '')
    session.set('coverage_surface_area_error', NOT_NUMERIC_VALUES)
    valid_data = False

if not context.validate_field(coverage_yearly_magnitude):
    session.set('coverage-error', '')
    session.set('coverage_yearly_magnitude_error', NOT_NUMERIC_VALUES)
    valid_data = False

if not context.validate_field(complementary_favourable_area):
    session.set('coverage-error', '')
    session.set('complementary_favourable_area_error', NOT_NUMERIC_VALUES)
    valid_data = False


#
# STEP 2: check if at least one method and conclusion has been filled
#

if not (method_range and conclusion_range or \
        method_area and conclusion_area or \
        method_structure and conclusion_structure or \
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

if (method_area and not conclusion_area) or (not method_area and conclusion_area):
    session.set('coverage-error', '')
    session.set('method_area_error', METH_CONCL_PAIR_MANDATORY)
    valid_data = False

if (method_structure and not conclusion_structure) or (not method_structure and conclusion_structure):
    session.set('structure-error', '')
    session.set('method_structure_error', METH_CONCL_PAIR_MANDATORY)
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

    records = context.sql_methods.lookup_method_conclusions(habitatcode=habitat, region=region)
    for record in records:
        if method_range == record['assessment_method'] and conclusion_range != record['conclusion_range']:
            errors.append(METH_CONCL_MISS_MATCHED % (method_range, conclusion_range))
        if method_area == record['assessment_method'] and conclusion_area != record['conclusion_coverage']:
            errors.append(METH_CONCL_MISS_MATCHED % (method_area, conclusion_area))
        if method_structure == record['assessment_method'] and conclusion_structure != record['conclusion_structure']:
            errors.append(METH_CONCL_MISS_MATCHED % (method_structure, conclusion_structure))
        if method_future == record['assessment_method'] and conclusion_future != record['conclusion_future']:
            errors.append(METH_CONCL_MISS_MATCHED % (method_future, conclusion_future))
        if method_assessment == record['assessment_method'] and conclusion_assessment != record['conclusion_assessment']:
            errors.append(METH_CONCL_MISS_MATCHED % (method_assessment, conclusion_assessment))

    if method_assessment == 'MTX':
        if method_range not in valid:
            valid.append(method_range)
        if method_area not in valid:
            valid.append(method_area)
        if method_structure not in valid:
            valid.append(method_structure)
        if method_future not in valid:
            valid.append(method_future)

    if len(valid)>2 or errors:
        session.set('warning-error', '')
        valid_data = False

if valid_data:
    if decision == 'OK':
        decision = 'OK?'
    else:
        decision = ''
    #insert data in database
    context.sql_methods.update_user_habitat_manual_assesment(MS='EU25', region=region,
                                habitatcode=habitat, range_surface_area=range_surface_area,
                                range_trend=range_trend, range_yearly_magnitude=range_yearly_magnitude,
                                coverage_yearly_magnitude=coverage_yearly_magnitude, complementary_favourable_range=complementary_favourable_range,
                                coverage_surface_area=coverage_surface_area, coverage_trend=coverage_trend,
                                complementary_favourable_area=complementary_favourable_area, method_range=method_range,
                                conclusion_range=conclusion_range, method_area=method_area,
                                conclusion_area=conclusion_area, method_structure=method_structure,
                                conclusion_structure=conclusion_structure, method_future=method_future,
                                conclusion_future=conclusion_future, method_assessment=method_assessment,
                                conclusion_assessment=conclusion_assessment, user=request.AUTHENTICATED_USER, 
                                last_update=DateTime().strftime('%Y-%m-%d %H:%M'), decision=decision)
    return RESPONSE.redirect('%s?group=%s&habitat=%s&region=%s' % (context.absolute_url(), group, habitat, region))
else:
    #put data on session
    session.set('range_surface_area', range_surface_area)
    session.set('method_range', method_range)
    session.set('conclusion_range', conclusion_range)
    session.set('range_trend', range_trend)
    session.set('range_yearly_magnitude', range_yearly_magnitude)
    session.set('complementary_favourable_range', complementary_favourable_range)

    session.set('coverage_surface_area', coverage_surface_area)
    session.set('method_area', method_area)
    session.set('conclusion_area', conclusion_area)
    session.set('coverage_trend', coverage_trend)
    session.set('coverage_yearly_magnitude', coverage_yearly_magnitude)
    session.set('complementary_favourable_area', complementary_favourable_area)

    session.set('conclusion_structure', conclusion_structure)
    session.set('method_structure', method_structure)

    session.set('conclusion_future', conclusion_future)
    session.set('method_future', method_future)

    session.set('method_assessment', method_assessment)
    session.set('conclusion_assessment', conclusion_assessment)
    return RESPONSE.redirect(request.HTTP_REFERER)
