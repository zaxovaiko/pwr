using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;

namespace contract
{
    [ServiceContract]
    public interface IServiceTask
    {
        [OperationContract]
        Task GetTaskById(int id);

        [OperationContract]
        void AddTask(Task task);

        [OperationContract]
        Task RemoveTask(int id);

        [OperationContract]
        Task UpdateTask(int id, string text, int times);
    }

    [DataContract]
    public class Task
    {
        [DataMember]
        public int id;

        [DataMember]
        public string text;

        [DataMember]
        public int times;

        public Task(int id, string text, int times)
        {
            this.id = id;
            this.text = text;
            this.times = times;
        }
    }
}
