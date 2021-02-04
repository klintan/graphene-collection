# Graphene collection - nifty middlewares and backends for graphene

Graphene is a GraphQL library for Python. It makes use of backends and middlewares to extend the functionality of it's core. 

I had some troubles finding middlewares and backends that were not focused on Django, so I collected them here for others to use.

Disclaimer: These are mere examples, and you should examine them carefully and possibly rewrite some of it before you put them in production. If you do make improvements, feel free to create a PR :) 


As of now these are available:

Security:
 - Middlewares:
 	- Hide introspection, make sure to hide the introspection in production.
 	- XSS field validation, make sure to escape xss for every field.
 - Backends: 
 	- Depth limitation, make sure to limit the depth of queries.


The source folder is structured as above to make it easy to find them.


https://docs.graphene-python.org/en/latest/execution/middleware/