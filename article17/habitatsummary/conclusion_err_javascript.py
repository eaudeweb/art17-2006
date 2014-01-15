# Script (Python)
# /article17/habitatsummary/conclusion_err_javascript
# params: ''
## Script (Python) "conclusion_err_javascript"
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

	var handleOK = function() {
		this.hide();
	};

	// Instantiate the Dialog
	warn_dialog = new YAHOO.widget.SimpleDialog("warn_err_dialog", 
					 { width: "300px", fixedcenter: true, visible: false, draggable: false,
					 close: false, icon: YAHOO.widget.SimpleDialog.ICON_WARN, constraintoviewport: true,
					 buttons: [ {text:"OK",  handler:handleOK} ]} );
	warn_dialog.setHeader("Warning!"); 
	warn_dialog.setBody("%s"); 
	warn_dialog.render("warning_container"); 
//-->
</script> """ % context.REQUEST.SESSION.get('warning-error', '')
