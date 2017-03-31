from __future__ import unicode_literals

import json
from mock import MagicMock, patch

from django.views.generic.edit import FormView
from django.forms import Form
from django.test import SimpleTestCase

from ajax_partials.mixins import (AjaxResponseAction, AjaxResponseMixin,
                                  FormAjaxMixin, AjaxResponseStatus,
                                  PartialAjaxMixin)


class DummyForm(Form):
    """ """


class AjaxResponseMixinTest(SimpleTestCase):

    class OkObject(AjaxResponseMixin):
        """ """

    def setUp(self):
        self.object = self.OkObject()

    def test_response_no_action(self):
        response = self.object.json_to_response()
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['action'], "nothing")
        self.assertEqual(content['status'], AjaxResponseStatus.SUCCESS)

    def test_response_with_action_refresh(self):
        response = self.object.json_to_response(
            action=AjaxResponseAction.REFRESH)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['action'], "refresh")
        self.assertEqual(content['status'], AjaxResponseStatus.SUCCESS)

    def test_response_with_action_redirect(self):
        response = self.object.json_to_response(
            action=AjaxResponseAction.REDIRECT,
            success_url="/unit/test")
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['action'], "redirect")
        self.assertEqual(content['status'], AjaxResponseStatus.SUCCESS)
        self.assertEqual(content['action_url'], "/unit/test")

    def test_get_action(self):
        self.assertEqual(self.object.get_action(), AjaxResponseAction.NOTHING)

    def test_get_action_invalid(self):
        self.assertRaises(ValueError, self.object.get_action, 'invalid')

    def test_get_status(self):
        self.assertEqual(self.object.get_status(), AjaxResponseStatus.SUCCESS)

    def test_get_status_invalid(self):
        self.assertRaises(ValueError, self.object.get_status, 'invalid')

    def test_get_json_data(self):
        self.assertEqual(self.object.get_json_data(), {})


class FormAjaxMixinTest(SimpleTestCase):

    class DummyFormView(FormAjaxMixin, FormView):
        """ """
        template_name = 'unit.html'
        prefix = 'unit'

        def get_success_url(self):
            return "/example/"

    def setUp(self):
        self.view = self.DummyFormView()
        self.view.request = MagicMock()
        self.form = MagicMock(spec=Form, errors={})

    def test_form_invalid_no_ajax(self):
        self.view.request.is_ajax.return_value = False
        response = self.view.form_invalid(self.form)
        self.assertEqual(response.status_code, 200)

    def test_form_invalid_as_ajax(self):
        self.view.request.is_ajax.return_value = True
        response = self.view.form_invalid(self.form)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(content['action'], "nothing")
        self.assertEqual(content['status'], AjaxResponseStatus.ERROR)

    def test_form_valid_no_ajax(self):
        self.view.request.is_ajax.return_value = False
        response = self.view.form_valid(self.form)
        self.assertEqual(response.status_code, 302)

    def test_form_valid_as_ajax(self):
        self.view.request.is_ajax.return_value = True
        response = self.view.form_valid(self.form)
        content = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(content['action'], "nothing")
        self.assertEqual(content['status'], AjaxResponseStatus.SUCCESS)

    def test_add_prefix_no_prefix(self):
        result = self.view.add_prefix({}, None)
        self.assertEqual(result, {})

    def test_add_prefix_with_prefix_view(self):
        self.view.prefix = None
        result = self.view.add_prefix({'field_1': 'invalid'}, None)
        self.assertEqual(result['field_1'], "invalid")

    def test_add_prefix_with_prefix(self):
        result = self.view.add_prefix({'field_1': 'invalid'}, 'test')
        self.assertEqual(result['test-field_1'], "invalid")


class PartialAjaxMixinTest(SimpleTestCase):
    """ """

    class DummyView(PartialAjaxMixin):
        """ """

        def get_template_names(self):
            return "example.html"

    def setUp(self):
        self.view = self.DummyView()
        self.view.request = MagicMock()

    @patch('ajax_partials.mixins.render_to_string',
           return_value="<html></html>")
    def test_render_to_response(self, render_to_string):
        result = self.view.render_to_response({})
        content = json.loads(result.content)
        self.assertEqual(content['content'], "<html></html>")
        render_to_string.assert_called_with(
            "example.html", {}, request=self.view.request)
