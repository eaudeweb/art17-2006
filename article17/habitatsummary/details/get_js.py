# Script (Python)
# /article17/habitatsummary/details/get_js
# params: 'region, habitat'
## Script (Python) "get_js"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=region, habitat
##title=
##
return """<script type="text/javascript">
	childPopups  = new Array();
	childPopupNr = 0;
	var so = new SWFObject("flamingo.swf?config=config_xml?region=%s%%26habitat%%3D%s%%26", "flamingo", "100%%", "100%%", "8", "#eaeaea");
	so.write("flashcontent");
</script>""" % (region, habitat)
