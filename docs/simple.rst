Simple Queries
--------------

.. caution:: There is no option to add a TTL (Time to live) or batch size optimizations to the Simple Queries due to how Arango is handling simple collection HTTP requests. Your request may time out and you'll see a CursorNextError exception. The AQL queries provide full functionality.

Here is an example of using ArangoDB's **simply queries**:

.. testcode::

    from python_aioarango import ArangoClient

    # Initialize the ArangoDB client.
    client = ArangoClient()

    # Connect to "test" database as root user.
    db = await client.db('test', username='root', password='passwd')

    # Get the API wrapper for "students" collection.
    students = db.collection('students')

    # Get the IDs of all documents in the collection.
    await students.ids()

    # Get the keys of all documents in the collection.
    await students.keys()

    # Get all documents in the collection with skip and limit.
    await students.all(skip=0, limit=100)

    # Find documents that match the given filters.
    await students.find({'name': 'Mary'}, skip=0, limit=100)

    # Get documents from the collection by IDs or keys.
    await students.get_many(['id1', 'id2', 'key1'])

    # Get a random document from the collection.
    await students.random()

    # Update all documents that match the given filters.
    await students.update_match({'name': 'Kim'}, {'age': 20})

    # Replace all documents that match the given filters.
    await students.replace_match({'name': 'Ben'}, {'age': 20})

    # Delete all documents that match the given filters.
    await students.delete_match({'name': 'John'})

Here are all simple query (and other utility) methods available:

* :func:`python_aioarango.collection.Collection.all`
* :func:`python_aioarango.collection.Collection.export`
* :func:`python_aioarango.collection.Collection.find`
* :func:`python_aioarango.collection.Collection.find_near`
* :func:`python_aioarango.collection.Collection.find_in_range`
* :func:`python_aioarango.collection.Collection.find_in_radius`
* :func:`python_aioarango.collection.Collection.find_in_box`
* :func:`python_aioarango.collection.Collection.find_by_text`
* :func:`python_aioarango.collection.Collection.get_many`
* :func:`python_aioarango.collection.Collection.ids`
* :func:`python_aioarango.collection.Collection.keys`
* :func:`python_aioarango.collection.Collection.random`
* :func:`python_aioarango.collection.StandardCollection.update_match`
* :func:`python_aioarango.collection.StandardCollection.replace_match`
* :func:`python_aioarango.collection.StandardCollection.delete_match`
* :func:`python_aioarango.collection.StandardCollection.import_bulk`
