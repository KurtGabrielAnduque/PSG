#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <windows.h>
#include <thread>
#include <chrono>
#include <vector>
#include <sstream>
#include <algorithm>
#include <queue>

using namespace std;


// FUNCTION PARA MAG CLEAR NG SCREEN
void clearscreen() {
    system("cls");
}

void menuHeader(){
    cout<<"==================Easy Buy CO.===================="<<endl;
}

// FUNCTION PARA SA PAG LOGIN AND REGISTER NG USERS
string LOGON(string (*Login)()) {
    int choice;

    while (true){
   
    menuHeader();
   
   cout << "[1] - Register" << endl;
   cout << "[2] - Login" << endl;
   cout << "[3] - Back" << endl;
   cout << "Enter choice: ";
   cin >> choice;

   switch (choice) {
   case 1: {
       string username, password;
       cout << "Enter username: ";
       cin >> username;
       cout << "Enter password: ";
       cin >> password;


       ofstream file(username + ".csv");
       if (!file) {
           cerr << "Error creating user file!" << endl;
           break;
       }

       file << username << endl << password<< endl;
       file.close();
       cout << "Registration successful!" << endl;
       system("pause");
       clearscreen();
       break;
       
   }
   case 2: {
       string username;
       do {
           username = Login();
           if (username.empty()) {
               clearscreen();
menuHeader();
               cout << "Incorrect username or password. Try again." << endl;
           }
       } while (username.empty());

 
       return username;
       break;
   }
   case 3:
    return "" ;

   default:
       cout << "Invalid choice. Exiting." << endl;
       return "";
   }
}
   
}

// sub function saan madedetermine kung may account sa files yung user after maglogin
string Login() {
    string user, pass, un, pw;

    cout << "Enter username: ";
    cin >> user;
    cout << "Enter password: ";
    cin >> pass;

    ifstream read(user + ".csv");
    if (!read.is_open()) {
        cout << "User does not exist." << endl;
        return "";
    }

    getline(read, un);
    getline(read, pw);

    if (user == un && pass == pw) {
        return user;
    } else {
        return "";
    }
}

// I convert into vector yung mga data from csv to string para magamit sya for sorting algorithm
vector<string> readCSV(const string& filename){


vector<string> data;
ifstream file(filename);

string line;
while(getline(file,line)){
stringstream ss(line); // ss/stringstream para pwede magcut through comma","
string value;
while(getline(ss,value,',')){
data.push_back(value);
}
}

file.close();
return data;
}

// sub function binary search magagmit sya sa function ng processPurchases
bool BinarySearch(const vector<string>& arr, const string& target){
int low = 0;
int high = arr.size() -  1;

while(low <= high){
int mid = (low + high)/2;

if(arr[mid] == target){
return true;
}else if (arr[mid] < target){
low = mid + 1;
}else{
high = mid - 1;
}
}
}

