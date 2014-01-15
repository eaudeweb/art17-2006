# Script (Python)
# /article17/habitatsummary/details/config_xml
# params: 'region, habitat'
## Script (Python) "config_xml"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=region, habitat
##title=
##
request = context.REQUEST
from Products.PythonScripts.standard import html_quote, url_quote

if region == '':
   region = '/%s/' % context.getRegions(habitat)
else:
   region = "/^%s/" % region
results = context.select_habitat_countries(region=region[1:-1].replace('^', '').split('|'), Habitatcode=habitat)

countries_style = []
countries = []
habitat_code = ''

for res in results:
    if res['eu_country_code'] == 'UK':
        country = 'GB'
    else: 
        if res['eu_country_code'] == 'EL':
           country = 'GR'
        else:
           country = res['eu_country_code']
    habitat_code = res['code']
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
        <item canhide="true" infourl="" label="Art17 Dissolved Dist." listento="OG10"/>
      </group>
      <group label="Base map" open="true">
        <item canhide="true" label="Land/Water" listento="OG5" infourl=""/>
        <item canhide="true" label="Borders & Boundaries" listento="OG13" infourl=""/>
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
        <fmc:LayerOGWMS id="OG10" format="PNG" url="art17ws?VERSION=1.1.1&SERVICE=WMS&SRS=EPSG:3035&EXCEPTIONS=INIMAGE&spc='%s'&method=art17wsGridDistH" QUERY_LAYERS="" LAYERS="art_17_Map_Distribution"/>
        <fmc:LayerOGWMS id="OG13" format="PNG" visible="false" url="art17ws?method=art17wsLineWork" VERSION="1.1.1" SERVICE="WMS" SRS="EPSG:3035" EXCEPTIONS="INIMAGE" QUERY_LAYERS="" LAYERS="Art_17_linework"/>
        <fmc:LayerOGWMS id="OG1" format="PNG" url="art17ws?VERSION=1.1.1&SERVICE=WMS&EXCEPTIONS=INIMAGE&%s&method=art17ws.py" SRS="EPSG:3035" QUERY_LAYERS="" LAYERS="Europe_BIOGEO_MERGE30Jan"/>
        <fmc:LayerOGWMS id="OG14" format="PNG" url="art17ws?rg=%s&method=art17wsEU25Zones" VERSION="1.1.1" SERVICE="WMS" SRS="EPSG:3035" EXCEPTIONS="INIMAGE" QUERY_LAYERS="" LAYERS="EU_25_biogeographical_Regions"/>
        <fmc:LayerOGWMS id="OG5" format="PNG" url="art17ws?method=art17wsBKG" VERSION="1.1.1" SERVICE="WMS" SRS="EPSG:3035" EXCEPTIONS="INIMAGE" QUERY_LAYERS="" LAYERS="Europe_BIOGEO_MERGE30Jan"/>
    
      </fmc:Map>
    </fmc:Container>

     <fmc:Map id="overview" right="right -10" top="10" width="100" height="100" extent="371363.8956955,-375446.023944,8078238.5599865,7331428.640347" fullextent="371363.8956955,-375446.023944,8078238.5599865,7331428.640347">
        <fmc:LayerOverview listento="map1" followfactor="600"/>
        <fmc:LayerOGWMS id="OverviewCountries" format="PNG" url="art17ws?method=art17wsCountries" VERSION="1.1.1" SERVICE="WMS" SRS="EPSG:3035" EXCEPTIONS="INIMAGE" QUERY_LAYERS="" LAYERS="Countries" extent="371363.8956955,-375446.023944,8078238.5599865,7331428.640347"/>
        <fmc:LayerOGWMS id="OverviewEurope" format="PNG" url="art17ws?method=art17wsBKG" VERSION="1.1.1" SERVICE="WMS" SRS="EPSG:3035" EXCEPTIONS="INIMAGE" QUERY_LAYERS="" LAYERS="Europe_BIOGEO_MERGE30Jan" extent="371363.8956955,-375446.023944,8078238.5599865,7331428.640347"/>
     </fmc:Map>

    
</FLAMINGO>""" % (','.join(extent), habitat_code, '&'.join(countries_style), region)

#request.RESPONSE.setHeader('Content-Type', 'text/xml')
return xml_output
