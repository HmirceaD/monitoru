"""module that holds the DatabaseHandler object"""
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


class DatabaseHandler(object):
    """this class establishes the connection
    to the mongodb database and creates the queries
    for searching the db"""
    def __init__(self, app):
        self.app = app

    def add_packet(self, packet):
        """adds a node in the collection"""
        mongo = PyMongo(self.app)

        nodes = mongo.db.node
        nodes.insert(packet)

    def database_config(self, config_manager):
        """configurates the db connection"""
        self.app.config['MONGO_DBNAME'] = config_manager.read_mongo_db()
        self.app.config['MONGO_URI'] = config_manager.read_mongo_uri()

    def get_node_data(self, node_id):
        """returns the data from a specific node"""
        mongo = PyMongo(self.app)
        nodes = mongo.db.node

        return nodes.find({'_id': ObjectId(node_id)})

    def get_distinct_nodes(self):
        """returns the last packet from distinct nodes"""
        mongo = PyMongo(self.app)
        node_ids = mongo.db.node

        return node_ids.find({})
