# Automationpactice.com_ui_test
* This is a very basic test automation example project created with Python 3.7, Selenium WebDriver, and pytest following Page Object Model.
The AUT is [a training online shop](http://automationpractice.com/). Also Chromedriver should be available in the path.

* Currently the project contains one test covering the following user story:
`As a user I want to be able to search for the selected product and get matching search results so that I can review results and select the product to buy.`

* The test is covering the following acceptance criteria:

      GIVEN Main Page is opened
      WHEN user enters search query into the search bar
      AND user hits ENTER
      THEN Search Results Page should be opened
      AND count of the displayed products should be more than 0
      AND the title of the first displayed product should match the user's search query
      AND the displayed product should have an image
