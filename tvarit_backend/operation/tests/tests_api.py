from django.test import TestCase
from django.urls import reverse
from rest_framework import status


class TestAdder(TestCase):

	def test_all_valid_same(self):
		data = {
			"num1": 10,
			"num2": 10,
			"num3": 10,
		}
		response = self.client.post(reverse("addition"), data)
		data = response.data["data"]
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(data["result"], 30)

	def test_all_valid_different(self):
		data = {
			"num1": 10,
			"num2": 20,
			"num3": 30,
		}
		response = self.client.post(reverse("addition"), data)
		data = response.data["data"]
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(data["result"], 60)

	def test_all_invalid_same(self):
		data = {
			"num1": 13,
			"num2": 13,
			"num3": 13,
		}
		response = self.client.post(reverse("addition"), data)
		data = response.data["data"]
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(data["result"], 0)

	def test_all_invalid_different(self):
		data = {
			"num1": 13,
			"num2": 17,
			"num3": 18,
		}
		response = self.client.post(reverse("addition"), data)
		data = response.data["data"]
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(data["result"], 0)

	def test_all_valid_string_data(self):
		data = {
			"num1": "10",
			"num2": 20,
			"num3": 30,
		}
		response = self.client.post(reverse("addition"), data)
		data = response.data["data"]
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(data["result"], 60)

	def test_missing_data(self):
		data = {
			"num1": "10",
		}
		response = self.client.post(reverse("addition"), data)
		data = response.data["data"]

		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
		self.assertEqual(data, {})
		self.assertEqual(response.data["message"], "Invalid request data")