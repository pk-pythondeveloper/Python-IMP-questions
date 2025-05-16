#set is collesction unorderd element
#add()	 	Adds an element to the set
# temp={12,23,45,18,31,45}
# temp.clear()
# print(temp)

# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
set1={23,15,16}
set2={56,65,16,28}
set1.difference_update(set2) # it remove only matching value
print(set1)

# discard()	 	#Remove the specified item,if element not found it not return errors
set1={23,15,16}
t=set1.discard(23) #it not return dicard element

print(t)
# intersection()	&	Returns a set, that is the intersection of two other sets #it return matching value
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)

#The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.
# isdisjoint()	 	Returns whether two sets have a intersection or not#Required. The set to search for equal items in
# issubset()	<=	Returns whether another set contains this set or not
#  	<	Returns whether all items in this set is present in other, specified set(s)
# issuperset()	>=	Returns whether this set contains another set or not
#  	>	Returns whether all items in other, specified set(s) is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others