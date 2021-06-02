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
            new Country { GDP = 23.7, Name = "Spain", Id = 2},
            new Country { GDP = 10.3, Name = "Ukraine", Id = 3},
            new Country { GDP = 120.3, Name = "USA", Id = 4},
            new Country { GDP = 101, Name = "Australia", Id = 5},
        };

        private static List<List<Country>> unions = new List<List<Country>>()
        {
            new List<Country> { countries[0], countries[1] },
            new List<Country> { countries[1], countries[2] },
            new List<Country> { countries[0], countries[3] },
            new List<Country> { countries[3], countries[2] },
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
            unions.RemoveAll(e => e.FindAll(r => r.Id == int.Parse(Id)).Count != 0);
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

        public string AddCountryUnionJson(string countryAId, string countryBId)
        {
            var countryA = countries.Find(e => e.Id == int.Parse(countryAId));
            var countryB = countries.Find(e => e.Id == int.Parse(countryBId));
            if (countryA == null || countryB == null)
            {
                throw new WebFaultException<string>("404: Not found", HttpStatusCode.NotFound);
            }
            foreach (var item in unions)
            {
                if (item.Find(e => e.Id == int.Parse(countryAId)) != null && item.Find(e => e.Id == int.Parse(countryBId)) != null)
                {
                    throw new WebFaultException<string>("409: Conflict", HttpStatusCode.Conflict);
                }
            }
            unions.Add(new List<Country>()
            {
                countryA, countryB
            });
            return "Added countries";
        }

        public List<Country> GetCountryUnionsJson(string Id)
        {
            var country = countries.Find(e => e.Id == int.Parse(Id));
            if (country == null)
            {
                throw new WebFaultException<string>("404: Not found", HttpStatusCode.NotFound);
            }
            List<Country> cs = new List<Country>();
            foreach (var item in unions)
            {
                var c = item.FindIndex(e => e.Id == int.Parse(Id));
                if (c != -1)
                {
                    cs.Add(item[c ^ 1]);
                }
            }
            return cs;
        }

        public string RemoveCountryUnionJson(string countryAId, string countryBId)
        {
            var countryA = countries.Find(e => e.Id == int.Parse(countryAId));
            var countryB = countries.Find(e => e.Id == int.Parse(countryBId));
            if (countryA == null || countryB == null)
            {
                throw new WebFaultException<string>("404: Not found", HttpStatusCode.NotFound);
            }
            for (int i = 0; i < unions.Count; i++)
            {
                if (unions.ElementAt(i).Contains(countryA) && unions.ElementAt(i).Contains(countryB))
                {
                    unions.RemoveAt(i);
                }
            }
            return "Deleted union";
        }
    }
}
