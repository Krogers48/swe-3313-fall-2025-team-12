<h1>Requirements</h1>
<h2>Version 1</h2>
<ul>
      <li><strong>T12E-1</strong>: Users</li>
        <ul>
            <li><strong>T12S-1</strong>: Self-Register</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 3 days</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>All users must have the ability to create their own accounts and login into them.</li>
                </ul>
            <li><strong>T12S-2</strong>: Unique Username and Password</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 2 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>All users must have a unique username and 6-character minimum password.</li>
        </ul>
    </ul>
      <li><strong>T12E-2</strong>: User Account Creation</li>
        <ul>
            <li><strong>T12S-3</strong>: Creation Page</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 3 days</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>The application must include a user account creation screen.</li>
                </ul>
            <li><strong>T12S-4</strong>: Creation Page Fields</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 0.5 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>The user account creation page must contain two fields, "Username" and "Password", and a "Create Account" button below the two fields.</li>
                </ul>
        </ul>
    </ul>
        <li><strong>T12E-3</strong>: Administrators</li>
        <ul>
            <li><strong>T12S-5</strong>: Admin Appointment</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 1 days</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>The application must include the ability to appoint admins from pre-existing users.</li>
                </ul>
            <li><strong>T12S-6</strong>: Sales Report</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 2 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>Admins must have the ability to generate a sales report. The report shows all items purchased and who purchased them.</li>
            </ul>
          <li><strong>T12S-7</strong>: Sales Report Export to CSV</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 2 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>The application must have the ability to export the sales report to a CSV file.</li>
            </ul>
            <li><strong>T12S-8</strong>: Add Inventory</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 3 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>Admin users must be able to open a page, enter information, choose a picture, and have information added to the database. </li>
          </ul>
        </ul>
      <li><strong>T12E-4</strong>: Admin Creation</li>
            <ul>
            <li><strong>T12S-9</strong>: Instructions On Manually Converting To Admin User</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.5 days</li>
                          <li><em>Functional/Non-functional</em>:Non-functional</li>
                          <li>The application must include step-by-step instructions created for the admins on how to manually convert a user account into an admin account in the database. The instructions must be understandable to the "not overly technical" admins.</li>
                      </ul>
            </ul>
      <li><strong>T12E-5</strong>: Admin Creation UI</li>
            <ul>
            <li><strong>T12S-10</strong>: Accessibilty to Admins</li>
                      <ul>
                          <li><em>Priority</em>: Needs to Have</li>
                          <li><em>Effort</em>: 0.5 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>Admins must have access to the Admin Creation UI after login.</li>
                      </ul>
            <li><strong>T12S-11</strong>: Search Box</li>
                      <ul>
                          <li><em>Priority</em>: Needs to Have</li>
                          <li><em>Effort</em>: 2 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The Admin Creation UI must contain a search box that checks for a match between the admin's query and the usernames of existing user accounts.</li>
                      </ul>
            <li><strong>T12S-12</strong>: List of Existing User Accounts</li>
                      <ul>
                          <li><em>Priority</em>: Needs to Have</li>
                          <li><em>Effort</em>: 3 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The Admin Creation UI must contain a list of all existing user accounts.</li>
                            <ul>
                                    <li>Each listed account must have an associated button labeled “Convert to Admin”.</li>
                                    <li>Once “Convert to Admin” is clicked, a dialog box must appear that reads  “Do you wish to transform the account: {user account username} Into an admin account?” </li>
                                    <li>Two options must exist under this dialogue: ‘Yes’ and ‘No’. </li>
                                    <li>If “No” is chosen, the dialogue box must be closed. </li>
                                    <li>If “Yes” is chosen, tha application must prompt the admin for their password.</li>
                                    <li>If the password is entered incorrectly, the password field must clear, and the application must inform the admin that their password is incorrect.</li>
                                    <li>If the password is entered correctly, the application must transform the user into an admin account. The dialogue box must close, and a new one must open that reads “The account {account username} is now an admin” with an “ok” button that the admin can click to close the dialogue box. </li>
            </ul>
      </ul>
      <li><strong>T12E-6</strong>: Login Page</li>
        <ul>
            <li><strong>T12S-13</strong>Login Page</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 3 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The application must have a login page.</li>
                      </ul>
            <li><strong>T12S-14</strong>Users and Admin Login Ability</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.5 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The login page must allow both users and admins to login. </li>
                      </ul>
            <li><strong>T12S-15</strong>Login Fields and Button</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 1 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The login page must contain two fields: "Username" and "Password". A button labeled "Login" must exist underneath the two fields.</li>
                      </ul>
      <li><strong>T12E-7</strong>: Main Screen</li>
      <li><strong>T12E-8</strong>: Items on the Main Screen</li>
            <ul>
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
                      </ul> 
            </ul>
      <li><strong>T12E-9</strong>: Shopping Cart Page</li>
                  <ul>
                  <li><strong>T12S-1</strong>Shopping Cart Page</li>
                        <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 3 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>There must be a Shopping Cart page.</li>
                      </ul>   
                  <li><strong>T12S-1</strong>Shopping Cart Display List</li>
                        <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The Shopping Cart page must display a list of every item in the user’s cart.</li>
                      </ul>  
                  <li><strong>T12S-1</strong>Shopping Cart Display List</li>
                    <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The Shopping Cart page must allow the user to remove any and all items from the list they chose (functional) </li>
                      </ul>   
                  <li><strong>T12S-1</strong>Shopping Cart Display List</li>
                    <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li></li> The Shopping Cart page must send the user back to the “main” page if they remove all items from their cart (functional)  </li>
                      </ul>   
                  <li><strong>T12S-1</strong>Shopping Cart Display List</li>
                    <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li></li> The Shopping Cart page must display the subtotal in US dollars, the subtotal is the total price of every item in the user’s cart at checkout</li>
                      </ul>   
                  <li><strong>T12S-1</strong>Shopping Cart Display List</li>
                    <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 day</li>
                          <li><em>Functional/Non-functional</em>:Non-functional</li>
                          <li>The subtotal must be recalculated as the user makes changes to their cart contents.</li>
                      </ul>
                  <li><strong>T12S-1</strong>Shopping Cart Display List</li>
                    <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The shopping cart page must contain a “pay now” button that brings up a “Pay Now” screen.</li>
                      </ul>   
                  <li><strong>T12S-1</strong>Shopping Cart Display List</li>
                        <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 day</li>
                          <li><em>Functional/Non-functional</em>:Non-functional</li>
                          <li> The user’s cart must hold all its items as the user navigates the site unless it is modified by the user or if the user completes a purchase. </li>
      </ul>   
      <li><strong>T12E-10</strong>: Confirm Order Page</li>
      <li><strong>T12E-11</strong>: Complete Order Page</li>
            <ul>
                  <li><strong>T12S-1</strong>Complete Order Page</li>
                  <ul>            
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>  There must be a “Complete Order” page. </li>
                        </ul>
                   <li><strong>T12S-1</strong>Complete Order Page</li>
                        <ul>            
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li> The Complete Order page must display a receipt containing all order information present on the “Confirm Order” page.</li>
                        </ul>
                   <li><strong>T12S-1</strong>Complete Order Page</li>
                        <ul>            
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li> The receipt must also include the last four digits of the user’s credit card number, and the user’s shipping address (functional) </li>
                        </ul>
                   <li><strong>T12S-1</strong>Complete Order Page</li>
                        <ul>            
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li> The receipt must be emailed to the user (from my understanding, all this means is that there is a page showing the receipt to the user) (functional)  </li>
                        </ul>
                  <li><strong>T12S-1</strong>Complete Order Page</li>
                        <ul>            
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 day</li>
                          <li><em>Functional/Non-functional</em>:Non-functional</li>
                          <li> The receipt must be emailed to the user via SendGrid (Non-functional) </li>
                        </ul>
                  <li><strong>T12S-1</strong>Complete Order Page</li>
                        <ul>            
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 day</li>
                          <li><em>Functional/Non-functional</em>:Non-functional</li>
                          <li>All items purchased by the user must be added to the sales report (functional) </li>
                        </ul>
                  <li><strong>T12S-1</strong>Complete Order Page</li>
                        <ul>            
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 day</li>
                          <li><em>Functional/Non-functional</em>:Non-functional</li>
                          <li> There must be an “ok” button that empties the cart and allows the user to exit the receipt and return to the “main” screen (functional)  </li>
                  </ul>
            </ul>
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






