async function translateText(){
    alert("entered function")
    try{
        const translatedText = await axios.post("http://127.0.0.1:5000/translate", {src_lang_data:"placeholder for html data"}).then(
            (res)=>{alert(
                res.data["src_lang_data"]);}
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