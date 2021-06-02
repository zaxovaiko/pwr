import { useState, useEffect } from "react";
import { addCountry as addCountryApi, updateCountry } from "../api";
import { defaultEditing } from "../pages/Home";

const defaultCountry = {
  Name: "",
  GDP: 0,
  id: "",
};

export default function AddForm({ edit, setCountries, setEditing }) {
  const [country, setCountry] = useState(defaultCountry);

  useEffect(() => {
    if (edit.editing) {
      setCountry(edit.country);
    }
  }, [edit]);

  function addCountry() {
    addCountryApi(country)
      .then((res) => {
        setCountries((p) => [...p, { ...country, Id: res }]);
        setCountry(defaultCountry);
      })
      .catch((err) => console.log(err));
  }

  function editCountry() {
    updateCountry(country.Id, country)
      .then(() => {
        // TODO: Add validation
        setCountries((p) => p.map(e => e.Id === country.Id ? country : e));
        setCountry(defaultCountry);
      })
      .catch((err) => console.log(err));
  }

  return (
    <div className="row mb-5">
      <div className="col-12">
        <h4>{edit.editing ? "Edit country" : "Add new country"}</h4>
        <div className="mt-3 input-group">
          <input
            value={country.Name}
            onChange={(e) =>
              setCountry((p) => ({ ...p, Name: e.target.value }))
            }
            type="text"
            required={true}
            className="form-control"
          />
          <input
            value={country.GDP}
            onChange={(e) =>
              setCountry((p) => ({ ...p, GDP: parseInt(e.target.value) }))
            }
            type="number"
            required={true}
            className="form-control"
          />
          <button
            onClick={() => (edit.editing ? editCountry() : addCountry())}
            className="btn btn-outline-success"
            type="button"
          >
            {edit.editing ? "Save" : "Add"}
          </button>
          {edit.editing && (
            <button
              onClick={() => {
                setEditing(defaultEditing);
                setCountry(defaultCountry);
              }}
              className="btn btn-outline-danger"
              type="button"
            >
              Cancel
            </button>
          )}
        </div>
      </div>
    </div>
  );
}
