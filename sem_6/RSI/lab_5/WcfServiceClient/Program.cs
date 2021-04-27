using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using WcfServiceClient.ServiceReference1;

namespace WcfServiceClient
{
    class Program
    {
        static void Main(string[] args)
        {
            CalculatorClient client1 = new CalculatorClient("WSHttpBinding_ICalculator");
            CalculatorClient client2 = new CalculatorClient("BasicHttpBinding_ICalculator");
            CalculatorClient client3 = new CalculatorClient("myEndpoint3");

            Console.WriteLine("Client1:");
            Console.WriteLine(client1.Add(2, 5));
            Console.WriteLine(client1.Sub(2, 5));
            Console.WriteLine(client1.Multiply(2, 5));
            Console.WriteLine(client1.Summarize(8));

            // HAVE PROBLEM HERE
            //Console.WriteLine("\nClient2:");
            //Console.WriteLine(client2.Add(4, 5));
            //Console.WriteLine(client2.Sub(4, 5));
            //Console.WriteLine(client2.Multiply(4, 5));
            //Console.WriteLine(client2.Summarize(8));

            Console.WriteLine("\nClient3:");
            Console.WriteLine(client3.Add(2, 3));
            Console.WriteLine(client3.Sub(2, 3));
            Console.WriteLine(client3.Multiply(2, 3));
            Console.WriteLine(client3.Summarize(8));
 
            Console.Read();
            client1.Close();
            client2.Close();
            client3.Close();
        }
    }
}
