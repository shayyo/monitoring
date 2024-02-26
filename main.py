import data_retriever
import opensearch_connect
import time
import random




#
#
# while True:
#     cpu_utilization_percentage = psutil.cpu_percent()
#     virtual_memory_percent = psutil.virtual_memory().percent
#     time.sleep(1)




if __name__ == '__main__':
    while True:

        opensearch_connect.opensearch_add_data(document=data_retriever.retrieve_memory_information(),
                                               index_name='my_memory_data', id=random.randrange(10000000000))
        opensearch_connect.opensearch_add_data(document=data_retriever.retrieve_disk_information('/'),
                                               index_name='my_disk_data', id=random.randrange(10000000000))
        opensearch_connect.opensearch_add_data(document=data_retriever.retrieve_cpu_information(),
                                                 index_name='my_cpu_data', id=random.randrange(10000000000))
        print('\nSearch results:')
        print( opensearch_connect.opensearch_search(index_name='my_memory_data', query={"query": {"match_all": {}}}) )
        print( opensearch_connect.opensearch_search(index_name='my_disk_data', query={"query": {"match_all": {}}}) )
        print( opensearch_connect.opensearch_search(index_name='my_cpu_data', query={"query": {"match_all": {}}}) )

        print( opensearch_connect.opensearch_count_documents(index_name='my_cpu_data', document={"query": {"match_all": {}}} ))



        time.sleep(2)

