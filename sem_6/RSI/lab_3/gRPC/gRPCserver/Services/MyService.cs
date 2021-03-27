using Google.Protobuf.WellKnownTypes;
using Grpc.Core;
using GRPCproto;
using Microsoft.Extensions.Logging;
using System;
using System.Collections.Generic;
using System.IO;
using System.Threading.Tasks;

namespace gRPCserver
{
    public class MyService : GRPCservice.GRPCserviceBase
    {

        private static string tempString = "";

        private readonly ILogger<MyService> _logger;
        public MyService(ILogger<MyService> logger)
        {
            _logger = logger;
        }

        public override Task<RepeatStringReply> RepeatString(RepeatStringRequest request, ServerCallContext context)
        {
            Console.WriteLine("Called repeatString task");
            tempString = request.Str;
            return Task.FromResult(new RepeatStringReply
            {
                Result = "".PadLeft(request.Num, 'X').Replace("X", request.Str)
            });
        }

        public override async Task<TimeoutPrintReply> TimeoutPrint(TimeoutPrintRequest request, ServerCallContext context)
        {
            Console.WriteLine("Called async timeout print task");
            await Task.Delay((int) request.Secs * 1000);   
            try
            {
                return await Task.FromResult(new TimeoutPrintReply
                {
                    Result = tempString[request.Index] + ""
                });
            } catch (Exception)
            {
                Console.WriteLine("String does not have as many chars!");
                return await Task.FromResult(new TimeoutPrintReply
                {
                    Result = "Something went wrong"
                });
            }
        }

        public override Task<UploadImageReply> UploadImage(UploadImageRequest request, ServerCallContext context)
        {
            Console.WriteLine("Called upload image method");

            var data = Convert.FromBase64String(request.Image);
            File.WriteAllBytes("../../../fromClient.jpg", data);

            return Task.FromResult(new UploadImageReply
            {
                Result = "Success"
            });
        }

        public override async Task DownloadImage(Empty request, IServerStreamWriter<DownloadImageResponse> responseStream, ServerCallContext context)
        {
            //return base.DownloadImage(request, responseStream, context);
            byte[] data = File.ReadAllBytes("../../../onServer.jpg");

            int parts = data.Length / 100;
            byte[] part;

            _logger.LogInformation("Sending image chunk...");
            for (int i = 0; i < 100; i++)
            {
                part = new byte[parts];
                Array.Copy(data, i * parts, part, 0, parts);

                await responseStream.WriteAsync(new DownloadImageResponse
                {
                    Image = Google.Protobuf.ByteString.CopyFrom(part)
                });
            }
            _logger.LogInformation("Image was sent.");
        }
    }
}
