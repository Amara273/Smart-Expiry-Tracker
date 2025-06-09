Demo: https://drive.google.com/file/d/1iJ3njnbu4_vMY1oFaQrLcmUFN3wSb8GQ/view?usp=sharing
# Smart-Expiry-Tracker

1. Secure Account System (Sign Up / Log In / Forgot Password)
	The system includes a secure login system with account creation and password recovery options. On launch, users are presented with a custom-styled Tkinter sign-up window.
	This is the Sign Up page, where users can create a new account by entering their email, username, and password.
	After entering a valid email and clicking the “Forgot Password” button, a new password is sent to the user's email inbox.
	A confirmation message indicates that a reset password has been sent.
By entering the newly reset password, users can log in to their account successfully.

3. Real-Time Alerts on Login
 	Immediately after a successful login, the application automatically scans the user’s inventory and displays a pop-up alert listing items either low in stock or near their expiry date.
	A pop-up alert showing low stock and nearly expired items right after login.
	By clicking the “Yes” button in the pop-up alert, users can view more detailed information about the listed products.

3. Add Item
 	A user-friendly form with labeled input fields allows users to add new items, specifying name, quantity, category, compartment, and expiry date.
	Add Item form showing input fields for all required item details.
	A pop-up dialog shows that the new item has been added successfully.

5. Display Items
 	Items are displayed in a visually organized list within the GUI, showing all item details in structured columns.

6. Check Expiry
 	Users can click on the “Check Expiry” function to view all items nearing expiry. 
	Near expiry and expired items are displayed in order of their expiration dates, with the soonest to expire shown first.

8. Sort Items
	Users can sort items using various criteria to organize their list more effectively. Sorting options include:
		Name: Alphabetically from A to Z or Z to A
		Priority: Mark an item to appear at the top of the list
		Quantity: From lowest to highest or highest to lowest
		Category: Group items by their assigned category
		Compartment: Sort items based on storage location
		Expiry Date: From nearest to farthest expiry
	Items are sorted alphabetically, with "Apple" pinned at the top.
	Items are organized by category.
	Items are arranged by compartment.
	Items in order of approaching expiry dates.

10. Filter Items
	Users can filter items by existing category using the buttons available in a pop-up window.
	By selecting the "Dessert and Cake" button in the pop-up window, only items under the category are displayed.

12. Check Low Stock
 	By clicking “Low Stock,” users can quickly see which items have quantities less than 2.
	Filtered list displaying only low-stock items (quantity < 2).

14. Exit System
 	A clean exit button allows users to safely close the application, with a confirmation dialog to prevent accidental exits.

The exit confirmation dialog appears after clicking the exit button.
