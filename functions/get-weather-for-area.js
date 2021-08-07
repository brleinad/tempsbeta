const axios = require('axios')

console.log('running in ', process.env.NODE_ENV)
if (process.env.NODE_ENV !== 'production') {
  require('dotenv').config();
}

async function main(area) {

  const lon = area.location.coordinates[0];
  const lat = area.location.coordinates[1];
  const openWeatherApiUrl =  `https://api.openweathermap.org/data/2.5/forecast?lat=${lat}&lon=${lon}&units=metric&appid=${process.env.OPENWEATHERMAP_API_KEY}`;
  try {
    const response = await axios.get(openWeatherApiUrl)
    console.log(response.data.list)
    return response.data.list;
  } catch(error) {
    console.error(error)
  } finally {
  }
}

const area =   {
    // _id: new ObjectId("610d834939a02791a5e983ff"), // TODO: figure out what to do with id
    name: 'Some crag',
    url: 'https://www.mountainproject.com/area/120620010/lac-moulineau',
    location: { type: 'Point', coordinates: [ -71.1, 46.134] }
  }


main(area).catch(console.error);