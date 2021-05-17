export function addCountry(country) {
  return fetch(process.env.REACT_APP_SERVER_URL + "/countries", {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify(country),
  }).then((res) => res.json());
}

export function getCountries() {
  return fetch(process.env.REACT_APP_SERVER_URL + "/countries", {
    headers: {
      Accept: "application/json",
    },
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
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    body: JSON.stringify(country),
  }).then((res) => res.json());
}