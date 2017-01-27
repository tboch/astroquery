# Licensed under a 3-clause BSD style license - see LICENSE.rst
"""
=============
Gaia TAP plus
=============

@author: Juan Carlos Segovia
@contact: juan.carlos.segovia@sciops.esa.int

European Space Astronomy Centre (ESAC)
European Space Agency (ESA)

Created on 30 jun. 2016


"""
import unittest
import os

from unittest.mock import Mock, MagicMock, patch
from astroquery.gaiatap.tapplus.conn.tapconn import TapConn
from astroquery.gaiatap.tapplus.conn.tests.DummyConn import DummyConn


def data_path(filename):
    data_dir = os.path.join(os.path.dirname(__file__), 'data')
    return os.path.join(data_dir, filename)

class ConnTest(unittest.TestCase):
    
    def testGet(self):
        mock = Mock()
        conn = DummyConn("http")
        conn.response.status = 222
        mock.get_connection.return_value = conn
        host = "testHost"
        serverContext = "testServerContext"
        tapContext = "testTapContext"
        connPort = 90
        connPortSsl = 943
        #TapConn
        tap = TapConn(ishttps=False, host=host, server_context=serverContext, tap_context=tapContext, port=connPort, sslport=connPortSsl, connhandler=mock)
        hostUrl = host + ":" + str(connPort) + "/" + serverContext + "/" + tapContext + "/"
        assert tap.get_host_url() == hostUrl, "Tap host. Expected %s, found %s" % (hostUrl, tap.get_host_url())
        hostUrlSecure = host + ":" + str(connPortSsl) + "/" + serverContext + "/" + tapContext + "/"
        assert tap.get_host_url_secure() == hostUrlSecure, "Tap host secure. Expected %s, found %s" % (hostUrlSecure, tap.get_host_url_secure())
        #GET
        subContext = "testSubContextGet"
        context = "/" + serverContext + "/" + tapContext + "/" + subContext
        r = tap.execute_get(subcontext=subContext)
        assert r.status == 222, "Status code, expected: %d, found: %d" % (222, r.status)
        assert r.getMethod() == 'GET', "Request method. Expected %s, found %s" % ('GET', r.getMethod())
        assert r.getContext() == context, "Request context. Expected %s, found %s" % (context, r.getContext())
        assert r.getBody() == None, "Request body. Expected %s, found %s" % ('None', str(r.getBody()))
        pass
    
    def testPost(self):
        mock = Mock()
        conn = DummyConn('http')
        conn.response.status = 111
        mock.get_connection.return_value = conn
        host = "testHost"
        serverContext = "testServerContext"
        tapContext = "testTapContext"
        connPort = 90
        connPortSsl = 943
        #TapConn
        tap = TapConn(ishttps=False, host=host, server_context=serverContext, tap_context=tapContext, port=connPort, sslport=connPortSsl, connhandler=mock)
        hostUrl = host + ":" + str(connPort) + "/" + serverContext + "/" + tapContext + "/"
        assert tap.get_host_url() == hostUrl, "Tap host. Expected %s, found %s" % (hostUrl, tap.get_host_url())
        hostUrlSecure = host + ":" + str(connPortSsl) + "/" + serverContext + "/" + tapContext + "/"
        assert tap.get_host_url_secure() == hostUrlSecure, "Tap host secure. Expected %s, found %s" % (hostUrlSecure, tap.get_host_url_secure())
        #GET
        subContext = "testSubContextGet"
        context = "/" + serverContext + "/" + tapContext + "/" + subContext
        data = "postData"
        r = tap.execute_post(subcontext=subContext, data=data)
        assert r.status == 111, "Status code, expected: %d, found: %d" % (111, r.status)
        assert r.getMethod() == 'POST', "Request method. Expected %s, found %s" % ('POST', r.getMethod())
        assert r.getContext() == context, "Request context. Expected %s, found %s" % (context, r.getContext())
        assert r.getBody() == data, "Request body. Expected %s, found %s" % (data, str(r.getBody()))
        pass
    
    def testLogin(self):
        mock = Mock()
        connSecure = DummyConn("https")
        connSecure.response.status = 333
        mock.get_connection_secure.return_value = connSecure
        host = "testHost"
        serverContext = "testServerContext"
        tapContext = "testTapContext"
        connPort = 90
        connPortSsl = 943
        #TapConn
        tap = TapConn(ishttps=False, host=host, server_context=serverContext, tap_context=tapContext, port=connPort, sslport=connPortSsl, connhandler=mock)
        hostUrl = host + ":" + str(connPort) + "/" + serverContext + "/" + tapContext + "/"
        assert tap.get_host_url() == hostUrl, "Tap host. Expected %s, found %s" % (hostUrl, tap.get_host_url())
        hostUrlSecure = host + ":" + str(connPortSsl) + "/" + serverContext + "/" + tapContext + "/"
        assert tap.get_host_url_secure() == hostUrlSecure, "Tap host secure. Expected %s, found %s" % (hostUrlSecure, tap.get_host_url_secure())
        #POST SECURE
        subContext = "testSubContextPost"
        context = "/" + serverContext + "/" + subContext
        data = "testData"
        r = tap.execute_secure(subcontext=subContext, data=data)
        assert r.status == 333, "Status code, expected: %d, found: %d" % (333, r.status)
        assert r.getMethod() == 'POST', "Request method. Expected %s, found %s" % ('POST', r.getMethod())
        assert r.getContext() == context, "Request context. Expected %s, found %s" % (context, r.getContext())
        assert r.getBody() == data, "Request body. Expected %s, found %s" % (data, str(r.getBody()))
        pass
    
    pass
