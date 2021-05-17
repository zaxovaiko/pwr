using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.ServiceModel.Activation;
using System.ServiceModel.Web;
using System.Text;

namespace service
{
    // NOTE: You can use the "Rename" command on the "Refactor" menu to change the class name "Service1" in code, svc and config file together.
    // NOTE: In order to launch WCF Test Client for testing this service, please select Service1.svc or Service1.svc.cs at the Solution Explorer and start debugging.
    [ServiceBehavior(InstanceContextMode =InstanceContextMode.Single)]
    [AspNetCompatibilityRequirements(RequirementsMode = AspNetCompatibilityRequirementsMode.Allowed)]
    public class MyRestService : IRestService
    {
        private static OutgoingWebResponseContext response;
        private static List<Country> countries = new List<Country>()
        {
            new Country { GDP = 12.2, Name = "Poland", Id = 1},
            new Country { GDP = 23.2, Name = "Spain", Id = 2},
            new Country { GDP = 10.3, Name = "Ukraine", Id = 3},
        };

        public string AddXml(Country country)
        {
            if (country == null)
            {
                throw new WebFaultException<string>("400: BadRequest", HttpStatusCode.BadRequest);
            }
            country.Id = countries.Count() + 1;
            int idx = countries.FindIndex(b => b.Id == country.Id);
            if (idx == -1)
            {
                countries.Add(country);
                response = WebOperationContext.Current.OutgoingResponse;
                response.StatusCode = HttpStatusCode.Created;
                return country.Id.ToString();
            }
            throw new WebFaultException<string>("409: Conflict", HttpStatusCode.Conflict);
        }

        public Country UpdateXml(string id, Country country)
        {
            if (country == null)
            {
                throw new WebFaultException<string>("400: BadRequest", HttpStatusCode.BadRequest);
            }
            int idx = countries.FindIndex(b => b.Id == Int32.Parse(id));
            if (idx == -1)
            {
                throw new WebFaultException<string>("404: Not Found", HttpStatusCode.NotFound);
            }
            countries[idx].Name = country.Name;
            countries[idx].GDP = country.GDP;
            return countries[idx];
        }

        public Country UpdateJson(string id, Country country)
        {
            return UpdateXml(id, country);
        }

        public string DeleteXml(string Id)
        {
            var country = countries.Find(e => e.Id == int.Parse(Id));
            if (country == null)
            {
                throw new WebFaultException<string>("404: Not found", HttpStatusCode.NotFound);
            }
            countries.Remove(country);
            return "Removed country = " + country.Name;
        }

        public List<Country> GetAllXml()
        {
            return countries;
        }

        public Country GetByIdXml(string Id)
        {
            var country = countries.Find(e => e.Id == int.Parse(Id));
            if (country == null)
            {
                throw new WebFaultException<string>("404: Not found", HttpStatusCode.NotFound);
            }
            return country;
        }

        public string AddJson(Country country)
        {
            return AddXml(country);
        }

        public string DeleteJson(string Id)
        {
            return DeleteXml(Id);
        }

        public List<Country> GetAllJson()
        {
            return GetAllXml();
        }

        public Country GetByIdJson(string Id)
        {
            return GetByIdXml(Id);
        }
    }
}
