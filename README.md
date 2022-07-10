# fampay-assignment
Suggested requirements:
1. Python 3.8+
2. Django 3.0.4+
3. Docker

Features:
1. Paginated query on youtube api
2. API calls on need basis and updates/calls for query accordingly saving quota
3. Automatic pickup of available keys for search api calls
4. Alternative approach DB setup
5. Function to keep the query updated
6. Docker composed with virtual environment requirements and migrations

To be improved on:
1. Background process - ideal implementation from external scheduler like airflow for key activation on quota exhaust and refreshes for query
2. Potential design for multiple query data storage