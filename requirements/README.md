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
                    <li><em>Effort</em>: 2 days</li>
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
                    <li><em>Effort</em>: 0.5 days</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>The user account creation page must contain two fields, "Username" and "Password", and a "Create Account" button below the two fields.</li>
                </ul>
            <li><strong>T12S-5</strong>: Password Storage</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 1 day</li>
                    <li><em>Functional/Non-functional</em>: Non-functional</li>
                    <li>The database must store passwords as hashed values with salting.</li>
                </ul>
        </ul>
        <li><strong>T12E-3</strong>: Administrators</li>
        <ul>
            <li><strong>T12S-6</strong>: Admin Appointment</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 1 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>The application must include the ability to appoint admins from pre-existing users.</li>
                </ul>
            <li><strong>T12S-7</strong>: Sales Report</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 2 days</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>Admins must have the ability to generate a sales report. The report shows all items purchased and who purchased them.</li>
                </ul>
          <li><strong>T12S-8</strong>: Sales Report Export to CSV</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 2 days</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>The application must have the ability to export the sales report to a CSV file.</li>
                </ul>
            <li><strong>T12S-9</strong>: Add Inventory</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 3 days</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>Admin users must be able to open a page, enter information, choose a picture, and have information added to the database. </li>
                </ul>
        </ul>
      <li><strong>T12E-4</strong>: Admin Creation</li>
            <ul>
            <li><strong>T12S-10</strong>: Instructions On Manually Converting To Admin User</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.5 days</li>
                          <li><em>Functional/Non-functional</em>:Non-functional</li>
                          <li>The application must include step-by-step instructions created for the admins on how to manually convert a user account into an admin account in the database. The instructions must be understandable to the "not overly technical" admins.</li>
                      </ul>
            </ul>
      <li><strong>T12E-5</strong>: Admin Creation UI</li>
            <ul>
            <li><strong>T12S-11</strong>: Accessibilty to Admins</li>
                      <ul>
                          <li><em>Priority</em>: Needs to Have</li>
                          <li><em>Effort</em>: 0.5 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>Admins must have access to the Admin Creation UI after login.</li>
                      </ul>
            <li><strong>T12S-12</strong>: Search Box</li>
                      <ul>
                          <li><em>Priority</em>: Needs to Have</li>
                          <li><em>Effort</em>: 2 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The Admin Creation UI must contain a search box that checks for a match between the admin's query and the usernames of existing user accounts.</li>
                      </ul>
            <li><strong>T12S-13</strong>: List of Existing User Accounts</li>
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
</ul>
      <li><strong>T12E-6</strong>: Login Page</li>
        <ul>
            <li><strong>T12S-14</strong>: Login Page</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 3 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The application must have a login page.</li>
                      </ul>
            <li><strong>T12S-15</strong>: Users and Admin Login Ability</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.5 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The login page must allow both users and admins to login. </li>
                      </ul>
            <li><strong>T12S-16</strong>: Login Fields and Button</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 1 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The login page must contain two fields: "Username" and "Password". A button labeled "Login" must exist underneath the two fields.</li>
                      </ul>
              </ul>
      <li><strong>T12E-7</strong>: Main Screen</li>
      <ul>
          <li><strong>T12S-17</strong>: Main Screen</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 3 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The application must contain a main screen that is visible to others after login or registration.</li>
                      </ul>
            <li><strong>T12S-18</strong>: Displaying Inventory</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The main screen must list all available inventory and sort it by price from highest to lowest. The main screen must not show uses any inventory that has already been sold.</li>
                      </ul>
            <li><strong>T12S-19</strong>: Add Multiple Items To Cart</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 1 day</li>
                          <li><em>Functional/Non-functional</em>:Non-functional</li>
                          <li>The main screen must allow users to add multiple items to the cart. 
                      </ul>
               <li><strong>T12S-20</strong>: Inventory Search Box</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The main screen must allow users to search inventory via a search box that looks for matches in either item name or item description. 
                      </ul>
                  <li><strong>T12S-21</strong>: Checkout Button</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 1 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The main screen must contain a checkout button that the user can click to go to the shopping cart page. This button must not work when the cart is empty. 
                      </ul>
              </ul>
      <li><strong>T12E-8</strong>: Items on the Main Screen</li>
            <ul>
            <li><strong>T12S-22</strong>: Main Screen Items Characteristics</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>Items Must have a short name, brief description, a picture (or pictures), a price, and a button that adds the item to the cart.</li>
                      </ul>
            <li><strong>T12S-23</strong>: Price Currency</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.5 days</li>
                          <li><em>Functional/Non-functional</em>:Non-functional</li>
                          <li>The pieces of the items must be in U.S. dollars.</li>
                      </ul>
            <li><strong>T12S-24</strong>: Price Formatting</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.5 days</li>
                          <li><em>Functional/Non-functional</em>:Non-functional</li>
                          <li>The prices of items must have "$" before them and be properly formatted with commas and decimal points.</li>
                            <ul>
                            <li>The prices of the items must be stored in a base-10 format. (functional)</li>
                            </ul>
                      </ul>
            </ul>
      <li><strong>T12E-9</strong>: Shopping Cart Page</li>
                  <ul>
                  <li><strong>T12S-25</strong>: Shopping Cart Page</li>
                        <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 3 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The application must include a shopping cart page.</li>
                      </ul>   
                  <li><strong>T12S-26</strong>: Shopping Cart Display List</li>
                        <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The shopping cart page must display a list of every item in the user’s cart.</li>
                      </ul>  
                  <li><strong>T12S-27</strong>: Display List Item Removal</li>
                    <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 1 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The shopping cart page must allow the user to remove any and all items from the list they chose. The page must send the user back to the “main” page if they remove all items from their cart. </li>
                      </ul>   
                  <li><strong>T12S-28</strong>: Currency</li>
                    <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.5 days</li>
                          <li><em>Functional/Non-functional</em>: Functional</li>
                          <li>The shopping cart page must display the subtotal in US dollars, the subtotal is the total price of every item in the user’s cart at checkout.</li>
                      </ul>   
                  <li><strong>T12S-29</strong>: Subtotal Recalculation</li>
                    <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.5 days</li>
                          <li><em>Functional/Non-functional</em>: Non-functional</li>
                          <li>The application must recalculate the subtotal as the user makes changes to their cart contents.</li>
                      </ul>
                  <li><strong>T12S-30</strong>: Pay Now Button</li>
                    <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 1 day</li>
                          <li><em>Functional/Non-functional</em>: Functional</li>
                          <li>The shopping cart page must contain a “pay now” button that brings up a “Pay Now” screen.</li>
                      </ul>   
                  <li><strong>T12S-31</strong>: User Cart</li>
                        <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 days</li>
                          <li><em>Functional/Non-functional</em>: Non-functional</li>
                          <li> The user’s cart must hold all its items as the user navigates the site unless it is modified by the user or if the user completes a purchase. </li>
                        </ul>
      </ul>   
      <li><strong>T12E-10</strong>: Confirm Order Page</li>
            <ul>
                  <li><strong>T12S-32</strong>: Confirm Order Page</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 3 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>There must be a confirm order page. The page must list the names and prices of what the user is buying, the subtutal of the user's order, the tax as ^% of the user's subtotal, the shipping cost associated with the user's shipping choice, and the grand total of the user's order.</li>
                      </ul>
                  <li><strong>T12S-33</strong>: Complete Order Button</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 1 day</li>
                          <li><em>Functional/Non-functional</em>: Functional</li>
                          <li>The confirm order page must have a complete order button that, when pressed, all purchased items must be removed from the inventory. The application must then send the user to the "Complete Order" page. </li>
                      </ul>
                    <li><strong>T12S-34</strong>: Return to Checkout Button</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.5 days</li>
                          <li><em>Functional/Non-functional</em>: Functional</li>
                          <li>The Confirm Order page must have a “Return to Checkout” button that returns the user to the “Checkout” page.</li>
                      </ul>
                         <li><strong>T12S-35</strong>: Continue Shopping Button</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.5 days</li>
                          <li><em>Functional/Non-functional</em>: Functional</li>
                          <li>The Confirm Order page must have a “Continue Shopping” button that returns the user to the “Main” page.</li>
                      </ul>
                            <li><strong>T12S-36</strong>: Cart Remaining The Same After Not Completing Order</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.25 days</li>
                          <li><em>Functional/Non-functional</em>: Functional</li>
                          <li>The user’s cart must remain the same if they chose not to complete the order. </li>
                      </ul>
              </ul>
      <li><strong>T12E-11</strong>: Complete Order Page</li>
            <ul>
                  <li><strong>T12S-37</strong>: Complete Order Page</li>
                  <ul>            
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The application must include a “Complete Order” page. </li>
                        </ul>
                   <li><strong>T12S-38</strong>: Receipt Display Information</li>
                        <ul>            
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 2 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li> The Complete Order page must display a receipt containing all order information present on the “Confirm Order” page. The receipt must also include the last four digits of the user’s credit card number, and the user’s shipping address.</li>
                        </ul>
                  <li><strong>T12S-39</strong>: SendGrid Receipt</li>
                        <ul>            
                          <li><em>Priority</em>: Needs To Have</li>
                          <li><em>Effort</em>: 2 days</li>
                          <li><em>Functional/Non-functional</em>: Non-functional</li>
                          <li> A receipt must be sent to the user. The receipt must be emailed to the user via SendGrid. </li>
                        </ul>
                  <li><strong>T12S-40</strong>: Add Information To Sales Report</li>
                        <ul>            
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 1 day</li>
                          <li><em>Functional/Non-functional</em>: Functional</li>
                          <li>The application must create a "sale" from the user's purchase that lists relevant information such as what was purchased, the user_id of the user that purchased it, the subtotal, the tax, the shipping cost, the total cost, and the date the purchase was made. The sales report must have this information added to it.</li>
                        </ul>
                  <li><strong>T12S-41</strong>: OK Button</li>
                        <ul>            
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.5 days</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li> There must be an “ok” button that empties the cart and allows the user to exit the receipt and return to the “main” screen.  </li>
                  </ul>
            </ul>
            <li><strong>T12S-42</strong>: Credit Card Information Deletion</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 1 day</li>
                    <li><em>Functional/Non-functional</em>: Non-functional</li>
                    <li>The application must delete the crdit card information of the user after the transaction is completed.</li>
        </ul>
      </ul>
      <li><strong>T12E-12</strong>: Sales Report</li>
            <ul>
            <li><strong>T12S-43</strong>: Sales Report Admin Accesibility</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.25 days</li>
                          <li><em>Functional/Non-functional</em>: Functional</li>
                          <li>The sales report must be accesible to admins.</li>
                      </ul>
            <li><strong>T12S-44</strong>: Sales Report Information Displayed</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 0.5 days</li>
                          <li><em>Functional/Non-functional</em>: Functional</li>
                          <li>The sales report must be made up of individual sales. Each sale, representing a purchase made by the user, must be displayed on the sales report.</li>
                      </ul>
            <li><strong>T12S-45</strong>: Sales Report Items Clickability</li>
                      <ul>
                          <li><em>Priority</em>: Would Be Nice To Have</li>
                          <li><em>Effort</em>: 0.5 days</li>
                          <li><em>Functional/Non-functional</em>: Functional</li>
                          <li>The items in the report must be clickable, and must redirect to the receipt associated with their purchase.</li>
                      </ul>
            <li><strong>T12S-46</strong>: Sales Report CSV Export</li>
                      <ul>
                          <li><em>Priority</em>: Must Have</li>
                          <li><em>Effort</em>: 1 day</li>
                          <li><em>Functional/Non-functional</em>:Functional</li>
                          <li>The sales report must have a button that exports the sales report to a CSV file.</li>
                      </ul>
                  </ul>
            </ul>
      <li><strong>T12E-13</strong>: Database Updating Page</li>
            <ul>
            <li><strong>T12S-47</strong>: Database Updating Page Text Fields</li>
                <ul>
                    <li><em>Priority</em>: Would Be Nice To Have</li>
                    <li><em>Effort</em>: 3 days</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>The Database Updating Page must contain three text fields: name (limited to 15 characters), description (limited to 50 characters), and price (will separate any erroneous input from the enumerated price itself when submitted to the database). </li>
       </ul>  
      <li><strong>T12S-48</strong>: Database Updating Page Picture Selection</li>
                <ul>
                    <li><em>Priority</em>: Would Be Nice To Have</li>
                    <li><em>Effort</em>: 2 days</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>The Database Updating page must contain a field to select pictures to add to the submission.</li>               
       </ul>  
      <li><strong>T12S-49</strong>: Add Item Button</li>
                <ul>
                    <li><em>Priority</em>: Would Be Nice To Have</li>
                    <li><em>Effort</em>: 0.5 days</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>Once all fields are filled, the admin can hit an "Add Item" button. The information must be entered into the database as a new item automatically once the "Add Item" button is pressed.</li>                          
       </ul>  
      <li><strong>T12S-50</strong>: Reload Fields After Submission</li>
                <ul>
                    <li><em>Priority</em>: Would Be Nice To Have</li>
                    <li><em>Effort</em>: 0.5 days</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>After entering the item, the page must be reloaded, all fields cleared, and page ready for another submission.</li>         
       </ul>  
      <li><strong>T12S-50</strong>: Admins Access</li>
                <ul>
                    <li><em>Priority</em>: Would Be Nice To Have</li>
                    <li><em>Effort</em>: 0.5 days</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>The data updating page must only be accessible to admins.</li>         
       </ul>  
      <li><strong>T12S-51</strong>: Admin Permissions </li>
                <ul>
                    <li><em>Priority</em>: Would Be Nice To Have</li>
                    <li><em>Effort</em>: 1 day</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>The database updating page must allow admins to add items, edit items, and delete items from inventory.</li>         
       </ul>  
    </ul>
      <li><strong>T12E-14</strong>: UI Mockup</li>
       <ul>
            <li><strong>T12S-52</strong>: High-fidelity mockup</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 7 days</li>
                    <li><em>Functional/Non-functional</em>: Functional</li>
                    <li>There must be a high-fidelity mockup of all screens and the application flow before coding is started.</li>
                </ul>
            <li><strong>T12S-53</strong>: UI Mockup Final Product Translation</li>
                <ul>
                    <li><em>Priority</em>: Must Have</li>
                    <li><em>Effort</em>: 7 days</li>
                    <li><em>Functional/Non-functional</em>: Non-functional</li>
                    <li>The UI Mockup must fully demonstrate how the requirements will translate to the final product such that the client will fully understand what to expect from the team</li>
            </ul>
       </ul>  
</ul>














