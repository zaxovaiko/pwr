import { useState, useEffect } from "react";
import AddForm from "./components/AddForm";
import { getCountries } from "./api";

export const defaultEditing = {
  editing: false,
  country: {},
};

function App() {
  const [countries, setCountries] = useState([]);
  const [editing, setEditing] = useState(defaultEditing);

  useEffect(() => {
    getCountries()
      .then((res) => setCountries(res))
      .catch((err) => console.log(err));
  }, []);

  function deleteCountry(id) {
    deleteCountry()
      .then(() => setCountries((p) => p.filter((e) => e.Id !== id)))
      .catch((err) => console.log(err));
  }

  return (
    <div className="container py-5">
      <AddForm edit={editing}  setEditing={setEditing} setCountries={setCountries} />

      {countries.length === 0 && <p>There is no any country yet</p>}
      {countries.length > 0 && (
        <div className="row">
          <h4>Countries:</h4>
          {countries.map((country) => (
            <div
              className="d-flex align-items-center col-12 mb-3 border-bottom p-2 justify-content-between"
              key={country.Name}
            >
              <p className="mb-0">
                {country.Name}, GDP: <b>{country.GDP}</b>
              </p>{" "}
              <div>
                <span
                  className="btn btn-success me-2"
                  onClick={() => setEditing({ editing: true, country })}
                >
                  Update
                </span>
                <span
                  className="btn btn-danger"
                  onClick={() => deleteCountry(country.Id)}
                >
                  Delete
                </span>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

export default App;
