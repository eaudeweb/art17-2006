# Script (Python)
# /article17/habitatsummary/conclusion_javascript
# params: ''
## Script (Python) "conclusion_javascript"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
if context.acl_manager.checkPermissionEditWiki():
    text_body = "Unless you are using Method 1 with same conclusion as for Method 2, please provide an explanation in the AuditTrail. "
else:
    text_body = "Unless you are using Method 1 with same conclusion as for Method 2, please add a comment with the explanation. "

return """
<script type="text/javascript">
<!--
	// put Yahoo class on body
	YAHOO.util.Dom.addClass(document.body, 'yui-skin-sam');

	// Define various event handlers for Dialog
	var handleYes = function() {
		var warning = document.getElementById('enable-warning');
		warning.value = "";
		form = document.getElementById('conclusion_form');
		form.submit();
		this.hide();
	};

	var handleNo = function() {
		this.hide();
	};

	// Instantiate the Dialog
	warn_dialog = new YAHOO.widget.SimpleDialog("warn_dialog", 
					 { width: "300px", fixedcenter: true, visible: false, draggable: false,
					 close: false, icon: YAHOO.widget.SimpleDialog.ICON_WARN, constraintoviewport: true,
					 buttons: [ { text:"Yes", handler:handleYes, isDefault:true },{ text:"No",  handler:handleNo } ]} );
	warn_dialog.setHeader("Warning!"); 
	warn_dialog.setBody("<center>At least one of the selected conclusions does not match the automatically computed conclusion for the selected method! <br /><br /> Are you sure you want to select this conclusion? <br /><br /> %s <\/center>"); 
	warn_dialog.render("warning_container"); 
//-->
</script>""" % text_body
