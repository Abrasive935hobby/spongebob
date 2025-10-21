# Name: Malcolm Edwards
# Student Number: W0522168
# Course: PROG1700
# Week: 7 – Sets CRUD Activity

# Step 2 – Create (C)
club_members = {"Alice", "Bob", "Charlie"}
print("Initial Members:", club_members)

# Adding a duplicate name
club_members.add("Alice")  # No error, but no duplicate added
print("After adding duplicate 'Alice':", club_members)

# Step 3 – Read (R)
print("Number of Members:", len(club_members))

for member in club_members:
    print("Member:", member)

# Step 4 – Update (U)
# Add new members
club_members.add("Diana")

# Remove a member
club_members.remove("Alice")  # Will raise error if Alice is not found
club_members.discard("Bob")   # Safe remove, no error if Bob not found

# Add 2-3 new names using update()
club_members.update({"Eve", "Frank", "Grace"})

print("Updated Members:", club_members)

# Step 5 – Delete (D)
club_members.clear()
print("Cleared Set:", club_members)

# Uncomment below to test deleting the entire set (this will cause an error if you try to print afterward)
# del club_members
# print(club_members)

# Step 6 – Real-World Application: Duplicate Email Cleanup
emails = ["test@gmail.com", "admin@gmail.com", "test@gmail.com", "info@gmail.com"]
unique_emails = set(emails)
print("Unique Emails:", unique_emails)

# Reflection:
# 1. How are sets different from lists or tuples?
#    Sets are unordered collections of unique elements, whereas lists and tuples can have duplicates and are ordered.
#    Sets are mutable like lists, but tuples are immutable.
#
# 2. Why is it useful that sets automatically remove duplicates?
#    This helps when you want to ensure data uniqueness without extra code,
#    such as cleaning duplicate entries or maintaining distinct values.
#
# 3. What type of data might you store in a set in a real program?
#    Examples include unique user IDs, tags, email addresses, or any collection where duplicates should be avoided.
