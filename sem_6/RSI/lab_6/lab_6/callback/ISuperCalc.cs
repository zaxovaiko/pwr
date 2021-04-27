using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;

namespace callback
{
    public interface ISuperCalcCallback
    {
        [OperationContract(IsOneWay = true)]
        void FactorialResult(double result);
        [OperationContract(IsOneWay = true)]
        void DoSomethingResult(string result);
    }

    [ServiceContract (SessionMode = SessionMode.Required, CallbackContract = typeof(ISuperCalcCallback))]
    public interface ISuperCalc
    {
        [OperationContract(IsOneWay = true)]
        void Factorial(double n);

        [OperationContract(IsOneWay = true)]
        void DoSomething(int sec);
    }
}
