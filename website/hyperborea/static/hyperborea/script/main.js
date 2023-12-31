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
        set_spell_book_button(spell_id)
        spell_modal.show();
    })
}

const update_spells = () => {
    let spellbook_json_string = localStorage.getItem('spellbook');

    if (spellbook_json_string === null) {
        spellbook_json_string = JSON.stringify([]);
    }

    document.querySelector('#spellbook_field').value = spellbook_json_string;

    const scope = document.querySelector('#scope').value;
    const level = document.querySelector('#level').value;
    const character_class = document.querySelector('#class').value;
        
    let cookie = document.cookie;
    let csrfToken = cookie.substring(cookie.indexOf('=') + 1);

    fetch('/get-spells', {
        method: 'POST',
        body: JSON.stringify({
            scope,
            level,
            character_class,
            spellbook_json_string
        }),
        headers: {
            'X-CSRFToken': csrfToken
        }
    })
    .then(response => response.json())
    .then(result => {
        document.querySelector('#page-title').innerHTML = result.page_title;

        document.querySelector('#spell-list').innerHTML='';

        if (result.spell_list.length == 0) {
            document.querySelector('#feedback').innerHTML = '<p class="text-center">No spells match selected specifications.</p>';
        } else {
            document.querySelector('#feedback').innerHTML = '';
        }

        
        for (spell of result.spell_list) {
            let spell_item_html = null;
            let selected_class = document.querySelector('#class').value;
            let selected_level = document.querySelector('#level').value;
            
            if (selected_class == 'all' && selected_level == 'all') {
                spell_item_html = `${ spell.name }<br>(${spell.character_class} Level ${spell.level})`;
            }

            if (selected_class == 'all' && selected_level != 'all') {
                spell_item_html = `${ spell.name }<br>(${spell.character_class})`;
            }

            if (selected_class != 'all' && selected_level == 'all') {
                spell_item_html = `${ spell.name }<br>(Level ${spell.level})`;
            }

            if (selected_class != 'all' && selected_level != 'all') {
                spell_item_html = `${ spell.name }`;
            }

            let spell_list_item = document.createElement('li');

            let spell_link = document.createElement('a');
            spell_link.dataset.spell_id = spell.spell_id;
            spell_link.setAttribute('href','javascript:void(0)');
            spell_link.innerHTML = spell_item_html;
            spell_link.addEventListener('click', (e) => {
                get_spell_description(e.target.dataset.spell_id)
            })

            spell_list_item.appendChild(spell_link);
            document.querySelector('#spell-list').appendChild(spell_list_item);
        }
    })

    return true;
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

    set_spell_book_button(spell_id)
    submit_spell_form()
};

const set_spell_book_button = (spell_id) => {
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

const submit_spell_form = () => {
        update_spells();
}

document.addEventListener('DOMContentLoaded', ()=>{
    document.querySelectorAll('#spell-form select').forEach((el)=>{
        el.addEventListener('change', () => {
            submit_spell_form();
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

    update_spells();
});