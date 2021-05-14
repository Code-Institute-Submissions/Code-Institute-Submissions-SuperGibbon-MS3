Please note this page is not sponsered or affilated with John Lewis in any way, this is just a personal project

# Cook Book - A place to find and share recipes

This project is designed to be place where users can come to find recipes or share recipes that they want the world to see. The project is linked with selling kitchen utensils and by including a link on the recipe page where utensils are shared it helps with brand recognition and potential sales. (in this case the brand is John Lewis, there is no official allifiation with the company)

## UX

It has been design to be simple and nice on the eyes and easy to use, the pages use a white and green colour scheme throughout and easy navigation using a navbar on the top of the page (sidebar for smaller devices)

## Wireframes

Wireframes were designed using Miro, they can be found here
[Wireframes](https://miro.com/app/board/o9J_lELdMyA=/)

## User Stories

1. As a user I want to be able to find recipes to cook, preferably with a search function to find a recipe name

2. As a user I want to be able to add a recipe to the website

3. As a user I want to be able to edit or delete recipes that I have added

4. As a user I want to be able to use the website on multiple devices of verying sizes

5. As a site owner I want to be able to promote a brand using links to specific sponsers

## Existing Features

- Recipe list that anyone can view whether signed in or not
- Register/Login/Logout functionality
- CRUD functionality for users that are logged in
- Simple UI design, easy to read, not distracting from purpose

## Future Features

- Further search functionality, currently only available via recipe name
- Tags to recipes so groups of recipes can be formed
- Nutritional information such as calories and allergins

## Tech Used

- [Materialize](https://materializecss.com/)
- **Materialize** is used to give the pages a uniform layout using the grid feature, Components are used to add additional features such as modal and collapsibles.

- [JQuery](https://jquery.com)
- The project uses **JQuery** as part of Materialize components

- [GoogleFonts](https://fonts.google.com/)
- The project uses **GoogleFonts** to provide the fonts used on the pages

## User Story Testing

1. As a user I want to be able to find recipes to cook, preferably with a search function to find a recipe name
    1. The recipes page is clear with a search function at the top to make finding recipes easy

    ![Recipe Page](assets/images/readme-images/recipes-search.jpg)

2. As a user I want to be able to add a recipe to the website
    1. Using the add recipe page, any user that is registered and logged in can easily add a recipe using the form

    ![Add recipe](assets/images/readme-images/add-recipe.jpg)

3. As a user I want to be able to edit or delete recipes that I have added
    1. All recipes added by a user will have an edit and delete button by their titles for simple editing or deleting by that user only

    ![Edit and delete recipe](assets/images/readme-images/editanddelete.jpg)

    2. When not logged or a different user views recipes the buttons are not visible

    ![No edit and delete recipe](assets/images/readme-images/nobuttons.jpg)

4. As a user I want to be able to use the website on multiple devices of verying sizes
    1. Responsive design means users can use main different screens and resolutions and still have full functionality

    ![Mobile](assets/images/readme-images/mobile.jpg)

    ![Mobile Plus](assets/images/readme-images/mobileplus.jpg)

    ![Tablet](assets/images/readme-images/tablet.jpg)

5. As a site owner I want to be able to promote a brand using links to specific sponsers
    1. Sponsers can be plugged using links on the home page, within the footer and also when viewing recipes under the equipment needed section

    ![Sponser](assets/images/readme-images/sponser.jpg)

## Feature Testing

| Feature | Action taken  | Expected result | Pass/Fail |
| :--- | :--- | :--- | :--- |    
| Navbar | Click Home | Takes me to homepage | Pass |
| Navbar | Click Recipes | Takes me to recipes page, generates recipe collapsible | Pass |
| Navbar | Click Register | Takes me to register page | Pass |
| Navbar | Click Log In | Takes me to login page | Pass |
| Navbar | Click Logo | Takes me to homepage | Pass |
| Homepage | Click "view the selection here" link | Takes me to John Lewis Utensil page | Pass |
| Footer | Click link in footer | Takes me to John Lewis Utensil page | Pass |
| Recipes (not logged in) | Click recipe name | Collapsible to open and show recipe | Pass |
| Recipes (not logged in) | Search for recipe | Results to show if recipe present | Pass |
| Recipes (not logged in) | After search click reset button | All recipes to show | Pass |
| Recipes (not logged in) | Look for edit or delete buttons for recipes | No buttons present | Pass |
| Recipes | Search for blank entry | Validation to fail and warn user | Pass |
| Register | Register blank entry | Validation to fail and warn user | Pass |
| Register | Click already regsitered Log In button | Go to login page | Fail |
| Register | Register with a username that already exists | Page refresh with warning of username exists to user | Pass |
| Register | Register with short username (under 5 characters) | Validation fail and warn user | Pass |
| Register | Register new user | Successfully register and take to recipe page | Pass |
| Logout(only available when logged in) | Click Logout button | Logout and take to login page | Pass |
| Add recipe(only avaialable when logged in) | Click Add recipe | take me to add recipe form | Pass |
| Add recipe form | Add blank recipe | Fail validation and warn user | Pass |
| Add recipe form | Test input fields | Accept valid inputs | Fail |
| Add recipe form | Add valid recipe | Accept recipe and go to recipes page showing recipes | Pass |
| Add recipe form | Click edit button on recipe | Go to edit recipe page | Pass |
| Add recipe form | Click delete button on recipe | Modal opens for deletion confirmation | Pass |
| Deletion modal | Click No to confirmation | Modal closes and disappears | Pass |
| Deletion modal | Click Yes to confirmation | Modal closes, deletes recipe | Pass |
| Edit page | Edit recipe fields and hit submit button | Accept and update recipe | Pass |
| Edit page | Click cancel button | Edit cancel and back to recipe page | Pass |

## Bugs

- Delete function didn't function correctly, always deleted first recipe - Fixed - Fixed modal target (was using data-target when materialize uses href for a tags)
- Already registered feature on register page didnt link to the login page - Fixed - missing href added to register.html
- Add recipe input fields accepting any input - Fixed - patter added to input tags, image source updated to url, collection added for difficulty so user can input only easy, medium or hard
- Edit page, steps, ingedients and equipment all come back as array, would be nice to update to string so format is easier to read on page but it doesnt affect functionality

## Deployment

The project has been deployed using Heroku

1. Create a local requirements.txt("pip3 freeze -- local > requirements.txt" in CLI) and Procfile("echo web: python app.py > Procfile" in CLI) ready to use with Heroku
2. Login to Heroku (sign up if not already a member)
3. Click on new and select Create new app
4. Your new app, must be unique and select region closest to you location
5. Connect Heroku app to GitHub, click the deploy tab of your app and click GitHub as your deploy method
6. Make sure you GitHub profile is dsiplay (if not you will need to log in to GitHub)
7. Next to your GitHub profile, search for your repository name and click search
8. Once repo found click Connect
9. At the top of the page go to Settings
10. Click reveal Config Vars
11. You will need to fill in your enviorment variables here, usually created in a env.py file, this file should not be part of your repo (add to your .gitignore)
12. Go back to the deploy tab
13. Click Enable automatic deployment
14. Click deploy branch
15. Once successfully deployed you will have a link to view your app
16. This will update whenever you push changes to GitHub 


### Acknowledgements

- A few acknowledgements here that I would have been stuck without;

- the method to convert strings to array was found here - https://appdividend.com/2020/09/25/how-to-convert-python-string-to-array/#:~:text=To%20convert%20String%20to%20array,elements%20as%20individual%20list%20items

- recipes that were used throughout development were found using - https://www.bbcgoodfood.com/recipes/

- authentication was taken from mongo mini project from course work, although I did refactor parts of it.

- Code Institute, Tutors and my Mentor were all a big part of making this project possible
