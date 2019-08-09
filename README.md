# My Journey with GraphQl

## What is GraphQL

GraphQL is a data query language developed internally by Facebook in 2012 before being publicly released in 2015. It provides an alternative to REST and ad-hoc webservice architectures.

## What is Graphene-Python

Graphene-Python is a library for building GraphQL APIs in Python easily, its main goal is to provide a simple but extendable API for making developers' lives easier.

## When should I use GraphQL

If you are creating a data-driven application of at least moderate complexity, GraphQL should absolutely merit primary consideration.

## GraphQL ecosystem have three main classes

**Query** — way to fetch data in a read-only manner from your GraphQL API (analogy of GET request in REST API).

**Mutation** — way to change(create/update/delete) data on your server (analogy of POST request in REST API).

**Subscription** — way to get a real-time feed of data from your server (something like traditional Web Sockets)

## Schema in GraphQL

It is something like dictionary in Python or object in Javascript, if it is possible to say, where key is name of field and value is type of this field.

*Supported data types in GraphQL*

Scalars(Int, Float, String, Boolean, ID)
List, Enum, Non-null and others…

You can find out more info about data types [here](https://graphql.org/learn/schema/)

## Why GraphQL is better

- this is a clear and simple API between the backend and the frontend
- you are not obliged to write documentation for API
- reducing communication costs, less connections
- no API versioning
- just a great tool for your API

## File and its Content

| Command | Description |
| --- | --- |
| 1_schema.py | 1) A VERY BASIC HELLO WORLD IMPLEMENTATION WITH GRAPHQL(python-graphene). |
| 2_schema.py | 1) QUERIES THAT HAVE FIELDS WITH SUBFIELDS (ARGUMENTS). 2) PAGINATION IN GRAPHQL AND HOW IT IS DONE. 3) MORE INTO RESOLVER FUNCTIONS |
| 3_schema.py | 1) MUTATION OR POST METHODS USING GRAPHQL. 2) PASSING DEFAULT VALUES FOR ARGUMENTS |
| 4_schema.py | 1) VARIABLES IN ACTION WITH MUTATION |
| 5_schema.py | 1) VARIABLES IN ACTION WITH QUERIES. 2) NAMING YOUR GRAPH QL QUERIES |
| 6_schema.py | 1) MUTATION PART 2 WITH CREATE POST TO UNDERSTAND THE USE OF INFO AND SELF PARAMS UNDER RESOLVER FUNCTIONS. |
| 7_schema.py | 1) USE OF INFO PARAM IN RESOLVER FUNCTION TO IMPLEMENT AUTHENTICATION |
| 8_schema.py | 1) USE OF SELF PARAM UNDER RESOLVER FUNCTIONS. |
