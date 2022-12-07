async function translateText(){
    alert("entered function")
    try{
        chrome.tabs.query({active: true, lastFocusedWindow: true}).then(
            async tabs => {
                let url = tabs[0].url
                const translatedText = await axios.post("http://127.0.0.1:5000/translate", {src_url:url}).then(
                (res)=>{alert(
                    res.data["src_lang_data"]);}
        )
            }
        )
    }
    catch(e){
        alert(e)
    }
  
}
alert("entered script")
translateText()

// TODO: 
//  1. Post HTML data to backend
//  2. Receive translated text
//  3. Display translated HTML page