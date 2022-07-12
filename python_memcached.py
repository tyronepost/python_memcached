from pymemcache.client import base


def do_some_query():
    # Replace with actual querying code to a database
    # a remote REST API, etc
    return 'blah'


client = base.Client(('localhost', 11211))
result = client.get('some_key')

if result is None:
    result = do_some_query()

    # Cache the result for next time
    client.set('some_key', result)

print(type(result))
print(result)
print(result.decode('utf-8'))
