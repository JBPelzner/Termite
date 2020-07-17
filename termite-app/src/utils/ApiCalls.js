// all api fetch calls live here, import them into particular components as needed

//use while running apis from server
//const hostname = 'http://ec2-18-188-128-88.us-east-2.compute.amazonaws.com';

//use while testing on local server apis
const hostname = 'http://localhost';

export function getModelData(webAddr) {
  return (
    fetch(hostname + ':3005/data/model?website_address=' + webAddr, {
      method: "GET",
      headers: {"Content-Type": "application/json"}
    })
    .then(res => res.json())
  );
};

export function getUserPreferences(userID) {
  return (
    fetch(hostname + ':3005/user/preferences?id=' + userID, {
      method: "GET",
      headers: {"Content-Type": "application/json"}
    })
    .then(res => res.json())
  );
};

export function postUserPreferences(userID, t1, t2, t3, t4, t5, t6) {
  fetch(hostname + ':3005/user/preferences', {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      id : userID,
      t1 : t1,
      t2 : t2,
      t3 : t3,
      t4 : t4,
      t5 : t5,
      t6 : t6
    })
  });
};

export function getUserAgreements(userID) {
  return (
    fetch(hostname + ':3005/user/agreements?id=' + userID, {
      method: "GET",
      headers: {"Content-Type": "application/json"}
    })
    .then(res => res.json())
  );
};

export function postUserAgreement(userID, webAddr) {
  fetch(hostname + ':3005/user/agreements', {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({
      user_id : userID,
      website_address : webAddr
    })
  });
};