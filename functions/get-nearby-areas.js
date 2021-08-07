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
  const  minDistanceInMeters = 100;
  const  maxDistanceInMeters = 50000;
  const searchCoordinates = [ -71.317758, 46.923325 ] // testing with somewhere in quebec

  try {
    await client.connect();
    const areas = client.db('tempsbeta').collection('areas');
    // areas.createIndex( { location: "2dsphere" } ) only have to run the first time // TODO: move to scraper/backend?
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


    const nearbyAreas = await areas.find(query).toArray();
    console.log(nearbyAreas);

  } catch(error) {
    console.error(error)
  } finally {
    await client.close()
  }
}

main().catch(console.error)