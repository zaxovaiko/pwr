import { Link } from "react-router-dom";

export default function Country({
  selected,
  setEditing,
  setUnion,
  deleteCountry,
  editable = false,
  Name,
  GDP,
  Id,
  id,
  deleteUnion
}) {
  
  return (
    <div
      className={`d-flex align-items-center col-12 mb-3 border-bottom p-2 justify-content-between ${
        selected ? "fw-bold" : ""
      }`}
      onClick={() => editable && setUnion(p => [...p, Id])}
    >
      <Link to={"/countries/" + Id} className={`text-decoration-none  ${selected ? 'link-danger' : 'link-dark'}`}>
        <p className="mb-0">
          {Name}, GDP: <b>{GDP}</b>
        </p>{" "}
      </Link>
      <div>
        {editable && (
          <span
            className="btn btn-success me-2"
            onClick={() =>
              setEditing({ editing: true, country: { Name, GDP, Id } })
            }
          >
            Update
          </span>
        )}
        <span className="btn btn-danger" onClick={() => editable ? deleteCountry(Id) : deleteUnion(id, Id)}>
          Delete
        </span>
      </div>
    </div>
  );
}
