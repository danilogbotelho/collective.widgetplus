====================
The Widget Namespace
====================

The widget namespace provides a way to traverse to the widgets of a
formlib form.

  >>> from collective.widgetplus.namespace import WidgetHandler

Let us define a form to test this behaviour.

  >>> from zope.formlib import form
  >>> from zope import interface, schema
  >>> class IMyContent(interface.Interface):
  ...     title = schema.TextLine(title=u'Title')
  >>> class MyContent(object):
  ...     interface.implements(IMyContent)
  ...     title=None
  >>> content = MyContent()
  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()
  >>> class MyForm(form.EditForm):
  ...     form_fields = form.Fields(IMyContent)
  >>> view = MyForm(content,request)
  >>> handler = WidgetHandler(view,request)
  >>> handler.traverse('title',None)
  <zope.formlib.textwidgets.TextWidget object at ...>
