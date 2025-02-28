from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username, password):
        
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections 
        self.client = MongoClient('mongodb://%s:%s@127.0.0.1:36231/AAC' %(username,password))
        self.database = self.client['AAC']
        
    # Method to implement the C in CRUD
    def create(self, data):
        
        # Conditional statement to check if data is null, 
        # and then return "true" if not, and "false" if null
        if data is not None:
            if data:
                self.database.animals.insert(data) 
                return True
        else:
            raise Exception("Nothing to save, because data parameter is empty.")
            return False
            
    # Method to implement the R in CRUD
    def read(self, search_parameter):
        
        # Conditional statement to check if search parameter is null, 
        # and then return search results
        if search_parameter is not None:
            search_results = self.database.animals.find(search_parameter,{"_id":False})
        else:
            search_results = self.database.animals.find({},{"_id":False})
        return search_results
        
    # Method to implement the U in CRUD
    def update(self, search_parameter, data):
        
        # Conditional statement to check if search parameter is null, 
        # and then return updated result(s) if not null, and error message if null
        if search_parameter is not None:
            if search_parameter:
                updated_results = self.database.animals.update_many(search_parameter, {'$set' : data})
                
                # Print amount of documents updated successfully if result is more than 0
                if updated_results.modified_count > 0:
                    print(f"{updated_results.modified_count} document(s) updated successfully.")
                    print(f"Updated data: {data}")
                    return True
        else:
            error_msg = "Nothing to update, because search parameter is empty."
            return error_msg
        
    # Method to implement the D in CRUD
    def delete(self, search_parameter):
        
        # Conditional statement to check if search parameter is null, 
        # and then return deleted result(s) if not null, and error message if null
        if search_parameter is not None:
            if search_parameter:
                deleted_results = self.database.animals.delete_many(search_parameter)
                
                # Print amount of documents deleted successfully if result is more than 0
                if deleted_results.deleted_count > 0:
                    print(f"{deleted_results.deleted_count} document(s) deleted successfully.")
                    print(f"Deleted data: {search_parameter}")
                    return True
        else:
            error_msg = "Nothing to delete, because search parameter is empty."
            return error_msg