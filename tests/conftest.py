# conftest.py
import pytest
import grpc
from concurrent import futures

from woolyherdz.generated import woolyherdz_pb2_grpc
from woolyherdz.grpc import WoolyherdzService

@pytest.fixture(scope="module")
def grpc_add_to_server():
    return woolyherdz_pb2_grpc.add_WoolyherdzService_to_server

@pytest.fixture(scope="module")
def grpc_servicer():
    return WoolyherdzService()

@pytest.fixture(scope="module")
def grpc_stub_cls(grpc_channel):
    return woolyherdz_pb2_grpc.WoolyherdzServiceStub
