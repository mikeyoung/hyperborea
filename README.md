# Spells of Hyperborea

## Introduction
Spells of Hyperborea is a tool for browsing an index of the hundreds of spells in the role playing game Hyperborea.  The app is designed to be a part of a set of upcoming apps that will aid play in various ways such as character management, in-game weather conditions, etc.  While the end user experience has been crafted to be simple, the back end employs a significant amount of logic to produce expected behavior.

## Distinctiveness and Complexity
All code written for the application is distinct from all previous projects I submitted for CS50W.  

## Application Design
A goal of this project was to balance the strengths of server rendering and client responsiveness.  The rules in Hyperborea are based on the original Dungeons & Dragons system which features multiple spells that are available to multiple character classes at differing levels.  For this reason there is a database table for spells, a table for classes and a junction table for referencing all the combinations of spells, level access and character classes.  Python and Django excel at processing queries from the database so I chose to handle all the filtering logic on the server side.  I opted to make the client fetch filtered lists and individual spell descriptions from the server in order to minimize space complexity on the client.

The spell lists, in all views, list each instance of the spell for each class.  This is intentional so that the results can be filtered and observed to see which classes have access to each spell at various levels.  The title of each page dynamically reflects the applied filters.

While navigating the site users can select spells to include in their "spellbook".  Spellbook in this context essentially means a favorites list.  I am going to be hosting this app on the internet so I chose to have the spellbook data be stored locally so that the server doesn't have the performance/storage overhead and security risks of public user accounts.  The spellbook data is populated into a hidden field in the main spell form prior to requests to fetch spell lists.

When a user changes the selected filters in the top dropdowns, or adds/removes a spell from the spellbook, the front end makes a REST call to the back end and submits the scope, character class and level desired.  The back end then creates a set of filters to apply to the query based on that criteria.  I initially went with using a series of Q objects and that may have been more efficient but I was not able to get it working so I used a list of rules that I passed into the objects filter call.  I am not sure but this may introduce problems at scale if it is loading the entire data set and then filtering afterwards.  I intend to look into that after adding the remaining spells to the database.

I also created an endpoint that is only accessible to the logged in admin user which will generate json file dumps of the three tables, so that in the future a pure client side app can run off static data.  None of these files are utilized in the current form of the app but the files are included in the static folder.  This endpoint can be accessed at 'create-json'.

I decided to use a font and color scheme that is reminiscent of the pulp sources for the Hyperborea setting.  There is noticeable font-replacement because the font is loaded in a non-blocking manner so that the page content can render quickly for all users.

Another goal of the project was to not employ any javascript frameworks or libraries.  This did require some manual updating of the dom in cases where a library could have provided binding, but I favored delivering a smaller codebase and redicing dependencies.  If the application's UI were to get significantly more complex I would likely look into converting some of the functionality to use VueJS.

Right now the project is limited to Levels 1-3 and spells A-D.  I am continuing to add data to the app.  Many spells require lists and tables and I did not want to delay the demonstration of the app for the data entry of such a large data set.

While using the app with developer tools open one can observe the network activity as the user modifies the specifications for the spell list and spell details.  Since this is all done with ajax endpoints, there is no disruption from a hard page reload.  All of the logic is stored in main.js in the static folder.

Future enhancements might include caching ajax responses and other response caching.  Right now the app makes fresh calls for every change and with what will ultimately be a static dataset it presents a prime opportunity for cacheing.

Bootstrap 5 was used to create a reponsive layout and for the spell detail modals.