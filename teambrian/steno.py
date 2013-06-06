from PIL import Image
im = Image.open("image.jpg")

text = """
The sketch:

REG: Daniel.

LORETTA: Daniel.

FRANCIS: Job.

REG: Job.

LORETTA: Job.

FRANCIS: Joshua.

REG: Joshua.

LORETTA: Joshua.

FRANCIS: Judges.

REG: Judges.

LORETTA: Judges.

FRANCIS: And Brian.

REG: And Brian.

LORETTA: And Brian.

REG: I now propose that all seven of these ex-brothers be now entered in the minutes as probationary martyrs to the cause.

LORETTA: I second that, Reg.

REG: Thank you, Loretta. On the nod. Siblings!

thump

Let us not be down-hearted. One total catastrophe like this is just the beginning! Their glorious deaths shall unite us all in a--

MATTHIAS: Look out!

BRIAN: Hello? Matthias! Reg!

REG: Go away!

BRIAN: Hm? Reg, it's me, Brian!

REG: Get off! Get off out of it!

BRIAN: Stan!

LORETTA: Piss off.

COMMANDO: Yeah, piss off!

REG: Bugger off.

bam bam bam bam bam bam bam bam bam bam bam bam

Ohh,...

bam bam bam bam bam

...shit!

bam

BRIAN: Uhh.

MATTHIAS: Coming!

bam bam bam bam bam bam bam bam bam bam bam bam

bam bam bam bam bam bam

BORING PROPHET: Yea, verily, at that time, it is written in the book of Obadiah. A man shall strike his donkey and his nephew's donkey and anyone...

crack

...in the vicinity...

creak crack

...of his nephew or the donkey.

MATTHIAS: My eyes are dim. I cannot see.

CENTURION: Are you Matthias?

MATTHIAS: Yes.

CENTURION: We have reason to believe you may be hiding one Brian of Nazareth, a member of the terrorist organisation, the 'People's Front of Judea'.

MATTHIAS: Me? No. I'm just a poor old man. I have no time for law-breakers. My legs are grey. My ears are gnarled. My eyes are old and bent.

CENTURION: Quiet! Silly person. Guards! Search the house.

clomp clomp clomp...

You know the penalty laid down by Roman law for harbouring a known criminal?

MATTHIAS: No.

CENTURION: Crucifixion.

MATTHIAS: Oh.

CENTURION: Nasty, eh?

MATTHIAS: Hm. Could be worse.

CENTURION: What do you mean, 'could be worse'?

MATTHIAS: Well, you could be stabbed.

CENTURION: Stabbed? Takes a second. Crucifixion lasts hours! It's a slow, horrible death!

MATTHIAS: Well, at least it gets you out in the open air.

CENTURION: You're weird.

clomp clomp clomp...

SERGEANT: No, sir. Couldn't find anything, sir.

CENTURION: But don't worry! You've not seen the last of us, weirdo.

MATTHIAS: Big Nose.

CENTURION: Watch it.

MATTHIAS: Phew, that was lucky.

BRIAN: I'm sorry, Reg.

REG: Ohhh, it's all right, siblings. He's sorry. He's sorry he led the Fifth Legion straight to our official headquarters. Well, that's all right, then, Brian. Sit down. Have a scone. Make yourself at home. You klutz! You stupid, bird-brained, flat-headed--

bam bam bam bam bam bam bam bam bam bam bam bam bam bam bam

creak crack

BORING PROPHET: ...this great, big, juicy melon behind.

bam bam bam bam bam bam

MATTHIAS: My legs are old and bent. My ears are grizzled. Yes?

CENTURION: There's one place we didn't look. Guards!

MATTHIAS: I'm just a poor old man.

clomp clomp clomp...

My eyesight is bad. My eyes are poor. My nose is knackered.

CENTURION: Have you ever seen anyone crucified?

MATTHIAS: Crucifixion's a doddle.

CENTURION: Don't keep saying that.

clomp clomp clomp...

SERGEANT: Found this spoon, sir.

CENTURION: Well done, Sergeant! We'll be back,... oddball.

bam bam bam bam bam

Open up!

MATTHIAS: You haven't given us time to hide.

"""
bytes = im.tobytes()


def increment(a):
  return a + ((a + 1812433253) % 53)

image_index = 0

for char in text:
  bytes = bytes[:image_index] +  char + bytes[image_index+1:]
  image_index = increment(image_index)

bytes = bytes[:image_index] +  "\x00" + bytes[image_index+1:]
im.frombytes(bytes)
im.save("out.png")


im2 = Image.open("out.png")
bytes2 = im2.tobytes()


index=0
output = []
while True:
  data = bytes2[index]
  if data == "\x00":
    break
  output.append(data)
  index = increment(index)

print "".join(output)