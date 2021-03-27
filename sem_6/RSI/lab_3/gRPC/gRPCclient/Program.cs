using Google.Protobuf.WellKnownTypes;
using Grpc.Core;
using Grpc.Net.Client;
using GRPCproto;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading;
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

            // Different params upload
            var reply = client.RepeatString(new RepeatStringRequest
            {
                Str = "hello",
                Num = 3
            });
            Console.WriteLine("Different types reply: " + reply.Result);

            // Async method
            var asyncReply = await client.TimeoutPrintAsync(new TimeoutPrintRequest
            {
                Index = 3,
                Secs = 1.5
            });
            Console.WriteLine("Async reply: " + asyncReply.Result);

            // Image upload
            byte[] data = File.ReadAllBytes("../../../onClient.jpg");
            var imageReply = client.UploadImage(new UploadImageRequest
            {
                Image = Convert.ToBase64String(data)
            });
            Console.WriteLine("Image upload: " + imageReply.Result);

            // Download image with stream %
            var downloadedImage = client.DownloadImage(new Empty());
            var dImage = new Stack<byte>();
            List<byte> array = new List<byte>();

            int j = 0;
            await foreach (var imagePart in downloadedImage.ResponseStream.ReadAllAsync())
            {
                for (int i = 0; i < imagePart.Image.Length; i++)
                {
                    array.Add(imagePart.Image[i]);
                }
                Console.Write("\r[{0}] {1}%", "*".PadLeft(j / 10, '*').PadRight(9, ' '), ++j);
                Thread.Sleep(50);
            }
            File.WriteAllBytes("../../../fromServer.jpg", array.ToArray());

            channel.ShutdownAsync().Wait();
            Console.Read();
        }
    }
}
