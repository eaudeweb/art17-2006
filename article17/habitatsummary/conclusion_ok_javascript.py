# Script (Python)
# /article17/habitatsummary/conclusion_ok_javascript
# params: ''
## Script (Python) "conclusion_ok_javascript"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
return """
<script type="text/javascript">
<!--
	// put Yahoo class on body
	YAHOO.util.Dom.addClass(document.body, 'yui-skin-sam');

	// Define various event handlers for Dialog
	var handleOK = function() {
		var warning = document.getElementById('enable-warning');
		warning.value = "";
		form = document.getElementById('conclusion_form');
		form.submit();
		this.hide();
	};

	// Instantiate the Dialog
	warn_ok_dialog = new YAHOO.widget.SimpleDialog("warn_ok_dialog", 
					 { width: "300px", fixedcenter: true, visible: false, draggable: false,
					 close: false, icon: YAHOO.widget.SimpleDialog.ICON_WARN, constraintoviewport: true,
					 buttons: [ {text:"OK",  handler:handleOK} ]} );
	warn_ok_dialog.setHeader("Warning!"); 
	warn_ok_dialog.setBody("In order for this assessment to be relevant for this consultation you must provide explantations regarding the modification you find necessary in <strong>Comments</strong> area of your assessment."); 
	warn_ok_dialog.render("warning_container"); 
//-->
</script> """
