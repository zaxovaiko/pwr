import { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import { getCountry, getUnions, deleteUnion as deleteUnionApi } from "../api";
import Country from "../components/Country";

export default function CountryPage({ match }) {
  const [country, setCountry] = useState({});
  const [unions, setUnions] = useState([]);

  useEffect(() => {
    getCountry(match.params.id)
      .then((data) => {
        setCountry(data);
        getUnions(match.params.id)
          .then((res) => setUnions(res))
          .catch((err) => console.log(err));
      })
      .catch((err) => console.log(err));
  }, [match.params.id]);

  function deleteUnion(idA, idB) {
    deleteUnionApi(idA, idB).then(res => {
      setUnions(p => p.filter(e => e.Id !== idB))
    }).catch((err) => {console.log(err)})
  }

  return (
    <>
      <h6>Country</h6>
      {!country.Id && <p>Country does not exist</p>}
      {country.Id && (
        <div>
          <h3>
            {country.Name} has <b>{country.GDP} trln</b> GDP
          </h3>
        </div>
      )}

      {unions.length === 0 && <p>Country does not have any union</p>}
      <div className="row">
        {unions.map((union) => (
          <Country key={union.Id} {...union} id={match.params.id} deleteUnion={deleteUnion}/>
        ))}
      </div>

      <Link to="/">
        <span className="btn btn-danger">Cancel</span>
      </Link>
    </>
  );
}