// ETO YUNG BUYER OPTION 3 GINAWA LANG FUNCTION MASYADONG MAGULO BASAHIN KUNG IKAKABIT PA SA MISMONG INT MAIN
//
void processPurchase(const string& username) {
    clearscreen();
    string target;
    int amount;

    cout << "====================== SEARCH ITEMS ======================" << endl;

    // Read shop data
    vector<string> shopData;
    vector<string> itemNames;
    ifstream shopFile("wholeshop.csv");
    if (!shopFile.is_open()) {
        cerr << "Error: Could not open the shop file!" << endl;
        return;
    }

    string line;
    while (getline(shopFile, line)) {
        shopData.push_back(line);

        // Extract item names for binary search
        stringstream ss(line);
        string item, quantity, seller, price;
        getline(ss, item, ','); // Extract item name
        getline(ss, quantity, ',');
        getline(ss, seller, ',');
        getline(ss, price, ',');
        itemNames.push_back(item);
    }
    shopFile.close();

    // Sort itemNames and shopData simultaneously
    vector<pair<string, string>> sortedData;
    for (size_t i = 0; i < itemNames.size(); i++) {
        sortedData.emplace_back(itemNames[i], shopData[i]);
    }
    sort(sortedData.begin(), sortedData.end());

    // Extract sorted itemNames and shopData back
   
    itemNames.clear();
    shopData.clear();
    for (const auto& pair : sortedData) {
        itemNames.push_back(pair.first);
        shopData.push_back(pair.second);
    }

    // Display available items
    // baka kasi makalimutan ng buyer yung mga tiningnan niya sa whole shop HAHHAHAH
    cout << "Available items:" << endl;
    for (const auto& record : shopData) {
        cout << record << endl;
    }
	cin.ignore();
    cout << endl << "Enter the item you want to buy: ";
    getline(cin, target);

    // Binary search para makita if available pa yung target
    if (!BinarySearch(itemNames, target)) {
        cout << "The item is unavailable." << endl;
        return;
    }

    // Locate the record for the target item
    // para makita yung amount ng item(target)
    string sellerName, priceStr;
    int availableStock = 0;
    for (const auto& record : shopData) {
        stringstream ss(record);
        string item, quantity, seller, price;
        getline(ss, item, ',');
        getline(ss, quantity, ',');
        getline(ss, seller, ',');
        getline(ss, price, ',');
        if (item == target) {
            availableStock = stoi(quantity);
            sellerName = seller;
            priceStr = price;
            break;
        }
    }

    cout << "Available stock: " << availableStock << endl;
    cout << "Price per unit: " << priceStr << endl;
    cout << "How many would you like to buy? ";
    cin >> amount;

    if (amount > availableStock) {
        cout << "Not enough stock available. Try again with a smaller quantity." << endl;
        return;
    }

	int price = stoi(priceStr);
    int totalPrice = price * amount;
    cout << "Total price: " << totalPrice << endl;
    
    // Update shop file after bumili ng seller
    ofstream shopFileOut("wholeshop_temp.csv");
    for (const auto& record : shopData) {
        stringstream ss(record);
        string item, quantity, seller;
        getline(ss, item, ',');
        getline(ss, quantity, ',');
        getline(ss, seller, ',');
		// price
		
		
        if (item == target && seller == sellerName) {
            shopFileOut << item << "," << (stoi(quantity) - amount) << "," << seller << endl;
        } else {
            shopFileOut << record << endl;
        }
    }
    shopFileOut.close();
    remove("wholeshop.csv");
    rename("wholeshop_temp.csv", "wholeshop.csv");

    // Update seller's inventory after bumili ng buyer
    vector<string> sellerInventory;
    ifstream sellerFile("inventory_" + sellerName + ".csv");
    while (getline(sellerFile, line)) {
        sellerInventory.push_back(line);
    }
    sellerFile.close();

    ofstream sellerFileOut("inventory_" + sellerName + ".csv");
    for (auto& record : sellerInventory) {
        stringstream ss(record);
        string item;
        int quantity;
        getline(ss, item, ',');
        ss >> quantity;

        if (item == target) {
            sellerFileOut << item << "," << (quantity - amount) << endl;
        } else {
            sellerFileOut << record << endl;
        }
    }
    sellerFileOut.close();

    // update purchase in buyer's cart option 3 to
    ofstream cartFile("buyer_cart_" + username + ".csv", ios::app);
    cartFile << target << "," << amount << "," << sellerName << endl;
    // (incomplete)
    // add the total amount 
    cartFile.close();
   
    // update purchases in the end of seller option 3 to
    ofstream purchaseFile("purchases_" + sellerName + ".csv", ios::app);
    purchaseFile << target << "," << amount << "," << username << endl;
    purchaseFile.close();
    
	
	ofstream profitFile("profit_" + sellerName + ".csv", ios::app);
    profitFile << target << "," << amount << "," << totalPrice << endl;
    profitFile.close();

    cout << "Purchase successful!" << endl;
}





