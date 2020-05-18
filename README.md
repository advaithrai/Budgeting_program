# Budgeting_program
Python folder to run my yearly and monthly expenses. Free-to-use

Hello hello, this is the Python script I made to take care of my own expenses for next year and for years to come hopefully. It was more trouble
than its worth and it took more time to debug than I expected, but here it is. It's not perfect, and it may still be a bit buggy, especially in
terms of error handling, so if you're using it for your own needs, there may be times where it freaks out. For the most part, your previous submissions should be saved,
so you may just need to restart the program to get back your data. If you see a problem, you can always email me here: advaith_rai@yahoo.com, and I'll debug it and update the
Git repo for everybody.

I know its ugly, but it works. I wasn't going to spend another 8 hours on it, but if 
somebody wants to build a GUI for it, go ahead and send me what you
have when you're done, lol.

Here's what I'm going to go over
--------------------------------
1. How it Works
2. Changes You May Have to Make
3. Contact Info and Final Statements


How it works:

Essentially, the program runs an Annual_budget class, which holds all 
of the data for a list of Month_budget classes.
You can create a new budget, or continue an old budget, just by choosing the
corresponding choice in the startup menu. To run the program, run the 'main.py'
file, but you will need the 'annual_budget.py' and 'monthly_budget.py' in the same folder

The program reads the data into a text file in the same folder as the python script to hold it while the program isn't running.
There isn't a whole lot of data, so I didn't think it was necessary to make a whole database for it. When the program starts up again,
 you can choose to read that data back into the program. NOTE: The text file data is pretty simple, BUT the formatting
 is pretty strict, so I don't recommend messing with it unless you want to screw up your data.

The only real inputs the program will expect of you will be:

    Names - Sometimes you will have to name things (Months, budgets, etc.), These can be whatever you want them to be
    Money - A lot of the program will ask for dollar amounts, feel free to add decimals or integers, but please no commas or dollar signs
    Choices - The menu's in this program will ask for a number (ex. 1-6). Please enter the number, not the phrase to select an option
    Y/N - These true or false statements will often ask for confirmation. They are not case-sensitive, but enter "Y/N" or "y/n" to answer



Changes You May Have to Make:

    1. The program is optimized for my needs specifically, so it takes an annual income, taxes it, and spreads it across the number of months you
    want the budget to be. If you need something that just adds in monthly income, you can choose to do so by creating an arbitrary annual income,
    then adjusting the actual monthly income as you see fit. Or, it might be easier just to rewrite the program to take in a default monthly income
    instead.

    2. TAXES: For these I used a function that estimates taxes by Federal Income Brackets of 2020. Obviously, taxes are a but more complicated, so you can
    adjust the code to forego this entirely and add your own estimated taxed income instead. ALSO, this program was made in Texas, which doesn't have
    a state tax, so you also may need to figure that out if you're in a different state.


Contact Info and Final Statements:

    Consider this program free-to-use and to modify for the general public, although if you sell or distribute this program script or any
     modified version of this script, for profit it's still legally considered my personal property.

    Besides that, use it however you want, make any changes that make the program easier for you to use. If you think you know a better way to design
    this, some more useful functionality, or you've got some changes you'd like to make, go ahead and send it to me, because I'd love to use it too.

    Contact me here: advaith_rai@yahoo.com
    My GitHub: github.com/advaithrai
