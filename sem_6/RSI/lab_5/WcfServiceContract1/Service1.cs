using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;

namespace WcfServiceContract1
{
    [ServiceBehavior(InstanceContextMode = InstanceContextMode.Single)]
    public class MyCalculator : ICalculator
    {
        double sum = 0;
        public double Add(double n1, double n2)
        {
            Console.WriteLine("Add(n1 = " + n1 + " n2 = " + n2 + ") res = " + n1 + n2);
            return n1 + n2;
        }

        public double Sub(double n1, double n2)
        {
            Console.WriteLine("Sub(n1 = " + n1 + " n2 = " + n2 + ") res = " + (n1 - n2));
            return n1 - n2;
        }

        public double Multiply(double n1, double n2)
        {
            Console.WriteLine("Mul(n1 = " + n1 + " n2 = " + n2 + ") res = " + n1 * n2);
            return n1 * n2;
        }

        public double Summarize(double n1)
        {
            sum += n1;
            return sum;
        }
    }
}
