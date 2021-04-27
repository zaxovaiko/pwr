using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;
using System.Threading;

namespace contract
{
    public class ServiceTask : IServiceTask
    {
        static List<Task> tasks = new List<Task>();

        public void AddTask(Task task)
        {
            tasks.Add(task);
            Console.WriteLine("Task was added to the list");
        }

        public Task GetTaskById(int id)
        {
            foreach (var task in tasks)
            {
                if (task.id == id)
                {
                    Console.WriteLine("Task was found by id ({0})", id);
                    return task;
                }
            }
            Console.WriteLine("Task was not found in the list");
            return null;
        }

        public Task RemoveTask(int id)
        {
            foreach (var task in tasks)
            {
                if (task.id == id)
                {
                    tasks.Remove(task);
                    Console.WriteLine("Task was removed.");
                    return task;
                }
            }
            Console.WriteLine("Task was not found to remove.");
            return null;
        }

        public Task UpdateTask(int id, string text, int times)
        {
            foreach (var task in tasks)
            {
                if (task.id == id)
                {
                    task.text = text;
                    task.times = times;
                    Console.WriteLine("Task was updated.");
                    return task;
                }
            }
            Console.WriteLine("Task was not found to update.");
            return null;
        }
    }
}
