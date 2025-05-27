weather_advice = input("What's the weather like today? (sunny/rainy/cold): ").lower()
if weather_advice == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather_advice == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather_advice == "cold":
    print("Make sure to wear a warm coat and a scarf")
else:
    print("Sorry, i don't have recommendations for this weather.")
