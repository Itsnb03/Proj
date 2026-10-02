# # q1 print twinkle twinkle little star poem

# print(''' Twinkle, twinkle, little star,
# How I wonder what you are!
# Up above the world so high,
# Like a diamond in the sky.

# When the blazing sun is gone,
# When he nothing shines upon,
# Then you show your little light,
# Twinkle, twinkle, all the night.

# Then the traveller in the dark,
# Thanks you for your tiny spark,
# He could not see which way to go,
# If you did not twinkle so.

# In the dark blue sky you keep,
# And often through my curtains peep,
# For you never shut your eye,
# Till the sun is in the sky.

# 'Tis your bright and tiny spark,
# Lights the traveller in the dark:
# Tho' I know not what you are,
# Twinkle, twinkle, little star. 

# ''')

# num = 2
# num2 = 3

# print(num + num2)

class solution:
    def romanToInt(self, s: str) -> int:
        roman_numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total = 0
        prev_value = 0  