from stream_it import db
from stream_it.models import *

def get_series_id(s_name):
    return Series.query.filter(Series.name==s_name).first().id

# db.drop_all()
# db.create_all()

# desci = "The story follows Light Yagami, a teen genius who discovers a mysterious notebook: the 'Death Note', which belonged to the Shinigami Ryuk, and grants the user the supernatural ability to kill anyone whose name is written in its pages."
# new_series = Series(name="Death Note",desc=desci)
# db.session.add(new_series)

# desci = "The plot of Attack on Titan centers on a civilization inside three walls, the last location where humans still live. Over one hundred years ago, humanity was driven to the brink of extinction after the emergence of humanoid giants called Titans, who attack and eat humans on sight. The last remnants of humanity retreated behind three concentric walls and enjoyed nearly a century of peace."
# new_series = Series(name="Attack on Titan",desc=desci)
# db.session.add(new_series)

ser_id =  get_series_id("Attack on Titan")

desci = "The story follows the adventures of Eren Jaeger, his childhood friends Mikasa Ackerman and Armin Arlert, whose lives are changed forever after a Colossal Titan breaches the wall of their home town. Vowing revenge and to reclaim the world from the Titans, Eren and his friends join the Scout Regiment, an elite group of soldiers who fight Titans."
new_season = Seasons(number=1,desc=desci,Series_id=ser_id)
db.session.add(new_season)

desci = "The season follows Eren Jaeger and his friends from the 104th Training Corps who have just begun to become full members of the Survey Corps. After fighting the Female Titan, Eren finds no time to rest as a horde of Titans is approaching Wall Rose and the battle for humanity continues. As the Survey Corps races to save the wall, they uncover more about the invading Titans and the dark secrets of their own members."
new_season = Seasons(number=2,desc=desci,Series_id=ser_id)
db.session.add(new_season)

desci = "The season follows Eren and his fellow soldiers from the Survey Corps who are still fighting for their survival against the terrifying Titans. However, threats arise not only from the Titans beyond the walls, but from the humans within them as well. After being rescued from the Colossal and Armored Titans, all seems well for the soldiers, until the government suddenly demands custody of Eren and Historia."
new_season = Seasons(number=3,desc=desci,Series_id=ser_id)
db.session.add(new_season)

desci = "The season follows Gabi Braun and Falco Grice, young Eldian Warrior candidates seeking to inherit Reiner's Armored Titan four years after the failed mission to claim the Founding Titan. Marley plans to invade Paradis to strengthen their weakening military and recover the Founding Titan. With the Survey Corps on the Marley shoreline, Gabi, Falco, Reiner, and other Titans go to war with the Paradis soldiers as Eren Jaeger reveals his new plan of attack on the Marleyan invaders: annihilation"
new_season = Seasons(number=4,desc=desci,Series_id=ser_id)
db.session.add(new_season)


db.session.commit()