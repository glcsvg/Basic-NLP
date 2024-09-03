# Import required modules
from nrclex import NRCLex


raw_text=["Upon losing his memory, a crown prince encounters a commoner’s life and experiences unforgettable \
    love as the husband to Joseon’s oldest bachelorette."]
raw_text_2 = "Upon losing his memory, a crown prince encounters a commoner’s life and experiences unforgettable \
    love as the husband to Joseon’s oldest bachelorette."
#raw_text = ['losing','memory','prince','love','husband']

a = ["If I did not  love you I wouldn't love you in the future"]
b = ["If I didn't x you I would not x you in the future"]


# emotion = NRCLex(a)
# print('\n\n', a, ': ', emotion.top_emotions)
# emotion = NRCLex(b)
# print('\n\n', b, ': ', emotion.top_emotions)



#raw_text_list = a.split(" ")

#print(raw_text_list)

for i in range(len(a)):

    # creating objects
    emotion = NRCLex(a[i])
    print('\n\n', a, ': ', emotion.top_emotions)
for i in range(len(b)):

    # creating objects
    emotion = NRCLex(b[i])
    print('\n\n', b[i], ': ', emotion.top_emotions)