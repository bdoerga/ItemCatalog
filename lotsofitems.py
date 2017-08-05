from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Category, Base, Item, User

engine = create_engine('sqlite:///itemcatalogwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine


DBSession = sessionmaker(bind=engine)

# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Category for Shells
category1 = Category(name="Shell")
session.add(category1)
session.commit()

# Shell Items
item1 = Item(user_id=1, name="Green Shell", description="When thrown, this shell travels in a straight line and knocks over the first Kart it hits.", category=category1)
session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Red Shell", description="These automatically lock onto and chase after the next Kart in front of you. When hit, the Kart rolls over.", category=category1)
session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Spiny Shell", description="A blue-winged spiky Koopa shell. It chases the leader and and releases a blue Bob-omb-like explosion upon contact.", category=category1)
session.add(item3)
session.commit()

# Category for Mushrooms
category2 = Category(name="Mushroom")
session.add(category2)
session.commit()

# Mushroom items
item4 = Item(user_id=1, name="Mushroom", description="Provides a short speed boost.", category=category2)
session.add(item4)
session.commit()

item5 = Item(user_id=1, name="Triple Mushroom", description="Provides 3 mushrooms for 3 short speed boosts.", category=category2)
session.add(item5)
session.commit()

item6 = Item(user_id=1, name="Golden Mushroom", description="Allows you to use Mushroom boosts as many times as you want for a short period of time", category=category2)
session.add(item6)
session.commit()

#Category for Power-Ups
category3 = Category(name="Power-Up")
session.add(category3)
session.commit()

# Power-up items
item7 = Item(user_id=1, name="Starman", description="These stars make the player invincible.", category=category3)
session.add(item7)
session.commit()

item8 = Item(user_id=1, name="Fire Flower", description="Allows you to throw fireballs that cause other Karts to spin out of control on impact.", category=category3)
session.add(item8)
session.commit()

item9 = Item(user_id=1, name="Boomerang Flower", description="Shoots three Boomerangs to attack other racers.", category=category3)
session.add(item9)
session.commit()

print "added user, categories and items!"
