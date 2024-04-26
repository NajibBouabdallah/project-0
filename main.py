import json
import random
import time
import streamlit


import requests

streamlit.title = "the amazing app. horrah!"
inputField = streamlit.text_input("what you wanna say? you can keep this field empty if you dont want to interact")


headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMzIyMDgwM2EtZDc2OS00NTg0LWExZjItZTEzNDgyOWZiYWNiIiwidHlwZSI6ImFwaV90b2tlbiJ9.WGkdfiAtmL9DoGznRa8_AOl76KFC2gNWlkwkX5Z8hCw"}

DrStrange = "Dr. Stephen Vincent Strange is a character appearing in American comic books published by Marvel Comics. \nThe character starts as an intelligent and egotistically arrogant neurosurgeon who is injured in a car accident. Because his hands had suffered severe nerve damage from the accident, he was told that current medical therapy and rehabilitation would not be enough to enable him to practice again as a surgeon. Unable to accept this prognosis, he travels the world searching for alternative ways of healing, which leads him to the Ancient One, the Sorcerer Supreme. Strange becomes his student and learns to be a master of both the mystical and the martial arts. He acquires an assortment of mystical objects, including the powerful Eye of Agamotto and Cloak of Levitation, and takes up residence in a mansion referred to as the Sanctum Sanctorum, located at 177A Bleecker Street, Greenwich Village, Manhattan, New York City. Strange assumes the title of Sorcerer Supreme and, with his friend and valet Wong, defends the world from mystical threats.\n\nIn live-action adaptations, the character was first portrayed by Peter Hooten in the 1978 television film Dr. Strange. Since 2016, Benedict Cumberbatch has portrayed the role of Stephen Strange in the Marvel Cinematic Universe.\n\ndoctor strange is now in trouble. and needs to discuses the multiverse with his closest friends and allies monkey D loffy, sherlock holmes, aiden pearce"

Luffy = "luffy is one of the Four Emperors, and at the young age of 19, Luffy is one of the four most powerful pirates in the world. He captains the Straw Hat Pirates, holding the greatest authority over a mighty and diverse crew consisting of several infamous members, many of whom are extremely powerful in their own right. Luffy has a tremendous amount of influence over his crewmates, so much so that they all trust him with their lives, despite his reckless behavior and, in some cases, even because of it.\nHe is also one of twelve pirates who have been dubbed the \"Worst Generation\", a group of individuals who have become infamous for the bold and major actions they have committed against the World Government, and all have bounties of over Beli100,000,000. Indirectly, he also has claim over the Straw Hat Grand Fleet, a massive fleet consisting of seven powerful New World crews numbering 5640 people in total, who all swore to serve under him of their own will and come to assist him whenever he may need them.The scope of Luffy's authority was considered by the World Government to be close to on par with the Four Emperors, the four most powerful and influential pirates in the world, and the press dubbed Luffy the \"Fifth Emperor\" as a result\nHowever, Luffy officially became an Emperor after defeating one of the previous Emperors, Kaidou , and his meteoric rise in status (in over two years) caused panic around the world; he currently holds a bounty of Beli3,000,000,000, which is currently the lowest Emperor bounty and equals the bounties of two of his fellow Worst Generation members—Kid and Law. His bounty is only surpassed by the bounties of the former Emperors Whitebeard, Big Mom, Kaidou, fellow Emperors Shanks, Blackbeard and Buggy, former Warlord Mihawk and the late Pirate King, Gol D. Roger himself\nLuffy is a fierce and formidable combatant who can invent extremely creative fighting techniques even during intense battles and has gone through harsh and rigorous training ever since he was a child. He has been taught by two legendary figures, his grandfather Monkey D. Garp, the \"Hero of the Marines\",\n and Silvers Rayleigh, the retired first mate of the Pirate King's crew. Despite acting goofy and eccentric most of the time, Luffy has proven to be a natural born leader.\nhe now needs to discuses the multiverse with his friends doctor strange, Aiden Pearce and sherlock Holmes"

Aiden = "Aiden Pearce (also known as The Vigilant/Vigilante and The Fox by the media) is the protagonist of Watch Dogs. He is a highly skilled and deadly black hat hacker who has access to the ctOS of Chicago using a highly specialized device greatly upgraded for him by Clara Lille, the Profiler. Because his actions led to a family tragedy, Aiden has taken to a personal crusade against the powers that be. His obsession with security, surveillance, and control borders on the paranoid and dangerous, extending to monitoring his own family (unbeknownst to them). \n\nhe's a highly skilled hacker and highly confident man. he now needs t discuses how to save the multiverse with his closest friends and allies doctor strange, Monkey D Luffy and Sherlock Holmes"

