from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

# es.indices.create(index="english")

doc_1 = {"sentence": "COVID-19 is amazing!"}
doc_2 = {"sentence": "WFH is awesome!"}

es.index(index="english", id=1, document=doc_1)
es.index(index="english", id=2, document=doc_2)

'''query = {
    "_analyzer":{
        "my_custom_analyzer":{
            "type":"custom",
            "tokenizer":"standard",
            "filter":[
                "uppercase"
            ]
        }
    }
}

query_uppercase = es.search(index="english", query=query)
print(query_uppercase)'''

query = {
    "match": {
        "sentence": "amazing"
    }
}

simple_match_query = es.search(index="english", query=query)
print(simple_match_query)

query = {
    "bool": {
        "must": [
            {
                "match": {
                    "sentence": "WFH"
                }
            },
            {
                "match": {
                    "sentence": "COVID-19"
                }
            }
        ]
    }
}

must_query = es.search(index="english", query=query)
print(must_query)

query = {
    "bool": {
        "must_not": [
            {
                "match": {
                    "sentence": "COVID-19"
                }
            }
        ]
    }
}

must_not_query = es.search(index="english", query=query)
print(must_not_query)

query = {
    "bool": {
        "should": [
            {
                "match": {
                    "sentence": "WFH"
                }
            },
            {
                "match": {
                    "sentence": "COVID-19"
                }
            }
        ]
    }
}

should_query = es.search(index="english", query=query)
print(should_query)

query = {
    "match_phrase": {
        "sentence": "COVID"
    }
}

match_phrase = es.search(index="english", query=query)
print(match_phrase)


doc_4 = {"sentence": "Hack COVID-19 is amazing!"}
doc_5 = {"sentence": "Hack-Quarantine is stunning!"}
doc_6 = {"sentence": "Hack nCov is great!"}

es.index(index="english", id=1, document=doc_4)
es.index(index="english", id=2, document=doc_5)
es.index(index="english", id=3, document=doc_6)

query = {
    "regexp": {
        "sentence": "s.*g"
    }
}

regexp_query = es.search(index="english", query=query)
print(regexp_query)


analyzer = ['standard','simple','whitespace','stop','keyword','pattern','fingerprint']

for analyze in analyzer:
    res = es.indices.analyze(body={
      "analyzer" : analyze,
      "text" : ["HELLO WORLD. Today is the 2nd day of the week!!!!     it is Monday."]
    })
    print("======",analyze,"========")
    for i in res['tokens']:
        print(i['token'])
    print("\n")



