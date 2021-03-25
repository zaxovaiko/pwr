using Grpc.Core;
using Mygrpcproto;
using System.Threading.Tasks;

namespace gRPCserver
{
    public class MyGrpcSrvImpl : MyGrpcSrv.MyGrpcSrvBase
    {
        public override Task<AddIntReply> addInt(AddIntRequest req, ServerCallContext ctx)
        {
            string comment = "hello";
            int result = 2;

            return Task.FromResult(new AddIntReply { Result = result, Comment = comment });
        }
    }
}
