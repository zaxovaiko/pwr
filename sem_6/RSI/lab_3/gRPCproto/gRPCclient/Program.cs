using Grpc.Core;
using Mygrpcproto;
using System;

namespace gRPCclient
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Starting gRPC client");
            Channel channel = new Channel("127.0.0.1:10000", ChannelCredentials.Insecure);

            var client = new MyGrpcSrv.MyGrpcSrvClient(channel);

            String str;
            int num1, num2;

            Console.WriteLine("Enter number 1: ");
            str = Console.ReadLine();

            if (int.TryParse(str, out num1))
            {
                Console.Write("Enter number 2: ");
                str = Console.ReadLine();

                if (int.TryParse(str, out num2))
                {
                    var reply = client.addInt(new AddIntRequest { Num1 = num1, Num2 = num2 });
                    Console.WriteLine("From server: " + reply.Comment + reply.Result);
                } else
                {
                    Console.WriteLine("Wrong data!");
                }
            }
            else
            {
                Console.WriteLine("Wrong data!");
            }
            Console.WriteLine("Stopping client");
            channel.ShutdownAsync().Wait();
        }
    }
}
