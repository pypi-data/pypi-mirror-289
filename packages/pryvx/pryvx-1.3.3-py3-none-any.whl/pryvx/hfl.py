import grpc
import pryvx_pb2
import pryvx_pb2_grpc
from sklearn.linear_model import LogisticRegression
import pickle
from concurrent import futures
import time

# Client
class FL_CLIENT:

    @staticmethod
    def train(features, labels):
        model = LogisticRegression()
        model.fit(features, labels)

        serialized_model = pickle.dumps(model)

        return serialized_model

    @staticmethod
    def send_params(serialized_model, connection_url):

        with grpc.insecure_channel(connection_url) as channel:
            stub = pryvx_pb2_grpc.ModelServiceStub(channel)

            model_params = pryvx_pb2.ModelParams(params=serialized_model)

            response = stub.SendModelParams(model_params)

            return "Model Params sent to server"


# Server
class ModelServicer(pryvx_pb2_grpc.ModelServiceServicer):
    def __init__(self):
        self.client_params = {}

    def SendModelParams(self, request, context):
        # Deserialize the model
        loaded_model = pickle.loads(request.params)

        # save model to gcp storage bucket

        print("Received model params from client")

        return pryvx_pb2.ModelParams(params=request.params)

class FL_SERVER:

    @staticmethod
    def start_server():
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        pryvx_pb2_grpc.add_ModelServiceServicer_to_server(ModelServicer(), server)
        server.add_insecure_port('[::]:50051')
        server.start()
        print("Server started. Listening on localhost:50051")

        try:
            while True:
                time.sleep(86400)
        except KeyboardInterrupt:
            server.stop(0)

