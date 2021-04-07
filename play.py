print("""This is a simple game made by a simple person
designed to simply test your attention to simple detail
and your simple ability to type. I hope you have fun
on your journey, and I shall see you at the end
(most likely in the form of credits).

If in the unfortunate event you wish to quit the game
prior to the end, please press CTRL + 'C' simultaneously.

WARNING: This simple game does not have a save feature.
I'm not that smart, yet.
""")

n = 1
while True:
	# option 1
	while n == 1:
		print("There are three doors: left, middle, right.")
		x = input("Please select one: ")
		if x == 'left':
			print("This door is jammed shut.")
		elif x == 'middle':
			print("This door is locked.")
		elif x == 'right':
			print("""\

The door opens.
Laid before you is a short, brick corridor with a
blazing torch hanging on a wall at the end.
The air is warm and humid, and you notice the
thick condensation that has formed on the walls.
""")
			n = 2 # moves to option 2
		else:
			print("Invalid Response")


	# option 2
	while n == 2:
		print("Please, choose an action: close door, move to torch")
		x = input('')
		if x == 'close door':
			print("""\

The door is shut.
""")
			n = 1 # moves back to option 1
		elif x == 'move to torch':
			print("""\

You teleport to the torch
(because walking isn't a thing in this game),
and you notice the corridor continues to the right.
Torches line the walls of the corridor lighting the
path forward.
""")
			n = 3 # moves to option 3
		else:
			print("Invalid Response")

	# option 3
	while n == 3:
		print("Please, choose an action: move back to door, continue through corridor")
		x = input('')
		if x == 'continue through corridor':
			print("""\

You decide to continue following the corridor
(utilizing the awesome powers of levetation)
until it leads you into a large room with a short,
circular stage in the center. A conical beam of
sunlight eminating from a hole built in the center
of the 50ft.-high ceiling (Idk what that is in
meters, and I'm too lazy to find out) decends onto
the stage illuminating a chest...a large chest in
the center. (Hopefully, the chest isn't fake.)
""")
			n = 4 # move to option 4
		elif x == 'move back to door':
			n = 2 # moves back to option 2
		else:
			print("Invalid Response")

	# option 4
	while n == 4:
		print("Please, choose an action: examine the room, inspect the chest")
		x = input('')
		if x == 'examine the room':
			print("""\
There isn't much else to notice in the room.
The chest continues to capture your attention.
At any moment, you expect to hear, "HEY!! Eyes
are up here!!", but instead, there's just silence.
""")
		elif x == 'inspect the chest':
			print("""\
You suddenly find yourself standing before
the chest (it's much bigger up close). You want
to touch it...you really want to touch it.
There's no lock; so, you decide to open it.
A loud "SNAP, CRACKLE, POP!!" eminates from
its hinges. You notice the seal of the chest
is lined with long, razer-sharp teeth. OH SHIT!!
You leap back just as the chest slams shut!
(I guess the chest was fake after all.)
You look back to notice the chest is standing
on two, spindley legs with two arms that look
like tree branches primed and ready to catch
its prey (you...that prey is you). A long,
slithery tongue snakes out of its mouth
looking for an angle of opportunity to taste
its potential meal.
""")
			n = 5
		else:
			print("Invalid Response")

	# option 5
	while n == 5:
		print("Please, choose an action: play dead, RUN!!, play Dark Souls")
		x = input('')
		if x == 'play dead':
			print("""\
Well, if it works for bears, then it might
work for this thing. You lay back down and
remain completely motionless making your
best impression of a dead person. You hear
the thudding of the creature's footsteps
as it steadily approaches you. As it nears,
a shadow is cast over your apparent
motionless body. Deep gurgles errupt from
the monster's heavy breathing sending
chills down your spine. It now looms over
your body. After a second, it yells out a
loud "RAAAAAWWWWWRRRR!!!" rivaling that of
a t-rex. Clearly, this is a scare tactic,
and it worked to a certain extent. Beads
of sweat begin to drip down your forehead.
Realizing that it doesn't matter if you're
dead or alive (and mainly because I'm
tired of typing this), the monster scoops
you up with its tongue, pulls you into its
mouth, and slams its face shut...
you're dead.
""")
			n = 1
		if x == 'RUN!!':
			print("""\
Scared out of your mind, you stumble
back up onto your feet (the same feet
that's definitely not designed for walking).
You try to put some distance between you
and the thing (by teleporting or something.
Idk.), but the monster is much faster.
Before you know it, the monster grabs you,
throws you into its mouth, and slams its
face shut...you're dead.
""")
			n = 1
		if x == 'play Dark Souls':
			print("""\
ROUND 1: FIGHT!!
As an experienced gamer, you recognize
that this thing is a mimic; so, you start
side-rolling. Fortunately, this thing is
much faster at moving forward than it is
at turning (thank God its look sensitivity
is down). It lunges forward going for the
creepiest bear hug you've ever seen just
as you dive out of the way. Ok. Now that
you know how to avoid it, how do you go
about killing it? You look up to see a
sword stuck in the floor. You teleport to
it and make a valiant attempt to free it.
It's stuck. You look over to see the
mimic barreling its way to you, its
thunderous footsteps growing louder and
louder as it closes the gap. With a
"FUS ROH DAH!!" and a sharp tug the heavy
sword is launched free. You barely hold
on long enough to stop the sword's
momentum directly above your head. The
mimic is fast approaching.

FINISH HIM!!
As the sword drops, you seal your eyes shut
and pull the handle upward towards the mimic
with all of your might and willpower in a
desparate attempt to make contact and
uppercut the beast. "SHHHHHINK!!" The blade
archs over your head and slams back into the
ground...silence.... You open your eyes to
see the mimic standing motionless just within
arms reach. Finally, the mimic's weight gives
in splitting it in two and collapsing on the
ground with a simultaneous, earth-shattering
thud that echoes throughout the chamber.
The beast is dead.
""")
			n = 6
		else:
			print("Invalid Response")
	if n == 6:
		print("""\
YOU WIN!!
Credits: Dustin Parkman
""")
		break
