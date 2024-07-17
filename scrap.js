const puppeteer = require('puppeteer');
const createCsvWriter = require('csv-writer').createObjectCsvWriter;

async function scrapeStores() {
  const browser = await puppeteer.launch({ headless: false }); // Set to false for debugging
  const page = await browser.newPage();
  await page.goto('https://shop.rangs.com.bd/stores', { waitUntil: 'networkidle2' });

  // Wait for the page content to load
  await new Promise(resolve => setTimeout(resolve, 5000));

  // Inspect the HTML content to find the correct selectors
  const content = await page.content();
  console.log(content);

  const stores = await page.evaluate(() => {
    // Adjust these selectors to match the actual page structure
    const storeElements = document.querySelectorAll('.store'); 
    const storeData = [];
    
    storeElements.forEach(store => {
      const name = store.querySelector('.store-name')?.innerText || 'No name'; // Adjust this selector
      const address = store.querySelector('.store-address')?.innerText || 'No address'; // Adjust this selector
      const mapLink = store.querySelector('a.map-link')?.href || 'No map link'; // Adjust this selector
      storeData.push({ name, address, mapLink });
    });

    return storeData;
  });

  // Setup CSV Writer
  const csvWriter = createCsvWriter({
    path: 'stores.csv',
    header: [
      { id: 'name', title: 'Name' },
      { id: 'address', title: 'Address' },
      { id: 'mapLink', title: 'Map Link' }
    ]
  });

  // Write data to CSV
  await csvWriter.writeRecords(stores);

  console.log('Data has been written to stores.csv');

  await browser.close();
}

scrapeStores();
