'''
John Carter
Created: 2021/07/03 19:13:07
Last modified: 2021/07/03 22:07:21
Save blog posts in JSON format to be called by app
'''

from pathlib import Path
import json

BLOG_FILE = Path('website/blogs.json').absolute()

blogs = {
    "mcloons": {
        "id": 3,
        "user": "John Carter",
        "title": "Mcloons Lobster Shack",
        "date": "25 August 2017",
        "photo": "mcloons_lobster_roll.jpg",
        "body": "Mcloons is the place that I look forward to going to most whenever I’m in Maine \
        (at least food-wise).  Its located in a beautiful spot on Spruce Head Harbor that \
        is very picturesque spot for sunsets.  Given their remote location, they are able \
        to pull up the lobsters from the ocean before your eyes to prepare them, which \
        means that they are extremely fresh and have incredible taste.  The lobster is \
        so tender it melts in your mouth (which is why I get a lobster roll 50% of the \
        time).  If you are planning to go this route with your meal, spring for the \
        “rolls royce”…. you won’t regret the extra meat.  As for the other 50% of the \
        time, one of my other favorites there are their crab cakes.   I don’t mind saying \
        that I have never had a better tasting crab cake in any seafood restaurant, and \
        they are the perfect size.\n \
        If these examples don’t have your mouth watering, then you need to have their \
        blueberry pie for an extra tasty dessert.  They serve you the perfect sliver of \
        warm blueberry pie with a scoop of french vanilla ice cream (one of the best \
        combos ever).  If you don’t think it’ll be as good as I am describing, notice \
        below that I didn’t include a photo of it (I was so excited to eat it that I \
        neglected to take a photo before wolfing it down.\n \
        When I went home with my mom following vacation, we started to have separation \
        anxiety so we discovered that you can order their food from anywhere and they \
        will ship it to you!  This is a perfect option for someone who is unable to get \
        to Maine as much as they wish they could.\n \
        Only downside: they close at 7pm, so make sure you remember you’re in Maine \
        before you drive there hungry at 7:30pm."
    },
    "cliff_house": {
        "id": 4,
        "user": "John Carter",
        "title": "The Cliff House",
        "date": "5 September 2019",
        "photo": "cliff_house.jpg",
        "body": "If you want to have a pleasant traveling experience in San Francisco, \
            let me offer you a piece of advice: AVOID THE CLIFF HOUSE RESTAURANT AT ALL \
                COSTS!\n \
        Now that I have my dramatic warning out of the way, let me explain my story.\
        I was traveling with my parents this fall throughout the United States on a \
        road trip to pick up some antique car parts. While driving up the Pacific Coast\
        Highway my mom decided to look for a nice seafood restaurant in San \
        Francisco and stumbled upon a listing for the Cliff House, a historic seafood \
        establishment that has been around since 1858. Many of the reviews discussing \
        the food quality seemed positive, and she didn’t see any of the reviews about \
        people’s cars being robbed at first glance.\n \
        We got there around 8pm or so and parked directly outside of the restaurant \
        under a streetlight, and we noticed a valet standing outside of the restaurant\
        as well. We went inside and were seated with no warnings about what could \
        (and would likely, as you’ll see soon) take place outside while we were dining. \
        After having a pretty nice meal (and dropping a cool $200 for only 3 people \
        to eat) we walked outside to find our car broken into (see photos below). \
        Thieves had absconded with my whole backpack, which had contained my $4000 \
        MacBook Pro, along with some other things worth some money too. While I \
        concede it was foolish to leave such an expensive machine in the car, it was \
        in the backpack, fully zipped, on the floor, with a blanket obscuring the \
        whole bag. So, while the thieves made off with some nice loot, there was no \
        way for them to know it was in the car before they broke in. It seems much \
        more likely that someone had watched us pull up (remember the valet standing\
        idly outside?), noticed our out-of-state tags, and called a band of thugs \
        who routinely rob from patrons of the restaurant to see what they could \
        take this time. Now, I say “routinely” in a very serious and realistic sense. \
        When we went back into the restaurant to speak to the management about seeing \
        the security tapes so we could have a better idea of the exact turn of events,\
        we were told that they “didn’t have the key” to access where the security \
        system was, and we’d have to wait for another day when someone would come \
        let us in to see them (I guess some unknown person has a key?). I explained \
        that we were leaving San Francisco that night and had a tight schedule to \
        make it home. To this they basically just said “well I guess you’re out of\
        luck.” They couldn’t even muster up a “sorry” for one of their customers \
        that just lost thousands of dollars for no reason except dining in their \
        restaurant. The only valuable information they could provide was that this \
        sort of thing “happens 15 times a day.” 15 times a day? Surely that must be \
        hyperbole. But no, even the police confirmed that much. Now you know why I \
        said “routinely.”\n \
        How a business that charges too much money for their food and has their \
        patrons stolen from 15 times a day stays in business I’ll never know. \
        Perhaps they are kept afloat by innocent (and apparently foolish) patrons \
        like us, but they’ll only get money from people like us once. You can be \
        sure they’ll never get another dime from me, and I hope not from anyone \
        who reads this blog either. So, please do yourself a favor, and when you \
        see the Cliff House, don’t be tempted to stop and eat. Just keep on going.\n \
        P.S.: I tried to include a link to their website, but it wouldn’t even load. \
        So if you want more info, take a look at their Wikipedia page."
    },
    "hills": {
        "id": 1,
        "user": "John Carter",
        "title": "Hill's Seafood Co.",
        "date": "1 June 2017",
        "photo": "mydinnerhills.jpg",
        "body": "A new(ish) seafood place that is worth checking out in midcoast Maine \
        is Hill’s Seafood Co in Rockland, Maine.  Less than a mile off of US Route 1, \
        the restaurant is a small venue with a large outside deck that has great view \
        of the picturesque Rockland Harbor, especially in the summer months when the \
        harbor has beautiful sunsets.  It is also situated in a prime location during \
        the times that Rockland hosts the Lobster Festival and the Maine Boats, Homes, \
        and Harbors Show in the late summer. \
        or an appetizer we got the very basic but tasty popcorn chicken topped with \
        barbecue sauce with a side of ranch dressing.  This was enough to whet our \
        appetites for our entrees.  For mine, I ordered the Lobster Mac ‘n’ Cheese \
        (one of my favorites at many restaurants in Maine), which was a simple dish \
        served with a side of broccoli and coleslaw.  You could tell that the lobster \
        was fresh and had plenty of large chunks of meat, and the actual Mac ‘n’ \
        Cheese was also good.  Side note: the broccoli may have been the best broccoli \
        I have ever eaten at a restaurant.  My dad ordered the Cajun Parmesan Haddock \
        which also had a tremendous taste (I tried some), and was served with the usual \
        fries and coleslaw.  As much as I wanted to try their dessert options, after \
        having the appetizer and finishing the entree, I found myself not having enough \
        room to try any of their desserts.  Definitely a place I would recommend.  \
        Here is a link to their website (complete with photos of the view from the deck)."
    },
    "peter_otts": {
        "id": 2,
        "user": "John Carter",
        "title": "Peter Ott's On The Water",
        "date": "5 June 2017",
        "photo": "lobster_roll_peter_otts.jpg",
        "body": "After traveling to Maine in the morning and having to do some \
        housework upon our arrival, my father and I were eager to not have to \
        cook dinner and go out to eat.  And since I enjoy taking pictures of some \
        of Maine’s prettier spots, many times I’ll suggest we go up to Camden, Maine \
        to get dinner because there are a few great restaurants on the Camden Harbor. \
        Last night we decided to go to Peter Ott’s on the harbor, which is a restaurant \
        that has been in its location since before I was born, but has since changed \
        hands a few times in the recent past.  Its most recent incarnation is that of \
        Peter Ott’s, which has a reputation for having an excellent menu, but also has \
        prices sometimes too steep even for those who don’t mind spending the money for \
        a great meal.  For an appetizer, we decided to order the crab cakes which had \
        an excellent sauce draped over two small crab cakes, with a small arugula salad \
        on the side.  The flavor was excellent.  Then, for dinner I ordered the classic \
        Maine lobster roll, which had the taste I was expecting, but not the price as it \
        was $22 for a small lobster roll and a little container of fries (see picture \
        below).  My father ordered the broiled haddock, which was a substantial piece \
        of meat with mashed potatoes and again, another excellent sauce on top of the \
        fish.  Here is a link to the dinner menu.  To cap off this great tasting meal, \
        I ordered the chocolate mousse for dessert.  I was surprised at its size, as it \
        was big enough for me to not want to finish it even though its taste was superb \
        and the raspberry sauce made it even better.  And even more than the taste of \
        the food, the background of the harbor at sunset made the meal seem even \
        greater.  A theme whose importance is paramount in these Maine restaurants \
        would be “location location location.”  Altogether even though the bill for \
        two people to eat dinner was almost appalling, the dinner was great and the \
        scenery even better.  Check out the photos below if you don’t believe me. "
    }
}

with open(BLOG_FILE, 'w') as json_file:
    json.dump(blogs, json_file)