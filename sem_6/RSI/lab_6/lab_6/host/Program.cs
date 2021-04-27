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
            Uri baseAddress1 = new Uri("http://localhost:10000/ComplexCalc");
            Uri baseAddress2 = new Uri("http://localhost:10000/AsyncComplexCalc");
            Uri baseAddress3 = new Uri("http://localhost:10000/AsyncSuperComplexCalc");

            ServiceHost myHost1 = new ServiceHost(typeof(MyComplexCalc), baseAddress1);
            ServiceHost myHost2 = new ServiceHost(typeof(MyAsyncComplexCalc), baseAddress2);
            ServiceHost myHost3 = new ServiceHost(typeof(MySuperCalc), baseAddress3);

            ServiceEndpoint endpoint1 = myHost1.AddServiceEndpoint(typeof(ICCalculator), new WSHttpBinding(), "endpoint1");
            ServiceEndpoint endpoint2 = myHost2.AddServiceEndpoint(typeof(IAsyncCCalculator), new BasicHttpBinding(), "endpoint2");
            ServiceEndpoint endpoint3 = myHost3.AddServiceEndpoint(typeof(ISuperCalc), new WSDualHttpBinding(), "endpoint3");

            // metadata
            ServiceMetadataBehavior smb = new ServiceMetadataBehavior();
            smb.HttpGetEnabled = true;
            myHost1.Description.Behaviors.Add(smb);
            myHost2.Description.Behaviors.Add(smb);
            myHost3.Description.Behaviors.Add(smb);

            try
            {
                myHost1.Open();
                myHost2.Open();
                myHost3.Open();
                Console.WriteLine("--> ComplexCalculator is running.");
                Console.WriteLine("--> AsyncComplexCalculator is running.");
                Console.WriteLine("--> Binding endpoint1 with: {0}", endpoint1.Binding.ToString());
                Console.WriteLine("--> Binding endpoint2 with: {0}", endpoint2.Binding.ToString());
                Console.WriteLine("--> Binding endpoint3 with: {0}", endpoint3.Binding.ToString());
                Console.WriteLine("--> Press ENTER to exit");
                
            } catch (CommunicationException e)
            {
                Console.WriteLine("Exception occurred: {0}", e);
                myHost1.Abort();
                myHost2.Abort();
                myHost3.Abort();
            }

            Console.Read();
            myHost1.Close();
            myHost2.Close();
            myHost3.Close();
        }
    }
}
