document.addEventListener("DOMContentLoaded", ()=>{
    document.querySelectorAll("#spell-form select").forEach((el)=>{
        el.addEventListener("change", ()=>{
            document.querySelector("#spell-form").submit();
        })            
    });
});