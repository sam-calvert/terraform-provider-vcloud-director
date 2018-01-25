# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from proto import disk_pb2 as proto_dot_disk__pb2


class IndependentDiskStub(object):
    # missing associated documentation comment in .proto file
    pass

    def __init__(self, channel):
        """Constructor.

    Args:
      channel: A grpc.Channel.
    """
        self.Create = channel.unary_unary(
            '/proto.IndependentDisk/Create',
            request_serializer=proto_dot_disk__pb2.CreateDiskInfo.
            SerializeToString,
            response_deserializer=proto_dot_disk__pb2.CreateDiskResult.
            FromString,
        )
        self.Read = channel.unary_unary(
            '/proto.IndependentDisk/Read',
            request_serializer=proto_dot_disk__pb2.ReadDiskInfo.
            SerializeToString,
            response_deserializer=proto_dot_disk__pb2.ReadDiskResult.
            FromString,
        )
        self.Delete = channel.unary_unary(
            '/proto.IndependentDisk/Delete',
            request_serializer=proto_dot_disk__pb2.DeleteDiskInfo.
            SerializeToString,
            response_deserializer=proto_dot_disk__pb2.DeleteDiskResult.
            FromString,
        )


class IndependentDiskServicer(object):
    # missing associated documentation comment in .proto file
    pass

    def Create(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        # missing associated documentation comment in .proto file
        pass
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IndependentDiskServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Create':
        grpc.unary_unary_rpc_method_handler(
            servicer.Create,
            request_deserializer=proto_dot_disk__pb2.CreateDiskInfo.FromString,
            response_serializer=proto_dot_disk__pb2.CreateDiskResult.
            SerializeToString,
        ),
        'Read':
        grpc.unary_unary_rpc_method_handler(
            servicer.Read,
            request_deserializer=proto_dot_disk__pb2.ReadDiskInfo.FromString,
            response_serializer=proto_dot_disk__pb2.ReadDiskResult.
            SerializeToString,
        ),
        'Delete':
        grpc.unary_unary_rpc_method_handler(
            servicer.Delete,
            request_deserializer=proto_dot_disk__pb2.DeleteDiskInfo.FromString,
            response_serializer=proto_dot_disk__pb2.DeleteDiskResult.
            SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'proto.IndependentDisk', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler, ))