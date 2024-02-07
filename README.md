# Spells of Hyperborea

## Introduction
Spells of Hyperborea is a tool for browsing an index of the hundreds of spells in the role playing game Hyperborea.  The app is designed to be a part of a set of upcoming apps that will aid play in various ways such as character management, in-game weather conditions, etc.  While the end user experience has been crafted to be simple, the back end employs a significant amount of logic to produce expected behavior.

## Distinctiveness and Complexity
All code written for the application is distinct from previous projects I submitted for CS50W.  There is no other project in the course that functions as a means to view and organize related game system elements into a user defined collection (in this case a spellbook).  Complexities that were new to this project include the use of a junction table and performing content filtration driven by data from both the database and client local storage.  The rules in Hyperborea are based on the original Dungeons & Dragons system which features multiple spells that are available to multiple character classes at differing levels.  For this reason there is a database table for spells, a table for classes and a junction table for referencing all the combinations of spells, level access and character classes.  The UI is also a significant step up with a responsive layout and elegant modals for spell details.

## How To Run
Assuming installation of python 3.10+ and Django: Navigate to application folder with manage.py use manage.py runserver

## Application Design
Python and Django excel at easily processing queries from the database so I chose to handle all the filtering logic on the server side.  I opted to make the client fetch filtered lists and individual spell descriptions from the server in order to minimize space requirements on the client (there are close to a thousand spells in the game, some of which are several paragraphs).

A goal of this project was to balance the strengths of server rendering and client responsiveness.  The spell lists, in all views, list each instance of the spell for each class.  This is intentional so that the results can be filtered and observed to see which classes have access to each spell at various levels.  The title of each page dynamically reflects the applied filters.

While navigating the site users can select spells to include in their "spellbook".  I am going to be hosting this app on the internet so I chose to have the spellbook data be stored locally so that the server doesn't have the performance/storage overhead and security risks of public user accounts.  The spellbook data is populated into a hidden field in the main spell form prior to requests to fetch spell lists.

When a user changes the selected filters in the top dropdowns, or adds/removes a spell from the spellbook, the front end makes a REST call to the back end and submits the scope, character class and level desired.  The back end then creates a set of filters to apply to the query based on that criteria.  I initially went with using a series of Q objects and that may have been more efficient but I was not able to get it working so I used a list of rules that I passed into the objects filter call.  I am not sure but this may introduce problems at scale if it is loading the entire data set and then filtering afterwards.  I intend to look into that after adding the remaining spells to the database.

I also created an endpoint that is only accessible to the logged in admin user which will generate json file dumps of the three tables, so that in the future a pure client side app can run off static data.  None of these files are utilized in the current form of the app but the files are included in the static folder.  This endpoint can be accessed at 'create-json'.

Another goal of the project was to not employ any javascript frameworks or libraries.  This did require some manual updating of the dom in cases where a library could have provided binding, but I favored delivering a smaller codebase and redicing dependencies.  If the application's UI were to get significantly more complex I would likely look into converting some of the functionality to use VueJS.

Right now the project is limited to Levels 1-3 and spells A-D.  I am continuing to add data to the app.  Many spells require lists and tables and I did not want to delay the demonstration of the app for the data entry of such a large data set.

While using the app with developer tools open one can observe the network activity as the user modifies the specifications for the spell list and spell details.  Since this is all done with ajax endpoints, there is no disruption from a hard page reload.  All of the logic is stored in main.js in the static folder.

Future enhancements might include caching ajax responses and other response caching.  Right now the app makes fresh calls for every change and with what will ultimately be a static dataset it presents a prime opportunity for cacheing.

## Files of Note

### hyperborea/hyperborea/static/hyperborea/css/style.css
This is CSS stylesheet for the application.

### hyperborea/static/hyperborea/script/main.js
This file contains the following javascript functions:
* get_spell_description(spell_id): Fetches the description for an individual spell.

* update_spells(): Inspects the values of the three dropdown filters and submits them to the server, getting back a filtered spell list and updating the UI.

* toggle_spellbook(spell_id): Adds or Removes the current featured spell_id from the users local storage "spellbook".

* set_spell_book_button(spell_id): Sets the label for the spellbook button to indicate addition or removal from spellbook.

### hyperborea/templates/hyperborea/layout.html
The default layout file.

### hyperborea/templates/hyperborea/layout.html
The default layout file.

### hyperborea/templates/hyperborea/spells.html
The main content template which inherits from layout.html

### hyperborea/admin.py
Sets which models are available in the django admin.

### hyperborea/models.py
Contains the definitions for the following models: Spell, CharacterClass, SpellListItem

### hyperborea/views.py
This file contains the following view functions:
* spells: A fallback server side call to fetch all spells from the database.  Useful for debugging.

* get_spells: Inspects the contents of form data to form filters with which to call the database and return filtered results via AJAX

* get_spell_description: Inspects the contents of form data to then call the database and return the description of the specified spell via AJAX

* create_json: Generates JSON data dumps of the main tables.  Requires admin login.

### hyperborea/static/hyperborea/json/character_classes.json
A data dump for all classes, to be used by javascript in future functionality.

### hyperborea/static/hyperborea/json/spell_list_itemss.json
A data dump for all spell lists, to be used by javascript in future functionality.

### hyperborea/static/hyperborea/json/spells.json
A data dump for all spell, to be used by javascript in future functionality.

