#!/usr/bin/env python3
"""
script that provides some stats about Nginx logs stored in MongoDB:
- Database: logs
- Collection: nginx
"""
from pymongo import MongoClient


def main():
    """
    script that provides some stats about Nginx logs stored in MongoDB:
    - Database: logs
    - Collection: nginx
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collections = db.nginx

    number_logs = nginx_collections.count_documents({})
    print(f"{number_logs} logs")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        number_method = nginx_collections.count_documents({"method": method})
        print(f"\tmethod {method}: {number_method}")
    filter_path = {"method": "GET", "path": "/status"}
    number_path = nginx_collections.count_documents(filter_path)
    print(f"{number_path} status check")
