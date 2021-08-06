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
    const query = { name: 'Mont Wright' };

    const climb = await areas.findOne(query);
    console.log(climb);

  } catch(error) {
    console.error(error)
  } finally {
    await client.close()
  }
}

main().catch(console.error)