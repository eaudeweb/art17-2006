# Script (Python)
# /article17/speciessummary/details/copy_of_config_xml
# params: "region='', species=''"
## Script (Python) "copy_of_config_xml"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=region='', species=''
##title=
##
request = context.REQUEST
from Products.PythonScripts.standard import html_quote, url_quote

if region == '':
   #region = '/MMED|MED|ATL|ALP|CON|PAN|BOR|MAC/'
   region = '/%s/' % context.getRegions(species)
else:
   region = "/^%s/" % region
results = context.select_species_countries(region=region[1:-1].replace('^', '').split('|'), assesment_speciesname=context.string_decode(species))
assesment_speciesname=url_quote(context.string_decode(species))

countries_style = []
countries = []
species_code = ''


for res in results:
    if res['eu_country_code'] == 'UK':
        country = 'GB'
    else: 
        if res['eu_country_code'] == 'EL':
           country = 'GR'
        else:
           country = res['eu_country_code']
    species_code = res['code']
    countries.append(country)
    countries_style.append('l=%s%s|%s' % (country, res['region'], context.background_colour(res['conclusion_assessment'])))

qstring="/%s/" % '|'.join(countries)
extent = context.get_coordinates(region, qstring)

xml_output = """
<?xml version="1.0" encoding="UTF-8"?>
<FLAMINGO xmlns:fmc="fmc" lang="en" tooltipdelay="500" maxwidth="680" maxheight="400" borderwidth="0">
    <fmc:Logo id="logo"/>

    <fmc:Legend left="right -140" top="120" bottom="bottom -30" right="right -2" listento="map1">
      <group label="Assess. layers" open="true">
        <item canhide="true" infourl="" label="Overall Assess." listento="OG1"/>
        <item canhide="true" infourl="" label="MS range poly" listento="OG2"/>
        <item canhide="true" infourl="" label="ETC/BD range grid" listento="OG11"/>
        <item canhide="true" infourl="" label="MS distrib. poly" listento="OG4"/>
        <item canhide="true" infourl="" label="MS distrib. points" listento="OG3"/>
        <item canhide="true" infourl="" label="ETC/BD distrib. grid" listento="OG10"/>
      </group>
      <group label="Base map" open="true">
        <item canhide="true" label="Land/Water" listento="OG5" infourl=""/>
        <item canhide="true" label="LineWork" listento="OG13" infourl=""/>
        <item canhide="true" label="Countries" listento="OG7" infourl=""/>
        <item canhide="true" label="Borders" listento="OG12" infourl=""/>
        <item canhide="true" label="BioGeo Zones" listento="OG6" infourl=""/>
        <item canhide="true" label="EU25 BioGeo Zones" listento="OG14" infourl=""/>
      </group>
    </fmc:Legend>

    <fmc:ToolGroup listento="map1" left="10" top="10">
        <fmc:ToolPan left="60" clickdelay="0" pandelay="0"/>
        <fmc:ToolZoomin left="0" zoomdelay="0" clickdelay="0"/>
        <fmc:ToolZoomout left="30" zoomdelay="0" clickdelay="0"/>
    </fmc:ToolGroup>
    <fmc:ButtonPrev left="108" top="12" listento="map1"/>
    <fmc:ButtonNext left="138" top="12" listento="map1"/>
    <fmc:ButtonFull left="168" top="12" listento="map1"/>


   
    <fmc:MonitorLayer id="monitor" left="14" top="50" skin="f1" listento="map1"/>
    <fmc:Container borderwidth="0" bordercolor="#b8b8b8" left="0" top="0" bottom="bottom -0" right="right -150">
      <fmc:BorderNavigation skin="F1" width="100%%" height="100%%" listento="map1"/>
      <fmc:Map id="map1" movequality="HIGH" left="0" top="0" bottom="bottom" right="right" visible="true" extenthistory="4" extent="%s" fullextent="371363.8956955,-375446.023944,8078238.5599865,7331428.640347">
        <fmc:LayerIdentifyIcon id="identifyicon" />
        <fmc:LayerOGWMS id="OG13" format="PNG" visible="false" url="art17ws?method=art17wsLineWork" VERSION="1.1.1" SERVICE="WMS" SRS="EPSG:3035" EXCEPTIONS="INIMAGE" QUERY_LAYERS="" LAYERS="Art_17_linework"/>
        <fmc:LayerOGWMS id="OG7" format="PNG" visible="false" url="art17ws?method=art17wsCountries" VERSION="1.1.1" SERVICE="WMS" SRS="EPSG:3035" EXCEPTIONS="INIMAGE" QUERY_LAYERS="" LAYERS="Countries"/>
        <fmc:LayerOGWMS id="OG12" format="PNG" url="art17ws?method=art17wsLines" VERSION="1.1.1" SERVICE="WMS" SRS="EPSG:3035" EXCEPTIONS="INIMAGE" QUERY_LAYERS="" LAYERS="Art_17_lines"/>
        <fmc:LayerOGWMS id="OG10" format="PNG" url="art17ws?VERSION=1.1.1&SERVICE=WMS&SRS=EPSG:3035&EXCEPTIONS=INIMAGE&spc='%s'&method=art17wsGridDistS" QUERY_LAYERS="" LAYERS="Art_17_Dissolved_GriddedMaps"/>
        <fmc:LayerOGWMS id="OG11" format="PNG" visible="false" url="art17ws?VERSION=1.1.1&SERVICE=WMS&SRS=EPSG:3035&EXCEPTIONS=INIMAGE&spc='%s'&method=art17wsGridRangeS" QUERY_LAYERS="" LAYERS="Art_17_Dissolved_GriddedMaps"/>
        <fmc:LayerOGWMS id="OG4" format="PNG" visible="false" url="art17ws?VERSION=1.1.1&SERVICE=WMS&SRS=EPSG:3035&EXCEPTIONS=INIMAGE&spc='%s'&method=art17wsMSPolyDistS" QUERY_LAYERS="" LAYERS="Polygon"/>
        <fmc:LayerOGWMS id="OG3" format="PNG" visible="false" url="art17ws?VERSION=1.1.1&SERVICE=WMS&SRS=EPSG:3035&EXCEPTIONS=INIMAGE&spc='%s'&method=art17wsMSPointDistS" QUERY_LAYERS="" LAYERS="Point"/>
        <fmc:LayerOGWMS id="OG2" format="PNG" visible="false" url="art17ws?VERSION=1.1.1&SERVICE=WMS&SRS=EPSG:3035&EXCEPTIONS=INIMAGE&spc='%s'&method=art17wsMSPolyRangeS" QUERY_LAYERS="" LAYERS="Polygon"/>
        <fmc:LayerOGWMS id="OG1" format="PNG" url="art17ws?VERSION=1.1.1&SERVICE=WMS&EXCEPTIONS=INIMAGE&%s&method=art17ws.py" SRS="EPSG:3035" QUERY_LAYERS="" LAYERS="Europe_BIOGEO_MERGE30Jan"/>
        <fmc:LayerOGWMS id="OG6" format="PNG" url="art17ws?rg=%s&method=art17wsOutline" VERSION="1.1.1" SERVICE="WMS" SRS="EPSG:3035" EXCEPTIONS="INIMAGE" QUERY_LAYERS="" LAYERS="Europe_BIOGEO_MERGE30Jan"/>
        <fmc:LayerOGWMS id="OG14" format="PNG" url="art17ws?rg=%s&method=art17wsEU25Zones" VERSION="1.1.1" SERVICE="WMS" SRS="EPSG:3035" EXCEPTIONS="INIMAGE" QUERY_LAYERS="" LAYERS="EU_25_biogeographical_Regions"/>
        <fmc:LayerOGWMS id="OG5" format="PNG" url="art17ws?method=art17wsBKG" VERSION="1.1.1" SERVICE="WMS" SRS="EPSG:3035" EXCEPTIONS="INIMAGE" QUERY_LAYERS="" LAYERS="Europe_BIOGEO_MERGE30Jan"/>
      </fmc:Map>
    </fmc:Container>

     <fmc:Map id="overview" right="right -10" top="10" width="100" height="100" extent="371363.8956955,-375446.023944,8078238.5599865,7331428.640347" fullextent="371363.8956955,-375446.023944,8078238.5599865,7331428.640347">
        <fmc:LayerOverview listento="map1" followfactor="600"/>
        <fmc:LayerOGWMS id="OverviewCountries" format="PNG" url="art17ws?method=art17wsCountries" VERSION="1.1.1" SERVICE="WMS" SRS="EPSG:3035" EXCEPTIONS="INIMAGE" QUERY_LAYERS="" LAYERS="Countries" extent="371363.8956955,-375446.023944,8078238.5599865,7331428.640347"/>
        <fmc:LayerOGWMS id="OverviewEurope" format="PNG" url="art17ws?method=art17wsBKG" VERSION="1.1.1" SERVICE="WMS" SRS="EPSG:3035" EXCEPTIONS="INIMAGE" QUERY_LAYERS="" LAYERS="Europe_BIOGEO_MERGE30Jan" extent="371363.8956955,-375446.023944,8078238.5599865,7331428.640347"/>
     </fmc:Map>

    
</FLAMINGO>""" % (','.join(extent), 
		assesment_speciesname, 
		assesment_speciesname, 
		assesment_speciesname, 
		assesment_speciesname, 
		assesment_speciesname, 
		'&'.join(countries_style), 
		region,region)

#request.RESPONSE.setHeader('Content-Type', 'text/xml')
return xml_output
