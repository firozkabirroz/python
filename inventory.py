from collections import Counter
def displayinventory(inventory):
    print("Inventory:")
    item_total=0
    for k,v in inventory.items():
        print( str(v) + ' ' + str(k))

        item_total= v+item_total

    print("total number of items: "+str(item_total))


def addToInventory(inventory,addItems):
    count={}
    for i in inventory:
        count.setdefault(i,0)
        count[i]=count[i]+1
        
    final=Counter(count)+Counter(addItems)
    
    return final

    
    




inv={'gold coin':42,'rope':1}
dragonLoot=['gold coin','dagger','gold coin','gold coin','ruby']
inv =addToInventory(dragonLoot,inv)

displayinventory(inv)


