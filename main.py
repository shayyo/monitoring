import data_retriever
import opensearch_connect
import time
import random


if __name__ == '__main__':
    while True:

        # add data - generate randon document ID
        # opensearch_connect.opensearch_add_data(document=data_retriever.retrieve_memory_data(),
        #                                        index_name='my_memory_data', id=random.randrange(10000000000))
        # opensearch_connect.opensearch_add_data(document=data_retriever.retrieve_disk_data('/'),
        #                                        index_name='my_disk_data', id=random.randrange(10000000000))
        # opensearch_connect.opensearch_add_data(document=data_retriever.retrieve_cpu_data(),
        #                                        index_name='my_cpu_data', id=random.randrange(10000000000))
        # print the data
        print('\nSearch results:')
        print( opensearch_connect.opensearch_search(index_name='my_memory_data', query={"query": {"match_all": {}}}) )
        print( opensearch_connect.opensearch_search(index_name='my_disk_data', query={"query": {"match_all": {}}}) )
        print( opensearch_connect.opensearch_search(index_name='my_cpu_data', query={"query": {"match_all": {}}}) )

        # count of each document type
        print('\nCount of documents:')
        print( opensearch_connect.opensearch_count_documents(index_name='my_memory_data', document={"query": {"match_all": {}}} ))
        print( opensearch_connect.opensearch_count_documents(index_name='my_disk_data', document={"query": {"match_all": {}}} ))
        print( opensearch_connect.opensearch_count_documents(index_name='my_cpu_data', document={"query": {"match_all": {}}} ))

        time.sleep(5)

