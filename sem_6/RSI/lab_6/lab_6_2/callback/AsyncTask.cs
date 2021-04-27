using contract;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;
using System.Threading;

namespace callback
{
    [ServiceBehavior(InstanceContextMode = InstanceContextMode.PerSession, ConcurrencyMode = ConcurrencyMode.Multiple)]
    public class AsyncTask : IAsyncTask
    {
        IAsyncTaskCallback callback = null;

        public AsyncTask()
        {
            callback = OperationContext.Current.GetCallbackChannel<IAsyncTaskCallback>();
        }

        public void Repeat(Task task)
        {
            Console.WriteLine("Repeat string '{0}' {1} times", task.text, task.times);
            Thread.Sleep(task.times * 1000);
            callback.RepeatResult(new string('+', task.times).Replace("+", task.text));
        }
    }
}
