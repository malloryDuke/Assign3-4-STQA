import unittest

from flask import abort, url_for
from flask_testing import LiveServerTestCase

from selenium import webdriver

from app import create_app, db


class TestBase(TestCase):

    def create_app(self):

        # pass in test configurations
        config_name = 'testing'
        app = create_app(config_name)
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        db.session.commit()
        db.drop_all()
        db.create_all()


    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class test_UI(object):

    def create_bmi_instance(self):
        """Log in as the test employee"""
        login_link = self.get_server_url()
        self.driver.get(login_link)
        self.driver.find_element_by_id("feet").send_keys(5)
        self.driver.find_element_by_id("inches").send_keys(5)
        self.driver.find_element_by_id("weight").send_keys(140)
        self.driver.find_element_by_id("btn").click()

    def create_retirement_instance(self):
        """Log in as the test employee"""
        login_link = self.get_server_url()
        self.driver.get(login_link)
        self.driver.find_element_by_id("age").send_keys(test_employee1_email)
        self.driver.find_element_by_id("salary").send_keys(
            test_employee1_password)
        self.driver.find_element_by_id("perSave").send_keys()
        self.driver.find_element_by_id("goal").send_keys()
        self.driver.find_element_by_id("btn2").click()
