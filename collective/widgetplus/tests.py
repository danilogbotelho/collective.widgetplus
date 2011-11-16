from zope import component
from zope.app.form.browser import TextWidget
from zope.app.form.interfaces import IInputWidget
from zope.app.testing import setup
from zope.publisher.interfaces.browser import IBrowserRequest
from zope.schema.interfaces import ITextLine
import doctest
import unittest


def setUp(test):
    setup.placefulSetUp()
    #factory, adapts=None, provides=None, name=''
    component.provideAdapter(TextWidget,(ITextLine,IBrowserRequest),
                             IInputWidget)


def tearDown(test):
    setup.placefulTearDown()


def test_suite():
    return doctest.DocFileSuite(
        'README.txt',
        setUp=setUp,tearDown=tearDown,
        optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS)
