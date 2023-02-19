# Exercise: Classes and Objects
## 1.	Storage
Create a class Storage. The __init__ method should accept one parameter - the capacity of the storage. The Storage class should also have an attribute called storage - empty list, where all the items will be stored. 
The class should have two additional methods:
*	add_product(product: str) - adds the product in the storage if there is enough space for it
*	get_products() - returns the storage list
#### Example

| Test Code | Output |
| --------- | ------ |
| storage = Storage(4)<br />storage.add_product("apple")<br />storage.add_product("banana")<br />storage.add_product("potato")<br />storage.add_product("tomato")<br />storage.add_product("bread")<br />print(storage.get_products()) | ["apple", "banana", "potato", "tomato"] |

## 2.	Weapon
Create a class Weapon. The __init__ method should receive a number of bullets (integer). Create an attribute called bullets to store that number. The class should also have the following methods:
*	shoot()
    *	If there are bullets in the weapon, reduce them by 1 and return a message "shooting..."
    *	If there are no bullets left, return: "no bullets left"
*	__repr__()
    *	Returns "Remaining bullets: {amount_of_bullets}"
    *	You can read more about the method here: link
#### Example

| Test Code | Output |
| --------- | ------ |
| weapon = Weapon(5)<br />print(weapon.shoot())<br />print(weapon.shoot())<br />print(weapon)<br />print(weapon.shoot())<br />print(weapon.shoot())<br />print(weapon.shoot())<br />print(weapon.shoot())<br />print(weapon) | shooting...<br />shooting...<br />Remaining bullets: 3<br />shooting...<br />shooting...<br />shooting...<br />no bullets left<br />Remaining bullets: 0 |

## 3.	Catalogue
Create a class Catalogue. The __init__ method should accept the name of the catalogue (string). Each catalogue should also have an attribute called products, an empty list. The class should also have three more methods:
*	add_product(product_name: str) - adds the product to the products' list
*	get_by_letter(first_letter: str) - returns a list containing only the products that start with the given letter
*	__repr__ - returns the catalogue info in the following format: 
"Items in the {name} catalogue:
{item1}
{item2}
…
{itemN}"
The items should be sorted alphabetically in ascending order.
#### Example

| Test Code | Output |
| --------- | ------ |
| catalogue = Catalogue("Furniture")<br />catalogue.add_product("Sofa")<br />catalogue.add_product("Mirror")<br />catalogue.add_product("Desk")<br />catalogue.add_product("Chair")<br />catalogue.add_product("Carpet")<br />print(catalogue.get_by_letter("C"))<br />print(catalogue) | ["Chair", "Carpet"]<br />Items in the Furniture catalogue:<br />Carpet<br />Chair<br />Desk<br />Mirror<br />Sofa |

## 4.	Town
Create a class Town. The __init__ method should receive the name of the town (string). Each town has a latitude - "0°N" upon initialization and a longitude - "0°E" upon initialization. It should also have 3 more methods:
*	set_latitude(latitude) - sets an latitude
*	set_longitude(longitude) - sets an longitude
*	__repr__ - returns a representation of the object in the following string format:
"Town: {name} | Latitude: {latitude} | Longitude: {longitude}"
#### Example

| Test Code | Output |
| --------- | ------ |
| town = Town("Sofia")<br />town.set_latitude("42° 41\' 51.04\" N")<br />town.set_longitude("23° 19\' 26.94\" E")<br />print(town) | Town: Sofia | Latitude: 42° 41' 51.04" N | Longitude: 23° 19' 26.94" E |

