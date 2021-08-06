const {MongoClient} = require('mongodb');

console.log('running in ', process.env.NODE_ENV)
if (process.env.NODE_ENV !== 'production') {
  require('dotenv').config();
}

async function main() {
  MONGODB_CLUSTER = process.env.MONGODB_CLUSTER;
  MONGODB_USER = process.env.MONGODB_USER;
  MONGODB_PASSWORD = process.env.MONGODB_PASSWORD;
  const uri = `mongodb+srv://${MONGODB_USER}:${MONGODB_PASSWORD}@${MONGODB_CLUSTER}?retryWrites=true&w=majority`;
  const client = new MongoClient(uri);
  try {
    await client.connect();
    const areas = client.db('tempsbeta').collection('areas');
    // const del= await areas.deleteMany({}); // WARNING: delete all documents!!!
    // console.log(del)

    const  minDistanceInMeters = 100;
    const  maxDistanceInMeters = 10000;
    const searchCoordinates = [ -71.317758, 46.923325 ]

    // areas.createIndex( { location: "2dsphere" } ) only have to run once?
    const query =
      {
        location:
          { $near :
              {
                $geometry: { type: "Point",  coordinates: searchCoordinates },
                $minDistance: minDistanceInMeters,
                $maxDistance: maxDistanceInMeters,
              }
          }
      };
    console.log(JSON.stringify(query))


    const nearbyAreas = await areas.find(query).toArray();
    console.log(nearbyAreas);

  } catch(error) {
    console.error(error)
  } finally {
    await client.close()
  }
}

main().catch(console.error)