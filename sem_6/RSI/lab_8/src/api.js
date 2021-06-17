const headers = {
  Accept: "application/json",
  "Content-Type": "application/json",
};

export function addCountry(country) {
  return fetch(process.env.REACT_APP_SERVER_URL + "/countries", {
    method: "POST",
    headers,
    body: JSON.stringify(country),
  }).then((res) => res.json());
}

export function getCountries() {
  return fetch(process.env.REACT_APP_SERVER_URL + "/countries", {
    headers,
  }).then((res) => res.json());
}

export function getCountry(id) {
  return fetch(process.env.REACT_APP_SERVER_URL + "/countries/" + id, {
    headers,
  }).then((res) => res.json());
}

export function getUnions(id) {
  return fetch(process.env.REACT_APP_SERVER_URL + "/unions/" + id, {
    headers,
  }).then((res) => res.json());
}

export function addUnion(countryAId, countryBId) {
  return fetch(process.env.REACT_APP_SERVER_URL + "/unions", {
    method: "POST",
    headers,
    body: JSON.stringify({
      countryAId,
      countryBId,
    }),
  }).then((res) => res.json());
}

export function deleteUnion(countryAId, countryBId) {
  return fetch(process.env.REACT_APP_SERVER_URL + "/unions", {
    method: "DELETE",
    headers,
    body: JSON.stringify({
      countryAId,
      countryBId,
    }),
  }).then((res) => res.json());
}

export function deleteCountry(id) {
  return fetch(process.env.REACT_APP_SERVER_URL + "/countries/" + id, {
    method: "DELETE",
  }).then((res) => res.json());
}

export function updateCountry(id, country) {
  return fetch(process.env.REACT_APP_SERVER_URL + "/countries/" + id, {
    method: "PUT",
    headers,
    body: JSON.stringify(country),
  }).then((res) => res.json());
}
