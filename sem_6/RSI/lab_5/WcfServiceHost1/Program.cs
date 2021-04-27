using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Security;
using System.ServiceModel;
using System.ServiceModel.Description;
using System.Text;
using System.Threading.Tasks;
using WcfServiceContract1;

namespace WcfServiceHost1
{
    class Program
    {
        static void Main(string[] args)
        {
            Uri baseAddress = new Uri("http://localhost:8000/NazwaBazowa");
            ServiceHost myHost = new ServiceHost(typeof(MyCalculator), baseAddress);

            BasicHttpBinding binding = new BasicHttpBinding();
            Console.WriteLine(binding.Security.Mode);
            binding.Security.Mode = BasicHttpSecurityMode.None;
            
            ServiceEndpoint endpoint1 = myHost.AddServiceEndpoint(typeof(ICalculator), new WSHttpBinding(), "endpoint1");
            ServiceEndpoint endpoint2 = myHost.AddServiceEndpoint(typeof(ICalculator), binding, "endpoint2");
            ServiceEndpoint endpoint3 = myHost.Description.Endpoints.Find(new Uri("http://localhost:8000/MyService/endpoint3"));

            ServiceMetadataBehavior smb = new ServiceMetadataBehavior();
            smb.HttpGetEnabled = true;
            myHost.Description.Behaviors.Add(smb);

            try
            {
                Console.WriteLine("Endpoints:");
                Console.WriteLine("Service endpoint {0}: ", endpoint1.Name);
                Console.WriteLine("Binding {0}: ", endpoint1.Binding.ToString());
                Console.WriteLine("ListenUri {0}: ", endpoint1.ListenUri.ToString());

                Console.WriteLine("\nService endpoint {0}: ", endpoint2.Name);
                Console.WriteLine("Binding {0}: ", endpoint2.Binding.ToString());
                Console.WriteLine("ListenUri {0}: ", endpoint2.ListenUri.ToString());

                myHost.Open();
                Console.WriteLine("Service is running");
                Console.WriteLine("Press ENTER to stop");
                Console.WriteLine();
            }
            catch (CommunicationException e)
            {
                Console.WriteLine(e.Message);
                myHost.Abort();
            }
            Console.Read();
            myHost.Close();
        }
    }
}
