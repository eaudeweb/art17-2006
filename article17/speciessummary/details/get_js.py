# Script (Python)
# /article17/speciessummary/details/get_js
# params: 'region, species'
## Script (Python) "get_js"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=region, species
##title=
##
return """<script type="text/javascript">
	childPopups  = new Array();
	childPopupNr = 0;
	var so = new SWFObject("flamingo.swf?config=config_xml?region=%s%%26species%%3D%s%%26", "flamingo", "100%%", "100%%", "8", "#eaeaea");
	so.write("flashcontent");
</script>""" % (region, species)
