using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Web;
using System.Text;
using System.ServiceModel.Activation;


namespace service
{
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the interface name "IService1" in both code and config file together.
    [ServiceContract]
    public interface IRestService
    {

        [OperationContract]
        [WebInvoke(Method = "*", UriTemplate="/countries")]
        List<Country> GetAllXml();

        [OperationContract]
        [WebGet(UriTemplate = "/json/countries", RequestFormat = WebMessageFormat.Json, ResponseFormat = WebMessageFormat.Json)]
        List<Country> GetAllJson();

        [OperationContract]
        [WebGet(UriTemplate = "/countries/{id}", ResponseFormat = WebMessageFormat.Xml)]
        Country GetByIdXml(string Id);

        [OperationContract]
        [WebGet(UriTemplate = "/json/countries/{id}", RequestFormat = WebMessageFormat.Json, ResponseFormat = WebMessageFormat.Json)]
        Country GetByIdJson(string Id);

        [OperationContract]
        [WebInvoke(UriTemplate = "/countries", Method = "POST", RequestFormat = WebMessageFormat.Xml)]
        string AddXml(Country country);

        [OperationContract]
        [WebInvoke(UriTemplate = "/json/countries", Method = "POST", RequestFormat = WebMessageFormat.Json, ResponseFormat = WebMessageFormat.Json)]
        string AddJson(Country country);

        [OperationContract]
        [WebInvoke(UriTemplate = "/countries/{id}", Method = "PUT", RequestFormat = WebMessageFormat.Xml)]
        Country UpdateXml(string id, Country country);

        [OperationContract]
        [WebInvoke(UriTemplate = "/json/countries/{id}", Method = "PUT", RequestFormat = WebMessageFormat.Json, ResponseFormat = WebMessageFormat.Json)]
        Country UpdateJson(string id, Country country);

        [OperationContract]
        [WebInvoke(UriTemplate = "/countries/{id}", Method = "DELETE")]
        string DeleteXml(string Id);

        [OperationContract]
        [WebInvoke(UriTemplate = "/json/countries/{id}", Method = "DELETE", RequestFormat = WebMessageFormat.Json, ResponseFormat = WebMessageFormat.Json)]
        string DeleteJson(string Id);

        [OperationContract]
        [WebInvoke(BodyStyle = WebMessageBodyStyle.Wrapped, UriTemplate = "/json/unions", Method = "POST", RequestFormat = WebMessageFormat.Json, ResponseFormat = WebMessageFormat.Json)]
        string AddCountryUnionJson(string countryAId, string countryBId);

        [OperationContract]
        [WebGet(UriTemplate = "/json/unions/{id}", RequestFormat = WebMessageFormat.Json, ResponseFormat = WebMessageFormat.Json)]
        List<Country> GetCountryUnionsJson(string Id);

        [OperationContract]
        [WebInvoke(BodyStyle = WebMessageBodyStyle.Wrapped, UriTemplate = "/json/unions", Method = "DELETE", RequestFormat = WebMessageFormat.Json, ResponseFormat = WebMessageFormat.Json)]
        string RemoveCountryUnionJson(string countryAId, string countryBId);
    }


    [DataContract]
    public class Country
    {
        [DataMember(Order =0)]
        public int Id { get; set; }
        
        [DataMember(Order = 1)]
        public double GDP { get; set; }
        
        [DataMember(Order = 2)]
        public string Name { get; set; }
    }
}
