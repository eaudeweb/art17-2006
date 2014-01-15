# Script (Python)
# /article17/habitatsummary/generate_conclusion_values
# params: ''
## Script (Python) "generate_conclusion_values"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=
##
# Example code:

# Import a standard function, and get the HTML request and response objects.
from Products.PythonScripts.standard import html_quote
request = container.REQUEST
RESPONSE =  request.RESPONSE

decisions = context.sql_methods.select_decisions()

output = []
buffer = []

output.append("""<script type="text/javascript">""")
output.append("""TableKit.options.editAjaxURI = 'updateDecision';""")
output.append("""TableKit.Editable.addCellEditor(""")
output.append("""new TableKit.Editable.CellEditor('decision_field', {""")
output.append("""element : 'select',""")
output.append("""attributes : {name : 'decision', title : 'Please select a decision from the list'},""")
output.append("""selectOptions : [""")
for decision in decisions:
    decision = decision['decision']
    buffer.append("""['%s', '%s']""" % (decision, decision))
output.append(','.join(buffer))
output.append("""]""")
output.append("""})""")
output.append(""");""")
output.append("""</script>""")

return "\n".join(output)
