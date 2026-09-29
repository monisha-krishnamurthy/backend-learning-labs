from elasticsearch import Elasticsearch

es = Elasticsearch(hosts="http://localhost:9200")

es.indices.create(index="first_index")
es.indices.exists(index="first_index")

doc_1 = {"city": "Paris", "country": "France"}
doc_2 = {"city": "Vienna", "country": "Austria"}
doc_3 = {"city": "London", "country": "England"}

es.index(index="cities", doc_type="places", id=1, body=doc_1)
es.index(index="cities", doc_type="places", id=2, body=doc_2)
es.index(index="cities", doc_type="places", id=3, body=doc_3)

res = es.get(index="cities", doc_type="places", id=1)
res

res["_source"]

doc_1 = {"sentence":"Hack COVID-19 is amazing!"}
doc_2 = {"sentence":"Hack-Quarantine is stunning!"}

es.index(index="english", doc_type="sentences", id=1, body=doc_1)
es.index(index="english", doc_type="sentences", id=2, body=doc_2)

