// ------------------------------------------------------------------------------------------------------------------------------------
// Name: Windows 95 Key Generator
// Date: Jan 2026 | Updated: March 2026 (Added Code-Comments & Documentation)
//
// Description:
//
//		Just a little fun side-project I wanted to try out as I was playing around with old motherboard BIOS ROMs &
//	 System Emulations. So I made this for everytime I had to install Windows 95 to a virtual machine, I did not have
//   to keep going back to websites and finding a key or copy/pasting. Plus since the format of how Microsoft created 
//   these keys is public knowledge so I figured it would be fun to re-create that in Python and C++.
//   This is the C++ Version of the Key Generator...
//
//	 Windows 95 Key Format: dddyy-OEM-xxxxxxx-zzzzz
// 
//			-- ddd: Day of the Year (001 - 365)
//			--  yy: Two-Digit Year of Issue (95 - 02)
//			--   x: First Digit Must be 0 | Final Digit Cannot be = 0, 8, 9 | Must be Added Together & Divisible by 7 (EVENLY)
//			--   z: Any 5 Digits of Choice (No Restrictions)
// 
//		Final Key Output Example:
//			06197-OEM-0014907-15227
// 
// -------------------------------------------------------------------------------------------------------------------------------------

// Import Pool

#include <iostream>    // Importing C++ Libary Handling Input/Output Streams (User-Inputs, Display Print-Outs, etc)
#include <random>	   // Importing C++ Random Generation Engine for Random Number Generation
#include <string>      // Importing C++ String Library for Handling (Splicing, Concats, etc) & Type-Conversions
#include <sstream>	   // Importing C++ Streaming String Library for More Advanced Functions (String-Augmentation with Concatenation, etc)
#include <iomanip>	


// Defining the Main Function

int main() {


	// Initializing the Random Generation Engine (Hardware Device)
	std::random_device rd;			// Instantiating the Random Engine as 'rd'
	std::mt19937 gen(rd());				// Calling the Random Engine for Generation


	// Instantiating Distribution Ranges for Use with Random Generation Engine
	std::uniform_int_distribution<> day_dist(1, 365);			// Distribution for the Day-Values (Between 001 & 365)
	std::uniform_int_distribution<> yr_dist(1995, 2002);		// Distribution for the Year-Values (1995 = Release | 2002 = End of Life)
	std::uniform_int_distribution<> x_dist(0, 9);				// Distribution for the 'x' section of digits 
	std::uniform_int_distribution<> z_dist(11111, 99999);       // Distribution for the 'z' section of digits

	// Initializing StringStream Variable as 'ss'
	std::stringstream ss;


	// Generating the Day-Values Section for CD-Key (ddd)

	int day_rng = day_dist(gen);						// Randomly Generating the Day-Values for the Key using Day-Values Distribution (001 - 365)
	std::string day_str = std::to_string(day_rng);		// Type-Converting the Generated Day-Value from Integer to String 

	if (day_str.length() < 3) {							// If-Statement Catches the Length of the Generated Day Value for Zeros-Padding

		if (day_str.length() < 2) {                     // Another If-Statement Catches if Generated Day-Value is Single-Digit
			day_str = "00" + day_str;					// Single-Digit Found -- Padding with '00' (e.g.:  4 --> 004)
		}

		else {											// Else Statement Handles Double-Digits Filtering
			day_str = "0" + day_str;                    // Double-Digit Found -- Padding with '0' (e.g.:   14 --> 014)
		}
	}



	// Generating the Year-Values Section for CD-key (yy)

	int yr_rng = yr_dist(gen);							// Randomly Generating the Year-Values for Key using Year-Value Distribution (1995-2002)
	std::string yr_str = std::to_string(yr_rng);		// Type-Converting the Generated Year-Value from Integer to String
	yr_str = yr_str.substr(2);				// Splicing Out the Last Two Digits of the Year (e.g,: 1995 --> 95)

	std::string key_p1 = day_str + yr_str + "-OEM-";		// Assembling the First Part of the Windows 95 Key (dddyy-OEM)



	// Creating the 'x' Section Values for CD-Key ('-xxxxxxx-') --- MUST MEET VALID CONDITIONS!


	int dig_2;		// Declaring the X-Section Digit Variables Pre-Loop
	int dig_3;
	int dig_4;
	int dig_5;
	int dig_6;
	int dig_last;

	int div_chk = 1;				// Initialized Value for MOD-7 Check Conditions 
	while (div_chk % 7 != 0) {		// While-Loop Generates Keys Until Valid-Conditions are Satisfied


		// Generating the Middle Part of 'x' Section (x#####x)

		dig_2 = x_dist(gen);				// Randomly Generated Number for 2nd Digit Position in 'x' Section of CD-Key (e.g. - 0#xxxxx)
		dig_3 = x_dist(gen);				// Randomly Generated Number for 3rd Digit Position in 'x' Section of CD-Key (e.g. - 0x#xxxx)
		dig_4 = x_dist(gen);				// Randomly Generated Number for 4th Digit Position in 'x' Section of CD-kEy (e.g. - 0xx#xxx)
		dig_5 = x_dist(gen);				// Randomly Generated Nunber for 5th Digit Position in 'x' Section of CD-Key (e.g. - 0xxx#xx)
		dig_6 = x_dist(gen);				// Randomly Generated Number for 6th Digit Position in 'x' Section of CD-Key (e.g. - 0xxxx#x)


		// Randomly Generated Number for Final Digit Position in 'x' Section of CD-Key (e.g. - 0xxxxx#)
		dig_last = x_dist(gen);				

		while (dig_last == 0 || dig_last == 8 || dig_last == 9) {	// While-Condition Catches if the Final Digit RNG is 0, 8, 9 (Not Allowed)

			dig_last = x_dist(gen);									// Re-Generates the Final Digit Position until a Value other than 0, 8, 9 is Met
		}

		// MOD-7 Division Check -- Must be EVENLY Divisible by 7 After Summing -- Program Continues After Validation
		div_chk = (0 + dig_2 + dig_3 + dig_4 + dig_5 + dig_6 + dig_last);

		
		// If the Division-Check Passes (Evenly-Divisible by 7)
		if (div_chk % 7 == 0) {

			ss << '0' << dig_2 << dig_3 << dig_4 << dig_5 << dig_6 << dig_last;  // All the Generated Digits are Bucketed into StringStream (It collects Data regardless of type)
		}
	}
	std::string x_section = ss.str();								// The StringStream Bucket Holding Data Elements Are Converted to Single-String

	


	// Creating the 'z' Section of Values in Windows 95 CD-Key (Values Have No Restriction)

	int z_digits = z_dist(gen);										// Randomly Generating the 'z' Section of Digits in the Windows 95 Key (11111-99999)
	std::string z_section = std::to_string(z_digits);				// Generated Number is Type-Converted from Integer to String
	

	// Assembling the Windows 95 Key 
	std::string cd_key = key_p1 + x_section + "-" + z_section;      // Windows 95 Key is Generated (dddyy-OEM-xxxxxxx-zzzzz)


	std::cout << "Windows 95 Key: " << cd_key;						// Generated Key is Displayed to User
	std::cout << "\nPress Any Key to Quit Program...";				// Letting the User Know the Next Step
	std::cin.get();													// Program is Halted Here and Waits for User-Input to Terminate

	return 0;														// Program Terminates | return 0 = Successful 

}