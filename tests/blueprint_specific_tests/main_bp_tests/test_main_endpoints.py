# -*- coding: utf-8 -*-
"""
Unit tests for endpoints in the main blueprint
"""
import pytest
from urllib.parse import urlparse
from flask import url_for

def test_index_route(test_client):
    """
    TEST the main route
    """
    res = test_client.get("/index", follow_redirects=False)
    assert res.status_code == 200

def test_share_route(test_client):
    """
    GIVEN calling the route "/share"
    WHEN no user is logged in
    THEN should return success code
    """
    res = test_client.get("/share")
    assert res.status_code == 200

def test_faq_route(test_client):
    """
    GIVEN calling the route "/faq"
    WHEN no user is logged in
    THEN should return success code
    """
    res = test_client.get("/faq")
    assert res.status_code == 200

def test_contact_us_route(test_client):
    """
    GIVEN calling the route "/contact_us"
    WHEN no user is logged in
    THEN should return success code
    """
    res = test_client.get("/contact_us")
    assert res.status_code == 200

def test_about_route(test_client):
    """
    GIVEN calling the route "/about"
    WHEN no user is logged in
    THEN should return success code
    """
    res = test_client.get("/about")
    assert res.status_code == 200

def test_tutorial_route(test_client):
    """
    GIVEN calling the route "/tutorial"
    WHEN no user is logged in
    THEN should return success code
    """
    res = test_client.get("/tutorial")
    assert res.status_code == 200
