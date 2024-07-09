def print_catalog(): 
    # Prices of individual items 
    item1_price = 200.0 
    item2_price = 400.0 
    item3_price = 600.0 
 
    # Calculating combo prices with discounts 
    combo1_price = (item1_price + item2_price) * 0.9  # 10% discount 
    combo2_price = (item2_price + item3_price) * 0.9  # 10% discount 
    combo3_price = (item1_price + item3_price) * 0.9  # 10% discount 
    gift_pack_price = (item1_price + item2_price + item3_price) * 0.75  # 25% discount 
 
    # Printing the catalog 
    print("Online Store") 
    print("-----------------------------") 
    print(f"{'Product(s)':<25} {'Price':>10}") 
    print(f"{'-'*35}") 
    print(f"{'Item 1':<25} {item1_price:>10.2f}") 
    print(f"{'Item 2':<25} {item2_price:>10.2f}") 
    print(f"{'Item 3':<25} {item3_price:>10.2f}") 
    print(f"{'Combo 1 (Item 1 + 2)':<25} {combo1_price:>10.2f}") 
    print(f"{'Combo 2 (Item 2 + 3)':<25} {combo2_price:>10.2f}") 
    print(f"{'Combo 3 (Item 1 + 3)':<25} {combo3_price:>10.2f}") 
    print(f"{'Combo 4 (Item 1 + 2 + 3)':<25} {gift_pack_price:>10.2f}") 
    print(f"{'-'*35}") 
    print("For delivery Contact: 98764678899") 
 
# Calling the function to print the catalog 
print_catalog() 
