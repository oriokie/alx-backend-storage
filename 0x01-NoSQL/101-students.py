#!/usr/bin/env python3
"""
Python function that returns all students sorted by average score"""


def top_students(mongo_collection):
    """
    Python function that returns all students sorted by average score
    """
    students = mongo_collection.aggregate([
        {"$unwind": "$topics"},
        {"$project": {
            "_id": 1,
            "name": 1,
            "averageScore": {"$avg": "$topics.score"}
        }},
        {"$sort": {"averageScore": -1}}
    ])
    return students
