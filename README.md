# Odoo Development Module
## Author: Adalberto Vazquez

This module contains information about the contacts list (clients and suppliers) and create new views of the res.partner module:
* List view with genre
* Form view with the genre
* Pivot table to show the name (rows) and genre (cols) of each contact

### Models

This module contains one single model named "models_genre.py" inside the models folder. In this file we inherit the 'res.partner' model and create a new field named "genre_field".


### Views

The available views in this module are the following:
* **menu_view.xml**: This view contains information about the views to include in the menu and we create the menu item.
* **tree_view.xml**: In this view we inherit the tree view from 'res.partner' (inherited xml) adding the field 'genre' to the list.
* **form_view.xml**: This form view is inherited from the 'res.partner' including the new "genre_field" declared in the "models_genre.py" file.
* **pivot_view.xml**: The pivot view is a pivot table containing information about each contact, using the name as row and the genre as column.
* **add_module_to_menu.xml**: This view help us to make this module visible in the menu as "Reports", giving access to the group "base.group_system".

### Static

This folder contains the "logo.png" file for this module, is a cup of coffee (because I love coffee) and a green background because it's my favourite color.

### Extras

The main folder contains a "SQL_statement.sql" file that you could run directly in the SQL of odoo database using the Postgres syntax to alter the default value of each field in the 'res.partner' table.

I couldn't add the button to change genre (once I added the "genre_field" in the 'res.partner' model the form view never changed again), so I deleted the view to keep in this repository only the files that we can use.

### Images of this module

![Logo](/images/module_logo.PNG)

![Reports_menu](/images/reports_menu.png)

![Tree_view](/images/tree_view.PNG)

![Form_view1](/images/form_view1.PNG)

![Form_view2](/images/form_view2.PNG)

![Pivot_view](/images/pivot_view.PNG)
