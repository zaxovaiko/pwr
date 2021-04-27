using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;
using System.Threading;

namespace contract
{
    public class MyComplexCalc : ICCalculator
    {
        public ComplexNum addCNum(ComplexNum n1, ComplexNum n2)
        {
            Console.WriteLine("...called addCNum()");
            return new ComplexNum(n1.real + n2.real, n1.imag + n2.imag);
        }
    }

    public class MyAsyncComplexCalc : IAsyncCCalculator
    {
        public void Fun1(string s1)
        {
            Console.WriteLine("...Fun1 - start");
            Thread.Sleep(4000);
            Console.WriteLine("...Fun1 - stop");
            return;
        }

        public void Fun2(string s2)
        {
            Console.WriteLine("...Fun2 - start");
            Thread.Sleep(2000);
            Console.WriteLine("...Fun2 - stop");
            return;
        }
    }
}
