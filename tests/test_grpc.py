# test_grpc.py
import grpc
import pytest
from woolyherdz.generated import woolyherdz_pb2

def test_UploadDataset(grpc_stub):
    # Simulate uploading a dataset
    response = grpc_stub.UploadDataset(woolyherdz_pb2.UploadDatasetRequest(token="valid_token", dataset=b"dummy dataset"))
    assert response.status == "Received"

def test_TrainModel(grpc_stub):
    # Simulate training a model
    response = grpc_stub.TrainModel(woolyherdz_pb2.TrainModelRequest(token="valid_token", datasetId="dummy_dataset_id"))
    assert response.status == "Training started: echo"

def test_Predict(grpc_stub):
    # Simulate making a prediction
    response = grpc_stub.Predict(woolyherdz_pb2.PredictRequest(token="valid_token", modelId="dummy_model_id", inputData=b"test input"))
    assert response.outputData == "Prediction result: echo"

def test_GetStatus(grpc_stub):
    # Simulate retrieving the status of a task
    response = grpc_stub.GetStatus(woolyherdz_pb2.StatusRequest(token="valid_token", taskId="upload_dataset_task"))
    assert response.status == "Received"
