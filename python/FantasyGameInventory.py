def display(inventory):
    print("Inventory:")
    count = 0
    for i,j in inventory.items():
        print(str(j)+"  " +i)
        count += j
    print("Total number of items:"+str(count))
if __name__ =="__main__":    
    inventory = {'rope':1, 'torch':6, 'gold coin':42, 'dagger':1, 'arrow':12}
    display(inventory)