using client.TaskRef;
using System;
using System.Collections.Generic;
using System.Linq;
using System.ServiceModel;
using System.Text;
using System.Threading.Tasks;
using Task = client.TaskRef.Task;

namespace client
{
    class AsyncTaskCallback : IAsyncTaskCallback
    {
        public void RepeatResult(string result)
        {
            Console.WriteLine("Async function ended execution: {0}", result);
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            ServiceTaskClient client = new ServiceTaskClient("WSHttpBinding_IServiceTask");

            Task task1 = new Task { id = 1, text = "hello", times = 5 };
            Task task2 = new Task { id = 2, text = "world", times = 2 };
            Task task3 = new Task { id = 3, text = "koala", times = 4 };
            Task task4 = new Task { id = 4, text = "macro", times = 3 };

            Console.WriteLine("Client ServiceTask is running");

            client.AddTask(task1);
            client.AddTask(task2);
            client.AddTask(task3);
            client.AddTask(task4);
            Console.WriteLine("Tasks were added.");

            var removedTask = client.RemoveTask(3);
            var task = client.GetTaskById(3);
            Console.WriteLine("Removed task id: {0}", removedTask.id);
            Console.WriteLine("Task should not exists: {0}", task);

            Console.WriteLine();
            AsyncTaskCallback callback = new AsyncTaskCallback();
            InstanceContext ctx = new InstanceContext(callback);
            AsyncTaskClient asyncClient = new AsyncTaskClient(ctx);

            Console.WriteLine("Async requests:");
            var exampleTask = client.GetTaskById(4);
            asyncClient.Repeat(task1);
            asyncClient.Repeat(exampleTask);

            Console.WriteLine("Press ENTER to exit");
            Console.Read();

            client.Close();
            asyncClient.Close();
        }
    }
}
