import logging
import grpc
import mylist_pb2
import mylist_pb2_grpc
import sys



def run(target_host, target_port):
    with grpc.insecure_channel(f"{target_host}:{target_port}") as channel:
        stub = mylist_pb2_grpc.MyListStub(channel=channel)
        response = stub.GiveMyList(mylist_pb2.MyListRequest())
        for file in response.files:
            print(file)

if __name__ == "__main__":
    logging.basicConfig()
    target_host, target_port = sys.argv[1], sys.argv[2]
    run(target_host=target_host, target_port=target_port)