const get_spell_description = (spell_id) => {
    let cookie = document.cookie;
    let csrfToken = cookie.substring(cookie.indexOf('=') + 1);

    fetch('/get-spell-description', {
        method: 'POST',
        body: JSON.stringify({
            spell_id: spell_id
        }),
        headers: {
            'X-CSRFToken': csrfToken
        }
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        console.log(result);
    })
}

document.addEventListener('DOMContentLoaded', ()=>{
    document.querySelectorAll('#spell-form select').forEach((el)=>{
        el.addEventListener('change', ()=>{
            document.querySelector('#spell-form').submit();
        })            
    });

    document.querySelectorAll('.spell-list a').forEach((el) => {
        el.addEventListener('click', (el) => {
            get_spell_description(el.target.dataset.spell_id)
        })
    });
});