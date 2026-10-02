# Backend Learning Labs

Python exercises exploring search, message queues, and database-backed web applications. This repository consolidates earlier standalone experiments into one learning collection.

**Stack:** Python · Elasticsearch · RabbitMQ · Flask · PostgreSQL · Docker

## Explore the examples

- [Elasticsearch queries](elasticsearch/query-examples/): indexing, matching, Boolean queries, regular expressions, and analyzers.
- [Elasticsearch with Docker](elasticsearch/docker-examples/): local service configuration and query examples.
- [RabbitMQ work queues](rabbitmq/work-queues/): sending, receiving, and distributing background work.
- [RabbitMQ routing, topics, and RPC](rabbitmq/routing-topics-rpc/): publish/subscribe patterns, message filtering, and remote procedure calls.
- [Flask and PostgreSQL](flask-postgres/): student-record CRUD routes and direct database operations.

## Getting started

```bash
git clone https://github.com/monisha-krishnamurthy/backend-learning-labs.git
cd backend-learning-labs
python3 -m venv .venv
source .venv/bin/activate
```

Each folder is a separate exercise. There is no shared application entry point or complete environment setup. Inspect the example's imports and service settings before running it.

- Elasticsearch examples expect a local service and, for some queries, existing indices and data.
- RabbitMQ examples expect a local broker. Run consumers and producers in separate terminals.
- PostgreSQL examples expect existing databases and tables. Some scripts insert, update, or delete records; use a disposable local learning database.

## Current limitations

The Flask example is incomplete: its referenced HTML templates and database schema are not included. Database credentials and a Flask secret are currently hardcoded and should be replaced with local environment configuration before reuse. The delete route also needs a parameterized SQL query.

These exercises preserve learning work; they are not production-ready services. Dependencies and service versions need validation before running them in a fresh environment.
