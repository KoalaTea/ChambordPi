"""
    The document module contains a Document class to represent documents in the database.
    It also contains the DocumentException class to represent exceptions that may occur.
"""

from bson import ObjectId
from bson.errors import InvalidId
from pymongo.errors import InvalidName
from config import DB

class DocumentException(Exception):
    """
    Class for Document Exceptions.
    """
    pass

class Document(object):
    """
    Base class for representing mongo documents.
    """
    def __init__(self, collectionName, doc=None):
        """
        Initialize a document object (Does not commit to database).
        """
        if collectionName is None or collectionName == "":
            raise DocumentException('Error: Cannot create document with no collection')
        
        try:
            self.collection = Document.getCollection(collectionName)
            self.collectionName = collectionName
        except InvalidName:
            raise DocumentException('Collection "{}" not found'.format(collectionName))

        self.doc = doc if doc is not None else {}

    def __getattribute__(self, name):
        """
        Returns any attribute belonging to the Document object.
        If the attribute doesn't exist, it will get the field from the document
        """
        try:
            # If we have the attribute, get it
            return object.__getattribute__(self, name)
        except AttributeError:
            # Otherwise, attempt to fetch it from the document
            return self.getField(name)

    @property
    def docID(self):
        """
        Return the document's ID as an ObjectId
        """
        try:
            return ObjectId(self.doc['_id'])
        except KeyError:
            raise DocumentException('Document ID not found')
        except InvalidId:
            raise DocumentException('Invalid Document ID')

    def commit(self):
        """
        Commits the document to the database.
        """
        self.collection.save(self.doc) 

    def update(self):
        """
        Fetch an updated version of the document from the database.
        """
        self.doc = self.collection.find_one(self.identifier)
        return self.doc is not None

    def delete(self):
        """
        Delete this document from the database.
        """
        return Document.remove(self.collectionName, self.identifier)

    def getField(self, field):
        """
        Return a field from the document, or None if no such field exists.
        """
        return self.doc.get(field, None) if self.doc is not None else None

    def setField(self, key, value):
        """
        Set the value of a given key in the Document.
        """
        self.doc[key] = value

    @staticmethod
    def getCollection(collection_name):
        """
        Retrieve a collection from the database.
        """
        return DB.get_collection(collection_name)

    @staticmethod
    def get(collection_name, search=None):
        """
        Search for a document in a given collection, returning a list of JSON documents.
        """
        return [d for d in Document.getCollection(collection_name).find(search if search is not None else {})]

    @staticmethod
    def remove(collection_name, docID):
        """
        Remove a document from a given collection.
        """
        return Document.getCollection(collection_name).delete_one({'_id': ObjectId(str(docID))}).deleted_count > 0
