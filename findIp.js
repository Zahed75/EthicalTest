const dns = require('dns');

const domain = 'seaqua.io'; // Remove the protocol prefix from the domain

dns.resolve(domain, (error, addresses) => {
    if (error) {
        console.error('Error:', error);
    } else {
        console.log(`The IP address of ${domain} is: ${addresses}`);
    }
});
