from opensearchpy import OpenSearch, exceptions

host = '3.67.8.37'
port = 9200
auth = ('admin', '"hG8Fndffr121234"')


# Create the client with SSL/TLS and hostname verification disabled.
client = OpenSearch(
    hosts = [{'host': host, 'port': port}],
    http_compress = True, # enables gzip compression for request bodies
    http_auth = auth,
    use_ssl = True,
    verify_certs = False,
    ssl_assert_hostname = False,
    ssl_show_warn = False
)


index_name = 'python-own-backup'
index_body = {
  'settings': {
    'index': {
      'number_of_shards': 4
    }
  }
}
#
# try:
#     response = client.indices.create(index_name, body=index_body)
#     print(response)
# except:
#     print(exceptions.RequestError(400))


# document = {
#   'title': 'MEMORY INFORMATION',
#   'TOTAL_MEMORY': '17G'
# }
id = '5'


def opensearch_add_data(document):
    response = client.index(body=document, index=index_name, id=id, refresh=True)
    print('\nAdding document:')
    print(response)



# Search for the document.
q = 'memory'
query = {
  'size': 5,
  'query': {
    'multi_match': {
      'query': q,
      'fields': ['title^2', 'TOTAL_MEMORY']
    }
  }
}


def opensearch_search():
    response = client.search(body=query, index=index_name)
    print('\nSearch results:')
    print(response)


