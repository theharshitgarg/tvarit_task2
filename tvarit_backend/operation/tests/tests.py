from django.test import TestCase

from operation.services.addition import AdditionService

class TestAdder(TestCase):
	# def __init__(self):
	# 	self.service = AdditionService()

	def setUp(self):
		self.service = AdditionService()

	def test_valid(self):
		data = {
			"num1": 10,
			"num2": 13,
			"num3": 100,
		}

		self.assertEqual(self.service.result(data), 110)


	def test_valid_combo_teen_same(self):
		data = {
			"num1": 10,
			"num2": 10,
			"num3": 10,
		}

		self.assertEqual(self.service.result(data), 30)

	def test_combo_teen(self):
		data = {
			"num1": 15,
			"num2": 13,
			"num3": 17,
		}

		self.assertEqual(self.service.result(data), 15)

	def test_invalid_combo_teen_same(self):
		data = {
			"num1": 13,
			"num2": 13,
			"num3": 13,
		}

		self.assertEqual(self.service.result(data), 0)

	def test_valid_combo_teen_same(self):
		data = {
			"num1": 13,
			"num2": 13,
			"num3": 13,
		}

		self.assertEqual(self.service.result(data), 0)		
