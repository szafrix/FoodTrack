# Objective:

Verify if LLMs are able to correctly estimate calories and nutrients if they are given a name of the product and the quantity eaten.

## Analysis outline

1) Download a set of products from Open Food Facts along with their nutrient information.

To make the analysis as complete as possible, I'll stratify the products used for comparison by collecting equal amount of products (30) from the following categories:

1. Raw Ingredients:
   1. Apples 2000000151184
   2. Bananas 95159331
   3. Oranges
   4. Strawberries
   5. Blueberries
   6. Carrots
   7. Broccoli 8033803726749
   8. Spinach 5054781512257
   9. Kale 0077890260456
   10. Tomatoes 20930769
   11. Cucumbers 4088600352725
   12. Bell peppers
   13. Onions
   14. Garlic 3770013085024
   15. Potatoes 3276559054390
   16. Sweet potatoes
   17. Almonds 4088600441689
   18. Walnuts
   19. Cashews
   20. Peanuts
   21. Sunflower seeds 2200280444206
   22. Pumpkin seeds
   23. Chia seeds
   24. Quinoa
   25. Brown rice 4088600511467
   26. Lentils 5018095011271
   27. Chickpeas
   28. Black beans
   29. Kidney beans 20166090
   30. Oats

2. Minimally Processed Foods:
   1. Whole milk 5000436589341
   2. Skim milk 9300639400013
   3. Greek yogurt 5201054017432
   4. Plain yogurt
   5. Cheddar cheese 5000295142893
   6. Mozzarella cheese 3263859406820
   7. Cottage cheese 8480000609632
   8. Butter 5740900404465
   9. Eggs 20057251
   10. Egg whites
   11. Chicken breast 3302740059186
   12. Ground beef 3661112092108
   13. Salmon fillet 20668518
   14. Tuna steak
   15. Pork chops
   16. Turkey breast 4056489320180
   17. Lamb chops
   18. Tofu 5034467000223
   19. Tempeh 5034467000872
   20. Seitan 3229820796642
   21. Honey
   22. Maple syrup 20760069
   23. Agave nectar 5060069170033
   24. Coconut oil
   25. Olive oil 4056489141877
   26. Avocado oil
   27. Ghee
   28. Almond milk
   29. Soy milk
   30. Coconut milk

3. Basic Processed Foods:
   1. Whole wheat bread 0072250037129
   2. White bread
   3. Rye bread
   4. Sourdough bread 5025125000112
   5. Bagels
   6. English muffins
   7. Pita bread
   8. Tortillas 4056489506829
   9. Spaghetti 8076800195057
   10. Penne pasta
   11. Egg noodles
   12. Rice noodles 5020580019686
   13. Canned tomatoes 20004132
   14. Canned corn
   15. Canned green beans 20009847
   16. Canned peas 8480000331366
   17. Canned peaches
   18. Canned pineapple 20253929
   19. Frozen peas
   20. Frozen corn
   21. Frozen broccoli
   22. Frozen spinach 3599741006329
   23. Frozen mixed vegetables 3083681105247
   24. Frozen berries
   25. Frozen mango
   26. Tomato sauce
   27. Applesauce
   28. Peanut butter 20474478
   29. Almond butter
   30. Jam 20114671

4. Moderately Processed Foods:
   1. Corn flakes 5059319014814
   2. Bran flakes
   3. Oatmeal 0705599014147
   4. Granola
   5. Potato chips 5941000025639
   6. Tortilla chips
   7. Pretzels 3245414021068
   8. Popcorn
   9. Crackers
   10. Rice cakes
   11. Ketchup 8715700017006
   12. Mustard
   13. Mayonnaise 8722700479475
   14. BBQ sauce
   15. Soy sauce 8715035110106
   16. Hot sauce
   17. Salad dressing
   18. Ham
   19. Bacon 3449865302664
   20. Salami
   21. Pepperoni 5054775296774
   22. Sausages
   23. Deli turkey
   24. Deli chicken
   25. Canned soup 
   26. Instant noodles 8852018101024
   27. Frozen vegetables with sauce
   28. Flavored yogurt
   29. Flavored milk
   30. Fruit snacks

