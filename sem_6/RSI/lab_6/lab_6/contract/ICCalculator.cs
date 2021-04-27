using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;

namespace contract
{
    [ServiceContract]
    public interface IAsyncCCalculator
    {
        [OperationContract(IsOneWay = true)]
        void Fun1(String s1);
        [OperationContract]
        void Fun2(String s2);
    }

    [ServiceContract]
    public interface ICCalculator
    {
        [OperationContract]
        ComplexNum addCNum(ComplexNum n1, ComplexNum n2);
    }

    [DataContract]
    public class ComplexNum
    {
        string description = "Complex number ";

        [DataMember]
        public double real;

        [DataMember]
        public double imag;

        [DataMember]
        public string Desc
        {
            get { return description; }
            set { description = value; }
        }

        public ComplexNum(double r, double i)
        {
            this.real = r;
            this.imag = i;
        }
    }
}
