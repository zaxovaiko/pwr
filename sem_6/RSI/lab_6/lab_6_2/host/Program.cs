using callback;
using contract;
using System;
using System.Collections.Generic;
using System.Linq;
using System.ServiceModel;
using System.ServiceModel.Description;
using System.Text;
using System.Threading.Tasks;

namespace host
{
    class Program
    {
        static void Main(string[] args)
        {
            Uri baseAddress1 = new Uri("http://localhost:10000/Task");
            Uri baseAddress2 = new Uri("http://localhost:10000/AsyncTask");

            ServiceHost myHost1 = new ServiceHost(typeof(ServiceTask), baseAddress1);
            ServiceHost myHost2 = new ServiceHost(typeof(AsyncTask), baseAddress2);

            ServiceEndpoint endpoint1 = myHost1.AddServiceEndpoint(typeof(IServiceTask), new WSHttpBinding(), "endpoint1");
            ServiceEndpoint endpoint2 = myHost2.AddServiceEndpoint(typeof(IAsyncTask), new WSDualHttpBinding(), "endpoint2");

            // metadata
            ServiceMetadataBehavior smb = new ServiceMetadataBehavior();
            smb.HttpGetEnabled = true;
            myHost1.Description.Behaviors.Add(smb);
            myHost2.Description.Behaviors.Add(smb);

            try
            {
                myHost1.Open();
                myHost2.Open();
                Console.WriteLine("🚩 host is running.");
                Console.WriteLine("Binding endpoint1 with: {0}", endpoint1.Binding.ToString());
                Console.WriteLine("Binding endpoint2 with: {0}", endpoint2.Binding.ToString());
                Console.WriteLine("Press ENTER to exit");
                Console.WriteLine();
                
            } catch (CommunicationException e)
            {
                Console.WriteLine("Exception occurred: {0}", e);
                myHost1.Abort();
                myHost2.Abort();
            }

            Console.Read();
            myHost1.Close();
            myHost2.Close();
        }
    }
}