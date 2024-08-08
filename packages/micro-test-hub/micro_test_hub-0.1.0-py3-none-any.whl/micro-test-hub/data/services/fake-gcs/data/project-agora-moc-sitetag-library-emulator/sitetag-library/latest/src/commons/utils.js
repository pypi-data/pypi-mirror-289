// function getBrowser() {
//     if ((navigator.userAgent.indexOf("Opera") || navigator.userAgent.indexOf("OPR")) != -1) {
//         return "Opera";
//     } else if (navigator.userAgent.indexOf("Chrome") != -1) {
//         return "Chrome";
//     } else if (navigator.userAgent.indexOf("Safari") != -1) {
//         return "Safari";
//     } else if (navigator.userAgent.indexOf("Firefox") != -1) {
//         return "Firefox";
//     } else if (navigator.userAgent.indexOf("MSIE") != -1 || !!document.documentMode) {
//         return "IE";
//     } else {
//         return "Unknown";
//     }
// }

// function loadScript(d, url, s, id, callback, cross) {
//     var js, fjs = d.getElementsByTagName(s)[0];
//     if (d.getElementById(id)) return;
//     js = d.createElement(s);
//     js.id = id;
//     js.async = true;
//     js.type = 'text/javascript';

//     if (cross)
//         js.crossOrigin = "anonymous"

//     js.src = url;

//     if (js.readyState) {
//         js.onreadystatechange = function () {

//             if (js.readyState == "loaded" || js.readyState == "complete") {
//                 js.onreadystatechange = null;
//                 callback();
//             }
//         };
//     } else {

//         js.onload = function () {
//             callback();
//         };
//     }

//     fjs.parentNode.insertBefore(js, fjs);
// }

export function callScript(text) {
  var tagString = decodeURIComponent(text);
  try{
      var dom = new DOMParser().parseFromString(tagString, "text/html");
      var incomingScript = dom.getElementsByTagName("script")[0];
      var incomingAttributes = incomingScript.attributes;
      var head = document.getElementsByTagName("head")[0];
      var script = document.createElement("script");
      for (const attr of incomingAttributes) {
          script.setAttribute(attr["name"], attr["value"]);
      }
      head.appendChild(script);
  } catch (error){
      console.error(`Could not serve tag: ${tagString}`);
      console.error(error);
  }
}

export function callScripts(text) {
    const incomingScripts = getScripts(text)
    const scripts = createDomScriptsFromTextNodes(incomingScripts)
    scripts.map(appendIntoHead)
}

function getScripts(text) {
    const dom = new DOMParser().parseFromString(text, "text/html");
    return dom.getElementsByTagName("script");
  }
  
  function createDomScriptsFromTextNodes(TextNodes){
    let scriptNodes = []
    for (const incomingScript of TextNodes) {
      var script = document.createElement("script");
      for (const attr of incomingScript.attributes) {
        script.setAttribute(attr["name"], attr["value"]);
      }
      if (incomingScript.text) {
        script.text = incomingScript.text;
      }
      scriptNodes.push(script)
    }
    return scriptNodes
  }
  
  function appendIntoHead(script) {
    var head = document.getElementsByTagName("head")[0];
    head.appendChild(script);
  }
