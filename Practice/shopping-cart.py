def shopping_cart(*args, **kwargs):
    print("Shopping Cart:")

    # item_num = 0
    # for arg in args:
    #     item_num += 1
    #     print(f"{item_num}. {arg}")

    for item_num, product in enumerate(args, start=1):
        print(f"{item_num}. {product}")

    print("\nCustomer Details:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

    print(f"\nTotal items: {len(args)}")

shopping_cart(
    "Laptop",
    "Mouse",
    "Keyboard",
    name="Sarah",
    location="Lagos",
    payment="Card"
)