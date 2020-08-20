var c_url = this.location.href;

var o_host = this.location.host;

var o_url = this.location.origin;


chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    // console.log(sender.tab ?
    //             "from a content script:" + sender.tab.url :
    //             "from the extension");
    if (request.greeting == "hello") {
      sendResponse({host: o_host, href: c_url, origin: o_url});
      return true;
    }

  });


// chrome.runtime.onMessage.addListener(function(request, sender, sendResponse){

//     console.log(request, sender, sendResponse);
//     sendResponse('message:', request);
//     return true;
// });


// function ping() {
//   chrome.runtime.sendMessage('ping', response => {
//     if(chrome.runtime.lastError) {
//       setTimeout(ping, 1000);
//     } else {
//       // Do whatever you want, background script is ready now
//     }
//   });
// }
// ping();




// chrome.runtime.onMessage.addListener(
//   function(request, sender, sendResponse) {

//     return true;
//     console.log(request);

//     console.log(sender.tab ?
//                 "from a content script:" + sender.tab.url :
//                 "from the extension");
//     if (request.greeting == "hello") {
//       sendResponse({farewell: "goodbye"});
//     }
    
//   });



// chrome.runtime.sendMessage({todo: 'checkTabActivation'}, function(response) {
//   console.log(response.tab_url);
// });


// chrome.runtime.onMessage.addListener(
//   function(request, sender, sendResponse) {
//     console.log(sender.tab ?
//               "from a content script:" + sender.tab.url :
//               "from the extension");

// chrome.runtime.onMessage.addListener(function(){
//   console.log('TESTING MESSAGE RECEPTION');
  


//   // if (request.this_url == c_url) {
//   //   sendResponse({confirmation: "Adding a count to the storage object for this host"});
//   // }
// });


setTimeout(function() { 
  // the `null` argument allows us to call all items in storage
  chrome.storage.sync.get(null, function(entries) {
    console.log('UPDATED LIST OF ALL ENTRIES INCLUDING THIS SITE:', entries);

    console.log('WE WANT TO SEE IF THE VISIT COUNT GOT SAVED TO CHROME STORAGE');
    console.log(entries[this.location.host]['visit_count']);
  });
}, 200);





chrome.storage.sync.get(null, function (obj) {

  var host_keys = Object.keys(obj);


  if (host_keys.length == 0) {
    console.log('------FIRST ENTRY TO CHROME STORAGE------');
  }


  if (host_keys.includes(this.location.host) != 1) {

    console.log('------NEW ORIGIN------');

    var new_site_object = {};      

    var host_name = this.location.host;
    var URLorigin = this.location.origin;
    var d = new Date();
    var time_logged = d.toString();

    new_site_object[host_name] = {};      
    new_site_object[host_name]['origin'] = URLorigin;
    new_site_object[host_name]['date'] = time_logged;
    new_site_object[host_name]['first_site'] = this.location.href;
    new_site_object[host_name]['last_site'] = this.location.href;
    new_site_object[host_name]['visit_count'] = 1;
    

    console.log('------ENTRY FOR THIS HOST:------', new_site_object);

    chrome.storage.sync.set(new_site_object);
  }

  else {
    console.log('------WE RETRIEVED THE SAME ORIGIN------');
    console.log('STORAGE OBJECT FOR THIS HOST:', obj[this.location.host]);

    console.log('OBJ:', obj);
    console.log('OBJ AT THIS HOST ENTRY:', obj[this.location.host]);
    console.log('OBJ AT THE HOST ENTRY VISIT COUNT:', obj[this.location.host]['visit_count']);

    // var xyz = obj[this.location.host]['visit_count'];
    // xyz ++;
    // console.log('VISIT COUNT AFTER ITERATION:', xyz);

    // var new_visit_count = Number(obj[this.location.host]['visit_count'] + 1);
    // console.log('VISIT COUNT AFTER ITERATION:', new_visit_count);

    // var last_site_update = this.location.href;
    // console.log('VARIABLE VALUE AFTER POPULATION AFTER ITERATION:', last_site_update);



    // var updated_entry = obj;
    // console.log(updated_entry);

    // updated_entry[this.location.host]['visit_count'] = new_visit_count;
    // updated_entry[this.location.host]['last_site'] = last_site_update;

    // console.log(updated_entry[this.location.host]);


    // chrome.storage.sync.set(updated_entry);



  }
});

// console.log(host_name);    
// chrome.storage.sync.set(updated_entry);

  