// Helper function to trim leading and trailing whitespace
string trim(const string& str) {
    size_t first = str.find_first_not_of(" \t");
    size_t last = str.find_last_not_of(" \t");
    return (first == string::npos || last == string::npos) ? "" : str.substr(first, last - first + 1);
}



bool searchAndRemoveBuyerCart(const string& buyer, const string& item, const string& quantity, const string& username) {
    string cartFile = "buyer_cart_" + buyer + ".csv";
    string tempFile = "temp_cart_" + buyer + ".csv";
    ifstream cart(cartFile);
    ofstream tempCart(tempFile);

    if (!cart.is_open()) {
        cout << "No cart data found for buyer: " << buyer << endl;
        return false;
    }

    if (!tempCart.is_open()) {
        cout << "Error creating temporary file for buyer: " << buyer << endl;
        return false;
    }

    bool itemFound = false;
    string line;

    while (getline(cart, line)) {
        stringstream ss(line);
        string cartItem, cartQuantity, cartBuyer, cartSeller;
        getline(ss, cartItem, ',');
        getline(ss, cartQuantity, ',');
        getline(ss, cartSeller);

        // Match item, quantity, and buyer
        if (cartItem == item && cartQuantity == quantity && cartSeller == username && !itemFound) {
            cout << "Item found and removed from buyer's cart!" << endl;
            cout << "Item: " << cartItem << ", Quantity: " << cartQuantity << endl;
            itemFound = true;
        } else {
            tempCart << line << endl;
        }
    }

    cart.close();
    tempCart.close();

    if (itemFound) {
        remove(cartFile.c_str());
        rename(tempFile.c_str(), cartFile.c_str());
    } else {
        remove(tempFile.c_str());
        cout << "Item not found in buyer's cart." << endl;
    }

    return itemFound;
}

void displayProfit(const string& username) {
    clearscreen();
    string line;
    int totalProfit = 0;

    ifstream profitFile("profit_" + username + ".csv");
    if (!profitFile.is_open()) {
        cout << "No profit data found for " << username << "." << endl;
        return;
    }

    cout << "===================== YOUR PROFITS =====================" << endl;
    cout << "Item, Quantity Sold, Earnings" << endl;

    while (getline(profitFile, line)) {
        stringstream ss(line);
        string item, quantity, earnings;
        getline(ss, item, ',');
        getline(ss, quantity, ',');
        getline(ss, earnings, ',');

        cout << item << ", " << quantity << ", " << earnings << endl;
        totalProfit += stoi(earnings);
    }
    profitFile.close();

    cout << "========================================================" << endl;
    cout << "Total Profit (php): " << totalProfit << endl;
    system("pause");
    clearscreen();
}



