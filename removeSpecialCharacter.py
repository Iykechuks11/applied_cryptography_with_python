def message(m):
    # l = list(m)
    # new_list = []
    new_m = ''

    for i in m:
        if (i == ',') or (i == '.') or (i == '/') or (i == "'"):
            m.replace(i, '')
        else:
            new_m += i
            
    return new_m


# to_str = message('ASSS,ASASAS.ASAS,')
# print(to_str)

messenger = message(""" 
        In the small town of Willowbrook, there lived a man named Thomas who was known for his cunning ways and sharp tongue. Thomas had spent most of his life manipulating others for his own gain, leaving a trail of broken relationships and shattered dreams in his wake. He took pleasure in exploiting people's weaknesses, believing that kindness was a sign of weakness itself.
        
        However, as Thomas grew older, a sense of emptiness began to gnaw at him. Despite his material wealth, he felt a profound loneliness that no amount of money could fill. His conscience, long buried under layers of deceit, started to stir, reminding him of the pain he had caused others.

        One stormy night, as Thomas sat alone in his lavish mansion, he found himself reflecting on his life choices. Memories of the people he had hurt flashed before his eyes, each face etched with sorrow and betrayal. He realized with a pang of regret that his actions had left a trail of devastation, not only in the lives of others but also in his own soul.
        
        Driven by an overwhelming sense of guilt, Thomas made a decision that would change the course of his life. He resolved to seek redemption for his past sins and make amends to those he had wronged. With a newfound determination, he embarked on a journey of repentance, determined to right the wrongs of his past.
        
        Thomas began by reaching out to those he had hurt, offering heartfelt apologies and restitution where possible. He spent hours listening to their grievances, allowing himself to feel their pain and remorsefully acknowledging the harm he had caused. His genuine contrition touched the hearts of many, gradually earning him forgiveness and reconciliation.

        As Thomas walked the path of repentance, he discovered unexpected blessings along the way. He found solace in the forgiveness of others, and his relationships began to heal as trust was slowly rebuilt. With each act of kindness and humility, he felt the heavy burden of guilt lifting from his shoulders, replaced by a sense of inner peace he had long forgotten.
        
        In time, Thomas became a beacon of hope and inspiration in Willowbrook, his transformation serving as a testament to the power of repentance and redemption. Though he could never erase the pain he had caused, he dedicated the rest of his days to making a positive impact on the world, using his second chance to spread love and kindness wherever he went.
        
        And so, the story of Thomas serves as a reminder that no matter how far we may stray from the path of righteousness, it is never too late to turn back, seek forgiveness, and embark on a journey of repentance that leads to healing and redemption.
        """)

print(message(messenger))
