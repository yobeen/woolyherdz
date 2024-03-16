from .generated import woolyherdz_pb2, woolyherdz_pb2_grpc
from .status_manager import StatusManager

class WoolyherdzService(woolyherdz_pb2_grpc.WoolyherdzService):
    def __init__(self):
        self.status_manager = StatusManager()

    def UploadDataset(self, request, context):
        # Example task status update
        self.status_manager.update_status("upload_dataset_task", "Received")
        return woolyherdz_pb2.UploadDatasetResponse(status='Received')

    def TrainModel(self, request, context):
        return woolyherdz_pb2.TrainModelResponse(modelId='dummy_model_id', status='Training started: echo')

    def Predict(self, request, context):
        return woolyherdz_pb2.PredictResponse(outputData='Prediction result: echo')

    def GetStatus(self, request, context):
        task_status = self.status_manager.get_status(request.taskId)
        return woolyherdz_pb2.StatusResponse(status=task_status)