print('Welcome to your hotel \"THE TASTE\"')
user_choise = input('Enter your choice of Meal(Veg:v, Nonveg:n): ')

match(user_choise.lower()):
    case 'v' : 
        print('VEG Menu \n 1:Dosa 2:Idli-Vada 3:Mangalore-Buns 4:Chitranna')
        item_choice = int(input('Enter your choice (1-4): '))

        match(item_choice):
            case 1 : print('Davanagere Benne Dosa')
            case 2 : print('Tasty Mallige Idli')
            case 3 : print('Mangaluru Special Sweet Buns')
            case 4 : print('Spicy Masala Chitranna')
 
    case 'n' : 
        print('NONVEG Menu \n 1:Chicken-Biryani 2:Mutton-Pulav 3:Tale-Kaalu')
        item_choice = int(input('Enter your choise (1-3): '))

        match(item_choice):
            case 1 : print('Chicken Biryani')
            case 2 : print('Mutton Pulav')
            case 3 : print('Tale mamsa')
            case _ : print('Liver Fry')

print('Thank you! Visit Again')