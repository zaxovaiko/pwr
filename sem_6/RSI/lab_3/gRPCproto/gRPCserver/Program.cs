using Grpc.Core;
using Mygrpcproto;
using System;

namespace gRPCserver
{
    class Program
    {
        const int port = 10000;
        static void Main(string[] args)
        {
            Console.WriteLine("Starting Hello gRPC server");
            Server myServer = new Server
            {
                Services = { MyGrpcSrv.BindService(new MyGrpcSrvImpl()) },
                Ports = { new ServerPort("localhost", port, ServerCredentials.Insecure) }
            };
            myServer.Start();
            Console.WriteLine("Hello gRPC server listeting on port " + port);
            Console.WriteLine("Press any key to stop the server");
            Console.ReadKey();
            myServer.ShutdownAsync().Wait();
        }
    }
}
