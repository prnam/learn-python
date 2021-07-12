# Return output as per the example given below for given input containing full name and email address.
# Example: Full Name <fullname@example.in>, GitHub <github@example.in>
def fullname_emails(people):
    results=[]
    for email, fullname in people:
        results.append("{} <{}>".format(fullname,email))
    return results

print(fullname_emails([('github@example.in', 'GitHub'),('pranam@example.in', 'Pranam')]))