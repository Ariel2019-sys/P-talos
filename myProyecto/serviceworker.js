var CACHE_NAME = 'my-site-cache-v1';
var urlsToCache = [
  '/',
  
  

];

self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function (cache) {
        console.log('Opened cache');
        return cache.addAll(urlsToCache);
      })
  );
});



self.addEventListener('fetch',function(event){
  event.respondWith(
    
    fetch(event.request)
    .then((result)=>{
      return caches.open(CACHE_NAME)
      .then(function(c){
        c.put(event.request.url,result.clone())
        return result;
      })
    })
    .catch(function(e){
      return caches.match(event.request)
    })
  );
});







importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-app.js');
importScripts('https://www.gstatic.com/firebasejs/3.9.0/firebase-messaging.js');



  var firebaseConfig = {
    apiKey: "AIzaSyDHnY2BhpRreLmRfeE_jUnIgeG0rMgWPxk",
    authDomain: "petalos-1bd0d.firebaseapp.com",
    databaseURL: "https://petalos-1bd0d.firebaseio.com",
    projectId: "petalos-1bd0d",
    storageBucket: "petalos-1bd0d.appspot.com",
    messagingSenderId: "944101874954",
    appId: "1:944101874954:web:f257bb72239c251b8faef3"
  };

  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);

  let messaging = firebase.messaging();


  messaging.setBackgroundMessageHandler(function (payload) {
    console.log("ha llegado notificacion");
    let title = payload.notification.title;

    let options = {
      body: payload.notification.body,
      icon: payload.notification.icon
    }
    self.registration.showNotification(title, options);
  })

