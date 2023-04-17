                                    Pagination
Pagination is the process of dividing a large set of results into smaller, more manageable "pages" to improve performance and provide a better user experience.
It is commonly used in web applications to display large sets of data in a more organized and readable manner.

                                    Overview:
REST (Representational State Transfer) is an architectural style for web services that uses HTTP (Hypertext Transfer Protocol) to access resources.
RESTful APIs provide a standard way for clients to interact with servers and retrieve data.

                                    Filtering:
Filtering allows clients to retrieve specific data from an endpoint based on certain criteria.
URL parameters are the easiest way to add basic filtering to REST APIs.
For example, if you have an endpoint for items that are for sale,
you can filter by the property name such as GET /items?state=active or GET /items?state=active&seller_id=1234.
However, this only works for exact matches. What if you want to do a range such as a price or date range?

The problem is URL parameters only have a key and a value but filters are composed of three components:

1. The property or field name
2. The operator such as eq, lte, gte
3. The filter value

There are various ways to encode these three components into URL param key/values. One way is to use square brackets [] on the key name, known as LHS Brackets.
For example, GET /items?price[gte]=10&price[lte]=100 would find all the items where the price is greater than or equal to 10, but less than or equal to 100.
This method provides greater flexibility in what the filter value is for clients but may require more work on the server side to parse and group the filters.
Another method is to design an API to take the operator on the RHS instead of LHS, known as RHS Colon. For example, GET /items?price=gte:10&price=lte:100 would
find all the items where the price is greater than or equal to 10, but less than or equal to 100. This method is easiest to parse on the server side, 
especially if duplicate filters are not supported.

If you require search on your endpoint, you can add support for filters and ranges directly with the search parameter.
If you’re already using ElasticSearch or other Lucene based technology, you could support the Lucene syntax or ElasticSearch Simple Query Strings directly.
This method is the most flexible queries for API users and requires almost no parsing required on the backend, can pass directly to search engine or database.

                                    Pagination:
Pagination allows endpoints that return a list of entities to have some sort of paging to prevent extraneous network traffic.
Paging requires an implied ordering. By default this may be the item’s unique identifier, but can be other ordered fields such as a created date.

The simplest form of paging is Offset Pagination, which became popular with apps using SQL databases which already have LIMIT and OFFSET clauses.
For example, GET /items?limit=10&offset=20 would return items 21-30. However, this method has some limitations, including the possibility of duplicates or
gaps in the data if the offset changes between requests.

Cursor-based pagination is a more reliable method of paging. Cursors are opaque strings that encode enough information to continue the pagination in the next request.
For example, GET /items?limit=10&before=ZG9nOjEyMzQ1Njc4 would return the 10 items before the item with the ID of 12345678.
This method ensures that the same items are not returned twice and can handle additions or deletions to the data set.

                                    Learning Objectives
At the end of this project, you are expected to be able to explain to anyone

1. How to paginate a dataset with simple page and page_size parameters
2. How to paginate a dataset with hypermedia metadata
3. How to paginate in a deletion-resilient manner
