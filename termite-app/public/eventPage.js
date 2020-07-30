import {postOriginAddress} from '../src/utils/ApiCalls.js';

//get userid

function getRandomToken() {
    // E.g. 8 * 32 = 256 bits token
    var randomPool = new Uint8Array(32);
    crypto.getRandomValues(randomPool);
    var hex = '';
    for (var i = 0; i < randomPool.length; ++i) {
        hex += randomPool[i].toString(16);
    }
    // E.g. db18458e2782b2b77e36769c569e263a53885a9944dd0a861e5064eac16f1a
    return hex;
}


chrome.runtime.onInstalled.addListener(function () {
  chrome.tabs.query({'currentWindow': true, 'lastFocusedWindow': true}, function (tabs) {
    for (i = 0; i < tabs.length; i++) {
      console.log(tabs[i].id);
      chrome.tabs.reload(tabs[i].id);
    }
  });
});



// chrome.runtime.onMessage.addListener( function(request, sender, sendResponse) {
//   console.log(request);
// });   

chrome.tabs.onActivated.addListener(function (info) {
  console.log('FROM BACKGROUND PAGE');
  // console.log('INFO:', info);


  
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {

    try {
      chrome.tabs.sendMessage(tabs[0].id, {greeting: "hello"}, function(response) {
        console.log(response);

        chrome.storage.sync.get('userid', function(items) {
            var userid = items.userid;
            if (userid) {
                useToken(userid);
            } else {
                userid = getRandomToken();
                chrome.storage.sync.set({userid: userid}, function() {
                    useToken(userid);
                });
            }
            function useToken(userid) {
                postOriginAddress(response.origin, userid);
            }
        });


        

        setTimeout(function() { 
          chrome.storage.sync.get(null, function(entries) {
            console.log('UPDATED LIST OF ALL ENTRIES INCLUDING THIS SITE:', entries);

            console.log('WE WANT TO SEE IF THE VISIT COUNT GOT SAVED TO CHROME STORAGE');
            console.log(entries[response.host]['visit_count']);
          });
        }, 200);



        chrome.storage.sync.get(null, function(entries) {

          if (Object.keys(entries).includes(response.host)) {

            var host_url = response.host;
            var updated_entry = entries;  
            console.log(updated_entry[host_url]['visit_count']);
  
            var new_visit_count = Number(updated_entry[host_url]['visit_count'] + 1);
            updated_entry[host_url]['visit_count'] = new_visit_count;
  
            var last_site_update = response.href;
            updated_entry[host_url]['last_site'] = last_site_update;
          

            console.log(updated_entry[host_url]['visit_count']);


            chrome.storage.sync.set(updated_entry);

          }
        });
      });
    }
    catch (e) {
      console.log('NOT A VALID URL', e.message);
    }
  }); 




  // runtime.Port.chrome.tabs.connect(integer tabId, object connectInfo)


 


  // var tab_id = info.tabId;

  // chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {

  //   var tab_id = tabs[0].id;
  //   console.log('NEW ACTIVE TAB ID:', tab_id); 
  //   // console.log('URL VARIABLE TYPE:', typeof tab_id); 

  //   var tab_url = tabs[0].url;
  //   console.log('NEW ACTIVE TAB AT THIS URL:', tab_url); 
  //   // console.log('URL VARIABLE TYPE:', typeof tab_url);

    
  //   chrome.tabs.sendMessage(tab_id, {greeting: "hello"}, function(response) {
  //     console.log(response.farewell);


  //   });


    
});





// });









// chrome.runtime.onMessage.addListener(function(request, sender, sendResponse) {
//   console.log(request);

//   if (request.todo == 'checkTabActivation') {
//     chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {

//       var tab_id = tabs[0].id;
//       console.log('NEW ACTIVE TAB AT THIS URL:', tab_id); 
//       console.log('URL VARIABLE TYPE:', typeof tab_id); 
        
  
//       var tab_url = tabs[0].url;
//       console.log('NEW ACTIVE TAB AT THIS URL:', tab_url); 
//       console.log('URL VARIABLE TYPE:', typeof tab_url);
  
//       sendResponse({tab_url: tab_url});

//     });

//   }

// });


// chrome.tabs.query({active: true, currentWindow: true},function(tabs) {
//   chrome.tabs.sendMessage(tabs[0].id, {greeting: "hello"}, function(response) {
//       // console.log(response);
//       return true;
//   });
// }); 






//   chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
//     chrome.tabs.sendMessage(tabs[0].id, {greeting: "hello"}, function(response) {
//       console.log(response.farewell);
//     });
//   });

  

  // if (message.todo == 'checkTabActivation') {

  //     chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {

  //       var tab_id = tabs[0].id;
  //       console.log('NEW ACTIVE TAB AT THIS URL:', tab_id); 
  //       console.log('URL VARIABLE TYPE:', typeof tab_id); 
          

  //       var tab_url = tabs[0].url;
  //       console.log('NEW ACTIVE TAB AT THIS URL:', tab_url); 
  //       console.log('URL VARIABLE TYPE:', typeof tab_url);

  //       sendResponse({tab_url: tab_url});
  //       // }
  //     });

  // });
// });



  // chrome.runtime.onMessage.addListener(function(message, callback) {
  //   if (message == 'hello') {
  //     sendResponse({greeting: 'welcome!'})
  //   } else if (message == 'goodbye') {
  //     chrome.runtime.Port.disconnect();
  //   }
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


// chrome.tabs.onActivated.addListener(function(info) {
//     var tab = chrome.tabs.get(info.tabId, function(tab) {
//         localStorage["current_url"] = tab.url;
//     });
// });



// console.log('THIS IS WORKING FROM THE EVENT PAGE');

// console.log('CURRENT ORIGIN: ', origin);

// chrome.storage.sync.set({'page_origin': origin}, function() {
//           // Notify that we saved.
//           // message('Settings saved');
//           console.log('ORIGIN SAVED IN CHROME STORAGE');
//       });

          // chrome.storage.sync.get('page_origin', function(obj){
          //   console.log('CHROME STORAGE VALUE FOR CURRENT ORIGIN:', obj.page_origin);
          //   $('#current-origin').text(obj.page_origin);  


// console.log(location.reload(true));
