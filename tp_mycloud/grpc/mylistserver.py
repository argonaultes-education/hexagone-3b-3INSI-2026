import pathlib
import sys
import mylist_pb2_grpc
import mylist_pb2
import grpc
from concurrent import futures
import logging



class MyListServer(mylist_pb2_grpc.MyListServicer):
    
    def GiveMyList(self, request, context):
        target_path = sys.argv[1]
        target_pathlib = pathlib.Path(target_path)
        result = list(map(lambda f: f.as_posix(), list(target_pathlib.iterdir())))
        return mylist_pb2.MyListResponse(files=result)
        

def serve():
    port = "50051"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mylist_pb2_grpc.add_MyListServicer_to_server(MyListServer(), server)
    server.add_insecure_port("[::]:" + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()

if __name__ == "__main__":
    logging.basicConfig()
    serve()