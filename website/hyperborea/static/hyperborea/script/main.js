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
        document.querySelector('#spell_modal .modal-title').innerHTML = result.spell_name;
        document.querySelector('#spell_modal .modal-body').innerHTML = result.spell_description;
        setSpellBookButton(spell_id)
        spell_modal.show();
    })
}

const spell_modal = new bootstrap.Modal(document.getElementById('spell_modal'), {
    keyboard: false
});

const toggle_spellbook = (spell_id) => {
    spellbook_set = 'spellbook' in localStorage ? localStorage.getItem('spellbook') : null;
    if (spellbook_set) {
        spellbook_set.add(spell_id);
        localStorage.setItem('spellbook', spellbook_set)
    } else {
        spellbook_set = new Set();
        spellbook_set.add(spell_id);
        localStorage.setItem('spellbook', spellbook_set)
    }

    setSpellBookButton(spell_id)
};

const setSpellBookButton = (spell_id) => {
    spell_in_spellbook = false;

    spellbook_set = 'spellbook' in localStorage ? localStorage.getItem('spellbook') : null;

    if (spellbook_set && spell_id in spellbook_set) {
        spell_in_spellbook = true;
    }

    if (spell_in_spellbook) {
        document.querySelector('#spellbook-toggle-link').innerHTML = 'Add to Spellbook'
    } else {
        document.querySelector('#spellbook-toggle-link').innerHTML = 'Remove from Spellbook'
    }
};

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