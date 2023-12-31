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
        document.querySelector('#spellbook-toggle-link').dataset.spell_id = spell_id;
        setSpellBookButton(spell_id)
        spell_modal.show();
    })
}

const spell_modal = new bootstrap.Modal(document.getElementById('spell_modal'), {
    keyboard: false
});

const toggle_spellbook = (spell_id) => {
    spellbook_array = localStorage.getItem('spellbook');
    if (spellbook_array) {
        spellbook_set = new Set(JSON.parse(spellbook_array));

        if (spellbook_set.has(spell_id)) {
            spellbook_set.delete(spell_id);
        } else {
            spellbook_set.add(spell_id);
        }

        spellbook_array = Array.from(spellbook_set);
        localStorage.setItem('spellbook', JSON.stringify(spellbook_array))
    } else {
        spellbook_array = [spell_id];
        localStorage.setItem('spellbook', JSON.stringify(spellbook_array));
    }

    submitSpellForm()
};

const setSpellBookButton = (spell_id) => {
    spellbook_array = localStorage.getItem('spellbook');

    if (spellbook_array) {
        spellbook_set = new Set(JSON.parse(spellbook_array));
        if (spellbook_set.has(spell_id)) {
            document.querySelector('#spellbook-toggle-link').innerHTML = 'Remove from Spellbook'
            return true;
        }
    }

    document.querySelector('#spellbook-toggle-link').innerHTML = 'Add to Spellbook';
    return true;
};

const submitSpellForm = () => {
        spellbook_json_string = localStorage.getItem('spellbook');

        if (spellbook_json_string === null) {
            spellbook_json_string = JSON.stringify([]);
        }

        document.querySelector('#spellbook_field').value = spellbook_json_string;

        document.querySelector('#spell-form').submit();
}

document.addEventListener('DOMContentLoaded', ()=>{
    document.querySelectorAll('#spell-form select').forEach((el)=>{
        el.addEventListener('change', () => {
            submitSpellForm();
        })            
    });

    document.querySelectorAll('.spell-list a').forEach((el) => {
        el.addEventListener('click', (e) => {
            get_spell_description(e.target.dataset.spell_id)
        })
    });

    document.querySelector('#spellbook-toggle-link').addEventListener('click', (e) => {
        toggle_spellbook(e.target.dataset.spell_id)
    });
});