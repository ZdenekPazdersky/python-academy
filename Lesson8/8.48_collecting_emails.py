# ###2DO
# Your task is to create multiple functions that will work together in one program and will produce a result in form of a dictionary representing the following mapping:
#
# emails that contain numeric characters found in the string my_str
# all the email domains (part after the '@' symbol) found in the string my_str
# What the multiple functions could do?
#
# extract all the emails from the string my_str
# collect only email containing numeric characters
# extract all email domains
# And here we have the variable my_str containing the target string:
#
# Example of running the program:
#
# ~/PythonBeginner/Lesson5 $ python collect_email.py
# {'domains': ['email.cz', 'info.com,', 'gmail.com', 'money.fr', 'info.cz.'],
# 'emails_with_nums': ['tiger123@email.cz', 'b2b@money.fr']}
# The main function should be named main(), it should call all the other needed function and return the result. As you can see from the example above, The result should be a dictionary with keys domains and emails_with_nums, containing values - lists with relevnt emails.
#
# Our online editor is unsuitable for this kind of task. Considering the scope, it'll be better to do it in your own local code editor. Just copy and paste it here when you think it's OK and run the tests.
#
# Of course, if you've been doing all the task on your computer, that is fine too and you can just keep doing that :)
# ######

my_str = '''Lorem ipsum dolor sit amet, consectetur adipiscing
        elit. Mauris vulputate lacus id eros consequat tempus.
        Nam viverra velit sit amet lorem lobortis, at tincidunt
        nunc ultricies. Duis facilisis ultrices lacus, id
        tiger123@email.cz auctor massa molestie at. Nunc tristique
        fringilla congue. Donec ante diam cnn@info.com, dapibus
        lacinia vulputate vitae, ullamcorper in justo. Maecenas
        massa purus, ultricies a dictum ut, dapibus vitae massa.
        Cras abc@gmail.com vel libero felis. In augue elit, porttitor
        nec molestie quis, auctor a quam. Quisque b2b@money.fr
        pretium dolor et tempor feugiat. Morbi libero lectus,
        porttitor eu mi sed, luctus lacinia risus. Maecenas posuere
        leo sit amet spam@info.cz. elit tincidunt maximus. Aliquam
        erat volutpat. Donec eleifend felis at leo ullamcorper cursus.
        Pellentesque id dui viverra, auctor enim ut, fringilla est.
        Maecenas gravida turpis nec ultrices aliquet.'''

def main(my_str):
    my_str = my_str.split()
    dicti = {'emails': [], 'domains': [], 'emails_with_nums' : []}
    dicti_str = []
    def extract_emails(seq):
        for index in my_str:
            if '@' in index:
                # position_at = index.find('@')
                # print(position_at)
                dicti_str.append(index) #creating list with all emails
        return dicti_str
    def extract_domains(dik, klic):
        str1 = []
        for index in dik.get(klic):
            position_at = index.find('@')
            str1.append(index[position_at + 1:])
        return str1
    def extract_num_emails(dik, klic):
        str2 = []
        for index in dik.get(klic):
            position_at = index.find('@')
            if not str(index[:position_at]).isalpha():
                str2.append(index)
        return str2

    dicti.update(emails=extract_emails(my_str))
    dicti.update(domains=extract_domains(dicti, 'emails'))
    dicti.update(emails_with_nums=extract_num_emails(dicti, 'emails'))

    print(dicti)

main(my_str)