Sherlock = "Sherlock Holmes is a fictional detective created by British author Arthur Conan Doyle. Referring to himself as a \"consulting detective\" in his stories, Holmes is known for his proficiency with observation, deduction, forensic science and logical reasoning that borders on the fantastic, which he employs when investigating cases for a wide variety of clients, including Scotland Yard. The character Sherlock Holmes first appeared in print in 1887's A Study in Scarlet. His popularity became widespread with the first series of short stories in The Strand Magazine, beginning with \"A Scandal in Bohemia\" in 1891; additional tales appeared from then until 1927, eventually totalling four novels and 56 short stories. All but one[a] are set in the Victorian or Edwardian eras, between about 1880 and 1914. Most are narrated by the character of Holmes's friend and biographer Dr. John H. Watson, who usually accompanies Holmes during his investigations and often shares quarters with him at the address of 221B Baker Street, London, where many of the stories begin. Though not the first fictional detective, Sherlock Holmes is arguably the best known.[1] By the 1990s, there were already over 25,000 stage adaptations, films, television productions and publications featuring the detective,[2] and Guinness World Records lists him as the most portrayed human literary character in film and television history.Holmes' popularity and fame are such that many have believed him to be not a fictional character but a real individual;numerous literary and fan societies have been founded on this pretence. Avid readers of the Holmes stories helped create the modern practice of fandom.[7] The character and stories have had a profound and lasting effect on mystery writing and popular culture as a whole, with the original tales as well as thousands written by authors other than Conan Doyle being adapted into stage and radio plays, television, films, video games, and other media for over one hundred years"


url = "https://api.edenai.run/v2/text/chat"
payload = {
    "providers": "openai",
    "text": "hello doctor strange, we need your help with the multi-verse issue",
    "chatbot_global_action": DrStrange,
    "previous_history": [],
    "temperature": 1,
    "max_tokens": 256,
    "fallback_providers": ""
}
ConvoIdx = 1

response = requests.post(url, json=payload, headers=headers)
result = json.loads(response.text)

ConvoHistory = [{'role':'user','message': result['openai']['generated_text']}]
ConvoIdx += 1
print("Dr Strange: " + result['openai']['generated_text'])

def StrangeMessage(idx):
    payload = {
        "providers": "openai",
        "text": ConvoHistory[-1]['message'],
        "chatbot_global_action": DrStrange,
        "previous_history": [],
        "temperature": 1,
        "max_tokens": 256,
        "fallback_providers": ""
    }

    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    strResponse = result['openai']['generated_text']
    ConvoHistory.append({'role':'user','message': strResponse})
    print("Dr strange: " + result['openai']['generated_text'])
    idx += 1

def LuffyMessage(idx):
    payload = {
        "providers": "openai",
        "text": ConvoHistory[-1]['message'],
        "chatbot_global_action": Luffy,
        "previous_history": [],
        "temperature": 1,
        "max_tokens": 256,
        "fallback_providers": ""
    }
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    strResponse = result['openai']['generated_text']
    ConvoHistory.append({'role':'user','message': strResponse})
    print("Luffy: " + result['openai']['generated_text'])
    idx += 1
def AidenMessage(idx):
    payload = {
        "providers": "openai",
        "text": ConvoHistory[-1]['message'],
        "chatbot_global_action": Aiden,
        "previous_history": [],
        "temperature": 1,
        "max_tokens": 256,
        "fallback_providers": ""
    }
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    strResponse = result['openai']['generated_text']
    ConvoHistory.append({'role':'user','message': strResponse})
    print("Aiden: " + result['openai']['generated_text'])
    idx += 1
def SherlockMessage(idx):
    payload = {
        "providers": "openai",
        "text": ConvoHistory[-1]['message'],
        "chatbot_global_action": Sherlock,
        "previous_history": [],
        "temperature": 1,
        "max_tokens": 256,
        "fallback_providers": ""
    }
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    strResponse = result['openai']['generated_text']
    ConvoHistory.append({'role':'user','message': strResponse})
    print("Sherlock" + result['openai']['generated_text'])
    idx += 1
    ConvoHistory.append(response.content)


numOfCovos = 0
while(numOfCovos < 20):
    chance = random.random()
    numOfCovos += 1
    if(inputField != ""):
        print("user: " + inputField)
        ConvoHistory.append({'role': 'user', 'message': inputField})
    funcs = [StrangeMessage, AidenMessage, LuffyMessage, SherlockMessage]
    random.choice(funcs)(ConvoIdx)
    time.sleep(200)
