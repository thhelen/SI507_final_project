from PIL import Image
print('Welcome!')
print('This project aims to produce visualizations of the data obtained from Spotify and Billboard over a number of decades')
while True:
    print('Please choose a visualization you would like to see:')
    print('1. Correlation between various features of songs')
    print('2. Visualizing which characteristics of songs affect their popularity over different time periods')
    print('3. Analyze how features have varied popularity over a period of time\n')
    while True:
        in1_input = input('Option: ')
        if in1_input.isdigit():
            in1 = int(in1_input)
            if in1 >= 1 and in1 <= 3:
                break
            else:
                print('Invalid option. Please enter a value from 1-3.')
        else:
            print('Invalid input. Please enter a number.')
    if in1==1:
        image = Image.open("C:/Users/thhelen/Desktop/si507_lec/hw/correlation_heatmap.png")
        image.show()
    elif in1==2:
        print('1. Do you want a visualization based on the spotify data of popularity?')
        print('2. Do you want a visualization based on the Billboard data of popularity?')
        while True:
            user_input = input("Please enter 1 or 2: ")
            if user_input.isdigit():
                in2 = int(user_input)
                if in2 >= 1 and in2 <= 2:
                    break
                else:
                    print('Invalid option. Please enter a value 1 or 2.')
            else:
                print('Invalid input. Please enter a number.')
        if in2==1:
            print('Please choose depth of tree from 1-10. Depth = 2 is optimal.')
            while True:
                depth_input = input('Depth: ')
                if depth_input.isdigit():
                    depth = int(depth_input)
                    if depth >= 1 and depth <= 10:
                        break
                    else:
                        print('Invalid depth. Please enter a value between 1 and 10.')
                else:
                    print('Invalid input. Please enter a number.')
            if depth!=2:
                image = Image.open(f"C:/Users/thhelen/Desktop/si507_lec/hw/tree_spotify_{depth}.png")
                image.show()
            else:
                image = Image.open(f"C:/Users/thhelen/Desktop/si507_lec/hw/optimal_spotify.png")
                image.show()
        else:
            print('Please choose depth of tree from 1-10. Depth = 4 is optimal.')
            while True:
                depth_input = input('Depth: ')
                if depth_input.isdigit():
                    depth = int(depth_input)
                    if depth >= 1 and depth <= 10:
                        break
                    else:
                        print('Invalid depth. Please enter a value between 1 and 10.')
                else:
                    print('Invalid input. Please enter a number.')
            if depth!=4:
                image = Image.open(f"C:/Users/thhelen/Desktop/si507_lec/hw/tree_BB_{depth}.png")
                image.show()
            else:
                image = Image.open(f"C:/Users/thhelen/Desktop/si507_lec/hw/optimal_BB.png")
                image.show()
    else:
        print('Which feature would you like to analyze: \n1. acousticness \n2. danceability \n3. energy \n4. tempo \n5. valence')
        while True:
            feature_input = input('Feature: ')
            if feature_input.isdigit():
                feature = int(feature_input)
                if feature >= 1 and feature <= 5:
                    break
                else:
                    print('Invalid feature. Please enter a value from 1-5.')
            else:
                print('Invalid input. Please enter a number.')
        if feature==1:
            image = Image.open(f"C:/Users/thhelen/Desktop/si507_lec/hw/acousticness_vs_popularity.png")
            image.show()
        elif feature==2:
            image = Image.open(f"C:/Users/thhelen/Desktop/si507_lec/hw/danceability_vs_popularity.png")
            image.show()
        elif feature==3:
            image = Image.open(f"C:/Users/thhelen/Desktop/si507_lec/hw/energy_vs_popularity.png")
            image.show()
        elif feature==4:
            image = Image.open(f"C:/Users/thhelen/Desktop/si507_lec/hw/tempo_vs_popularity.png")
            image.show()
        elif feature==5:
            image = Image.open(f"C:/Users/thhelen/Desktop/si507_lec/hw/valences_vs_popularity.png")
            image.show()
    print('Would you like to continue? Enter 1 if yes, 2 if no.')
    while True:
        in3_input = input('Option: ')
        if in3_input.isdigit():
            in3 = int(in3_input)
            if in3 >= 1 and in3 <= 2:
                break
            else:
                print('Invalid option. Please enter a value 1 or 2.')
        else:
            print('Invalid input. Please enter a number.')
    if in3 ==2:
        break
    else:
        print('Lets start over!')