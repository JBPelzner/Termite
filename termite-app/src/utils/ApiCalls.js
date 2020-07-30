// all api fetch calls live here, import them into particular components as needed

//use while running apis from server
const hostname = 'http://ec2-18-224-6-72.us-east-2.compute.amazonaws.com';

//use while testing on local server apis
//const hostname = 'http://localhost';


//function calls 

// this one will be attached to an event listener, when a tab 
// is activated

export function postOriginAddress(origin_url, userID) {
  return (
    fetch(hostname + ':3005/scraper/', {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({url: origin_url, user_id: userID})
    })
   //.then(res => res.json())
  );
};

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


export function getUserAgreementsFrontend(userID) {
  return (
    fetch(hostname + ':3005/user/user_agreements_frontend?id=' + userID, {
      method: "GET",
      headers: {"Content-Type": "application/json"}
    })
    .then(res => res.json())
  );
};






