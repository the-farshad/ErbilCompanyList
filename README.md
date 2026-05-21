# ErbilCompanyList

Scrape the public company directory of the
[Erbil Chamber of Commerce and Industry](https://www.erbilchamber.org)
into a CSV file.

For each registered company the scraper collects the managing director,
company activity, registration number, date of registration, mobile number,
address and shareholders.

## Requirements

- Python 3

Install the dependencies:

```sh
pip install -r requirements.txt
```

## Usage

```sh
python erbilChamber.py
```

Results are appended to `ErbilChamber.csv`. If a run is interrupted, the last
processed offset is printed so it can be resumed.

## License

Released under the [GPL-3.0](LICENSE) license.
