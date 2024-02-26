import data_retriever
import time




#
#
# while True:
#     cpu_utilization_percentage = psutil.cpu_percent()
#     virtual_memory_percent = psutil.virtual_memory().percent
#     time.sleep(1)




if __name__ == '__main__':
    while True:
        print(data_retriever.retrieve_memory_information())
        print(data_retriever.retrieve_cpu_information())
        print(data_retriever.retrieve_disk_information('/'))
        print()
        time.sleep(3)
