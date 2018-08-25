"""server that offers REST api for checking
the nodes in the db and handles the db
connection"""
import os
import sys
from flask import render_template
from flask import Flask
from flask import request
from server.modules.consume_packet_thread import ConsumePacketThread
from server.modules.database_manager import DatabaseHandler
from server.modules import supported_metrics
from client import config_handler

APP = Flask(__name__)
DATABASE_OBJECT = DatabaseHandler(APP)


def start_server():
    """starts the thread that consumes the packets and the
    server"""
    try:
        if not os.path.isfile(sys.argv[1]):
            print("You don't have the configuration file")
            sys.exit(1)
    except IndexError:
        print("You must enter a config file")
        sys.exit(2)

    config_manager = config_handler.ConfigParser(sys.argv[1])

    DATABASE_OBJECT.database_config(config_manager)

    consume_packet_thread = ConsumePacketThread(APP, config_manager)
    consume_packet_thread.start()

    APP.run(config_manager.read_server_ip(),
            config_manager.read_server_port())


@APP.route('/')
def index_route():
    """'menu' for index route"""
    return '<h3>/node/{id} for searching a nodes data' \
           '<br>/nodes for latest info about each distinct node' \
           '<br>/metriclist for a specific metric of each distinct node'\
           "<br>/metrics?a=metric1&b=metric2"


@APP.route('/metriclist')
def metrics_route():
    """renders the supported metrics"""
    return render_template("metrics.html",
                           metrics=supported_metrics.METRICS_LIST)


@APP.route('/metrics', methods=['GET'])
def node_metrics():
    """queries the node info by metrics for all
    distinct nodes"""
    is_metric = True

    metrics = request.args.to_dict().values()

    for arg_metric in metrics:
        metric_is_supported = False
        for supp_metric in supported_metrics.METRICS_LIST:
            if arg_metric == supp_metric:
                metric_is_supported = True

        if not metric_is_supported:
            is_metric = False

    if is_metric and metrics is not False:

        cursor_list = DATABASE_OBJECT.get_distinct_nodes()

        node_info_list = []
        for cursor in cursor_list:

            temp_dict = {
                "_id": cursor.get('_id')
            }

            for metric in metrics:
                temp_dict[metric] = cursor.get('{}'.format(metric))

            node_info_list.append(temp_dict)

        return render_template("nodes.html",
                               title="Metrics",
                               nodes=node_info_list)

    return "One or more of the specified metrics " \
           "is not supported or no metrics given"


@APP.route("/nodes")
def all_nodes():
    """queries the last data for all distinct nodes"""
    cursor = DATABASE_OBJECT.get_distinct_nodes()

    nodes = []

    for item in cursor:
        nodes.append(item)

    return render_template("nodes.html",
                           title="All machines",
                           nodes=nodes)


@APP.route('/node/<node_id>')
def node_route(node_id):
    """queries for a specific node's info"""
    node_info = DATABASE_OBJECT.get_node_data(node_id)
    node_value = None

    for temp_node in node_info:
        node_value = temp_node

    return render_template("nodes.html",
                           title="Node: %s" % node_id,
                           nodes=node_value)
