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
    
    @app.route('/api/v1/', methods=['GET'])
    def info_by_country():
        
        country = ''
        if 'country' in request.args:
            country = str(request.args['country'])
            
        else:
            return "Error: No country field provided. Please specify a country."
    

        results = []

        for record in records:
            if record['country'].lower() == country.lower():
                results.append(record)
        
        
        return jsonify(results)    
    app.run()
    
    


    
    