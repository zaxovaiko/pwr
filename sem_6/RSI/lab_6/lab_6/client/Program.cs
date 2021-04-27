using client.ServiceReference1;
using client.ServiceReference2;
using client.ServiceReference3;
using System;
using System.Collections.Generic;
using System.Linq;
using System.ServiceModel;
using System.Text;
using System.Threading.Tasks;

namespace client
{
    class SuperCalcCallback : ISuperCalcCallback
    {
        public void DoSomethingResult(string result)
        {
            Console.WriteLine("Factorial = {0}", result);
        }

        public void FactorialResult(double result)
        {
            Console.WriteLine("Calcs = {0}", result);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            CCalculatorClient client1 = new CCalculatorClient("WSHttpBinding_ICCalculator");

            // numbers
            ComplexNum cnum1 = new ComplexNum();
            cnum1.real = 1.2;
            cnum1.imag = 3.4;
            ComplexNum cnum2 = new ComplexNum();
            cnum1.real = 5.6;
            cnum1.imag = 7.8;

            Console.WriteLine("Client1 - start");
            Console.WriteLine("calling addCNum()");
            ComplexNum result1 = client1.addCNum(cnum1, cnum2);
            Console.WriteLine("addCNum() = ({0}, {1})", result1.real, result1.imag);
            client1.Close();


            // second client
            Console.WriteLine("Client2 - start");
            AsyncCCalculatorClient client2 = new AsyncCCalculatorClient("BasicHttpBinding_IAsyncCCalculator");
            Console.WriteLine("...calling Fun1()");
            client2.Fun1("Client2");
            Console.WriteLine("...continue after Fun1()");

            Console.WriteLine("...calling Fun2()");
            client2.Fun2("Client2");
            Console.WriteLine("...continue after Fun2()");
            

            // third client
            Console.WriteLine("Client3 - start");

            SuperCalcCallback callback = new SuperCalcCallback();
            InstanceContext ic = new InstanceContext(callback);
            SuperCalcClient client3 = new SuperCalcClient(ic);

            double value1 = 10;
            Console.WriteLine("...calling Factorial({0})", value1);
            client3.Factorial(value1);

            int value2 = 5;
            Console.WriteLine("...calling DoSomething");
            client3.DoSomething(value2);

            value1 = 20;
            Console.WriteLine("...calling Factorial({0})", value1);
            client3.Factorial(value1);

            Console.WriteLine("...Client must wait for results");

            Console.WriteLine("--> Press ENTER to continue");
            Console.Read();

            client2.Close();
            client3.Close();
        }
    }
}
