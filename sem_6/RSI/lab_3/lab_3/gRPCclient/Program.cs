using Grpc.Core;
using Grpc.Net.Client;
using GRPCproto;
using System;
using System.IO;
using System.Threading.Tasks;

namespace gRPCclient
{
    class Program
    {
        static async Task Main(string[] args)
        {
            var channel = GrpcChannel.ForAddress("http://localhost:5000");
            var client = new GRPCservice.GRPCserviceClient(channel);
            Console.WriteLine("Clint was started");

            // Async method
            var asyncReply = await client.TimeoutPrintAsync(new TimeoutPrintRequest
            {
                Index = 3,
                Secs = 1.5
            });
            Console.WriteLine("Async reply: " + asyncReply.Result);

            // Different params upload
            var reply = client.RepeatString(new RepeatStringRequest
            {
                Str = "hello",
                Num = 3
            });
            Console.WriteLine("Different types reply: " + reply.Result);

            // Image upload
            byte[] data = File.ReadAllBytes("./cat.jpg");

            // Different params upload
            var imageReply = client.UploadImage(new UploadImageRequest
            {
                Image = Convert.ToBase64String(data)
            });
            Console.WriteLine("Image upload: " + imageReply.Result);

            channel.ShutdownAsync().Wait();
            Console.Read();
        }
    }
}
