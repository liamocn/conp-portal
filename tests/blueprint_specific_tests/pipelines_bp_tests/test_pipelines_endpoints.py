# -*- coding: utf-8 -*-
"""
Unit tests for endpoints in the pipelines blueprint
"""
import pytest
import app.cli as cli
from urllib.parse import urlparse
from flask import url_for



def test_pipelines_route(test_client):
    """
    GIVEN calling the route "/pipelines"
    WHEN no user is logged in
    THEN should return success code
    """
    res = test_client.get("/pipelines")
    assert res.status_code == 200


def test_pipeline_search_route(session, test_client, app, runner):
    """
    GIVEN calling the route "/pipeline-search"
    WHEN no user is logged in
    AND no filter is used
    THEN should return success code and all pipelines
    """

    #cli.register(app)
    #result = runner.invoke(args=["update_pipeline_data"])

    headers = {'Content-Type': 'application/json'}
    res = test_client.get("/pipeline-search", headers = headers)
    assert res.status_code == 200

    body = res.get_json(force=True)

    assert type(body) != type(None)
    assert body["authorized"] == False
    assert type(body["elements"]) != type(None)
    assert body["total"] > 0

def test_pipeline_search_route_with_filter(session, test_client):
    """
    GIVEN calling the route "/pipeline-search"
    WHEN no user is logged in
    AND a filter is used
    THEN should return success code and filtered pipelines
    """

    headers = {'Content-Type': 'application/json'}
    res = test_client.get("/pipeline-search", headers = headers)

    body = res.get_json(force=True)

    unfilteredTotal = body["total"]

    query = {'search': 'bids'}
    headers = {'Content-Type': 'application/json'}
    res = test_client.get("/pipeline-search", headers = headers, query_string = query)
    assert res.status_code == 200

    body = res.get_json(force=True)

    assert type(body) != type(None)
    assert body["authorized"] == False
    assert type(body["elements"]) != type(None)
    assert body["total"] > 0

    assert body["total"] < unfilteredTotal


def test_tools_route(test_client):
    """
    GIVEN calling the route "/tools"
    WHEN no user is logged in
    THEN should return success code
    """
    res = test_client.get("/tools")
    assert res.status_code == 200
