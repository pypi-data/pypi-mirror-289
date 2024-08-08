function serveHandler(text){
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

function serve_pa_headertag(text){

    if (document.readyState === "interactive" || document.readyState === "complete"){
        serveHandler(text)
    }else{
        document.addEventListener("DOMContentLoaded", function(){
            serveHandler(text)
            
        });
    }
}

export function run(text, eventTrackerEndpoint=null, eventTrackerLibraryUrl=null, siteId=null){
    serve_pa_headertag(text);
}