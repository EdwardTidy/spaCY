import spacy

nlp = spacy.load('en_core_web_sm')

# Garden path sentences

garden_1 = "The old man the boat."
garden_2 = "Mary gave the child the dog bit a Band-Aid."
garden_3 = "The horse raced past the barn fell."
garden_4 = "The complex houses married and single soldiers and their families."
garden_5 = "The florist sent the flowers was pleased."

gardenPathSentences = [garden_1, garden_2, garden_3, garden_4, garden_5]

# Tokenisation

for sentence in gardenPathSentences:

    #Tokenisation
    print([(word, word.orth_, word.orth) for word in nlp(sentence) if not word.is_punct | word.is_space])

    # Entity recognition
    print([(word, word.label_, word.label) for word in nlp(sentence).ents])

"""
Noticed that using garden path sentences like the one above, while tokenisation works, entity recognition is only in garden_2, because this is the only one with an entity (Mary). Going to try again below with some non garden paths
"""

non_garden_1 = "George Timothy Clooney (born May 6, 1961) is an American actor and filmmaker. He is the recipient of numerous accolades, including a British Academy Film Award, four Golden Globe Awards, four Screen Actors Guild Awards, and two Academy Awards, one for his acting and the other as a producer. In 2018, he was the recipient of the AFI Life Achievement Award."
non_garden_2 = "Batman & Robin is a 1997 American superhero film based on the DC Comics characters Batman and Robin by Bill Finger and Bob Kane. It is the fourth and final installment of Warner Bros.'s initial Batman film series, a sequel to Batman Forever and the only film in the series made without the involvement of Tim Burton in any capacity."
non_garden_3 = "Up in the Air is a 2009 American comedy-drama film directed by Jason Reitman. It was written by Reitman and Sheldon Turner, based on the 2001 novel Up in the Air by Walter Kirn. The story is centered on traveling corporate 'downsizer' Ryan Bingham (George Clooney). Vera Farmiga, Anna Kendrick, and Danny McBride also star."
non_garden_4 = "Nick Naylor (Aaron Eckhart) is a Big Tobacco spokesman using 'research' from an institution he's the vice-president of, a tobacco lobby called the 'Academy of Tobacco Studies'. It claims there is no link between tobacco and lung disease. Naylor and his friends, firearm lobbyist Bobby Jay Bliss (David Koechner) and alcohol lobbyist Polly Bailey (Maria Bello), meet every week and jokingly call themselves the 'Merchants of Death' or 'The MOD Squad'."
non_garden_5 = "Samuel Pack Elliott (born August 9, 1944) is an American actor. He is the recipient of several accolades, including a National Board of Review Award, and has been nominated for an Academy Award, two Golden Globe Awards, two Primetime Emmy Awards, and two Screen Actors Guild Awards."

nonGardenSentences = [non_garden_1, non_garden_2, non_garden_3, non_garden_4, non_garden_5]

for sentence in nonGardenSentences:

    # Entity recognition
    print([(word, word.label_, word.label) for word in nlp(sentence).ents])

"""I was surprised at spaCy being able to classify Batman both as a PERSON and a WORK_OF_ART depending on whether the film or the character was being spoken about. Also being able to identify every week being a reference to DATE surprised me"""

# In requirements .txt I have included spaCy, not a specific version and have not included Python either as I do not think this needs to be included (pip can't be run without Python to install required modules)