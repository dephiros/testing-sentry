# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import helloworld2_pb2 as helloworld2__pb2


class Greeter2Stub(object):
    """The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello2 = channel.unary_unary(
                '/helloworld2.Greeter2/SayHello2',
                request_serializer=helloworld2__pb2.HelloRequest2.SerializeToString,
                response_deserializer=helloworld2__pb2.HelloReply2.FromString,
                )
        self.SayHelloStreamReply2 = channel.unary_stream(
                '/helloworld2.Greeter2/SayHelloStreamReply2',
                request_serializer=helloworld2__pb2.HelloRequest2.SerializeToString,
                response_deserializer=helloworld2__pb2.HelloReply2.FromString,
                )
        self.SayHelloBidiStrea2 = channel.stream_stream(
                '/helloworld2.Greeter2/SayHelloBidiStrea2',
                request_serializer=helloworld2__pb2.HelloRequest2.SerializeToString,
                response_deserializer=helloworld2__pb2.HelloReply2.FromString,
                )


class Greeter2Servicer(object):
    """The greeting service definition.
    """

    def SayHello2(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHelloStreamReply2(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SayHelloBidiStrea2(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Greeter2Servicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello2': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello2,
                    request_deserializer=helloworld2__pb2.HelloRequest2.FromString,
                    response_serializer=helloworld2__pb2.HelloReply2.SerializeToString,
            ),
            'SayHelloStreamReply2': grpc.unary_stream_rpc_method_handler(
                    servicer.SayHelloStreamReply2,
                    request_deserializer=helloworld2__pb2.HelloRequest2.FromString,
                    response_serializer=helloworld2__pb2.HelloReply2.SerializeToString,
            ),
            'SayHelloBidiStrea2': grpc.stream_stream_rpc_method_handler(
                    servicer.SayHelloBidiStrea2,
                    request_deserializer=helloworld2__pb2.HelloRequest2.FromString,
                    response_serializer=helloworld2__pb2.HelloReply2.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'helloworld2.Greeter2', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Greeter2(object):
    """The greeting service definition.
    """

    @staticmethod
    def SayHello2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/helloworld2.Greeter2/SayHello2',
            helloworld2__pb2.HelloRequest2.SerializeToString,
            helloworld2__pb2.HelloReply2.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHelloStreamReply2(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/helloworld2.Greeter2/SayHelloStreamReply2',
            helloworld2__pb2.HelloRequest2.SerializeToString,
            helloworld2__pb2.HelloReply2.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SayHelloBidiStrea2(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/helloworld2.Greeter2/SayHelloBidiStrea2',
            helloworld2__pb2.HelloRequest2.SerializeToString,
            helloworld2__pb2.HelloReply2.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