void processSellerOrders(const string& username) {
    clearscreen();

// APPLYING QUEUE LESSON
    queue<string> pendingOrders; // Queue to store pending orders
   
    string line;
// FROM CSV ILOLOAD PAPUNTANG VECTOR PARA MA MODIFY FOR SHIPPING
    // Load purchases from file into the queue
    ifstream purchases("purchases_" + username + ".csv");
    if (!purchases.is_open()) {
        cout << "No purchase data found for this seller." << endl;
        return;
    }

    while (getline(purchases, line)) {
        pendingOrders.push(line);
    }
    purchases.close();

    if (pendingOrders.empty()) {
        cout << "No pending purchases at the moment." << endl;
        return;
    }

    while (!pendingOrders.empty()) {
        clearscreen();

//naka arrange
        // Display the next order in the queue
        string currentOrder = pendingOrders.front();
        stringstream ss(currentOrder);
        string item, quantity, buyer;

        getline(ss, item, ',');
        getline(ss, quantity, ',');
        getline(ss, buyer, ',');

        cout << "Next order in the queue:" << endl;
        cout << "Item: " << item << ", Amount: " << quantity << ", Buyer: " << buyer << endl;

        // option para sa shipping ng seller
        //
        cout << "\nOptions:" << endl;
        cout << "[1] Ship out this order" << endl;
        cout << "[2] Exit to main menu" << endl;
        cout << "Enter choice: ";
        int action;
        cin >> action;

        if (action == 1) {
            // Ship out the order
            cout << "Shipping out the order for " << buyer << "..." << endl;

            // Remove the order from the queue
            pendingOrders.pop();

            // Update the purchases file(csv ng pending orders ng sellers)
            ofstream tempFile("purchases_temp.csv");
            queue<string> tempQueue = pendingOrders; // Copy remaining orders to temp file
            while (!tempQueue.empty()) {
                tempFile << tempQueue.front() << endl;
                tempQueue.pop();
            }
            tempFile.close();

            // Replace the original file with the updated file
            remove(("purchases_" + username + ".csv").c_str());
            rename("purchases_temp.csv", ("purchases_" + username + ".csv").c_str());

if (searchAndRemoveBuyerCart(buyer, item, quantity, username)) {
       cout << "Item is confirmed in the buyer's cart." << endl;
   } else {
       cout << "Item is not in the buyer's cart." << endl;
   }

            cout << "Order shipped successfully!" << endl;
            this_thread::sleep_for(chrono::seconds(10));
           
           
        }  else if (action == 2) {
            // Exit to main menu
            cout << "Exiting to main menu..." << endl;
            break;
        } else {
            cout << "Invalid choice. Please try again." << endl;
        }
    }

    if (pendingOrders.empty()) {
        cout << "All orders have been processed!" << endl;
        clearscreen();
    }
}

void removeZeroItems(const string& fileName) {
    ifstream file(fileName);
    string line;
    vector<string> lines;
   
    // Read the header line
    getline(file, line);
    lines.push_back(line);
   
    // Read all lines and store them in the vector, skipping those with 0 quantity
    while (getline(file, line)) {
        stringstream ss(line);
        string item, quantityStr, seller;
        int quantity;
       
        getline(ss, item, ','); // Get item name
        getline(ss, quantityStr, ','); // Get quantity as string
        getline(ss, seller, ','); // Get seller name
       
        quantity = stoi(quantityStr); // Convert quantity string to integer
       
        // Only keep items with quantity > 0
        if (quantity > 0) {
            lines.push_back(line);
        }
    }
    file.close();

    // Write the updated data back to the file
    ofstream outFile(fileName);
    for (const string& line : lines) {
        outFile << line << endl;
    }
    outFile.close();

}










