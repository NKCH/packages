"""
import pymongo

client = pymongo.MongoClient("mongodb+srv://DBadmin:DBpass%24123@cluster0-895fg.mongodb.net/Anvayam?"
                             + "retryWrites=true&w=majority")
db = client.Anvayam

coll1 = db.BannerContent
print(coll1)
bdata1 = {
    'code': "ADWS",
    'name': "Anvayam Digital Water Solutions",
    'shortDesc': "Anvayam Digital Water Solutions",
    'imgUrl': "/gsp_backend/resources/data/images/ADWS.jpg"
}
coll1.insert_one(bdata1)
bdata2 = {
    'code': "IIOT",
    'name': "IIOT & Industry 4.0",
    'shortDesc': "Anvayam Industrial IOT Solutions",
    'imgUrl': "/gsp_backend/resources/data/images/IIOT.jpg"
}
coll1.insert_one(bdata2)
bdata3 = {
    'code': "HAPS",
    'name': "Home Automation Products and Solutions",
    'shortDesc': "Anvayam Home Automation Products and Solutions",
    'imgUrl': "/gsp_backend/resources/data/images/HAPS.jpg"
}
result = coll1.insert_one(bdata3)
print("coll1 complete" + result)

coll2 = db.Products
pdata1 = {
    'prodCode': "AROC",
    'name': "Reverse Osmosis Controllers",
    'shortDesc': "RO controller for Commercial and Domestic Use.",
    'desc': "Anvayam offers digital controllers for RO on both domestic and commercial space including wireless and cloud services.",
    'usp': ["", "", ""],
    'catCode': "ADWS",
    'imgUrl': "/gsp_backend/resources/data/images/AROC.jpg",
    'isHomeEnable': True,
    'styleClass': "110"
}
coll2.insert_one(pdata1)
pdata2 = {
    'prodCode': "AAFC",
    'name': "Agarbhathi Autofeeder and Funnel Controllers",
    'shortDesc': "Anvayam offers digital controllers for Agarbhathi Autofeeder and Funnel Controllers, including wireless and cloud services.",
    'desc': "",
    'usp': ["", "", ""],
    'catCode': "IIOT",
    'imgUrl': "/gsp_backend/resources/data/images/AAFC.jpg",
    'isHomeEnable': True,
    'styleClass': "200"
}
coll2.insert_one(pdata2)
pdata3 = {
    'prodCode': "AIOT",
    'name': "Anvayam Industrial IOT services",
    'shortDesc': "Anvayam provides services in the space of Wireless solutions using IoT communication protocols like GSM, Bluetooth, Wi-Fi (802.11), NFC, LoRa, ZigBee etc",
    'desc': "",
    'usp': ["", "", ""],
    'catCode': "IIOT",
    'imgUrl': "/gsp_backend/resources/data/images/AIOT.jpg",
    'isHomeEnable': True,
    'styleClass': "210"
}
coll2.insert_one(pdata3)
pdata4 = {
    'prodCode': "AHAS",
    'name': "Anvayam Home Automation Solutions",
    'shortDesc': "Anvayam strives to make homes become safer, smarter and savvy.",
    'desc': "",
    'usp': ["", "", ""],
    'catCode': "HAPS",
    'imgUrl': "/gsp_backend/resources/data/images/AHAS.jpg",
    'isHomeEnable': True,
    'styleClass': "300"
}
coll2.insert_one(pdata4)
pdata5 = {
    'prodCode': "AESS",
    'name': "Anvayam Embedded Systems Solutions",
    'shortDesc': "Anvayam provides Defence, Aerospace, Industrial and commercial grade embedded services and fully customized architectures for your embedded systems.",
    'desc': "",
    'usp': ["", "", ""],
    'catCode': "HAPS",
    'imgUrl': "/gsp_backend/resources/data/images/AESS.jpg",
    'isHomeEnable': True,
    'styleClass': "310"
}
coll2.insert_one(pdata5)
pdata6 = {
    'prodCode': "ASWL",
    'name': "Smart Water Level Controller and Wireless Monitor",
    'shortDesc': "Smart Water Level Controller and Wireless Monitor.",
    'desc': "",
    'usp': ["", "", ""],
    'catCode': "ADWS",
    'imgUrl': "/gsp_backend/resources/data/images/ASWL.jpg",
    'isHomeEnable': False,
    'styleClass': "100"
}
coll2.insert_one(pdata6)
pdata7 = {
    'prodCode': "ASFM",
    'name': "Smart Flow meter and wireless indicator",
    'shortDesc': "RO controller for Commercial and Domestic Use.",
    'desc': "",
    'usp': ["", "", ""],
    'catCode': "ADWS",
    'imgUrl': "/gsp_backend/resources/data/images/ASFM.jpg",
    'isHomeEnable': False,
    'styleClass': "120"
}
coll2.insert_one(pdata7)
pdata8 = {
    'prodCode': "ASWA",
    'name': "Smart Water ATMs",
    'shortDesc': "Smart Water ATMs",
    'desc': "",
    'usp': ["", "", ""],
    'catCode': "ADWS",
    'imgUrl': "/gsp_backend/resources/data/images/ASWA.jpg",
    'isHomeEnable': False,
    'styleClass': "130"
}
coll2.insert_one(pdata8)
pdata9 = {
    'prodCode': "AEWC",
    'name': "Electronic Water Conditioners",
    'shortDesc': "Electronic Water Conditioners",
    'desc': "",
    'usp': ["", "", ""],
    'catCode': "ADWS",
    'imgUrl': "/gsp_backend/resources/data/images/AEWC.jpg",
    'isHomeEnable': False,
    'styleClass': "140"
}
result = coll2.insert_one(pdata9)
print("coll1 complete" + result)
"""