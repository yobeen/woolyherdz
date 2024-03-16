from concurrent import futures
import grpc

from .generated import woolyherdz_pb2_grpc
from .grpc import WoolyherdzService

from .auth import AuthInterceptor

class Server:

    @staticmethod
    def run():
        # Create a server with the AuthInterceptor
        server = grpc.server(
            futures.ThreadPoolExecutor(max_workers=10),
            interceptors=[AuthInterceptor()]  # Include the interceptor here
        )
        woolyherdz_pb2_grpc.add_WoolyherdzServicer_to_server(WoolyherdzService(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        server.wait_for_termination()
