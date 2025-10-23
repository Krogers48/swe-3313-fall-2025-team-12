<h1>Requirements</h1>
<h2>Version 1</h2>
<ul>
      <li><strong>T12E-1</strong>: Users</li>
        <ul>
            <li><strong>T12S-1</strong>: Self-Register</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 2 days</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>Users must be able to create their own accounts.</li>
                </ul>
            <li><strong>T12S-2</strong>: Login</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 1 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>Users must be able to login to their accounts.</li>
                </ul>
            <li><strong>T12S-3</strong>: Unique Username and Password</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 2 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>All users must have a unique username and 6-character minimum password.</li>
        </ul>
    </ul>
      <li><strong>T12E-2</strong>: User Account Creation</li>
        <ul>
            <li><strong>T12S-4</strong>: Creation Page</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 2 days</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>There must be a user account creation page.</li>
                </ul>
            <li><strong>T12S-5</strong>: Creation Page Fields</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 1 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>The User Account Creation page must contain two fields: "Username" and "Password".</li>
                </ul>
            <li><strong>T12S-6</strong>: Create Account Button</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 2 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>The User Account Creation page must contain a "Create Account" button below the first two fields.</li>
        </ul>
    </ul>
        <li><strong>T12E-3</strong>: Administrators</li>
        <ul>
            <li><strong>T12S-1</strong>: Admin Appointment</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 0.5 days</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>An ability to appoint admins from pre-existing users must exist.</li>
                </ul>
            <li><strong>T12S-2</strong>: Sales Report</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 1 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>Admins must be able to generate a sales report that shows everything purchased and who purchased it.</li>
            </ul>
          <li><strong>T12S-3</strong>: Sales Report Export to CSV</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 1 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>A method to export the sales report to a CSV must exist.</li>
            </ul>
            <li><strong>T12S-4</strong>: Add Inventory</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 1 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>Admin users must be able to open a page, enter information, choose a picture, and have information added to the database. </li>
          </ul>
        </ul>
      <li><strong>T12E-4</strong>: Admin Creation</li>
            <ul>
            <li><strong>T12S-1</strong>: Instructions On Manually Converting To Admin User</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.5 days</li>
                          <li><em>Functional/Non-functional</em>:Non-functional</li>
                          <li>There must be step-by-step instructions created for the admins on how to manually convert a user account into an admin account in the database.</li>
                      </ul>
            <li><strong>T12S-1</strong>: Easy To Understand Instructions</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.5 days</li>
                          <li><em>Functional/Non-functional</em>:Non-functional</li>
                          <li>The instructions must be understandable to the "not overly technical" admins.</li>
                      </ul>
      <li><strong>T12E-5</strong>: Admin Creation UI</li>
            <ui>
            <li><strong>T12S-1</strong>: Accessibilty to Admins</li>
                      <ul>
                          <li><em>Priority</em>: Needs to Have</li>
                          <li><em>Effort</em>: 1 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The Admin Creation UI must be accessible to admins after login.</li>
                      </ul>
            <li><strong>T12S-1</strong>: Search Box</li>
                      <ul>
                          <li><em>Priority</em>: Needs to Have</li>
                          <li><em>Effort</em>: 2 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The Admin Creation UI must contain a search box that checks for a match between the admin's query and the usernames of existing user accounts.</li>
                      </ul>
            <li><strong>T12S-1</strong>: List of Existing User Accounts</li>
                      <ul>
                          <li><em>Priority</em>: Needs to Have</li>
                          <li><em>Effort</em>: 2 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The Admin Creation UI must contain a list of all existing user accounts.</li>
                            <ul>
                                  <li>    Each account in the list must have a button labeled “Convert to Admin” associated with it </li>
                                        <li>Once “Convert to Admin” is clicked, a dialog box must appear that reads  “Do you wish to transform the account: {user account username} Into an admin account?” </li>
                                          <li>There must be two options under this dialogue: ‘Yes’ and ‘No’ </li>
                                          <li>If “No” is chosen, the dialogue box must be closed (functional) </li>
                                          <li>If “Yes” is chosen, the admin must be prompted for their password (functional)</li>
                                          <li>If the password is entered incorrectly, the password field must be cleared, and the admin must be informed that their password was incorrect (functional) </li>
                                          <li>If the password is entered correctly, the user account must be transformed into an admin account, the dialogue box must be closed, and a new one must open that reads “The account {account username} is now an admin” with an “ok” button that the admin can click to close the dialogue box. (functional) </li>
            </ul>
      </ul>
      <li><strong>T12E-6</strong>: Login Page</li>
            <li><strong>T12S-1</strong>Login Page</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 3 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>There must be a login page.</li>
                      </ul>
            <li><strong>T12S-1</strong>Users and Admin Login Ability</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.5 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The Login page must allow both users and admins to login. </li>
                      </ul>
            <li><strong>T12S-1</strong>Login Fields</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 1 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The Login page must contain two fields: "Username" and "Password".</li>
                      </ul>
      <li><strong>T12E-7</strong>: Main Screen</li>
      <li><strong>T12E-8</strong>: Items on the Main Screen</li>
            <li><strong>T12S-1</strong>Main Screen Items Characteristics</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>Items Must have a short name, brief description, a picture (or pictures), a price, and a button that adds the item to the cart.</li>
                      </ul>
            <li><strong>T12S-1</strong>Price Currency</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.5 day</li>
                          <li><em>Functional/Non-functional</em>:Non-functional</li>
                          <li>The pieces of the items must be in U.S. dollars.</li>
                      </ul>
            <li><strong>T12S-1</strong>Price '$'</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.5 day</li>
                          <li><em>Functional/Non-functional</em>:Non-functional</li>
                          <li>The prices of items must have "$" before them.</li>
                  <li><strong>T12S-1</strong>Price '$'</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.5 day</li>
                          <li><em>Functional/Non-functional</em>:Non-functional</li>
                          <li>The prices of items must have "$" before them.</li>
                            
      <li><strong>T12E-9</strong>: Shopping Cart Page</li>
          There must be a Shopping Cart page (functional) 

    The Shopping Cart page must display a list of every item in the user’s cart (functional) 

    The Shopping Cart page must allow the user to remove any and all items from the list they chose (functional) 

    The Shopping Cart page must send the user back to the “main” page if they remove all items from their cart (functional) 

    The Shopping Cart page must display the subtotal in US dollars, the subtotal is the total price of every item in the user’s cart at checkout (functional) 

    The subtotal must be recalculated as the user makes changes to their cart contents (non-functional) 

    The shopping cart page must contain a “pay now” button that brings up a “Pay Now” screen (functional) 

    The user’s cart must hold all its items as the user navigates the site unless it is modified by the user or if the user completes a purchase (non-functional) 
      <li><strong>T12E-10</strong>: Confirm Order Page</li>
      <li><strong>T12E-11</strong>: Complete Order Page</li>
          There must be a “Complete Order” page (functional) 

    The Complete Order page must display a receipt containing all order information present on the “Confirm Order” page (functional) 

    The receipt must also include the last four digits of the user’s credit card number, and the user’s shipping address (functional) 

    The receipt must be emailed to the user (from my understanding, all this means is that there is a page showing the receipt to the user) (functional) 

    The receipt must be emailed to the user via SendGrid (Non-functional) 

    All items purchased by the user must be added to the sales report (functional) 

    There must be an “ok” button that empties the cart and allows the user to exit the receipt and return to the “main” screen (functional) 
      <li><strong>T12E-12</strong>: Sales Report</li>
            <ui>
            <li><strong>T12S-1</strong>Sales Report Admin Accesibility</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 1 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The sales report must be accesible to admins.</li>
                      </ul>
            <li><strong>T12S-1</strong>Sales Report Information Displayed</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 1 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The sales report must show every purchased item and who purchased the items.</li>
            <li><strong>T12S-1</strong>Sales Report Items Clickability</li>
                      <ul>
                          <li><em>Priority</em>: Would Be Nice To Have</li>
                          <li><em>Effort</em>: 1 day</li>
                          <li><em>Functional/Non-functional</em>Fnctional</li>
                          <li>The items in the report must be clickable, and must redirect to the receipt associated with their purchase</li>
            <li><strong>T12S-1</strong>Sales Report CSV Export</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 1 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The sales report must have a button that exports the sales report to a CSV file.</li>
                      </ul>
      <li><strong>T12E-13</strong>: Database Updating Page</li>
            <li><strong>T12S-3</strong>: Database Updating Page Text Fields</li>
                <ul>
                    <li><em>Priority</em>: Would Be Nice To Have</li>
                    <li><em>Effort</em>: 1 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>The Database Updating Page must contain three text fields: name (limited to 15 characters), description (limited to 50 characters), and price (will separate any erroneous input from the enumerated price itself when submitted to the database). </li>
       </ul>  
      <li><strong>T12S-3</strong>: Database Updating Page Picture Selection</li>
                <ul>
                    <li><em>Priority</em>: Would Be Nice To Have</li>
                    <li><em>Effort</em>: 1 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>The Database Updating page must contain a field to select pictures to add to the submission.</li>               
       </ul>  
      <li><strong>T12S-3</strong>: Add Item Button</li>
                <ul>
                    <li><em>Priority</em>: Would Be Nice To Have</li>
                    <li><em>Effort</em>: 1 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>Once all fields are filled, the admin can hit an "Add Item" button. The information must be entered into the database as a new item automatically once the "Add Item" button is pressed.</li>                          
       </ul>  
      <li><strong>T12S-3</strong>: Reload Fields After Submission</li>
                <ul>
                    <li><em>Priority</em>: Would Be Nice To Have</li>
                    <li><em>Effort</em>: 1 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>After entering the item, the page must be reloaded, all fields cleared, and page ready for another submission.</li>         
       </ul>  
    </ul>
      <li><strong>T12E-4</strong>: UI Mockup</li>
       <ul>
            <li><strong>T12S-1</strong>: High-fidelity mockup</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 1 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>There must be a high-fidelity mockup of all screens and the application flow before coding is started.</li>
                </ul>
            <li><strong>T12S-3</strong>: UI Mockup Final Product Translation</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 1 day</li>
                    <li><em>Functional/Non-functional</em>: Non-functional</li>
                    <li>The UI Mockup must fully demonstrate how the requirements will translate to the final product such that the client will fully understand what to expect from the team</li>
            </ul>
       </ul>  
</ul>

