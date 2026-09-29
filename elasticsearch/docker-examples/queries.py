import json

from elasticsearch import Elasticsearch

# create a client instance of Elasticsearch
elastic_client = Elasticsearch("http://localhost:9200")

index_name = "companydatabase"

# Python dictionary object representing an Elasticsearch JSON query:
search_param_fname = {
    'match': {
        'FirstName': 'PEGGIE'
    }
}

# get another response from the cluster
fname_response = elastic_client.search(index=index_name, query=search_param_fname)
print('first name query:', json.dumps(fname_response.body.get('hits'), indent=2))

search_param_salary = {
    'match': {
        'Salary': 106000  # Use number because salary is a number
    }
}

salary_response = elastic_client.search(index=index_name, query=search_param_salary)
print('salary query', json.dumps(salary_response.body.get('hits'), indent=2))

search_param_designation = {
    'match': {
        'Designation': 'Vice President'
    }
}

designation_response = elastic_client.search(index=index_name, query=search_param_designation)
print('designation query', json.dumps(designation_response.body.get('hits'), indent=2))
