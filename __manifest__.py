{
    "name": "Library Management",
    "version": "18.0.1.0.0",
    "category": "Services",
    "summary": "Simple library management module",
    "description": """
        Simple module for managing books.
    """,
    "license": "LGPL-3",
    "depends": ["base"],
    "data": [
                "security/ir.model.access.csv",
                "views/library_book_views.xml", 
    ],
    "installable": True,
    "application": True, 
}