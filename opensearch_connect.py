from opensearchpy import OpenSearch, exceptions

host = '127.0.0.1'
port = 9200
auth = ('admin', 'hG8Fndffr121234')


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


def opensearch_add_data(index_name, document, id):
    response = client.create(index=index_name, body=document, id=id, refresh=True)
    return response


def opensearch_count_documents(index_name, document):
    response = client.count(index=index_name, body=document)
    return response



def opensearch_search(index_name, query):
    response = client.search(index=index_name, body=query)
    return response


