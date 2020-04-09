import flask
from flask import request, jsonify
import main
from main import *



if __name__ == '__main__':
    
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True
    
    json = get_json_covid()
    records = json

    @app.route('/', methods=['GET'])
    def home():    
        return jsonify(json)
    
    @app.route('/api/v1/country/<name>', methods=['GET'])
    def info_by_country(name):
        name = name.lower()

        if len(name) == 0:
        
            return "Error: No country found"
    

        results = [record for record in records if record['country'].lower() == name]

        
        
        return jsonify(results)

    @app.route('/api/v1/country/<name>/<query>', methods=['GET'])
    def country_specific_query(name,query):
        
        name = name.lower()
        if len(name) == 0:
        
            return "Error: No country found"
    

        results = [record for record in records if record['country'].lower() == name]

        if len(results) > 0:
            try:
                result = results[0][query]
            except KeyError:
                return "Error: Invalid query"
        else:
            return "Error: No country found"

       
        
        return jsonify({query:result})

    
    app.run()
    
    


    
    