"""module that holds the test for app.py"""
from flask_testing import TestCase
from server.modules import supported_metrics
import server.app as app


class TestApp(TestCase):
    """tests if the routes in app.py work correctly
    and if the consumer starts"""

    def create_app(self):

        return app.APP

    def setUp(self):
        self.app = app.APP.test_client()
        self.app.testing = True

    def test_index_route(self):
        """tests if the index route is accessed correctly"""
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_metrics_route(self):
        """tests if the route returns the correct code
        and renders the correct template"""
        result = self.app.get('/metriclist')
        self.assertEqual(result.status_code, 200)
        self.assert_template_used('metrics.html')
        self.assert_context('metrics',
                            supported_metrics.METRICS_LIST)

    def test_node_metrics(self):
        """tests if the route returns the correct code
        and renders the correct template"""
        result = self.app.get('/nodes')
        self.assertEqual(result.status_code, 200)
        self.assert_template_used('nodes.html')
        self.assert_context('title',
                            "All machines")

    def test_all_nodes(self):
        """tests if the route returns the correct code
        and renders the correct template"""
        result = self.app.get('/nodes')
        self.assertEqual(result.status_code, 200)
        self.assert_template_used('nodes.html')
