
# NewsAggregator

This project was made to provide a collection of present day news to users in real time, along with the ability to filter by their desired category

This app was made possible using Django



## Run Locally

Clone the project

```bash
  git clone https://github.com/sanathboddhula/news_aggregator
```

Go to the project directory

```bash
  cd news_aggregator
```

Start the server

```bash
   python manage.py runserver
```


## API Reference

#### Get all items

```http
  GET http://api.mediastack.com/v1/news?access_key=api_key&countries=us&categories={category}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `api_key` | `string` | **Required**. Your API key |




## Authors

- [@sanathboddhula](https://github.com/sanathboddhula)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.

