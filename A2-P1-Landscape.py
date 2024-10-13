#Program 1 – Landscape Calculator
#A landscaping company needs a program that computes the price of landscaping for a new housing development. 

#Student #: 0433704   
#Student Name:  Zachary Rudolf

def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)
    # •	There is a base labour charge of $1000. 
    # •	If the surface (length * width) is over 5000 square feet, add $500. 
    # •	The cost is calculated per square foot. If the grass is “fescue” the cost is $0.05; for “bentgrass” it is $0.02; “campus” is $0.01. 
    # •	Each tree requested has a $100 charge. 

    baseCharge=1000
    length=0.0
    width=0.0
    grassSqFt=0.0
    grassCost=0.0
    totalSqFt=0.0
    treeCost=100
    treeAmt=0
    houseNo=""
    grassType=""

    #greeting for program/description
    print("Thank you for choosing Prog Landscaping!\n")
    #input from user for house number, yard size, grass type, and tree count
    houseNo=input("Enter House Number: ")
    length=float(input("\nEnter property depth (feet): "))
    width=float(input("\nEnter property width (feet): "))
    grassType=input("\nEnter type of grass (fescue, bentgrass, campus): ").lower()
    treeAmt=int(input("\nEnter the number of trees: ")) 
    #if statements for grass type, yard size, and trees 
    totalSqFt=length*width
    if grassType=="fescue":
            grassSqFt=0.05
    elif grassType=="bentgrass":
            grassSqFt=0.02
    elif grassType=="campus": 
            grassSqFt=0.01 
    grassCost=totalSqFt*grassSqFt 
    treeCost=treeAmt*100
    if totalSqFt > 5000:
        total=grassCost+treeCost+baseCharge+500
    else:
        total=grassCost+treeCost+baseCharge
    #print command for total owed for house number
    print("Total cost for house {0} is: ${1:,.2f}".format(houseNo, total))
    # YOUR CODE ENDS HERE

main()