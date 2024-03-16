import grpc
from grpc import ServerInterceptor, ServicerContext, StatusCode
from typing import Callable, Any

class Unauthenticated(Exception):
    pass

# Dummy mapping of endpoint names to required permissions
ENDPOINT_TO_PERM = {
    'UploadDataset': 'upload',
    'TrainModel': 'train',
    'Predict': 'predict',
    'GetStatus': 'status',
}

def get_token_from_metadata(metadata):
    for key, value in metadata:
        if key == 'authorization':
            return value
    return None

def check_user_auth(permission, token):
    # Dummy check: In a real scenario, validate the token and check permissions
    return token == "valid_token"

class AuthInterceptor(ServerInterceptor):
    def intercept(
        self,
        method: Callable,
        request_or_iterator: Any,
        context: ServicerContext,
        method_name: str,
    ) -> Any:
        metadata = context.invocation_metadata()
        endpoint = method_name.split("/")[-1]
        
        if not metadata:
            context.set_code(StatusCode.UNAUTHENTICATED)
            context.set_details("No auth token sent")
            raise Unauthenticated("No auth token sent", StatusCode.UNAUTHENTICATED)
        
        token = get_token_from_metadata(metadata)
        if token is None:
            context.set_code(StatusCode.UNAUTHENTICATED)
            context.set_details("Auth token not found")
            raise Unauthenticated("Auth token not found", StatusCode.UNAUTHENTICATED)
        
        authed = check_user_auth(ENDPOINT_TO_PERM.get(endpoint, ''), token)
        if not authed:
            context.set_code(StatusCode.UNAUTHENTICATED)
            context.set_details("You don't have access to this resource")
            raise Unauthenticated("You don't have access to this resource.", StatusCode.UNAUTHENTICATED)
        
        return method(request_or_iterator, context)
