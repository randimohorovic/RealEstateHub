import boto3
#testirao vise puta scraper i fetchanje, nema duplikata, iz baze
# se skenira i vrati sve tocne rezultate,
# tesitram ispis podataka iz baze
dynamodb = boto3.resource("dynamodb", region_name="eu-north-1")

table = dynamodb.Table('RealEstateListings')
table_mondo = dynamodb.Table("MondoListings")
table_njuskalo = dynamodb.Table("NjuskaloListings")
response = table.scan()
response2 = table_mondo.scan()
response3 = table_njuskalo.scan()

items = response.get('Items', [])
for item in items:
    print(item)

items2 = response2.get('Items', [])
for item in items2:
    print(item)

items3 = response3.get('Items', [])
for item in items3:
    print(item)

print(len(items))
print(len(items2))
print(len(items3))