// Main function
int main() {
while(true){
    int choice1;
   
menuHeader();

    cout<<"Select Type of Account:"<<endl;
    cout << "\t[1] = Seller" << endl;
    cout << "\t[2] = Buyer" << endl;
    cout << "\t[3] = Exit" << endl;
    cout << "Enter choice: ";
    cin >> choice1;
    clearscreen();

    if (choice1 == 1) {
        string username = LOGON(Login);
        clearscreen();

            if (username.empty()) {
                // User selected "Back" in LOGON
                continue; // Return to the main menu
            }

while(true){
int out;



if (!username.empty()) {
           int select;
          menuHeader();
           cout << "Welcome back, "<< username << "!" <<endl;
         
         
           cout << "\t[1] = Sell Items" << endl;
           cout << "\t[2] = Check Inventory" << endl;
           cout << "\t[3] = Process Buyers" << endl;
           cout << "\t[4] = Display Profit" << endl;
           cout << "\t[5] = Exit"<<endl;
           cout << "Enter choice: ";
           cin >> select;
           out = select;

           switch (select) {
           case 1:
           {

           clearscreen();
		  string sell;
		  int quantity;
		  int price;
		
		menuHeader();
			cin.ignore();
		  cout << "Enter the item you want to sell: ";
		  getline(cin,sell);
		  
		  cout << "Enter the quantity: ";
		  cin >> quantity;
		  cout << "Price per piece: ";
		  cin>> price;
		
		string shopFile = "wholeshop.csv";
		
		   // Check if the file is empty or does not exist
		   ifstream shopCheck(shopFile);
		   bool isFileEmpty = shopCheck.peek() == ifstream::traits_type::eof(); // Check if file is empty
		   shopCheck.close();
		
		   // Open file in append mode
		   ofstream file(shopFile, ios::app);
		
		   // Write the header if the file is empty
		   if (isFileEmpty) {
		       file << "Item,Quantity,Seller,Price per each" << endl; // Add the heading
   			}	

			file.close();
			
			  // Update shop inventory  
			  file.open("wholeshop.csv", ios::app);
			  file << sell << "," << quantity << "," << username << "," << price << endl;
			  file.close();
			
			  // Update seller's inventory
			  file.open("inventory_" + username + ".csv", ios::app);
			  file << sell << "," << quantity << endl;
			  file.close();
			
			  cout << "Item added successfully!" << endl;
			  system("pause");
			  clearscreen();
			  break;

             
           }
            case 2:
            {
            clearscreen();
            string items;
           
            removeZeroItems("inventory_" + username + ".csv");
            removeZeroItems("wholeshop.csv");
           
                ifstream checkinventory;
                checkinventory.open("inventory_" + username + ".csv");
               
               
                cout << "===================== YOUR INVENTORY ====================="<<endl;
                while(getline(checkinventory,items)){
                cout << items << endl;
               

}

cout << endl;
cout << endl;
system("pause");
            clearscreen();
            break;
            }
           
           
            case 3:
            {
            processSellerOrders(username);
    		break;
         
			}
           
			
			case 4:
				displayProfit(username);
    			break;
            }
        }
        if (out == 5){
        clearscreen();
        break;
       
}
       
   


}
       
     
 
       
    } else if (choice1 == 2) {
        string username = LOGON(Login);
                    clearscreen();
       if (username.empty()) {
                // User selected "Back" in LOGON
                continue; // Return to the main menu
            }

while(true){
int out;

        if (!username.empty()) {
            int select;
            clearscreen();
            menuHeader();
            cout <<"Welcome back, "<< username << "!"<<endl;
            cout <<"\t[1] = Viewshop"<<endl;
            cout <<"\t[2] = Buy"<<endl;
            cout <<"\t[3] = Check Cart"<<endl;
            cout <<"\t[4] = Exit"<<endl;
            cout <<"Enter choice: ";
            cin >> select;
           
            clearscreen();
           
            switch (select){
            case 1:
            {
   
			   vector<string> items;
			   string line;
			   ifstream shopFile("wholeshop.csv");
			   
			   if (!shopFile.is_open()) {
			       cerr << "Error: Could not open the shop file!" << endl;
			       break;
			   }
			   
			 
			   while (getline(shopFile, line)) {
			       items.push_back(line);
			   }
			   shopFile.close();
			
			   
			   sort(items.begin(), items.end());
			   
			   menuHeader();
			   cout << endl;
			   cout << "=========== Items in the shop (alphabetically sorted) ===========" << endl;
			   
			   cout << endl;
			   
			   for (const string& item : items) {
			       cout << item << endl;
			   }
			
			   cout << endl << endl;
			   cout << "=================================================================" << endl;
			   system("pause");
			   clearscreen();
			   break;
			}
           
           
            case 2:
            {
            processPurchase(username);
            system("pause");
            clearscreen();
            break;
}
           
           
            case 3:
            {
			clearscreen();
			menuHeader();
			           
			string line;
			ifstream cart("buyer_cart_" + username + ".csv");
			
			cout << "Your cart:" << endl;
			while (getline(cart, line)) {
			    cout << line << endl;
			  }
			  cart.close();
			system("pause");
			clearscreen();
			   break;

           
}
           
           
}
out = select;
        }
        if (out == 4){
        clearscreen();
        break;
       
}
  }
       
       
       
       
       
    } else if(choice1 == 3){
    cout << "Exiting program"<<endl;
    break;
}else {
        cout << "Invalid role selected. Exiting program." << endl;
        break;
    }
}
    return 0;
}