5. Highly Processed Foods:
   1. Frozen pizza 4056489451136
   2. TV dinners
   3. Chicken nuggets 20621650
   4. Fish sticks 3276170011185
   5. Frozen burritos
   6. Instant mac and cheese 0021000658831
   7. Canned ravioli 3038352880305
   8. Packaged cookies
   9. Packaged cakes
   10. Donuts 3178530412697
   11. Chocolate bars 3046920022651
   12. Candy bars
   13. Gummy candies
   14. Ice cream 8711327373105
   15. Frozen yogurt
   16. Popsicles
   17. Potato chips (flavored)
   18. Cheese puffs
   19. Microwave popcorn 8714601010895
   20. Breakfast pastries
   21. Fruit roll-ups
   22. Pudding cups
   23. Jell-O 7622300471811
   24. Instant mashed potatoes
   25. Boxed cake mix
   26. Boxed brownie mix
   27. Artificial sweeteners
   28. Margarine 3155251205296
   29. Processed cheese slices
   30. Canned cheese sauce

6. Specialty Foods:
   1. Whey protein powder 5060469988566
   2. Casein protein powder
   3. Soy protein powder
   4. Pea protein powder
   5. BCAA supplements
   6. Creatine supplements
   7. Pre-workout supplements
   8. Protein bars 20035525
   9. Energy gels
   10. Electrolyte drinks
   11. Beyond Meat burger 0850004207390
   12. Impossible burger
   13. Veggie burgers
   14. Tofu hot dogs
   15. Seitan chicken
   16. Vegan cheese 5202390015878
   17. Gluten-free bread
   18. Gluten-free pasta
   19. Gluten-free crackers
   20. Gluten-free cookies
   21. Lactose-free milk
   22. Sugar-free candy
   23. Keto bread 0073410957790
   24. Keto snacks
   25. Low-carb tortillas
   26. Meal replacement shakes
   27. Vitamin gummies
   28. Probiotic supplements
   29. Omega-3 supplements
   30. Multivitamin tablets

7. Beverages:
   1. Bottled water
   2. Sparkling water
   3. Cola 5449000214911
   4. Lemon-lime soda
   5. Root beer 07818707
   6. Orange soda 5056025440432
   7. Energy drinks 7090008099048
   8. Sports drinks
   9. Iced tea
   10. Hot tea
   11. Coffee
   12. Espresso
   13. Cappuccino
   14. Latte
   15. Orange juice
   16. Apple juice 20569105
   17. Grape juice
   18. Cranberry juice 0031200452009
   19. Tomato juice
   20. Vegetable juice
   21. Smoothies
   22. Lemonade 8002270576829
   23. Coconut water
   24. Kombucha
   25. Beer
   26. Wine
   27. Vodka
   28. Whiskey
   29. Rum
   30. Gin

8. Composite Dishes:
   1. Caesar salad
   2. Greek salad
   3. Cobb salad
   4. Pasta salad
   5. Potato salad
   6. Club sandwich
   7. BLT sandwich 4388844252233
   8. Grilled cheese sandwich
   9. Tuna salad sandwich
   10. Peanut butter and jelly sandwich
   11. Cheese pizza
   12. Pepperoni pizza 8410762220585
   13. Vegetable pizza
   14. Supreme pizza
   15. Chicken noodle soup
   16. Tomato soup 5000157062673
   17. Minestrone soup
   18. Clam chowder
   19. Beef stew 20289201
   20. Chicken stir-fry
   21. Beef and broccoli
   22. Spaghetti and meatballs
   23. Lasagna 8410173072025
   24. Macaroni and cheese
   25. Chili con carne 8480000231376
   26. Beef burrito 00131704
   27. Chicken fajitas
   28. Vegetable curry
   29. Pad Thai 3456700231355
   30. Fried rice
