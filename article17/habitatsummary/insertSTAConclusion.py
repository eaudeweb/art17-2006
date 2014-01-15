# Script (Python)
# /article17/habitatsummary/insertSTAConclusion
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
from DateTime import DateTime

request = container.REQUEST
RESPONSE =  request.RESPONSE
session = request.SESSION
form = request.form

auth_user = request.AUTHENTICATED_USER.getUserName()
valid_data = True
enable_warning = form.get('enable-warning', '1')

NOT_NUMERIC_VALUES = "Only numeric values with not more than two decimals are accepted!"
FIELD_MANDATORY = "In order to provide a correction at least one field must be filled!"
#
#load data from request
#

#MS
ms = form.get('ms', '')
habitatcode=form.get('habitatcode', '')
region=form.get('region', '')

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

if not context.validate_field(coverage_surface_area):
    session.set('coverage-error', '')
    session.set('coverage_surface_area_error', NOT_NUMERIC_VALUES)
    valid_data = False

if not context.validate_field(complementary_favourable_area):
    session.set('coverage-error', '')
    session.set('complementary_favourable_area_error', NOT_NUMERIC_VALUES)
    valid_data = False

#
# STEP 2: check if at least one field has been filled
#

if not (range_surface_area or conclusion_range or range_trend or complementary_favourable_range or \
        coverage_surface_area or conclusion_area or coverage_trend or complementary_favourable_area or \
        conclusion_structure or conclusion_future or conclusion_assessment):
    session.set('general-error', '')
    session.set('general_method_error', FIELD_MANDATORY)
    valid_data = False

#
# STEP 3: check if already exists a conclusion for the same MS
#

conclusions = context.sql_methods.lookup_user_conclusions(region=region, habitatcode=habitatcode, user=auth_user)
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
        ok_conclusions = context.sql_methods.lookup_OK_manual_assessment(habitatcode=habitatcode, region=region)
        errors = []
        for record in ok_conclusions:
            #range
            if range_surface_area and range_surface_area == context.str2num(record['range_surface_area']):
                errors.append('Surface (range)')
            if conclusion_range and conclusion_range == record['conclusion_range']:
                errors.append('Conclusion (range)')
            if range_trend and range_trend == record['range_trend']:
                errors.append('Trend (range)')
            if complementary_favourable_range and complementary_favourable_range == context.str2num(record['complementary_favourable_range']):
                errors.append('Ref. (range)')
            #area
            if coverage_surface_area and coverage_surface_area == context.str2num(record['coverage_surface_area']):
                errors.append('Surface (area)')
            if conclusion_area and conclusion_area == record['conclusion_area']:
                errors.append('Conclusion (area)')
            if coverage_trend and coverage_trend == record['coverage_trend']:
                errors.append('Trend (area)')
            if complementary_favourable_area and complementary_favourable_area == context.str2num(record['complementary_favourable_area']):
                errors.append('Ref. (area)')
            #struct&func
            if conclusion_structure and conclusion_structure == record['conclusion_structure']:
                errors.append('Conclusion (struct. & funct.)')
            #Future prosp.
            if conclusion_future and conclusion_future == record['conclusion_future']:
                errors.append('Conclusion (future prosp.)')
            #Overall asses.
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
        assessment = context.sql_methods.lookup_country_assessment(habitatcode=habitatcode, region=region, eu_country_code=ms)
        errors = []
        for record in assessment:
            #range
            if range_surface_area and range_surface_area == context.str2num(record['range_surface_area']):
                errors.append('Surface (range)')
            if conclusion_range and conclusion_range == record['conclusion_range']:
                errors.append('Conclusion (range)')
            if range_trend and range_trend == record['range_trend']:
                errors.append('Trend (range)')
            if complementary_favourable_range and complementary_favourable_range == '%s%s' % (record['complementary_favourable_range_q'], context.str2num(record['complementary_favourable_range'])):
                errors.append('Ref. (range)')
            #area
            if coverage_surface_area and coverage_surface_area == context.str2num(record['coverage_surface_area']):
                errors.append('Surface (area)')
            if conclusion_area and conclusion_area == record['conclusion_area']:
                errors.append('Conclusion (area)')
            if coverage_trend and coverage_trend == record['coverage_trend']:
                errors.append('Trend (area)')
            if complementary_favourable_area and complementary_favourable_area == '%s%s' % (record['complementary_favourable_area_q'], context.str2num(record['complementary_favourable_area'])):
                errors.append('Ref. (area)')
            #struct&func
            if conclusion_structure and conclusion_structure == record['conclusion_structure']:
                errors.append('Conclusion (struct. & funct.)')
            #Future prosp.
            if conclusion_future and conclusion_future == record['conclusion_future']:
                errors.append('Conclusion (future prosp.)')
            #Overall asses.
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
    context.sql_methods.insert_habitat_manual_assesment(MS=ms, region=region, habitatcode=habitatcode,
                            range_surface_area=range_surface_area, range_trend=range_trend, range_yearly_magnitude=range_yearly_magnitude,
                            coverage_yearly_magnitude=coverage_yearly_magnitude, complementary_favourable_range=complementary_favourable_range,
                            coverage_surface_area=coverage_surface_area, coverage_trend=coverage_trend,
                            complementary_favourable_area=complementary_favourable_area, method_range=method_range,
                            conclusion_range=conclusion_range, method_area=method_area, conclusion_area=conclusion_area,
                            method_structure=method_structure, conclusion_structure=conclusion_structure,
                            method_future=method_future, conclusion_future=conclusion_future,
                            method_assessment=method_assessment, conclusion_assessment=conclusion_assessment,
                            user=auth_user, last_update=DateTime().strftime('%Y-%m-%d %H:%M'), 
                            deleted_record=request.form.get('deleted_record', 0), decision=request.form.get('decision', ''),
                            user_decision=request.form.get('user_decision', ''), last_update_decision=request.form.get('last_update_decision', ''))
else:
    #put data on session
    session.set('ms', ms)
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
